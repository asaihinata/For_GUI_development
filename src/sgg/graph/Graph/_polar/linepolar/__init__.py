from ...dev import *
class Linepolar(polarElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.x,self.y=self._xyd(kw.get('x'),kw.get('y'),kw.get('data'))
  self.markersize=num0(kw.get('markersize'),10)
  self.marker=Marker(kw.get('marker','.')).marker
  self.line=Solid(kw.get('linestyle','-')).solid
  self.linewidth=num0(kw.get('linewidth'),2)
  self.plot(self.x,self.y,marker=self.marker,linewidth=self.linewidth,linestyle=self.line,markersize=self.markersize,alpha=self.alpha)
 def plot(self,x,y,marker='o',linewidth=2,linestyle='-',markersize=10,alpha=1):
  self.clear()
  self.graphdata=[self.ax.plot(x,y,marker=marker,linewidth=linewidth,markersize=markersize,linestyle=linestyle,alpha=alpha)]
  self._adjustment()
 def update(self,x=None,y=None,data=None,**kw):
  self._updates(**kw)
  if not isinstance(x,nListlike):x=self.x
  if not isinstance(y,nListlike):y=self.y
  self.x,self.y=self._xyd(x,y,data)
  self.markersize=num0(kw.get('markersize'),10)
  self.marker=Marker(kw.get('marker',self.marker)).marker
  self.line=Solid(kw.get('linestyle',self.line)).solid
  self.linewidth=num0(kw.get('linewidth'),2)
  self.plot(self.x,self.y,marker=self.marker,linewidth=self.linewidth,linestyle=self.line,markersize=self.markersize,alpha=self.alpha)
  self._redraw()
 def get(self):return self.graphdata
 def getx(self):return self.x
 def gety(self):return self.y