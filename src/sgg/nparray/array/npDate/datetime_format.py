from datetime import datetime
from typing import IO, Any

from dateutil.parser import parse

__all__ = ["DatetimeFormat"]


class DatetimeFormat:
    def __init__(
        self,
        timestr: bytes | str | IO[str] | IO[Any],
        dayfirst: bool | None = False,
        yearfirst: bool | None = False,
        ignoretz: bool = False,
        default: datetime | None = None,
    ) -> None:
        """日付の書式フォーマットから`datetime.datetime`オブジェクトに自動で変換するオブジェクト

        :param timestr: 日付,時刻スタンプを含む文字列を指定する
        :type timestr: bytes | str | IO[str] | IO[Any]
        :param dayfirst: 曖昧な3つの整数からなる日付の最初の値を`日`もしくは`月`として解釈するか指定する
        :type dayfirst: bool | None
        :param yearfirst: 曖昧な3つの整数からなる日付の最初の値を年として解釈するか指定する
        :type yearfirst: bool | None
        :param ignoretz: 日付文字列に含まれるタイムゾーン情報を無視するか指定する
        :type ignoretz: bool
        :param default: 指定された`timestr`に欠けている情報がある場合に補う日付時刻の基準を指定する
        :type default: datetime | None"""
        if default == None or not isinstance(default, datetime):
            default = datetime.today()
        self.__datetime = parse(
            timestr,
            parserinfo=None,
            dayfirst=dayfirst,
            yearfirst=yearfirst,
            ignoretz=ignoretz,
            default=default,
        )

    def __repr__(self) -> str:
        return f"DatetimeFormat('{self.datetime}')"

    @property
    def datetime(self) -> datetime:
        """変換された`datetime.datetime`オブジェクトのプロパティ"""
        return self.__datetime
