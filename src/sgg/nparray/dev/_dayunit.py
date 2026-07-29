from numpy import dtype,datetime64
from re import compile
__all__=["_dt64_unit","_get_dt64_unit",]
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


def _normalize_unit(unit: str):
    return _UNIT_ALIASES.get(unit, unit)


def _get_dt64_unit(value):
    s = _to_str(value).strip()
    m = _DTYPE_PATTERN.match(s)
    if m is not None:
        unit = m.group("unit")
        return _normalize_unit(unit) if unit is not None else ""
    normalized = _normalize_unit(s)
    if normalized in _VALID_UNITS:
        return normalized
    raise ValueError(f"認識できないdatetime64の単位/dtype文字列です: {value!r}")


def _dt64_unit(value):
    if isinstance(value, datetime64):
        return value
    unit = _get_dt64_unit(value)
    return f"datetime64[{unit}]" if unit else "datetime64"
