import os

from django.conf import settings
from kombu import Exchange

redis_socket_timeout = 3
redis_url = settings.CACHES['default']['LOCATION'][:-2]

broker_url = '{0}14'.format(redis_url)
result_backend = '{0}15'.format(redis_url)

default_exchange = Exchange('default', type='direct')

task_default_queue = 'default'
task_default_exchange = 'default'
task_default_routing_key = 'default'
# 不存储异步任务结果
task_ignore_result = True
broker_transport_options = {'visibility_timeout': 5 * 24 * 3600}

task_acks_late = True
if os.environ.get('celery_always_sync'):
    task_always_eager = True
    task_eager_propagates = True
