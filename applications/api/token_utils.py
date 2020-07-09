import base64
import hmac
import time

from django.conf import settings


def generate_token():
    ts_str = str(time.time() + settings.TOKEN_KEY_EXPIRE_TIME)
    ts_byte = ts_str.encode("utf-8")
    # 加密
    sha1_tshexstr = hmac.new(settings.TOKEN_KEY.encode("utf-8"), ts_byte, 'sha1').hexdigest()
    token = ts_str + ':' + sha1_tshexstr
    b64_token = base64.urlsafe_b64encode(token.encode("utf-8"))
    return b64_token.decode("utf-8")


def certify_token(token):
    if settings.DEBUG:
        return 1
    token = token.replace("%3D", "=")
    token_str = base64.urlsafe_b64decode(token).decode('utf-8')
    token_list = token_str.split(':')
    if len(token_list) != 2:
        return 0
    ts_str = token_list[0]
    if float(ts_str) < time.time():
        # token expired
        return 0
    known_sha1_tsstr = token_list[1]
    sha1 = hmac.new(settings.TOKEN_KEY.encode("utf-8"), ts_str.encode('utf-8'), 'sha1')
    calc_sha1_tsstr = sha1.hexdigest()
    if calc_sha1_tsstr != known_sha1_tsstr:
        # token certification failed
        return 0
    # token certification success
    return 1
