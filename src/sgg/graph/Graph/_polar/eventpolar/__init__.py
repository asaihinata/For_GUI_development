from ...dev import *

__all__=['Eventpolar']
class Eventpolar(polarElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.data=NPNumber(kw.get('data'))
  self.orientation=listchose(kw.get('orientation'),['vertical','horizontal'])
  self.linewidth=num0(kw.get('linewidth'),1)
  self.linelength=num0(kw.get('linelength'),1)
  self.linestyle=Solid(kw.get('linestyle','-')).solid
  self.plot(self.data,orientation=self.orientation,linewidth=self.linewidth,linelength=self.linelength,alpha=self.alpha,linestyle=self.linestyle)
 def plot(self,data,orientation='vertical',linewidth=1,linelength=1,alpha=1,linestyle=None):
  self.clear()
  self.graphdata=[self.ax.eventplot(ds,lineoffsets=self._places(data.ndim+1)[i],alpha=alpha,linelengths=linelength,linewidths=linewidth,orientation=orientation,linestyles=linestyle)for i,ds in enumerate(data)]
  self._adjustment()
 def update(self,data=None,**kw):
  self._updates(**kw)
  if isinstance(data,nListlike):self.data=NPNumber(data)
  self.orientation=listchose(kw.get('orientation'),['vertical','horizontal'],self.orientation)
  self.linewidth=num0(kw.get('linewidth'),self.linewidth)
  self.linelength=num0(kw.get('linelength'),self.linelength)
  self.linestyle=Solid(kw.get('linestyle',self.linestyle)).solid
  self.plot(self.data,orientation=self.orientation,linewidth=self.linewidth,linelength=self.linelength,alpha=self.alpha,linestyle=self.linestyle)
  self._redraw()
 def get(self):return self.graphdata
 def getdata(self):return self.data