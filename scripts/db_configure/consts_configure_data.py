import json

from applications.orms.crw_model import ConstConfigureV20191017Crw, AdBlackUidV20200710Cld, OnlineBrandAdV20200709Cld


def run():
    """常量数据配置表"""
    cc_obj = ConstConfigureV20191017Crw()
    cc_obj.cc_id = 1
    cc_obj.cc_name_en = 'scene_map'
    cc_obj.cc_name_ch = "场景映射"
    cc_obj.cc_value = json.dumps({
        'mainfeed': ['sfst', 'douyin'],
    })
    cc_obj.save(using='crw')

    ad_black = AdBlackUidV20200710Cld()
    ad_black.ad_b_is_redis_cache = 1
    ad_black.ad_b_ch = "小米公司"
    ad_black.ad_b_en = "Redmi"
    ad_black.ad_b_value = json.dumps(['001', '002', '003'])
    ad_black.save(using='cld')

    ad_black = AdBlackUidV20200710Cld()
    ad_black.ad_b_is_redis_cache = 1
    ad_black.ad_b_ch = "华为荣耀"
    ad_black.ad_b_en = "P30"
    ad_black.ad_b_value = json.dumps(['007', '008', '009'])
    ad_black.save(using='cld')

    ad_black = AdBlackUidV20200710Cld()
    ad_black.ad_b_is_redis_cache = 1
    ad_black.ad_b_ch = "oppo公司"
    ad_black.ad_b_en = "R9"
    ad_black.ad_b_value = json.dumps(['021', '032', '043'])
    ad_black.save(using='cld')

    brand = OnlineBrandAdV20200709Cld()
    brand.ob_ad_redis_cache = 1
    brand.ob_ad_bid = 'brand_1'
    brand.ob_ad_name = '雅诗兰黛'
    brand.ob_ad_de_name = '润肤精华液'
    brand.ob_ad_data = json.dumps({'image': 'image'})
    brand.ob_ad_budget = 888888
    brand.save(using='cld')

    brand = OnlineBrandAdV20200709Cld()
    brand.ob_ad_redis_cache = 1
    brand.ob_ad_bid = 'brand_2'
    brand.ob_ad_name = '北京现代汽车'
    brand.ob_ad_de_name = 'suv旗舰版'
    brand.ob_ad_data = json.dumps({'image': 'image'})
    brand.ob_ad_budget = 66666
    brand.save(using='cld')

    brand = OnlineBrandAdV20200709Cld()
    brand.ob_ad_redis_cache = 1
    brand.ob_ad_bid = 'brand_3'
    brand.ob_ad_name = '肯德基'
    brand.ob_ad_de_name = '肯德基夏日套餐'
    brand.ob_ad_data = json.dumps({'image': 'image'})
    brand.ob_ad_budget = 555555
    brand.save(using='cld')

    black = AdBlackUidV20200710Cld()
    black.ad_b_ch = '雅诗兰黛黑名单'
    black.ad_b_en = 'yashi_black'
    black.ad_b_value = json.dumps(['021', '032', '043'])
    black.ad_b_is_redis_cache = 1
    black.save(using='cld')

    black = AdBlackUidV20200710Cld()
    black.ad_b_ch = '北京现代黑名单'
    black.ad_b_en = 'beijing_black'
    black.ad_b_value = json.dumps(['021', '032', '043'])
    black.ad_b_is_redis_cache = 1
    black.save(using='cld')

    black = AdBlackUidV20200710Cld()
    black.ad_b_ch = '肯德基黑名单'
    black.ad_b_en = 'kfc_black'
    black.ad_b_value = json.dumps(['021', '032', '043'])
    black.ad_b_is_redis_cache = 1
    black.save(using='cld')
