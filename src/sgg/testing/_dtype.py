__all__ = [
    "testing_BoolCodes",
    "testing_BytesCodes",
    "testing_CharacterCodes",
    "testing_CLongDoubleCodes",
    "testing_Complex128Codes",
    "testing_Complex64Codes",
    "testing_ComplexFloatingCodes",
    "testing_DT64Codes",
    "testing_DT64Codes_any",
    "testing_DT64Codes_date",
    "testing_DT64Codes_datetime",
    "testing_DT64Codes_int",
    "testing_FlexibleCodes",
    "testing_Float16Codes",
    "testing_Float32Codes",
    "testing_Float64Codes",
    "testing_FloatingCodes",
    "testing_GenericCodes",
    "testing_InexactCodes",
    "testing_Int16Codes",
    "testing_Int32Codes",
    "testing_Int64Codes",
    "testing_Int8Codes",
    "testing_IntCCodes",
    "testing_IntegerCodes",
    "testing_IntPCodes",
    "testing_LongCodes",
    "testing_LongDoubleCodes",
    "testing_LongLongCodes",
    "testing_NumberCodes",
    "testing_ObjectCodes",
    "testing_SignedIntegerCodes",
    "testing_StrCodes",
    "testing_StringCodes",
    "testing_TD64Codes",
    "testing_TD64Codes_any",
    "testing_TD64Codes_int",
    "testing_TD64Codes_timedelta",
    "testing_UInt16Codes",
    "testing_UInt32Codes",
    "testing_UInt64Codes",
    "testing_UInt8Codes",
    "testing_UIntCCodes",
    "testing_UIntPCodes",
    "testing_ULongCodes",
    "testing_ULongLongCodes",
    "testing_UnsignedIntegerCodes",
    "testing_VoidCodes",
]

testing_BoolCodes = ["bool", "bool_", "?", "b1", "|b1", "=b1", "<b1", ">b1"]

testing_Int8Codes = ["int8", "byte", "b", "i1", "|i1", "=i1", "<i1", ">i1"]
testing_Int16Codes = ["int16", "short", "h", "i2", "|i2", "=i2", "<i2", ">i2"]
testing_Int32Codes = ["int32", "i4", "|i4", "=i4", "<i4", ">i4"]
testing_Int64Codes = ["int64", "i8", "|i8", "=i8", "<i8", ">i8"]

testing_IntCCodes = ["intc", "i", "|i", "=i", "<i", ">i"]
testing_LongCodes = ["long", "l", "|l", "=l", "<l", ">l"]
testing_LongLongCodes = ["longlong", "q", "|q", "=q", "<q", ">q"]
testing_IntPCodes = ["intp", "int", "int_", "n", "|n", "=n", "<n", ">n"]

testing_SignedIntegerCodes = (
    testing_Int8Codes
    + testing_Int16Codes
    + testing_Int32Codes
    + testing_Int64Codes
    + testing_IntCCodes
    + testing_LongCodes
    + testing_LongLongCodes
    + testing_IntPCodes
)

testing_UInt8Codes = ["uint8", "ubyte", "B", "u1", "|u1", "=u1", "<u1", ">u1"]
testing_UInt16Codes = ["uint16", "ushort", "H", "u2", "|u2", "=u2", "<u2", ">u2"]
testing_UInt32Codes = ["uint32", "u4", "|u4", "=u4", "<u4", ">u4"]
testing_UInt64Codes = ["uint64", "u8", "|u8", "=u8", "<u8", ">u8"]

testing_UIntCCodes = ["uintc", "I", "|I", "=I", "<I", ">I"]
testing_ULongCodes = ["ulong", "L", "|L", "=L", "<L", ">L"]
testing_ULongLongCodes = ["ulonglong", "Q", "|Q", "=Q", "<Q", ">Q"]
testing_UIntPCodes = ["uintp", "uint", "N", "|N", "=N", "<N", ">N"]

testing_UnsignedIntegerCodes = (
    testing_UInt8Codes
    + testing_UInt16Codes
    + testing_UInt32Codes
    + testing_UInt64Codes
    + testing_UIntCCodes
    + testing_ULongCodes
    + testing_ULongLongCodes
    + testing_UIntPCodes
)

testing_IntegerCodes = testing_UnsignedIntegerCodes + testing_SignedIntegerCodes

testing_Float16Codes = ["float16", "half", "e", "f2", "|f2", "=f2", "<f2", ">f2"]
testing_Float32Codes = ["float32", "single", "f", "f4", "|f4", "=f4", "<f4", ">f4"]
testing_Float64Codes = [
    "float64",
    "float",
    "double",
    "d",
    "f8",
    "|f8",
    "=f8",
    "<f8",
    ">f8",
]

testing_LongDoubleCodes = ["longdouble", "g", "|g", "=g", "<g", ">g"]

testing_FloatingCodes = (
    testing_Float16Codes
    + testing_Float32Codes
    + testing_Float64Codes
    + testing_LongDoubleCodes
)

testing_Complex64Codes = ["complex64", "csingle", "F", "c8", "|c8", "=c8", "<c8", ">c8"]

testing_Complex128Codes = [
    "complex128",
    "complex",
    "cdouble",
    "D",
    "c16",
    "|c16",
    "=c16",
    "<c16",
    ">c16",
]


testing_CLongDoubleCodes = ["clongdouble", "G", "|G", "=G", "<G", ">G"]

testing_ComplexFloatingCodes = (
    testing_Complex64Codes + testing_Complex128Codes + testing_CLongDoubleCodes
)

testing_InexactCodes = testing_FloatingCodes + testing_ComplexFloatingCodes
testing_NumberCodes = testing_IntegerCodes + testing_InexactCodes

testing_BytesCodes = ["bytes", "bytes_", "S", "|S", "=S", "<S", ">S"]
testing_StrCodes = ["str", "str_", "unicode", "U", "|U", "=U", "<U", ">U"]

testing_CharacterCodes = testing_BytesCodes + testing_StrCodes

testing_VoidCodes = ["void", "V", "|V", "=V", "<V", ">V"]

testing_FlexibleCodes = testing_CharacterCodes + testing_VoidCodes

testing_ObjectCodes = ["object", "object_", "O", "|O", "=O", "<O", ">O"]

# datetime64
testing_DT64Codes_any = ["datetime64", "M", "M8", "|M8", "=M8", "<M8", ">M8"]
testing_DT64Codes_date = [
    "datetime64[Y]",
    "M8[Y]",
    "|M8[Y]",
    "=M8[Y]",
    "<M8[Y]",
    ">M8[Y]",
    "datetime64[M]",
    "M8[M]",
    "|M8[M]",
    "=M8[M]",
    "<M8[M]",
    ">M8[M]",
    "datetime64[W]",
    "M8[W]",
    "|M8[W]",
    "=M8[W]",
    "<M8[W]",
    ">M8[W]",
    "datetime64[D]",
    "M8[D]",
    "|M8[D]",
    "=M8[D]",
    "<M8[D]",
    ">M8[D]",
]
testing_DT64Codes_datetime = [
    "datetime64[h]",
    "M8[h]",
    "|M8[h]",
    "=M8[h]",
    "<M8[h]",
    ">M8[h]",
    "datetime64[m]",
    "M8[m]",
    "|M8[m]",
    "=M8[m]",
    "<M8[m]",
    ">M8[m]",
    "datetime64[s]",
    "M8[s]",
    "|M8[s]",
    "=M8[s]",
    "<M8[s]",
    ">M8[s]",
    "datetime64[ms]",
    "M8[ms]",
    "|M8[ms]",
    "=M8[ms]",
    "<M8[ms]",
    ">M8[ms]",
    "datetime64[us]",
    "M8[us]",
    "|M8[us]",
    "=M8[us]",
    "<M8[us]",
    ">M8[us]",
    "datetime64[μs]",
    "M8[μs]",
    "|M8[μs]",
    "=M8[μs]",
    "<M8[μs]",
    ">M8[μs]",
]
testing_DT64Codes_int = [
    "datetime64[ns]",
    "M8[ns]",
    "|M8[ns]",
    "=M8[ns]",
    "<M8[ns]",
    ">M8[ns]",
    "datetime64[ps]",
    "M8[ps]",
    "|M8[ps]",
    "=M8[ps]",
    "<M8[ps]",
    ">M8[ps]",
    "datetime64[fs]",
    "M8[fs]",
    "|M8[fs]",
    "=M8[fs]",
    "<M8[fs]",
    ">M8[fs]",
    "datetime64[as]",
    "M8[as]",
    "|M8[as]",
    "=M8[as]",
    "<M8[as]",
    ">M8[as]",
]
testing_DT64Codes = (
    testing_DT64Codes_any
    + testing_DT64Codes_date
    + testing_DT64Codes_datetime
    + testing_DT64Codes_int
)

# timedelta64
testing_TD64Codes_any = ["timedelta64", "m", "m8", "|m8", "=m8", "<m8", ">m8"]
testing_TD64Codes_int = [
    "timedelta64[Y]",
    "m8[Y]",
    "|m8[Y]",
    "=m8[Y]",
    "<m8[Y]",
    ">m8[Y]",
    "timedelta64[M]",
    "m8[M]",
    "|m8[M]",
    "=m8[M]",
    "<m8[M]",
    ">m8[M]",
    "timedelta64[ns]",
    "m8[ns]",
    "|m8[ns]",
    "=m8[ns]",
    "<m8[ns]",
    ">m8[ns]",
    "timedelta64[ps]",
    "m8[ps]",
    "|m8[ps]",
    "=m8[ps]",
    "<m8[ps]",
    ">m8[ps]",
    "timedelta64[fs]",
    "m8[fs]",
    "|m8[fs]",
    "=m8[fs]",
    "<m8[fs]",
    ">m8[fs]",
    "timedelta64[as]",
    "m8[as]",
    "|m8[as]",
    "=m8[as]",
    "<m8[as]",
    ">m8[as]",
]
testing_TD64Codes_timedelta = [
    "timedelta64[W]",
    "m8[W]",
    "|m8[W]",
    "=m8[W]",
    "<m8[W]",
    ">m8[W]",
    "timedelta64[D]",
    "m8[D]",
    "|m8[D]",
    "=m8[D]",
    "<m8[D]",
    ">m8[D]",
    "timedelta64[h]",
    "m8[h]",
    "|m8[h]",
    "=m8[h]",
    "<m8[h]",
    ">m8[h]",
    "timedelta64[m]",
    "m8[m]",
    "|m8[m]",
    "=m8[m]",
    "<m8[m]",
    ">m8[m]",
    "timedelta64[s]",
    "m8[s]",
    "|m8[s]",
    "=m8[s]",
    "<m8[s]",
    ">m8[s]",
    "timedelta64[ms]",
    "m8[ms]",
    "|m8[ms]",
    "=m8[ms]",
    "<m8[ms]",
    ">m8[ms]",
    "timedelta64[us]",
    "m8[us]",
    "|m8[us]",
    "=m8[us]",
    "<m8[us]",
    ">m8[us]",
    "timedelta64[μs]",
    "m8[μs]",
    "|m8[μs]",
    "=m8[μs]",
    "<m8[μs]",
    ">m8[μs]",
]
testing_TD64Codes = (
    testing_TD64Codes_any + testing_TD64Codes_int + testing_TD64Codes_timedelta
)

testing_StringCodes = ["T", "|T", "=T", "<T", ">T"]

testing_GenericCodes = (
    testing_BoolCodes
    + testing_NumberCodes
    + testing_FlexibleCodes
    + testing_DT64Codes
    + testing_TD64Codes
    + testing_ObjectCodes
)
