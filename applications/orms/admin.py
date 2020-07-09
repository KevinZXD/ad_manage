from django.contrib import admin

from applications.orms.crw_model import ConstConfigureV20191017Crw, AdBlackUidV20200710Cld, OnlineBrandAdV20200709Cld, \
    AdUserProfileFeatureV20200709Cld


class ConstConfigureV20190320InfAdmin(admin.ModelAdmin):
    """常量配置表管理类"""
    list_display = ('cc_id', 'cc_name_ch', 'cc_name_en', 'admin_cc_value', 'cc_create_time', 'cc_modify_time')


class AdBlackUidV20200710CldAdmin(admin.ModelAdmin):
    """广告黑名单"""
    list_display = ('ad_b_id', 'ad_b_ch', 'ad_b_en', 'ad_b_value', 'ad_b_create_time', 'ad_b_modify_time')


class OnlineBrandAdV20200709CldAdmin(admin.ModelAdmin):
    """品牌广告"""
    list_display = ('ob_ad_id', 'ob_ad_bid', 'ob_ad_name', 'ob_ad_de_name', 'ob_ad_data', 'ob_ad_deliver_time','ob_ad_end_time','ob_ad_budget')


class AdUserProfileFeatureV20200709CldAdmin(admin.ModelAdmin):
    """用户基本画像"""
    list_display = ('u_id', 'u_ch', 'u_en', 'u_value', 'u_create_time', 'u_modify_time')


# 注册常量配置表
admin.site.register(ConstConfigureV20191017Crw, ConstConfigureV20190320InfAdmin)
admin.site.register(AdBlackUidV20200710Cld, AdBlackUidV20200710CldAdmin)
admin.site.register(OnlineBrandAdV20200709Cld, OnlineBrandAdV20200709CldAdmin)
admin.site.register(AdUserProfileFeatureV20200709Cld, AdUserProfileFeatureV20200709CldAdmin)
