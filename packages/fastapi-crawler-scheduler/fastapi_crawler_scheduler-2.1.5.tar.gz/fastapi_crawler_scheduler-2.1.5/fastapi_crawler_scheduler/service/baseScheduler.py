import os
import json
import six
import traceback
from typing import Dict

from uhashring import HashRing
from apscheduler.jobstores.redis import RedisJobStore
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.util import ref_to_obj

from fastapi_crawler_scheduler.service.dbRedisHelper import DbRedisHelper


class BaseScheduler(object):
    """
    任务管理和自身的异步任务
    :param DbRedisHelper对象 redis_db: DbRedisHelper对象
    :param BackgroundScheduler对象 scheduler: BackgroundScheduler对象
    :param str server_name: 服务器名字
    :param str project_name: 项目名字，主要区分不同项目
    :param RedisJobStore对象 redis_job_store: RedisJobStore对象
    """

    def __init__(
            self,
            redis_db: DbRedisHelper,
            scheduler: BackgroundScheduler,
            server_name: str,
            project_name: str,
            redis_job_store: RedisJobStore,

    ) -> None:
        self.server_name = server_name
        self.project_name = project_name
        self.redis_db = redis_db
        self.scheduler = scheduler
        self.process_id_list = []
        self.redis_job_store = redis_job_store

    def scheduler_add_job(
            self,
            **task_info
    ) -> None:
        '''
        向 apscheduler 中添加一个任务
        :param crawler_info: 任务参数
        :return:
        '''
        try:
            func = ref_to_obj(task_info.get('func'))
        except Exception as e:
            print(f"scheduler_add_job   函数错误 ：{e}")
            print(traceback.format_exc())
            return
        trigger = task_info.get('trigger')
        job_id = task_info.get('job_id')
        crawler_info = task_info.get('crawler_info')
        trigger_args = task_info.get('trigger_args')
        if self.redis_job_store.redis.hexists(self.redis_job_store.jobs_key, job_id):
            self.redis_job_store.remove_job(job_id=job_id)
        self.scheduler.add_job(
            func=func,
            id=job_id,
            trigger=trigger,
            kwargs=crawler_info,
            **trigger_args,
        )

    def check_process(self) -> None:
        '''
        检查进程
        :return:
        '''
        self.redis_db.process_acquire(f'{self.project_name}:node:{self.server_name}:{os.getpid()}')

    def get_process_list(self) -> list:
        '''
        获取当前项目所有进程信息
        :return:
        '''
        return self.redis_db.get_proces_info()

    def process_check_count(self, task_node_id: str, check_key: str) -> None:
        '''
        检查任务策略
        :param process_id: 进程pid
        :param check_key:  待检查任务键
        :return:
        '''
        if task_node_id not in self.process_id_list:
            if self.redis_db.acquire(lock_name=check_key):
                check_value = self.redis_db.from_key_get_value(key_name=check_key)
                if check_value is None:
                    return None
                check_process_number = check_value.get('check_process_number')
                if check_process_number is None:
                    check_process_number = 1
                else:
                    check_process_number += 1
                if check_process_number >= 3:
                    self.redis_db.delete_key(lock_name=check_key)
                else:
                    check_value['check_process_number'] = check_process_number
                    self.redis_db.string_set(key=check_key, value=json.dumps(check_value, ensure_ascii=False))
                self.redis_db.release(lock_name=check_key)

    def check_backend_task(self) -> None:
        node_process_id_list = self.get_process_list()
        self.process_id_list = [node_id.replace('node:', '').strip() for node_id in node_process_id_list]
        # 处理后端操作
        hr = HashRing(nodes=node_process_id_list)
        for backend_key in self.redis_db.get_backend_task():
            backend_info = self.redis_db.from_key_get_value(backend_key)
            if backend_info is None:
                self.redis_db.delete_key(lock_name=backend_key)
                continue
            lock_all_backend_key = f'{self.redis_db.prefix}:all:{backend_info["job_id"]}'
            all_backend_key = f'{self.project_name}:all:{backend_info["job_id"]}'
            if not self.redis_db.lock_exists(lock_name=lock_all_backend_key):
                process_node_id = hr.get_node(backend_info["job_id"])
                backend_info['process_node_id'] = process_node_id
                self.redis_db.string_set(key=all_backend_key, value=json.dumps(backend_info, ensure_ascii=False))
                self.redis_db.delete_key(lock_name=backend_key)

    def check_all_task(self) -> None:
        '''
        检查所有任务
        :return:
        '''
        node_process_id_list = self.get_process_list()
        self.process_id_list = [node_id.replace('node:', '').strip() for node_id in node_process_id_list]
        hr = HashRing(nodes=node_process_id_list)
        # 处理 all_task
        for all_key in self.redis_db.get_all_task():
            all_value = self.redis_db.from_key_get_value(all_key)
            if all_value is None:
                self.redis_db.delete_key(lock_name=all_key)
                continue
            if self.redis_db.acquire(lock_name=all_key):
                redis_process_node_id = all_value["process_node_id"]
                new_process_node_id = hr.get_node(all_value["job_id"])
                if new_process_node_id == redis_process_node_id:
                    process_id = int(str(redis_process_node_id).strip().split(':')[-1])
                    # 进程没变化
                    if all_value['is_change'] == 1:
                        next_key = f'{self.project_name}:{all_value["operation"]}:{self.server_name}:{all_value["job_id"]}:{process_id}'
                        self.redis_db.string_set(key=next_key, value=json.dumps(all_value, ensure_ascii=False))
                        all_value["is_change"] = 0
                        self.redis_db.string_set(key=all_key, value=json.dumps(all_value, ensure_ascii=False))
                else:
                    # 进程有变化
                    new_process_id = int(str(new_process_node_id).strip().split(':')[-1])
                    if all_value['operation'] == 'delete':
                        # operation = delete 的 无需执行以后操作
                        all_value["process_node_id"] = new_process_node_id
                        self.redis_db.string_set(key=all_key, value=json.dumps(all_value, ensure_ascii=False))
                        continue
                    redis_process_id = int(str(redis_process_node_id).strip().split(':')[-1])
                    delete_key = f'{self.project_name}:delete:{self.server_name}:{all_value["job_id"]}:{redis_process_id}'
                    all_value["details"] = "删除任务"
                    # 删除旧进程任务
                    self.redis_db.string_set(key=delete_key, value=json.dumps(all_value, ensure_ascii=False))
                    # 新进程中添加
                    all_value["process_node_id"] = new_process_node_id
                    insert_key = f'{self.project_name}:insert:{self.server_name}:{all_value["job_id"]}:{new_process_id}'
                    all_value["details"] = "进程变化，新增任务"
                    self.redis_db.string_set(key=insert_key, value=json.dumps(all_value, ensure_ascii=False))
                    all_value["is_change"] = 0
                    self.redis_db.string_set(key=all_key, value=json.dumps(all_value, ensure_ascii=False))
                self.redis_db.release(lock_name=all_key)

    def check_insert_task(self) -> None:
        '''
        检查新增任务
        :return:
        '''
        for insert_key in self.redis_db.get_insert_task():
            insert_value = self.redis_db.from_key_get_value(insert_key)
            if insert_value is None:
                self.redis_db.delete_key(lock_name=insert_key)
                continue
            try:
                process_node_id = insert_value['process_node_id']
                apscheduler_id = insert_value['job_id']
                task_node_id = process_node_id.replace('node:', '')
                belongs_to_task_node_list = [str(self.project_name), str(self.server_name), str(os.getpid())]
                belongs_to_task_node_id = ':'.join(belongs_to_task_node_list)
                if belongs_to_task_node_id == task_node_id:
                    if self.scheduler.get_job(job_id=apscheduler_id):
                        self.scheduler.remove_job(job_id=apscheduler_id)
                    self.scheduler_add_job(**insert_value)
                    self.redis_db.delete_key(lock_name=insert_key)
                else:
                    self.process_check_count(task_node_id=task_node_id, check_key=insert_key)
            except Exception as e:
                print(f"check_insert_task 函数 错误 ：{e}")
                print(traceback.format_exc())

    def check_update_task(self) -> None:
        '''
        检查更新任务,
        :return:
        '''
        for update_key in self.redis_db.get_update_task():
            update_value = self.redis_db.from_key_get_value(update_key)
            if update_value is None:
                self.redis_db.delete_key(lock_name=update_key)
                continue
            try:
                process_node_id = update_value['process_node_id']
                apscheduler_id = update_value['job_id']
                task_node_id = process_node_id.replace('node:', '')
                belongs_to_task_node_list = [str(self.project_name), str(self.server_name), str(os.getpid())]
                belongs_to_task_node_id = ':'.join(belongs_to_task_node_list)
                if belongs_to_task_node_id == task_node_id:
                    if self.scheduler.get_job(job_id=apscheduler_id):
                        self.scheduler.remove_job(job_id=apscheduler_id)
                    self.scheduler_add_job(**update_value)
                    self.redis_db.delete_key(lock_name=update_key)
                else:
                    self.process_check_count(task_node_id=task_node_id, check_key=update_key)
            except Exception as e:
                print(f"check_update_task 函数 错误 ：{e}")
                print(traceback.format_exc())

    def check_delete_task(self) -> None:
        '''
        检查删除任务
        :return:
        '''

        for delete_key in self.redis_db.get_delete_task():
            delete_value = self.redis_db.from_key_get_value(delete_key)
            if delete_value is None:
                self.redis_db.delete_key(lock_name=delete_key)
                continue
            try:
                process_node_id = delete_value['process_node_id']
                apscheduler_id = delete_value['job_id']
                task_node_id = process_node_id.replace('node:', '')
                belongs_to_task_node_list = [str(self.project_name), str(self.server_name), str(os.getpid())]
                belongs_to_task_node_id = ':'.join(belongs_to_task_node_list)
                if belongs_to_task_node_id == task_node_id:
                    if self.scheduler.get_job(job_id=apscheduler_id):
                        self.scheduler.remove_job(job_id=apscheduler_id)
                    self.redis_db.delete_key(lock_name=delete_key)
                else:
                    self.process_check_count(task_node_id=task_node_id, check_key=delete_key)
            except Exception as e:
                print(f"check_delete_task 函数 错误 ：{e}")
                print(traceback.format_exc())

    def insert_task(self, task_info: Dict) -> None:
        '''
        新增任务
        :param task_info:
        :return:
        '''
        task_info['operation'] = 'insert'
        task_info['is_change'] = 1
        self.redis_db.string_set(f'{self.project_name}:backend:{task_info.get("job_id")}',
                                 json.dumps(task_info, ensure_ascii=False))

    def delete_task(self, job_id: str) -> None:
        '''
        删除任务
        :param job_id:
        :return:
        '''
        crawler_info = dict()
        crawler_info['job_id'] = job_id
        crawler_info['is_change'] = 1
        crawler_info['operation'] = 'delete'
        self.redis_db.string_set(f'{self.project_name}:backend:{crawler_info.get("job_id")}',
                                 json.dumps(crawler_info, ensure_ascii=False))

    def check_redis_jobstores_jobs(self) -> None:
        '''
        异步检查 redis 中 apscheduler 的任务
        :return:
        '''
        job_process_dict = {}
        for all_key in self.redis_db.get_all_task():
            all_value = self.redis_db.from_key_get_value(all_key)
            if all_value is None:
                continue
            process_node_id = all_value["process_node_id"]
            job_id = all_value["job_id"]
            job_process_dict[job_id] = process_node_id
        if len(job_process_dict) == 0:
            return
        stores_job_task = self.redis_db.get_stores_job_task()
        for stores_job_key in stores_job_task:
            stores_job_run_times_key = stores_job_key.replace('jobs', 'run_times')
            job_states = self.redis_job_store.redis.hgetall(stores_job_key)
            stores_job_process_id = stores_job_key.replace('apscheduler:jobs', 'node')
            for job_id, job_state in six.iteritems(job_states):
                job_id = job_id.decode('utf-8')
                try:
                    belongs_to_process_id = job_process_dict[job_id]
                except KeyError:
                    continue
                if stores_job_process_id == belongs_to_process_id:
                    pass
                else:
                    with self.redis_job_store.redis.pipeline() as pipe:
                        pipe.hdel(stores_job_key, job_id)
                        pipe.execute()
                    with self.redis_job_store.redis.pipeline() as pipe:
                        pipe.zrem(stores_job_run_times_key, job_id)
                        pipe.execute()

    def check_redis_jobstores_run_times(self) -> None:
        '''
        异步检查 redis 中 apscheduler 的任务
        :return:
        '''
        job_process_dict = {}
        for all_key in self.redis_db.get_all_task():
            all_value = self.redis_db.from_key_get_value(all_key)
            if all_value is None:
                continue
            process_node_id = all_value["process_node_id"]
            job_id = all_value["job_id"]
            job_process_dict[job_id] = process_node_id
        if len(job_process_dict) == 0:
            return
        stores_job_run_time_task = self.redis_db.get_stores_job_run_time_task()
        for stores_job_run_times_key in stores_job_run_time_task:
            stores_job_key = stores_job_run_times_key.replace('run_times', 'jobs')
            stores_job_process_id = stores_job_run_times_key.replace('apscheduler:run_times', 'node')
            apscheduler_run_time_byte_list = self.redis_job_store.redis.zrange(stores_job_run_times_key, 0, 4821384687,
                                                                               withscores=True)
            for job_id_byte, run_time__byte_timestamp in apscheduler_run_time_byte_list:
                job_id = job_id_byte.decode('utf-8')
                try:
                    belongs_to_process_id = job_process_dict[job_id]
                except KeyError:
                    continue
                if stores_job_process_id == belongs_to_process_id:
                    pass
                else:
                    with self.redis_job_store.redis.pipeline() as pipe:
                        pipe.hdel(stores_job_key, job_id)
                        pipe.execute()
                    with self.redis_job_store.redis.pipeline() as pipe:
                        pipe.zrem(stores_job_run_times_key, job_id)
                        pipe.execute()

    def check_lost_tasks(self) -> None:
        redis_apscheduler_run_time_job_id_set = set()
        for apscheduler_run_time_key in self.redis_db.get_stores_job_run_time_task():
            apscheduler_run_time_byte_list = self.redis_job_store.redis.zrange(
                apscheduler_run_time_key, 0, 4821384687, withscores=True)
            for job_states_key_byte, run_time__byte_timestamp in apscheduler_run_time_byte_list:
                redis_apscheduler_run_time_job_id_set.add(job_states_key_byte.decode())
        for all_key in self.redis_db.get_all_task():
            all_value = self.redis_db.from_key_get_value(all_key)
            if all_value is None:
                continue
            if all_value.get('job_id') not in redis_apscheduler_run_time_job_id_set:
                if self.redis_db.acquire(lock_name=all_key):
                    all_value = self.redis_db.from_key_get_value(all_key)
                    if all_value is None:
                        continue
                    all_value['is_change'] = 1
                    self.redis_db.string_set(key=all_key, value=json.dumps(all_value, ensure_ascii=False))
                    self.redis_db.release(lock_name=all_key)

    def run(self) -> None:
        '''
        异步检查所有任务
        :return:
        '''
        self.check_backend_task()
        self.check_all_task()
        self.check_insert_task()
        self.check_update_task()
        self.check_delete_task()
