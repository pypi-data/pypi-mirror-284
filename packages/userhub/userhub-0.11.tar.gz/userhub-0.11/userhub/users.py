"""
Functionality of working with users
"""

from libdev.req import fetch
from libdev.log import log


LINK = "https://chill.services/api/"


async def get(
    token: str,
    data: dict = None,
):
    """Get"""

    if data is None:
        data = {}

    req = {
        "token": token,
        **data,
    }

    code, res = await fetch(LINK + "users/get/", req)
    if code != 200:
        log.error(f"{code}: {res}")
        return res
    return res
