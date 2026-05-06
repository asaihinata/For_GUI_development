from os import system as sys
from platform import system
from typing import Any

__all__=['clear']
class clear:
 '''コンソールを削除する。'''
 def __init__(self)->None:sys('cls' if system()=='Windows'else'clear')
 @classmethod
 def __instancecheck__(cls,ins:Any)->bool:return isinstance(ins,clear)