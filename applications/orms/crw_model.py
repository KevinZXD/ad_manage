import json

from django.db import models

from applications.orms.base_models import BaseMeta


class ConstConfigureV20191017Crw(models.Model):
    """常量配置表"""
    cc_id = models.AutoField(primary_key=True, verbose_name="主键")
    cc_name_ch = models.CharField(max_length=255, verbose_name='配置常量字段名称 中文')
    cc_name_en = models.CharField(unique=True, max_length=255, verbose_name='配置常量字段名称　英文')
    cc_value = models.TextField(verbose_name='常量数据')
    cc_create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    cc_modify_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    cc_is_redis_cache = models.BooleanField(default=1, verbose_name='是否设置redis 缓存')

    class Meta(BaseMeta):
        db_table = "const_configure_v20191017_crw"
        verbose_name_plural = "常量配置表"

    def admin_cc_value(self):
        if len(self.cc_value) > 500:
            return '数据过大,暂不展示,点击进入查看详情'
        return self.cc_value

    @staticmethod
    def gain_cc_value(cc_name_en):
        """根据值　获取结果"""
        cc_value = ConstConfigureV20191017Crw.objects.get(cc_name_en=cc_name_en).cc_value
        return json.loads(cc_value)

    @staticmethod
    def update_cc_value(cc_name_en, cc_value):
        con_obj = ConstConfigureV20191017Crw.objects.get(cc_name_en=cc_name_en)
        con_obj.cc_value = json.dumps(cc_value)
        con_obj.save(using='inf')


class AdUserProfileFeatureV20200709Cld(models.Model):
    """用户基本画像"""
    u_id = models.AutoField(primary_key=True, verbose_name="主键")
    u_ch = models.CharField(max_length=255, verbose_name='用户 中文')
    u_en = models.CharField(unique=True, max_length=255, verbose_name='用户　英文')
    u_value = models.TextField(verbose_name='用户基本画像')
    u_create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    u_modify_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    u_is_redis_cache = models.BooleanField(default=1, verbose_name='是否设置redis 缓存')

    class Meta(BaseMeta):
        db_table = "ad_user_profile_feature_v20200709_cld"
        verbose_name_plural = "用户基本画像"

    def admin_u_value(self):
        if len(self.u_value) > 500:
            return '数据过大,暂不展示,点击进入查看详情'
        return self.u_value

    @staticmethod
    def gain_u_value(u_en):
        """根据值　获取结果"""
        u_value = AdUserProfileFeatureV20200709Cld.objects.get(u_en=u_en).cc_value
        return json.loads(u_value)

    @staticmethod
    def update_u_value(u_en, u_value):
        con_obj = AdUserProfileFeatureV20200709Cld.objects.get(u_en=u_en)
        con_obj.u_value = json.dumps(u_value)
        con_obj.save(using='cld')


class OnlineBrandAdV20200709Cld(models.Model):
    ob_ad_id = models.AutoField(primary_key=True, verbose_name="主键")
    ob_ad_bid = models.CharField(max_length=255, verbose_name='品牌广告id')
    ob_ad_name = models.CharField(max_length=255, verbose_name='品牌广告商')
    ob_ad_de_name = models.CharField(max_length=255, verbose_name='在投品牌广告名称')
    ob_ad_data = models.TextField(verbose_name='品牌广告物料')
    ob_ad_deliver_time = models.DateTimeField(auto_now_add=True, verbose_name='品牌广告投放时间')
    ob_ad_end_time = models.DateTimeField(auto_now_add=True, verbose_name='品牌广告下线时间')
    ob_ad_budget = models.IntegerField(verbose_name='品牌广告预算')
    ob_ad_create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    ob_ad_modify_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    ob_ad_redis_cache = models.BooleanField(default=1, verbose_name='是否设置redis 缓存')

    class Meta(BaseMeta):
        db_table = "online_brand_ad_v20200709_cld"
        verbose_name_plural = "品牌广告"

    def admin_ob_ad_data(self):
        if len(self.ob_ad_data) > 500:
            return '数据过大,暂不展示,点击进入查看详情'
        return self.ob_ad_data

    @staticmethod
    def gain_ob_ad_data(ob_ad_bid):
        """根据值　获取结果"""
        ob_ad_data = OnlineBrandAdV20200709Cld.objects.get(ob_ad_bid=ob_ad_bid).ob_ad_data
        return json.loads(ob_ad_data)

    @staticmethod
    def update_ob_ad_data(ob_ad_bid, ob_ad_data):
        con_obj = OnlineBrandAdV20200709Cld.objects.get(ob_ad_bid=ob_ad_bid)
        con_obj.ob_ad_data = json.dumps(ob_ad_data)
        con_obj.save(using='cld')


class AdBlackUidV20200710Cld(models.Model):
    ad_b_id = models.AutoField(primary_key=True, verbose_name="主键")
    ad_b_ch = models.CharField(max_length=255, verbose_name='广告黑名单中文')
    ad_b_en = models.CharField(unique=True, max_length=255, verbose_name='广告黑名单英文')
    ad_b_value = models.TextField(verbose_name='黑名单数据')
    ad_b_create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    ad_b_modify_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    ad_b_is_redis_cache = models.BooleanField(default=1, verbose_name='是否设置redis 缓存')

    class Meta(BaseMeta):
        db_table = "ad_black_uid_v20200710_cld"
        verbose_name_plural = "广告黑名单"

    def admin_ad_b_value(self):
        if len(self.ad_b_value) > 500:
            return '数据过大,暂不展示,点击进入查看详情'
        return self.ad_b_value

    @staticmethod
    def gain_ab_b_value(ad_b_en):
        """根据值　获取结果"""
        ad_b_value = AdBlackUidV20200710Cld.objects.get(ad_b_en=ad_b_en).ad_b_value
        return json.loads(ad_b_value)

    @staticmethod
    def update_ab_b_value(ad_b_en, ad_b_value):
        con_obj = AdBlackUidV20200710Cld.objects.get(ad_b_en=ad_b_en)
        con_obj.ad_b_value = json.dumps(ad_b_value)
        con_obj.save(using='cld')
