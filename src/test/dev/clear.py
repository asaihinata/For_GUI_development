'''コンソールを削除するモジュール'''
from os import system as sys
from platform import system
__all__=['clear']
class clear:
 '''コンソールを削除する'''
 def __init__(self)->None:
  '''コンソールを削除する'''
  sys('cls' if system()=='Windows'else'clear')