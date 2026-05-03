from re import fullmatch
from numpy import pi
from ....types import Numbertype
from ..._function import listchose
__all__=['Angle','FMT','FMTSOLID','FMTSOLIDLIST','Hatch','Marker','NSolid','SCapstyle','Solid','SOLIDLIST','Textcoords','XYcoords']
COLOR=['b','c','g','k','m','r','w','y']
HATCH=[None,'o','oo','O','OO','x','xx','*','**','*-','+','++','+o','-','--','-\\\\','.','..','/','//','/o','O.','O|','\\','\\\\','\\|','o-','x*','|','|*','||']
MARKERS=[0,1,2,3,4,5,6,7,8,9,10,11,'1','2','3','4','8','d','D','h','H','none','None','o','p','P','s','v','x','X','',' ','*','+',',','.','<','>','^','_','|']
FMTMARKERS=['.','s','o','p','v','*','^','D']
FMTSOLID={'-':['-','solid'],'--':['--','dashed'],'-.':['-.','dashdot'],':':[':','dotted']}
FMTSOLIDLIST=['dashdot','dashed','dotted','solid','-','--','-.',':']
SOLID={'solid':['-','solid'],'dashed':['--','dashed'],'dashdot':['-.','dashdot'],'dotted':[':','dotted'],'None':['none',None,'None',' ','']}
SOLIDLIST=['dashdot','dashed','dotted','none',None,'None','solid','',' ','-','--','-.',':']
# スタイル
class Hatch:
 def __init__(self,hatch=None):self.hatch=[self._get(i) for i in hatch] if isinstance(hatch,list|tuple) else [self._get(hatch)]
 def _get(self,val):return val if val in HATCH else None
 def __iter__(self):return iter(self.hatch)
 def __len__(self):return len(self.hatch)
 def __str__(self):return self.hatch[0]
class Solid:
 def __init__(self,solid=None):self.solid=[self._get(i) for i in solid] if isinstance(solid,list|tuple) else [self._get(solid)]
 def _get(self,val):
  for k,v in FMTSOLID.items():
   if val in v:return k
  return 'solid'
 def __iter__(self):return iter(self.solid)
 def __len__(self):return len(self.solid)
 def __str__(self):return self.solid[0]
class NSolid:
 def __init__(self,solid=None):self.solid=[self._get(i) for i in solid] if isinstance(solid,list|tuple) else [self._get(solid)]
 def _get(self,val):
  for k,v in SOLID.items():
   if val in v:return k
  return None
 def __iter__(self):return iter(self.solid)
 def __len__(self):return len(self.solid)
 def __str__(self):return self.solid[0]
class Marker:
 def __init__(self,marker=None):self.marker=[self._get(i) for i in marker] if isinstance(marker,list|tuple) else [self._get(marker)]
 def _get(self,val):
  if(isinstance(val,str)and fullmatch(r'\$[a-zA-Z]\$',val)or(val in MARKERS)):return val
  else:return None
 def __iter__(self):return iter(self.marker)
 def __len__(self):return len(self.marker)
 def __str__(self):return self.marker[0]
class SCapstyle:
 def __init__(self,style='butt'):self.style=[listchose(i,['butt','projecting','round']) for i in style] if isinstance(style,list|tuple) else [listchose(style,['butt','projecting','round'])]
 def __iter__(self):return iter(self.style)
 def __len__(self):return len(self.style)
 def __str__(self):return self.style[0]
class FMT:
 def __init__(self,marker=None,line=None,color=None):
  self.t=''
  if marker!=None and marker in FMTMARKERS:self.t=self.t+marker
  if line!=None and isinstance(line,str):
   for k,v in FMTSOLID.items():
    if line in v:
     self.t=self.t+k
     break
  if color!=None and color in COLOR:self.t=self.t+color
 def __str__(self):return str(self.t)
# 数値
class Angle:
 def __init__(self,val,now='degrees',do='radian'):
  now,do=listchose(now,['degrees','radian']),listchose(do,['degrees','radian'])
  if not isinstance(val,Numbertype):val=0
  if now==do:self.val=val
  elif now=='degrees' and do=='radian':self.val=val*(pi/180)
  elif now=='radian' and do=='degrees':self.val=val*(180/pi)
 def __int__(self):return int(self.val)
 def __float__(self):return float(self.val)
class XYcoords:
 coordslist=['data','axes fraction','axes pixels','axes points','figure fraction','figure pixels','figure points']
 def __init__(self,arg):
  if arg in self.coordslist:self.xycoords=arg
  else:self.xycoords=None
 def get(self):return self.xycoords
 def __iter__(self):return iter(self.coordslist)
 def __str__(self):
  if self.xycoords==None or self.xycoords is None:return str('')
  return str(self.xycoords)
class Textcoords:
 coordslist=['data','axes fraction','axes pixels','axes points','figure fraction','figure pixels','figure points','offset pixels','offset points']
 def __init__(self,arg):
  if arg in self.coordslist:self.xycoords=arg
  else:self.textcoords=None
 def get(self):return self.textcoords
 def __iter__(self):return iter(self.coordslist)
 def __str__(self):
  if self.xycoords==None or self.xycoords is None:return str('')
  return str(self.xycoords)