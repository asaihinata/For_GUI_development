from ..dev import *
class Eventpolar(polarElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.data=self._dataarr(kw.get('data'))
  self.orientation=listchose(kw.get('orientation'),['vertical','horizontal'])
  self.linewidth=num0(kw.get('linewidth'),1)
  self.linelength=num0(kw.get('linelength'),1)
  self.linestyle=Solid(kw.get('linestyle','-')).solid
  self.plot(
self.data,
orientation=self.orientation,
linewidth=self.linewidth,
linelength=self.linelength,
alpha=self.alpha,
linestyle=self.linestyle
)
 def plot(self,data,orientation='vertical',linewidth=1,linelength=1,alpha=1,linestyle=None):
  self.clear()
  place=self._places(self.max_depth)
  self.graphdata=[self.ax.eventplot(ds,lineoffsets=place[i],alpha=alpha,linelengths=linelength,linewidths=linewidth,orientation=orientation,linestyles=linestyle)for i,ds in enumerate(data)]
  self._adjustment()
 def update(self,x=None,y=None,data=None,**kw):
  self._updates(**kw)
  if not isinstance(x,nListlike):x=self.x
  if not isinstance(y,nListlike):y=self.y
  self.x,self.y=self._xyd(x,y,data)
  self.width=range_num(num0s(kw.get('width'),self.width),0,1,self.width)
  self.align=listchose(kw.get('align'),['center','edge'],self.align)
  self.logs=bols(kw.get('logs'),self.logs)
  self.plot(self.x,self.y,alpha=self.alpha,width=self.width,align=self.align,logs=self.logs,color=self.color)
  self._redraw()
 def get(self):return [self.graphdata]
 def getx(self):return self.x
 def gety(self):return self.y