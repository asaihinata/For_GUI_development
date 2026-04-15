from .._graphhelp import *
class Linefill(twoDElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.x=self._dataarr(kw.get('x'),False)
  self.ymax=self._manyarr(kw.get('ymax'))
  self.ymin=self._manyarr(kw.get('ymin'))
  self.label=self.labels(kw.get('label'))[0]
  self.linewidth=num0(kw.get('linewidth'),0)
  self.centerlinewidth=num0(kw.get('centerlinewidth'),2)
  self.alpha=range_num(num0s(kw.get('alpha'),0.5),0,1,0.5)
  self.plot(self.x,self.ymax,self.ymin,alpha=self.alpha,linewidth=self.linewidth,centerlinewidth=self.centerlinewidth)
 def plot(self,x,ymax,ymin,alpha=0.5,linewidth=0,centerlinewidth=2):
  self.clear()
  for i in range(self.max_depth):
   ya,yi=ymax[i],ymin[i]
   fill=self.ax.fill_between(x,ya,yi,alpha=alpha,linewidth=linewidth,label=self.label[i])
   plot=self.ax.plot(x,(yi+ya)/2,linewidth=centerlinewidth,solid_capstyle='butt')
   self.graphdata.append([fill,plot[0]])
  self._apply_labels(self.xlabel,self.ylabel)
  self.legend()
  self._adjustment()
 def update(self,x=None,ymax=None,ymin=None,**kw):
  self._updates(**kw)
  if isinstance(x,NpArraytype):self.x=self._dataarr(x,False)
  if isinstance(ymax,NpArraytype):self.ymax=self._manyarr(ymax)
  if isinstance(ymin,NpArraytype):self.ymin=self._manyarr(ymin)
  self.linewidth=num0(kw.get('linewidth'),self.linewidth)
  self.centerlinewidth=num0(kw.get('centerlinewidth'),self.centerlinewidth)
  self.plot(self.x,self.ymax,self.ymin,alpha=self.alpha,linewidth=self.linewidth,centerlinewidth=self.centerlinewidth)
  self._redraw()
 def get(self):return self.graphdata
 def getx(self):return self.x
 def getymin(self):return self.ymin
 def getymax(self):return self.ymax