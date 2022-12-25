from typing import Optional

from storages import StorageType

from storages.async_storages.pickle_storage import PickleStorage
from storages.async_storages.json_storage import JSONStorage
from storages.async_storages.redis_storage import RedisStorage


async def load_storage(storage_type: StorageType,
                       file_path: Optional[str] = None,
                       redis_url: Optional[str] = None,
                       redis_data_key: Optional[str] = None):
    storage = {
        StorageType.pickle: PickleStorage,
        StorageType.json: JSONStorage,
        StorageType.redis: RedisStorage,
    }
    if storage_type in [StorageType.pickle, StorageType.json]:
        return await storage[storage_type].create(file_path)
    elif storage_type == StorageType.redis:
        return await storage[storage_type].create(redis_url, redis_data_key)


__all__ = (
    "PickleStorage",
    "JSONStorage",
    "RedisStorage",
    "load_storage",
)