from requests import get
from requests.exceptions import RequestException

__all__ = ["get_link_img"]


def get_link_img(link: str) -> bytes:
    """
    画像リンクからバイトデータに変換させる

    :param link: 画像リンクを指定する
    :type link: str
    :raises RequestException: リクエスト処理中に例外が発生した場合に発生させる
    :return: バイトデータを返す
    :rtype: bytes
    """
    try:
        response = get(link)
        response.raise_for_status()
        return response.content
    except RequestException as e:
        raise RequestException(e)
