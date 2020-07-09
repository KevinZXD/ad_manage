from __future__ import absolute_import, unicode_literals

import logging
import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')

app = Celery('hfax spider collection')

LOGGER = logging.getLogger('console_logger')

app.config_from_object('conf.celery_settings')
# 从所有已注册的Django应用配置中加载任务模块。从而使celery 能够自动发现这些任务
app.autodiscover_tasks()
