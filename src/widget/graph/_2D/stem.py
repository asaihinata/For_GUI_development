from itertools import product
from .._graphhelp import *
stem_line_list=['-','--','-.','-.']
stem_mark_list=['o','+','*','.','x','_','|','square','diamond','^','v','<','>','pentagram','hexagram']
stem_color_list=['r','g','b','c','m','y','k','w']
class Stem(twoDElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.x=self._manyarr(kw.get('x'))
  self.y=self._manyarr(kw.get('y'))
  self.colorlist=self._list_loop(self._stem_color_check(kw.get('color')),self.max_depth)
  self.line=self._list_loop(self._linefmt(kw.get('line')),self.max_depth)
  self.marker=self._list_loop(self._markerfmt(kw.get('marker')),self.max_depth)
  self.label=self.labels(kw.get('label'))[0]
  self.bottom=num0s(kw.get('bottom'))
  self.orientation=listchose(kw.get('orientation'),['vertical','horizontal'])
  self.plot(self.x,self.y,bottom=self.bottom,orientation=self.orientation,label=self.label,marker=self.marker,alpha=self.alpha)
 def plot(self,x,y,bottom=0,orientation='vertical',label=None,marker=stem_mark_list,alpha=1):
  self.clear()
  for i,(xs,ys) in enumerate(product(x,y)):
   stem=self.ax.stem(xs,ys,linefmt=self._lsmc(i),markerfmt=self._markerfmt(marker)[i],basefmt=self._lsmc(i),bottom=bottom,orientation=orientation,label=label[i])
   for j in stem.get_children():j.set_alpha(alpha)
   self.graphdata.append(stem)
  self._apply_labels(self.xlabel,self.ylabel)
  self.legend()
  self._adjustment()
 def update(self,x=None,y=None,**kw):
  self._updates(**kw)
  if isinstance(x,np.ndarray|list|tuple):self.x=self._manyarr(x)
  if isinstance(y,np.ndarray|list|tuple):self.y=self._manyarr(y)
  self.colorlist=self._list_loop(self._stem_color_check(self.colorlist),self.max_depth)
  self.line=self._list_loop(self._linefmt(kw.get('line',self.line)),self.max_depth)
  self.marker=self._list_loop(self._markerfmt(kw.get('marker',self.marker)),self.max_depth)
  self.bottom=num0s(kw.get('bottom'),self.bottom)
  self.orientation=listchose(kw.get('orientation'),['vertical','horizontal'],self.orientation)
  self.plot(self.x,self.y,bottom=self.bottom,orientation=self.orientation,label=self.label,marker=self.marker)
  self._redraw()
 def get(self):return self.graphdata
 def getx(self):return self.x
 def gety(self):return self.y
 def _linefmt(self,line):
  set_arr=[]
  if isinstance(line,str):set_arr=[listchose(line,stem_line_list)]
  elif isinstance(line,list|tuple):
   for i in line:
    if i in stem_line_list:set_arr.append(i)
  if len(set_arr)==0:return stem_line_list
  return set_arr
 def _markerfmt(self,marker):
  set_arr=[]
  if isinstance(marker,str):set_arr=[listchose(marker,stem_mark_list)]
  elif isinstance(marker,list|tuple):
   for i in marker:
    if i in stem_mark_list:set_arr.append(i)
  if len(set_arr)==0:set_arr=stem_mark_list
  return set_arr
 def _lsmc(self,val):return FMT(self.marker[val],self.line[val],self.colorlist[val]).fmt_txt
 def _stem_color_check(self,color):
  set_arr,set_color_arr=[],[]
  if isinstance(color,list|tuple):
   for i in color:
    if i in stem_color_list:set_color_arr.append(i)
   if len(set_color_arr)==0:color=stem_color_list
  elif isinstance(color,str):color=color
  else:color=stem_color_list
  for k,v in {'r':['r','red'],'g':['g','green'],'b':['b','blue'],'c':['c','cyan'],'m':['m','magenta'],'y':['y','yellow'],'k':['k','black'],'w':['w','white']}.items():
   if isinstance(color,str) and color in v:set_arr=[k]
   elif isinstance(color,list|tuple):
    for i in color:
     if i in v:set_arr.append(k)
  return set_arr