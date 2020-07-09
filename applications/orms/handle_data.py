import logging

from django import db
from django.db import IntegrityError
from retrying import retry

from applications.api.exception import DataException

LOGGER = logging.getLogger('console_logger')


class SaveData:
    @staticmethod
    @retry(retry_on_exception=lambda arg: isinstance(arg, db.utils.OperationalError), wait_fixed=500,
           stop_max_attempt_number=5)
    def insert_mysql_record_data(data, db_name):
        try:
            LOGGER.info('mysql 开始：mysql数据库插入数据')
            data.save(using=db_name)
            LOGGER.info(' mysql 成功：mysql数据库插入数据成功')
        except db.utils.OperationalError as error:
            raise error
        except IntegrityError as error:
            # Duplicate Entry
            if error.args[0] != 1062:
                raise error
        except Exception as error:
            LOGGER.error('mysql 失败：mysql插入数据错误')
            LOGGER.error(error)
            raise DataException(error)
