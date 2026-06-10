from ...dev import *

__all__=['RadarFill']
class RadarFill(RadarElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.plot(self.data,alpha=self.alpha)
 def plot(self,data,alpha=1):
  self.clear()
  self.graphdata=[self.ax.fill(self.theta,d,alpha=alpha)for d in data]
  self._adjustment()
 def update(self,**kw):
  self._updates(**kw)
  self.plot(self.data,alpha=self.alpha)
  self._redraw()
 def getdata(self):return self.data.tonp()
 def get(self):return self.graphdata