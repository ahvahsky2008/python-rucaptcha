import asyncio

from python_rucaptcha.core.enums import FunCaptchaEnm
from python_rucaptcha.fun_captcha import FunCaptcha

# Rucaptcha API Key from your account
RUCAPTCHA_KEY = "ad9053f111111111111111fa758570"


publickey = "69A21A01-CC7B-B9C6-1111-E7FA06677FFC"
pageurl = "https://api.funcaptcha.com/fc/api/nojs/"
surl = "https://client-api.arkoselabs.com"

fun_captcha = FunCaptcha(
    rucaptcha_key=RUCAPTCHA_KEY, pageurl=pageurl, publickey=publickey, surl=surl, method=FunCaptchaEnm.FUNCAPTCHA.value
)
result = fun_captcha.captcha_handler()
print(result)


async def run():
    try:
        result = await FunCaptcha(
            rucaptcha_key=RUCAPTCHA_KEY,
            pageurl=pageurl,
            publickey=publickey,
            surl=surl,
            method=FunCaptchaEnm.FUNCAPTCHA.value,
        ).aio_captcha_handler()
        print(result)
    except Exception as err:
        print(err)


asyncio.run(run())
