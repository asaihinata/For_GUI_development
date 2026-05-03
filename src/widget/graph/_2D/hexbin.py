from .._graphhelp import *
class Hexbin(twoDElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.x=self._dataarr(kw.get('x'))
  self.y=self._dataarr(kw.get('y'))
  c,extent,gridsize=kw.get('c'),kw.get('extent'),kw.get('gridsize',100)
  self.c=None if c is None else self._dataarr(c)
  self.gridsize=gridsize if list2int(gridsize) or isinstance(gridsize,int) else 100
  self.extent=extent if list4float(extent) else None
  self.xscale=listchose(kw.get('xscale'),['linear','log'])
  self.yscale=listchose(kw.get('yscale'),['linear','log'])
  self.mincnt=int1s(kw.get('mincnt'))
  bins=kw.get('bins')
  self.bins=bins if(bins=='log' or isinstance(bins,int|float) or (isinstance(bins,list|tuple) and (isinstance(i,int|float)for i in bins)))else None
  self.plot(self.x,self.y,self.c,gridsize=self.gridsize,xscale=self.xscale,yscale=self.yscale,mincnt=self.mincnt,extent=self.extent,bins=self.bins)
 def plot(self,x,y,c,gridsize=100,xscale='linear',yscale='linear',mincnt=None,extent=None,bins=None):
  self.clear()
  self.graphdata=self.ax.hexbin(x,y,c,bins=bins,gridsize=gridsize,xscale=xscale,yscale=yscale,mincnt=mincnt,extent=extent)
  self._apply_labels(self.xlabel,self.ylabel)
  self._adjustment()
 def update(self,x=None,y=None,c=None,**kw):
  self._updates(**kw)
  if isinstance(x,ndarray|list|tuple):self.x=self._dataarr(x)
  if isinstance(y,ndarray|list|tuple):self.y=self._dataarr(y)
  if isinstance(c,ndarray|list|tuple):self.c=self._dataarr(c)
  extent,gridsize=kw.get('extent',self.extent),kw.get('gridsize',self.gridsize)
  self.gridsize=gridsize if list2int(gridsize) or isinstance(gridsize,int) else 100
  self.extent=extent if list4float(extent) else None
  self.xscale=listchose(kw.get('xscale'),['linear','log'],self.xscale)
  self.yscale=listchose(kw.get('yscale'),['linear','log'],self.yscale)
  self.mincnt=int1s(kw.get('mincnt',self.mincnt))
  bins=kw.get('bins',self.bins)
  self.bins=bins if(bins=='log' or isinstance(bins,int|float) or (isinstance(bins,list|tuple) and (isinstance(i,int|float)for i in bins)))else None
  self.plot(self.x,self.y,self.c,gridsize=self.gridsize,xscale=self.xscale,yscale=self.yscale,mincnt=self.mincnt,extent=self.extent,bins=self.bins)
  self._redraw()
 def get(self):return [self.graphdata]
 def getx(self):return self.x
 def gety(self):return self.y