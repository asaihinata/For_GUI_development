"""フレームワーク全体で使用する型を設定しているモジュール"""

from re import compile, fullmatch

__VALID_UNITS = {
    "Y",
    "M",
    "W",
    "D",
    "h",
    "m",
    "s",
    "ms",
    "us",
    "ns",
    "ps",
    "fs",
    "as",
    "μs",
}
__BYTEORDER_CHARS = "|=<>"
__DT64_PATTERN = compile(r"^(?:datetime64|M8)\[(?P<unit>\w+)\]$")
__DT64_GENERIC_PATTERN = compile(r"^(?:datetime64|M8)$")


def _dt64_unit(spec):
    if isinstance(spec, bytes):
        spec = spec.decode("ascii")
    elif not isinstance(spec, str):
        return "datetime64[D]"
    spec = spec.strip()
    if spec and spec[0] in __BYTEORDER_CHARS:
        spec = spec[1:]
    if not spec:
        return "datetime64[D]"
    match = __DT64_PATTERN.match(spec)
    if match:
        unit = match.group("unit")
        if unit not in __VALID_UNITS:
            return "datetime64[D]"
        return f"datetime64[{unit}]"
    if __DT64_GENERIC_PATTERN.match(spec):
        return "datetime64"
    if spec in __VALID_UNITS:
        return f"datetime64[{spec}]"
    return "datetime64[D]"


def _get_dt64_unit(dtype_str, auto="D"):
    if not isinstance(dtype_str, str | bytes):
        return auto
    dtype_str = _dt64_unit(dtype_str)
    if dtype_str[0] in [">", "|", "<", "="]:
        dtype_str = dtype_str[1:]
    m = fullmatch(r"datetime64\[(\w+)\]", dtype_str)
    if m is None:
        return auto
    return m.group(1)
