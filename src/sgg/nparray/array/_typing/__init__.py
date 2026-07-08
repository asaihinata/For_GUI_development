from numpy import datetime64, issubdtype
from numpy._typing._char_codes import _DT64Codes

__all__ = [
    "_ArrayLikeAnyString_co",
    "_ArrayLikeBool_co",
    "_ArrayLikeDateParse_co",
    "_ArrayLikeNumber_co",
    "_ArrayLikeTD64_co",
    "_CharType",
    "_DATE_UNITL",
    "_DT64Codes",
    "_DTypeLikeTD64",
    "_DTypeT",
    "_NATIVETIME_UNITL",
    "_NumberT",
    "_ShapeT",
    "_StrT",
    "ArrayLikeAny",
    "ArrayLikeBool",
    "ArrayLikeDateParse",
    "ArrayLikedatetime",
    "ArrayLikeNS",
    "ArrayLikeNumber",
    "ArrayLikeString",
    "DateParseScalar",
    "DATESUNIT",
    "DateUnit",
    "Incomplete",
    "NativeTimeUnit",
    "serchDtype",
    "TypeArray2LikeAny",
    "TypeArray2LikeBool",
    "TypeArray2Likedatetime",
    "TypeArray2LikeNS",
    "TypeArray2LikeNumber",
    "TypeArray2LikeString",
    "TypeArrayLikeAny",
    "TypeArrayLikeBool",
    "TypeArrayLikedatetime",
    "TypeArrayLikeNS",
    "TypeArrayLikeNumber",
    "TypeArrayLikeString",
    "TypeArraysLikeAny",
    "TypeArraysLikeBool",
    "TypeArraysLikedatetime",
    "TypeArraysLikeNS",
    "TypeArraysLikeNumber",
    "TypeArraysLikeString",
    "TypeNumber",
    "TypeStr",
]


def serchDtype(dtype="datetime64[D]"):
    if issubdtype(dtype, datetime64) or dtype in _DT64Codes:
        return dtype
    return "datetime64[D]"
