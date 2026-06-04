from ...dev import *
__all__=['SSBarGraph']
class SSBarGraph(twoElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.data=NPNumber(kw.get('data'))
  self.dataname=NPArray(kw.get('dataname'),depth_limit=1)
  self.width=range_num(num0s(kw.get('width'),0.8),0,1,0.8)
  self.plot(self.data,self.dataname,label=self.label,alpha=self.alpha,width=self.width)
 def plot(self,data:NPNumber,dataname:NPArray,label=None,alpha=1,width=0.8):
  self.clear()
  width=width/data.shape[0]
  arr=np.arange(data.ndim+1)
  self.graphdata=[self.ax.bar(arr+width*i,xs,width=width,label=label[i],align='edge',alpha=alpha)for i,xs in enumerate(data)]
  self.set_xticks(data.lengtharange(0.5)[0],dataname)
  self._apply_labels(self.xlabel,self.ylabel)
  self.legend()
  self._adjustment()
 def update(self,data=None,dataname=None,**kw):
  self._updates(**kw)
  if isinstance(data,nListlike):self.data=NPNumber(data)
  if isinstance(dataname,nListlike):self.dataname=NPArray(dataname,depth_limit=1)
  self.width=range_num(num0s(kw.get('width'),self.width),0,1,self.width)
  self.plot(self.data,self.dataname,label=self.label,alpha=self.alpha,width=self.width,align=self.align)
  self._redraw()
 def get(self):return self.graphdata
 def getdata(self):return self.data.tonp()
 def getdata(self):return self.dataname.tonp()