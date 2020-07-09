import json
import logging

from django_redis import get_redis_connection

from applications.orms.crw_model import ConstConfigureV20191017Crw

LOGGER = logging.getLogger('console_logger')


class RedisManager:
    """原生redis处理"""

    @staticmethod
    def hash_set(key, value, name='consts_configure_cache', alias='default'):
        """哈希设置"""
        LOGGER.info('redis_hash_set_cache_start: name:%s key:%s  value:%s', name, key, value)
        con = get_redis_connection(alias=alias)
        con.hset(name=name, key=key, value=value)
        LOGGER.info('redis_hash_set_cache_success: name:%s key:%s  value:%s', name, key, value)

    @staticmethod
    def __hash_get(key, name='consts_configure_cache', alias='default'):
        """哈希获取"""
        LOGGER.info('redis_hash_get_cache_start: name:%s key:%s ', name, key)
        con = get_redis_connection(alias=alias)
        value = con.hget(name=name, key=key)
        LOGGER.info('redis_hash_get_cache_success: name:%s key:%s  value:%s', name, key, value)

        return value

    @staticmethod
    def get_cache_consts_value(key, name='consts_configure_cache'):
        """获取常量缓存的配置"""
        # 从缓存中获取结果
        const_value = RedisManager.__hash_get(name=name, key=key)
        # 缓存中没有数据从数据库获取结果
        if not const_value:
            const_value = ConstConfigureV20191017Crw.objects.get(cc_name_en=key).cc_value
            # 设置缓存
            RedisManager.hash_set(name=name, key=key, value=const_value)
        return json.loads(const_value)

    @staticmethod
    def get_cache_consts_string_value(key, name='consts_configure_cache'):
        """获取常量缓存的配置"""
        # 从缓存中获取结果
        const_value = RedisManager.__hash_get(name=name, key=key)
        # 缓存中没有数据从数据库获取结果
        if not const_value:
            const_value = ConstConfigureV20191017Crw.objects.get(cc_name_en=key).cc_value
            # 设置缓存
            RedisManager.hash_set(name=name, key=key, value=const_value)
        return const_value.decode() if const_value else const_value

    @staticmethod
    def get(key, alias='default'):
        con = get_redis_connection(alias=alias)
        value = con.get(key)
        return value.decode() if value else value

    @staticmethod
    def set(key, value, expire=None, alias='default'):
        con = get_redis_connection(alias=alias)
        con.set(key, value, ex=expire)

    @staticmethod
    def lpush(key, value, alias='default'):
        con = get_redis_connection(alias=alias)
        con.lpush(key, value)

    @staticmethod
    def remove(key, alias='default'):
        con = get_redis_connection(alias=alias)
        con.move(key)

    @staticmethod
    def lpop(key, alias='default'):
        con = get_redis_connection(alias=alias)
        value = con.lpop(key)
        return value.decode() if value else value

    @staticmethod
    def rpop(key, alias='default'):
        con = get_redis_connection(alias=alias)
        value = con.rpop(key)
        return value.decode() if value else value
