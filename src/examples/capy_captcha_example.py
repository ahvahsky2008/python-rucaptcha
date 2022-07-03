import asyncio

from python_rucaptcha.CapyPuzzle import CapyPuzzle, aioCapyPuzzle
from python_rucaptcha.enums import CapyPuzzleEnm

# Rucaptcha API Key from your account
RUCAPTCHA_KEY = "ad9053f3182ca81755768608fa758570"
captchakey = "PUZZLE_Cme4hZLjuZRMYC3uh14C52D3uNms5w"
pageurl = "https://www.capy.me/account/register/"
api_server = "https://jp.api.capy.me/"
versions = ["puzzle", "avatar"]

capy = CapyPuzzle(
    rucaptcha_key=RUCAPTCHA_KEY,
    captchakey="PUZZLE_Cme4hZLjuZRMYC3uh14C52D3uNms5w",
    pageurl="https://www.capy.me/account/register/",
    method=CapyPuzzleEnm.CAPY.value,
    api_server=api_server,
    version=versions[0],
)
result = capy.captcha_handler()

print(result)


async def run():
    try:
        result = await aioCapyPuzzle(
            rucaptcha_key=RUCAPTCHA_KEY,
            captchakey="PUZZLE_Cme4hZLjuZRMYC3uh14C52D3uNms5w",
            pageurl="https://www.capy.me/account/register/",
            method=CapyPuzzleEnm.CAPY.value,
            api_server=api_server,
            version=versions[0],
        ).captcha_handler()
        print(result)
    except Exception as err:
        print(err)


asyncio.run(run())
