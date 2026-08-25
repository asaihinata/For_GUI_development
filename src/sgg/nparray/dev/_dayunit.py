from re import compile

from numpy import datetime64, dtype

__all__ = [
    "_dt64_unit",
    "_get_dt64_unit",
]
_VALID_UNITS = frozenset(
    {"Y", "M", "W", "D", "h", "m", "s", "ms", "us", "ns", "ps", "fs", "as"}
)
_UNIT_ALIASES = {"μs": "us"}
_DTYPE_PATTERN = compile(r"^(?:datetime64|[|=<>]?M8)(?:\[(?P<unit>[^\[\]]+)\])?$")


def _to_str(value):
    if isinstance(value, bytes):
        return value.decode("ascii")
    if isinstance(value, str):
        return value
    try:
        return str(dtype(value))
    except TypeError:
        pass
    raise TypeError(f"{value}にはstrまたはbytesを指定してください")


def _normalize_unit(unit):
    return _UNIT_ALIASES.get(unit, unit)


def _get_dt64_unit(value):
    s = _to_str(value).strip()
    m = _DTYPE_PATTERN.match(s)
    if m is not None:
        unit = m.group("unit")
        return "" if unit is None else _normalize_unit(unit)
    normalized = _normalize_unit(s)
    if normalized in _VALID_UNITS:
        return normalized
    raise ValueError(f"{value}は認識できないdatetime64の単位もしくはdtypeの文字列です")


def _dt64_unit(value):
    if isinstance(value, datetime64):
        return value
    unit = _get_dt64_unit(value)
    return f"datetime64[{unit}]" if unit else "datetime64[D]"
