from django.db.models.signals import post_save
from django.dispatch import receiver

from applications.common.redis import RedisManager
from applications.orms.crw_model import ConstConfigureV20191017Crw


@receiver(post_save, sender=ConstConfigureV20191017Crw)
def handle_consts_configure_cache(instance, **kwargs):
    # pylint:disable=unused-argument
    """常量缓存配置"""
    # 获取常量名称
    consts_field = instance.cc_name_en
    # 获取常量值
    consts_value = instance.cc_value
    # 是否存储缓存
    is_redis_cache = instance.cc_is_redis_cache
    if is_redis_cache:
        # 原生redis
        RedisManager.hash_set(key=consts_field, value=consts_value)

