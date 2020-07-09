from django.contrib import admin

from applications.orms.crw_model import ConstConfigureV20191017Crw


class ConstConfigureV20190320InfAdmin(admin.ModelAdmin):
    """常量配置表管理类"""
    list_display = ('cc_id', 'cc_name_ch', 'cc_name_en', 'admin_cc_value', 'cc_create_time', 'cc_modify_time')


# 注册常量配置表
admin.site.register(ConstConfigureV20191017Crw, ConstConfigureV20190320InfAdmin)
