from django.conf import settings


# pylint:disable=unused-argument,no-self-use
class DCRouter:
    """
    数据库主从读写分离路由
    """

    def db_for_read(self, model, **hints):
        """
        读取时选择从库
        :param model:
        :param hints:
        :return:
        """
        if model._meta.db_table.endswith('inf'):
            if 'inf_replica' in settings.DATABASES:
                return 'inf_replica'
            return 'inf'
        if model._meta.db_table.endswith('cld'):
            return 'cld'
        if model._meta.db_table.endswith('crw'):
            return 'crw'
        return None

    def db_for_write(self, model, **hints):
        """
        写入时选择主库
        :param model:
        :param hints:
        :return:
        """
        if model._meta.db_table.endswith('cld'):
            return 'cld'
        if model._meta.db_table.endswith('inf'):
            return 'inf'
        if model._meta.db_table.endswith('crw'):
            return 'crw'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return True
