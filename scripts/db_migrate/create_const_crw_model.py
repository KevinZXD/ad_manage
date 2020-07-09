from django.db import connections

from applications.orms import crw_model as models


def run():
    connection = connections['crw']
    with connection.schema_editor() as schema_editor:
        # 创建
        schema_editor.create_model(models.ConstConfigureV20191017Crw)
    connection = connections['cld']
    with connection.schema_editor() as schema_editor:
        # 创建
        schema_editor.create_model(models.AdUserProfileFeatureV20200709Cld)
        schema_editor.create_model(models.OnlineBrandAdV20200709Cld)
        schema_editor.create_model(models.AdBlackUidV20200710Cld)

