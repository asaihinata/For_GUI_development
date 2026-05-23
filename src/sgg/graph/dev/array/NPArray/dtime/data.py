from typing import Literal,TypeAlias
__all__=['TypeDlike','serch_dtype','DTYPE_LIST','DTYPE_SHORT_LIST','DTYPE_DICT']
TypeDlike:TypeAlias=Literal['datetime64[Y]','datetime64[M]','datetime64[W]','datetime64[D]','datetime64[h]','datetime64[m]','datetime64[s]','datetime64[ms]','datetime64[us]','datetime64[ns]','datetime64[ps]','datetime64[fs]','datetime64[as]','Y','M','W','D','h','m','s','ms','us','ns','ps','fs','as']|None
def serch_dtype(dtype='datetime64[ms]'):
 if dtype in DTYPE_LIST:return dtype
 elif dtype in DTYPE_SHORT_LIST:return DTYPE_DICT.get(dtype)
 return 'datetime64[ms]'
DTYPE_LIST:list[str]=[
'datetime64[Y]',
'datetime64[M]',
'datetime64[W]',
'datetime64[D]',
'datetime64[h]',
'datetime64[m]',
'datetime64[s]',
'datetime64[ms]',
'datetime64[us]',
'datetime64[ns]',
'datetime64[ps]',
'datetime64[fs]',
'datetime64[as]'
]
DTYPE_SHORT_LIST:list[str]=[
'Y','M','W',
'D','h','m',
's','ms','us',
'ns','ps','fs',
'as'
]
DTYPE_DICT:dict[str,str]={
'Y':'datetime64[Y]',
'M':'datetime64[M]',
'W':'datetime64[W]',
'D':'datetime64[D]',
'h':'datetime64[h]',
'm':'datetime64[m]',
's':'datetime64[s]',
'ms':'datetime64[ms]',
'us':'datetime64[us]',
'ns':'datetime64[ns]',
'ps':'datetime64[ps]',
'fs':'datetime64[fs]',
'as':'datetime64[as]'
}