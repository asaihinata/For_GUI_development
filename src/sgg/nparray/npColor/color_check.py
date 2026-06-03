from re import compile,findall
import numpy as np
__all__=['check']
HEX6_RE=compile(r'^#[0-9a-f]{6}$')
HEX3_RE=compile(r'^#[0-9a-f]{3}$')
RGB_RE=compile(r'^rgb\((\d+),(\d+),(\d+)\)$')
RGBA_RE=compile(r'^rgba\((\d+),(\d+),(\d+),([0-9.]+)\)$')
HSV_RE=compile(r'^hsv\((\d+),(\d+),(\d+)\)$')
def chagehex6(val):
 val=val[0][1:]
 return np.fromiter((int(val[i:i+2],16)for i in range(0,len(val),2)),dtype=np.int16)
def chage(val):return np.array(val[0],np.int8)
def check(name):
 if name[0]=='#':
  if HEX6_RE.match(name):return chagehex6(findall(HEX6_RE,name))
  if HEX3_RE.match(name):
   def sets(t):return f'{t}{t}'
   val=findall(HEX3_RE,name)[0][1:]
   return np.fromiter((int(sets(val[i:i+1]),16)for i in range(0,len(val))),dtype=np.int16)
 if RGB_RE.match(name):return chage(findall(RGB_RE,name))
 if RGBA_RE.match(name):return chage(findall(RGBA_RE,name))
 if HSV_RE.match(name):return chage(findall(HSV_RE,name))