# _*_ coding: utf-8 _/*_
# 个人仓库
import os
import string
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
            logger.error(f"重复数据")
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
