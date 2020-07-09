import logging

from django.conf import settings
from django.core.mail import EmailMultiAlternatives

LOGGER = logging.getLogger('console_logger')


def send_mail(subject, content, sender, recipients, attachment):  # coverage:ignore=
    """
    要配置settings.py的邮件服务器才能够发送
    :param subject: 邮件主题
    :param content: 邮件内容
    :param sender:  邮件发送者
    :param recipients: 邮件接收者list
    :param attachment: 邮件附件list
    :return:
    """
    msg = EmailMultiAlternatives(subject, content, sender, recipients)
    msg.content_subtype = "html"
    # 添加附件（可选）
    for attach in attachment:
        msg.attach_file(attach)
    # 发送
    msg.send()


def send_warning_mail(msg, title='第三方服务异常'):
    """
    发邮件函数
    :param msg: 邮件内容
    :param title: 邮件标题
    :return:
    """
    # 邮件提醒
    if settings.ENVIRONMENT == "development":  # coverage:ignore=
        return

    try:
        send_mail('【{}】{}'.format(settings.ENVIRONMENT, title), msg, settings.EMAIL_HOST_USER,
                  settings.RECEIVER_EMAIL_GROUP, [])
    except Exception as error:
        LOGGER.warning('email send error:%s', error)
