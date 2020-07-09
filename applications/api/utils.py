import json
import logging
import re
import time
import uuid

from django.conf import settings

from applications.api.exception import ExternalServerCalledFailure, ChannelException
from applications.api.signals import *
from applications.email import send_warning_mail


LOGGER = logging.getLogger('console_logger')

