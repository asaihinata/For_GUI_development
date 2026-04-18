from matplotlib.ticker import PercentFormatter
from .._graphhelp import *
class Stacked(twoDElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.data=self._manyarr(kw.get('data'))
  self.dataname=self._dataarr(kw.get('dataname'),False)
  if self.data.shape[0]!=self.dataname.shape[0]:
   raise ValueError('配列のエラー')
  self.label=self.labels(kw.get('label'),self.data.shape[1])[0]
  self.width=range_num(num0s(kw.get('width'),0.8),0,1,0.8)
  self.anchor=self._anchor(kw.get('labelanchor'),(0,1))
  self.labelplace=self._getlabelplace(self.anchor,kw.get('labelplace','lower left'))
  self.plot(self.data,self.dataname,label=self.label,width=self.width)
 def plot(self,data,dataname,label=None,width=0.8):
  self.clear()
  self.ax.set_ylim(0,100)
  self.graphdata=[self._survey(data,dataname,label,width=width)]
  self.ax.yaxis.set_major_formatter(PercentFormatter(xmax=100))
  self._apply_labels(self.xlabel,self.ylabel)
  self._adjustment()
 def _survey(self,data:np.ndarray,dataname,label=None,width=0.8):
  data,lens,lisarr=data.T,len(dataname),[]
  data_percent=data/data.sum(axis=0)*100
  bottom=np.zeros(lens)
  for i,labels in enumerate(label):
   lisarr=self.ax.bar(dataname,data_percent[i],bottom=bottom,label=labels,width=width)
   bottom+=data_percent[i]
  self.legend(ncols=lens)
  return lisarr
 def update(self,data=None,dataname=None,**kw):
  self._updates(**kw)
  if isinstance(data,NpArraytype):self.data=self._manyarr(data)
  if isinstance(dataname,NpArraytype):self.dataname=self._dataarr(dataname,False)
  if self.data.shape[0]!=self.dataname.shape[0]:
   raise ValueError('配列のエラー')
  self.label=self.labels(kw.get('label',self.label),self.data.shape[1])[0]
  self.width=range_num(num0s(kw.get('width'),self.width),0,1,self.width)
  self.plot(self.data,self.dataname,label=self.label,width=self.width)
  self._redraw()
 def get(self):return self.graphdata
 def getdata(self):return self.data
class Stackedh(twoDElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.data=self._manyarr(kw.get('data'))
  self.dataname=self._dataarr(kw.get('dataname'),False)
  if self.data.shape[0]!=self.dataname.shape[0]:
   raise ValueError('配列のエラー')
  self.label=self.labels(kw.get('label'),self.data.shape[1])[0]
  self.width=range_num(num0s(kw.get('width'),0.8),0,1,0.8)
  self.anchor=self._anchor(kw.get('labelanchor'),(0,1))
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
  data_percent=data/data.sum(axis=0)*100
  left=np.zeros(lens)
  for i,labels in enumerate(label):
   lisarr=self.ax.barh(dataname,data_percent[i],left=left,label=labels,height=height)
   left+=data_percent[i]
  self.legend(ncols=lens)
  return lisarr
 def update(self,data=None,dataname=None,**kw):
  self._updates(**kw)
  if isinstance(data,NpArraytype):self.data=self._manyarr(data)
  if isinstance(dataname,NpArraytype):self.dataname=self._dataarr(dataname,False)
  if self.data.shape[0]!=self.dataname.shape[0]:
   raise ValueError('配列のエラー')
  self.label=self.labels(kw.get('label',self.label),self.data.shape[1])[0]
  self.height=range_num(num0s(kw.get('height'),self.height),0,1,self.height)
  self.plot(self.data,self.dataname,label=self.label,height=self.height)
  self._redraw()
 def get(self):return self.graphdata
 def getdata(self):return self.data