from ...dev import *

__all__=['BarGraph']
class BarGraph(twoElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.x=NPArray(kw.get('x'),depth_limit=1)
  self.y=NPNumber(kw.get('y'))
  self.logs=bols(kw.get('logs'),False)
  self.width=range_num(num0s(kw.get('width'),1),0,1,1)
  self.align=listchose(kw.get('align'),['center','edge'])
  self.plot(self.x,self.y,label=self.label,alpha=self.alpha,width=self.width,align=self.align,logs=self.logs)
 def plot(self,x,y,label,alpha=1,width=0.8,align='center',logs=False):
  self.clear()
  self.graphdata=[self.ax.bar(xs,ys,log=logs,label=label[i],alpha=alpha,width=width,align=align)for i,(xs,ys) in enumerate(TwoArray(x,y,ydtype=np.float64))]
  self.set_xticks(x.lengtharange(),x.tonp())
  self._apply_labels(self.xlabel,self.ylabel)
  self.legend()
  self._adjustment()
 def update(self,x=None,y=None,**kw):
  self._updates(**kw)
  if isinstance(x,nListlike):self.x=NPArray(x,depth_limit=1)
  if isinstance(y,nListlike):self.y=NPNumber(y)
  self.width=range_num(num0s(kw.get('width'),self.width),0,1,self.width)
  self.align=listchose(kw.get('align'),['center','edge'],self.align)
  self.logs=bols(kw.get('logs'),self.logs)
  self.plot(self.x,self.y,label=self.label,alpha=self.alpha,width=self.width,align=self.align,logs=self.logs)
  self._redraw()
 def get(self):return self.graphdata
 def getx(self):return self.x.tonp()
 def gety(self):return self.y.tonp()