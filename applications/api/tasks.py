import logging

import requests

from applications.email import send_warning_mail
from conf.celery import app as celery_app

LOGGER = logging.getLogger('console_logger')


@celery_app.task(bind=True)
def callback_am_crawl_result_api(self, url, params):
    """运营商授权结果"""
    # 没有服务端的url
    if not url:
        return
    try:

        return
    except Exception as ex:
        self.retry(exc=ex, countdown=2 ** self.request.retries, max_retries=10)
