# _*_ coding: utf-8 _/*_
# 个人仓库
import asyncio
import functools
import os
import string
import time
from typing import List

from loguru import logger
from motor.motor_asyncio import AsyncIOMotorClient
from zhon.hanzi import punctuation


def is_docker():
    """
    判断是否在docker
    :return:
    """
    path = '/proc/self/cgroup'
    return (os.path.exists('/.dockerenv') or
            os.path.isfile(path) and any('docker' in line for line in open(path)))


def filter_punctuations(text):
    """
    清除标点
    :param text:
    :return:
    """
    for i in string.punctuation:
        text = text.replace(i, "")
    for i in punctuation:
        text = text.replace(i, "")
    return text


class AioMongoTool(object):
    """
    连接mango
    """
    _mongo: AsyncIOMotorClient = None
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.client = args[0]
            cls._instance.db = args[1]
        return cls._instance

    def __init__(self, uri: str, db: str):
        self.connect(uri, db)

    def connect(self, uri: str, db: str):
        self.client = AsyncIOMotorClient(uri)
        self.db = self.client[db]

    async def close(self) -> None:
        if self.client:
            await self.client.close()

    async def find_one(self, collection_name: str, filter: dict) -> dict:
        collection = self.db[collection_name]
        result = await collection.find_one(filter, {"_id": False})
        return result

    async def find_many(self, collection_name: str, filter: dict) -> List[dict]:
        collection = self.db[collection_name]
        result = []
        async for doc in collection.find(filter):
            result.append(doc)
        return result

    async def insert_one(self, collection_name: str, document: dict):
        collection = self.db[collection_name]
        try:
            result = await collection.insert_one(document)
            if result:
                return True
            else:
                return False
        except Exception:
            logger.error(f"重复数据: {document.get('_id')}")
            return False

    async def insert_many(self, collection_name: str, document: List[dict]):
        collection = self.db[collection_name]
        result = await collection.insert_many(document)
        if result:
            return True
        else:
            return False

    async def update_one(self, collection_name: str, filter: dict, update: dict):
        collection = self.db[collection_name]
        result = await collection.update_one(filter, update)
        if result:
            return True
        else:
            return False

    async def update_many(self, collection_name: str, filter: dict, update: dict):
        collection = self.db[collection_name]
        result = await collection.update_many(filter, update)
        if result:
            return True
        else:
            return False

    async def delete_one(self, collection_name: str, filter: dict):
        collection = self.db[collection_name]
        result = await collection.delete_one(filter)
        if result:
            return True
        else:
            return False

    async def delete_many(self, collection_name: str, filter: dict):
        collection = self.db[collection_name]
        result = await collection.delete_many(filter)
        if result:
            return True
        else:
            return False


class useRetry(object):
    """
    用于函数重试的装饰器，支持异步函数 失败后返回None

    :param max_retry: 最大重试次数
    :param retry_interval: 重试间隔
    :param retry_exceptions: 重试异常

    >>> @useRetry(max_retry=3, retry_interval=1)
    ... def test():
    ...     print('test')
    ...     raise Exception('test')
    """

    def __init__(self, max_retry=3, retry_interval=1, retry_exceptions=None):
        self.max_retry = max_retry
        self.retry_interval = retry_interval
        self.retry_exceptions = retry_exceptions or (Exception,)

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            retry = 0
            while retry < self.max_retry:
                try:
                    return func(*args, **kwargs)
                except self.retry_exceptions as e:
                    retry += 1
                    if retry >= self.max_retry:
                        return
                    time.sleep(self.retry_interval)

        @functools.wraps(func)
        async def async_wrapper(*args, **kwargs):
            retry = 0
            while retry < self.max_retry:
                try:
                    return await func(*args, **kwargs)
                except self.retry_exceptions as e:
                    retry += 1
                    if retry >= self.max_retry:
                        return
                    await asyncio.sleep(self.retry_interval)

        wrapper_func = async_wrapper if asyncio.iscoroutinefunction(func) else wrapper
        return wrapper_func
