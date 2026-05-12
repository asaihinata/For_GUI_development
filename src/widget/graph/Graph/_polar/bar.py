from ...dev import *
class Barpolar(polarElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.x=self._dataarr(kw.get('x'))
  self.y=self._dataarr(kw.get('y'))
  self.logs=bols(kw.get('logs'),False)
  self.width=range_num(num0s(kw.get('width'),1),0,1,1)
  self.align=listchose(kw.get('align'),['center','edge'])
  self.plot(self.x,self.y,alpha=self.alpha,width=self.width,align=self.align,logs=self.logs,color=self.color)
 def plot(self,x,y,alpha=1,width=1,align='center',logs=False,color=None):
  self.clear()
  self.graphdata=self.ax.bar(x,y,log=logs,bottom=0,color=color,alpha=alpha,width=width,align=align)
  self._adjustment()
 def update(self,x=None,y=None,**kw):
  self._updates(**kw)
  if isinstance(x,np.ndarray|list|tuple):self.x=self._dataarr(x)
  if isinstance(y,np.ndarray|list|tuple):self.y=self._dataarr(y)
  self.width=range_num(num0s(kw.get('width'),self.width),0,1,self.width)
  self.align=listchose(kw.get('align'),['center','edge'],self.align)
  self.logs=bols(kw.get('logs'),self.logs)
  self.plot(self.x,self.y,alpha=self.alpha,width=self.width,align=self.align,logs=self.logs,color=self.color)
  self._redraw()
 def get(self):return [self.graphdata]
 def getx(self):return self.x
 def gety(self):return self.y