from threading import Thread, get_ident
from menglingtool.queue import Mqueue
import traceback
import os
import logging
import time
import asyncio

# 便捷获取log对象
def getLogger(name, level=logging.INFO, log_path=None) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)
    handler = logging.FileHandler(log_path) if log_path else logging.StreamHandler()
    formatter = logging.Formatter("[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def run_thread_tasks(task_queue: Mqueue, getGood, gooder_getResult, good_num: int,
                     logger: logging.Logger = None,
                     is_put_args=False,
                     is_put_kwargs=False,
                     is_put_time=True) -> list:
    logger = logger if logger else getLogger(f'pid-{get_ident()}')
    logger.info(f'PID-{os.getpid()} worker num: {good_num}')

    def _worker():
        gooder = getGood()
        while True:
            que, index, args, kwargs = task_queue.get()
            sd = time.time()
            try:
                result = gooder_getResult(gooder, *args, **kwargs)
                err = None
            except:
                err = traceback.format_exc()
                result = None

            logger.info(f'args:{args}, kwargs:{kwargs}, is_err:{bool(err)}')
            rdt = {}
            if is_put_args: rdt['args'] = args
            if is_put_kwargs: rdt['kwargs'] = kwargs
            rdt['index'] = index
            rdt['result'] = result
            rdt['err'] = err
            if is_put_time: rdt['time'] = time.time() - sd
            que.put(rdt)

    ts = [Thread(target=_worker, daemon=True) for _ in range(good_num)]
    [t.start() for t in ts]
    return ts


def arg_in_task_puts(task_queue: Mqueue, vs: list) -> (Mqueue, int): # type: ignore
    return all_in_task_puts(task_queue, [[(v,), {}] for v in vs])


def args_in_task_puts(task_queue: Mqueue, argss: list) -> (Mqueue, int): # type: ignore
    return all_in_task_puts(task_queue, [[args, {}] for args in argss])


def kwargs_in_task_puts(task_queue: Mqueue, kwargss: list) -> (Mqueue, int): # type: ignore
    return all_in_task_puts(task_queue, [[(), kwargs] for kwargs in kwargss])


def all_in_task_puts(task_queue: Mqueue, args_and_kwargs: list) -> (Mqueue, int): # type: ignore
    result_queue = Mqueue()
    task_queue.puts(*[(result_queue, i, *args_kwargs) for i, args_kwargs in enumerate(args_and_kwargs)])
    return result_queue, len(args_and_kwargs)


def getResults(result_queue: Mqueue, maxlen: int, is_sorded=True) -> list:
    while result_queue.qsize() < maxlen:
        time.sleep(1)
    ls = result_queue.to_list()
    return sorted(ls, key = lambda x: x['index']) if is_sorded else ls


async def async_getResults(result_queue: Mqueue, maxlen: int, is_sorded=True) -> list:
    while result_queue.qsize() < maxlen:
        await asyncio.sleep(1)
    ls = result_queue.to_list()
    return sorted(ls, key = lambda x: x['index']) if is_sorded else ls