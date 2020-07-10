import json

from applications.orms.crw_model import ConstConfigureV20191017Crw, AdBlackUidV20200710Cld, OnlineBrandAdV20200709Cld, \
    AdUserProfileFeatureV20200709Cld


def run():
    """常量数据配置表"""
    cc_obj = ConstConfigureV20191017Crw()
    cc_obj.cc_name_en = 'scene_map'
    cc_obj.cc_name_ch = "场景映射"
    cc_obj.cc_value = json.dumps({
        'mainfeed': ['sfst', 'douyin'],
    })
    cc_obj.save(using='crw')

    cc_obj = ConstConfigureV20191017Crw()
    cc_obj.cc_name_en = '流量降级开关'
    cc_obj.cc_name_ch = "flow_control"
    cc_obj.cc_value = "false"
    cc_obj.save(using='crw')

    cc_obj = ConstConfigureV20191017Crw()
    cc_obj.cc_name_en = '流量业务策略'
    cc_obj.cc_name_ch = "场景映射"
    cc_obj.cc_value = json.dumps({
        '01': ['业务策略1', '业务策略2'],
        '02': ['业务策略3', '业务策略4'],
        '03': ['业务策略5', '业务策略6'],
    })
    cc_obj.save(using='crw')

    ad_black = AdBlackUidV20200710Cld()
    ad_black.ad_b_is_redis_cache = 1
    ad_black.ad_b_ch = "小米公司"
    ad_black.ad_b_en = "Redmi"
    ad_black.ad_b_value = json.dumps(['10001', '10002', '10003'])
    ad_black.save(using='cld')

    ad_black = AdBlackUidV20200710Cld()
    ad_black.ad_b_is_redis_cache = 1
    ad_black.ad_b_ch = "华为荣耀"
    ad_black.ad_b_en = "P30"
    ad_black.ad_b_value = json.dumps(['10007', '10008', '10009'])
    ad_black.save(using='cld')

    ad_black = AdBlackUidV20200710Cld()
    ad_black.ad_b_is_redis_cache = 1
    ad_black.ad_b_ch = "oppo公司"
    ad_black.ad_b_en = "R9"
    ad_black.ad_b_value = json.dumps(['10021', '10032', '10043'])
    ad_black.save(using='cld')

    brand = OnlineBrandAdV20200709Cld()
    brand.ob_ad_redis_cache = 1
    brand.ob_ad_bid = 'brand_1'
    brand.ob_ad_name = '雅诗兰黛'
    brand.ob_ad_de_name = '润肤精华液'
    brand.ob_ad_data = json.dumps({"product":"雅诗兰黛","version":"v2","name":"润肤精华液","monitor_url":"监控链接"})
    brand.ob_ad_budget = 888888
    brand.save(using='cld')

    brand = OnlineBrandAdV20200709Cld()
    brand.ob_ad_redis_cache = 1
    brand.ob_ad_bid = 'brand_2'
    brand.ob_ad_name = '北京现代汽车'
    brand.ob_ad_de_name = 'suv旗舰版'
    brand.ob_ad_data = json.dumps({"product":"北京现代汽车","version":"v2","name":"北京现代汽车","monitor_url":"监控链接"})
    brand.ob_ad_budget = 66666
    brand.save(using='cld')

    brand = OnlineBrandAdV20200709Cld()
    brand.ob_ad_redis_cache = 1
    brand.ob_ad_bid = 'brand_3'
    brand.ob_ad_name = '肯德基'
    brand.ob_ad_de_name = '肯德基夏日套餐'
    brand.ob_ad_data = json.dumps({"product":"kfc","version":"v1","name":"肯德基","monitor_url":"监控链接"})
    brand.ob_ad_budget = 555555
    brand.save(using='cld')

    black = AdBlackUidV20200710Cld()
    black.ad_b_ch = '雅诗兰黛黑名单'
    black.ad_b_en = 'yashi_black'
    black.ad_b_value = json.dumps(['10021', '10032', '10043'])
    black.ad_b_is_redis_cache = 1
    black.save(using='cld')

    black = AdBlackUidV20200710Cld()
    black.ad_b_ch = '北京现代黑名单'
    black.ad_b_en = 'beijing_black'
    black.ad_b_value = json.dumps(['10021', '10032', '10043'])
    black.ad_b_is_redis_cache = 1
    black.save(using='cld')

    black = AdBlackUidV20200710Cld()
    black.ad_b_ch = '肯德基黑名单'
    black.ad_b_en = 'kfc_black'
    black.ad_b_value = json.dumps(['10021', '10032', '10043'])
    black.ad_b_is_redis_cache = 1
    black.save(using='cld')

    user = AdUserProfileFeatureV20200709Cld()
    user.u_ch = '张三'
    user.u_en = '10001'
    user.u_value = json.dumps({'age': '11', 'area': '北京', 'device': '安卓', 'sex': '男', 'hobby': '篮球', 'tag': '喜欢购物'})
    user.u_is_redis_cache = 1
    user.save(using='cld')

    user = AdUserProfileFeatureV20200709Cld()
    user.u_ch = '李四'
    user.u_en = '10002'
    user.u_value = json.dumps({'age': '12', 'area': '上海', 'device': 'ios', 'sex': '女', 'hobby': '裙子', 'tag': '喜欢美食'})
    user.u_is_redis_cache = 1
    user.save(using='cld')

    user = AdUserProfileFeatureV20200709Cld()
    user.u_ch = '王五'
    user.u_en = '10003'
    user.u_value = json.dumps({'age': '27', 'area': '成都', 'device': 'ios', 'sex': '女', 'hobby': '汽车', 'tag': '喜欢汽车'})
    user.u_is_redis_cache = 1
    user.save(using='cld')
