from matplotlib.ticker import PercentFormatter
from ..dev import *
class Stackedh(twoElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.data=self._manyarr(kw.get('data'))
  self.dataname=self._dataarr(kw.get('dataname'),False)
  if self.data.shape[0]!=self.dataname.shape[0]:
   raise ValueError('配列のエラー')
  self.anchor=self._anchor(kw.get('labelanchor'),(1,0.85))
  self.labelplace=self._getlegendplace(self.anchor,kw.get('labelplace','center left'))
  self.height=range_num(num0s(kw.get('height'),0.8),0,1,0.8)
  self.plot(self.data,self.dataname,label=self.label,height=self.height)
 def plot(self,data,dataname,label=None,height=0.8):
  self.clear()
  self.ax.invert_yaxis()
  self.ax.set_xlim(0,100)
  self.graphdata=[self._survey(data,dataname,label,height=height)]
  self.ax.xaxis.set_major_formatter(PercentFormatter(xmax=100))
  self._apply_labels(self.xlabel,self.ylabel)
  self._adjustment()
 def _survey(self,data:np.ndarray,dataname,label=None,height=0.8):
  data,lens,lisarr=data.T,len(dataname),[]
  data_percent,left=data/data.sum(axis=0)*100,np.zeros(lens)
  for i,ds in enumerate(data_percent):
   lisarr=self.ax.barh(dataname,ds,left=left,label=label[i],height=height)
   left+=ds
  self.legend()
  return lisarr
 def update(self,data=None,dataname=None,**kw):
  self._updates(**kw)
  if isinstance(data,nListlike):self.data=self._manyarr(data)
  if isinstance(dataname,nListlike):self.dataname=self._dataarr(dataname,False)
  if self.data.shape[0]!=self.dataname.shape[0]:
   raise ValueError('配列のエラー')
  self.height=range_num(num0s(kw.get('height'),self.height),0,1,self.height)
  self.plot(self.data,self.dataname,label=self.label,height=self.height)
  self._redraw()
 def get(self):return self.graphdata
 def getdata(self):return self.data