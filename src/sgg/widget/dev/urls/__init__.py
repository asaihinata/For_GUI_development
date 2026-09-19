from requests import get
from validators.url import url

__all__ = ["urlFormat", "linkcheck"]


def urlFormat(link):
    if url(link):
        return True
    else:
        return False


def linkcheck(link, timeout=5):
    if isinstance(timeout, float):
        timeout = int(timeout)
    elif not isinstance(timeout, int) or timeout < 0:
        timeout = 5
    if not urlFormat(link):
        return False
    try:
        response = get(link, timeout=timeout)
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False
