__all__ = ["urlFormat", "linkcheck"]

def urlFormat(link: str) -> bool:
    """指定された値が有効なURLか判定する

    :param link: 値を指定する
    :type link: str
    :return: 指定された値が有効なURLか返す
    :rtype: bool
    """

def linkcheck(link: str, timeout: int = 5) -> bool:
    """指定されたURLが実際に存在するか判定する

    :param link: 値を指定する
    :type link: str
    :param timeout: 応答を待つ秒数を指定する
    :type timeout: int
    :return: 指定されたURLが実際に存在するか返す
    :rtype: bool
    """
