from ...dev import *
__all__=['SSBarhGraph']
class SSBarhGraph(twoElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.data=NPNumber(kw.get('data'))
  self.dataname=NPArray(kw.get('dataname'),depth_limit=1)
  self.logs=bols(kw.get('logs'),False)
  self.height=range_num(num0s(kw.get('height'),0.8),0,1,0.8)
  self.align=listchose(kw.get('align'),['center','edge'])
  self.plot(self.data,self.dataname,label=self.label,alpha=self.alpha,height=self.height,align=self.align)
 def plot(self,data:NPNumber,dataname,label=None,alpha=1,height=0.8,align='center'):
  self.clear()
  height=height/data.ndim
  arr=np.arange(data.ndim+1)
  self.graphdata=[self.ax.barh(arr+height*i,xs,height=height,label=label[i],align=align,alpha=alpha)for i,xs in enumerate(data)]
  self._apply_labels(self.xlabel,self.ylabel)
  self.legend()
  self._adjustment()
 def update(self,data=None,dataname=None,**kw):
  self._updates(**kw)
  if isinstance(data,nListlike):self.data=NPNumber(data)
  if isinstance(dataname,nListlike):self.dataname=NPArray(dataname,depth_limit=1)
  self.height=range_num(num0s(kw.get('height'),self.height),0,1,self.height)
  self.align=listchose(kw.get('align'),['center','edge'],self.align)
  self.logs=bols(kw.get('logs'),self.logs)
  self.plot(self.data,self.dataname,label=self.label,alpha=self.alpha,height=self.height,align=self.align,logs=self.logs)
  self._redraw()
 def get(self):return self.graphdata
 def getx(self):return self.data
 def gety(self):return self.dataname