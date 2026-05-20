from ...dev import *
class Radarplot(RadarElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.plot(self.data)
 def plot(self,data):
  self.clear()
  self.graphdata=[self.ax.plot(self.theta,d)for d in data]
  self._adjustment()
 def update(self,data=None,**kw):
  self._updates(**kw)
  if not isinstance(data,nListlike):self.data=self._dataarr(data,False).T
  self.plot(self.data)
  self._redraw()
 def get(self):return self.graphdata