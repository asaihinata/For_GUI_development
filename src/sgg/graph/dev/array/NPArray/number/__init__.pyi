from ..base import NPArray
__all__=['NPNumber']
class NPNumber(NPArray):
 def __init__(self,data,dtype=None):...
 def cussum(self)->NPNumber:'''一つ前の元の値との和を求める。'''
 def cumprod(self)->NPNumber:'''一つ前の元の値との積を求める。'''