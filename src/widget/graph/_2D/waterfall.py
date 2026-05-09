from .._graphhelp import *
def _bar_x_lists(lists,ylen):
 if ylen==None or not isinstance(lists,np.ndarray|list|tuple):return None
 else:
  lists=lists[0]
  xlen=len(lists)
  return np.array([str(i) for i in lists] if xlen==ylen or xlen<ylen else [lists[i] for i in range(xlen)])
class Waterfall(twoDElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.y=self._dataarr(kw.get('y'),False)
  self.x=_bar_x_lists(self._onearr(kw.get('x')),len(self.y))
  self.bottom=np.cumsum(np.append(0,self.y)[0:np.array(self.y).size])
  self.ucolor=parsecolor(kw.get('ucolor'),'#156082')
  self.dcolor=parsecolor(kw.get('dcolor'),'#e97132')
  self.width=range_num(num0s(kw.get('width'),1),0,1,1)
  self.sums=bols(kw.get('sums'),False)
  self.sumstext=kw.get('sumstext','sum')
  self.colorline=parsecolor(kw.get('colorline'),'#4477aa')
  self.linestyle=Solid(kw.get('linestyle','-')).solid
  self.plot(self.x,self.y,alpha=self.alpha,width=self.width,sums=self.sums,sumstext=self.sumstext,bottom=self.bottom,color=self.colorline,linestyle=self.linestyle)
 def plot(self,x,y,alpha=1,width=1,sums=False,sumstext='sum',bottom=None,color=None,linestyle='-'):
  self.clear()
  if sums:x,y,bottom=np.append(x,sumstext),np.append(y,y.sum()),np.append(bottom,0)
  self.color=np.where(y<=0,self.dcolor,self.ucolor)
  self.graphdata=[self.ax.bar(x,y,color=self.color,alpha=alpha,width=width,align='center',bottom=bottom)]
  self.ax.set_xticks(np.arange(len(x)),labels=x)
  yticks=self.ax.get_yticks()
  self.ax.set_ylim(yticks.min(),yticks.max())
  if width!=1:self._horiline(np.cumsum(y),width,color,linestyle)
  self._apply_labels(self.xlabel,self.ylabel)
 def update(self,x=None,y=None,**kw):
  self._updates(**kw)
  if isinstance(y,np.ndarray|list|tuple):self.y=self._dataarr(y,False)
  if isinstance(x,np.ndarray|list|tuple):self.x=_bar_x_lists(self._onearr(x),len(self.y))
  self.sums=bols(kw.get('sums'),self.sums)
  self.sumstext=kw.get('sumstext',self.sumstext)
  self.bottom=_waterfall_sum(self.y)
  self.ucolor=parsecolor(kw.get('ucolor'),self.ucolor)
  self.dcolor=parsecolor(kw.get('dcolor'),self.dcolor)
  self.width=range_num(num0s(kw.get('width'),self.width),0,1,self.width)
  self.colorline=parsecolor(kw.get('colorline'),self.colorline)
  self.linestyle=str(NSolid(kw.get('linestyle',self.linestyle)))
  self.plot(self.x,self.y,alpha=self.alpha,width=self.width,sums=self.sums,sumstext=self.sumstext,bottom=self.bottom,color=self.colorline,linestyle=self.linestyle)
  self._redraw()
 def get(self):return self.graphdata
 def getx(self):return self.x
 def gety(self):return self.y
 def _horiline(self,lin,width=1,color=None,linestyle='-'):
  lens,width,xmaxs,xmins=len(lin)-1,width/2,[],[]
  for i in range(lens):
   if lin[i]==lin[i+1]:ma,mi=i+width,i+1.5
   else:ma,mi=i+1-width,i+width
   xmaxs.append(ma)
   xmins.append(mi)
  self.ax.hlines(y=lin,xmin=xmins+[0],xmax=xmaxs+[0],colors=color,linestyles=linestyle)
class Waterfallh(twoDElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.y=self._dataarr(kw.get('y'),False)
  self.x=_bar_x_lists(self._onearr(kw.get('x')),len(self.y))
  self.bottom=np.cumsum(np.append(0,self.y)[0:np.array(self.y).size])
  self.ucolor=parsecolor(kw.get('ucolor'),'#156082')
  self.dcolor=parsecolor(kw.get('dcolor'),'#e97132')
  self.height=range_num(num0s(kw.get('height'),1),0,1,1)
  self.sums=bols(kw.get('sums'),False)
  self.sumstext=kw.get('sumstext','sum')
  self.colorline=parsecolor(kw.get('colorline'),'#4477aa')
  self.linestyle=Solid(kw.get('linestyle','-')).solid
  self.plot(self.x,self.y,alpha=self.alpha,height=self.height,sums=self.sums,sumstext=self.sumstext,bottom=self.bottom,color=self.colorline,linestyle=self.linestyle)
 def plot(self,x,y,alpha=1,height=1,sums=False,sumstext='sum',bottom=None,color=None,linestyle='-'):
  self.clear()
  if sums:x,y,bottom=np.append(x,sumstext),np.append(y,y.sum()),np.append(bottom,0)
  self.color=np.where(y<=0,self.dcolor,self.ucolor)
  self.graphdata=[self.ax.barh(x,y,color=self.color,alpha=alpha,height=height,align='center',left=bottom)]
  if height!=1:self._vlines(np.cumsum(y),height,color,linestyle)
  self.ax.set_yticks(np.arange(len(x)),labels=x)
  xticks=self.ax.get_xticks()
  self.ax.set_xlim(xticks.min(),xticks.max())
  self._apply_labels(self.xlabel,self.ylabel)
  self._adjustment()
 def update(self,x=None,y=None,**kw):
  self._updates(**kw)
  if isinstance(y,np.ndarray|list|tuple):self.y=self._dataarr(y,False)
  if isinstance(x,np.ndarray|list|tuple):self.x=_bar_x_lists(self._onearr(x),len(self.y))
  self.bottom=_waterfall_sum(self.y)
  self.sums=bols(kw.get('sums'),self.sums)
  self.sumstext=kw.get('sumstext',self.sumstext)
  self.ucolor=parsecolor(kw.get('ucolor'),self.ucolor)
  self.dcolor=parsecolor(kw.get('dcolor'),self.dcolor)
  self.height=range_num(num0s(kw.get('height'),self.height),0,1,self.height)
  self.colorline=parsecolor(kw.get('colorline'),self.colorline)
  self.linestyle=str(NSolid(kw.get('linestyle',self.linestyle)))
  self.plot(self.x,self.y,alpha=self.alpha,height=self.height,sums=self.sums,sumstext=self.sumstext,bottom=self.bottom,color=self.colorline,linestyle=self.linestyle)
  self._redraw()
 def get(self):return self.graphdata
 def getx(self):return self.x
 def gety(self):return self.y
 def _vlines(self,lin,height=1,color=None,linestyle='-'):
  lens,height,xmaxs,xmins=len(lin)-1,height/2,[],[]
  for i in range(lens):
   if lin[i]==lin[i+1]:ma,mi=i+height,i+1.5
   else:ma,mi=i+1-height,i+height
   xmaxs.append(ma)
   xmins.append(mi)
  self.ax.vlines(x=lin,ymin=xmins+[0],ymax=xmaxs+[0],colors=color,linestyles=linestyle)