from django.db.models.signals import post_save
from django.dispatch import receiver

from applications.common.redis import RedisManager
from applications.orms.crw_model import ConstConfigureV20191017Crw, AdUserProfileFeatureV20200709Cld, \
    OnlineBrandAdV20200709Cld, AdBlackUidV20200710Cld


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


@receiver(post_save, sender=AdUserProfileFeatureV20200709Cld)
def handle_ad_user_cache(instance, **kwargs):
    # pylint:disable=unused-argument
    """常量缓存配置"""
    # 获取常量名称
    consts_field = instance.u_en
    # 获取常量值
    consts_value = instance.u_value
    # 是否存储缓存
    is_redis_cache = instance.u_is_redis_cache
    if is_redis_cache:
        # 原生redis
        RedisManager.hash_set(key=consts_field, value=consts_value, name='ad_user_profile')


@receiver(post_save, sender=OnlineBrandAdV20200709Cld)
def handle_brand_cache(instance, **kwargs):
    # pylint:disable=unused-argument
    """常量缓存配置"""
    # 获取常量名称
    consts_field = instance.ob_ad_bid
    # 获取常量值
    consts_value = instance.ob_ad_data
    # 是否存储缓存
    is_redis_cache = instance.ob_ad_redis_cache
    if is_redis_cache:
        # 原生redis
        RedisManager.hash_set(key=consts_field, value=consts_value, name='ad_online_brand')

@receiver(post_save, sender=AdBlackUidV20200710Cld)
def handle_ad_black_cache(instance, **kwargs):
    # pylint:disable=unused-argument
    """常量缓存配置"""
    # 获取常量名称
    consts_field = instance.ad_b_en
    # 获取常量值
    consts_value = instance.ad_b_value
    # 是否存储缓存
    is_redis_cache = instance.ad_b_is_redis_cache
    if is_redis_cache:
        # 原生redis
        RedisManager.hash_set(key=consts_field, value=consts_value, name='ad_black_uids')

