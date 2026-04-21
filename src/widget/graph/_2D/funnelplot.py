from matplotlib.ticker import MaxNLocator
from .._graphhelp import *
class Funne(twoDElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.data=self._dataarr(kw.get('data'))
  xmajormaxbins=intsmin(kw.get('xmajormaxbins'),3,11)
  if not isinstance(xmajormaxbins,int):
   raise TypeError('xmajormaxbinsに整数を指定してください')
  elif xmajormaxbins%2==0:
   raise ValueError('xmajormaxbinsは2n+1の整数で指定してください')
  else:self.xmajormaxbins=xmajormaxbins
  ymajormaxbins=intsmin(kw.get('ymajormaxbins'),3,11)
  if not isinstance(ymajormaxbins,int):
   raise TypeError('ymajormaxbinsに整数を指定してください')
  elif ymajormaxbins%2==0:
   raise ValueError('ymajormaxbinsは2n+1の整数で指定してください')
  else:self.ymajormaxbins=ymajormaxbins
  self.ax.xaxis.set_major_locator(MaxNLocator(nbins=self.xmajormaxbins,integer=self.xmajorint))
  self.ax.yaxis.set_major_locator(MaxNLocator(nbins=self.ymajormaxbins,integer=self.ymajorint))
  self.plot(self.data)
 def plot(self,data):
  self.clear()
  self.graphdata=[self._funne(data)]
  self._apply_labels(self.xlabel,self.ylabel)
  self._adjustment()
 def _funne(self,data:np.ndarray):
  data_max=data.max()
  self.ax.set_xlim([0,data_max])
  lists1=np.delete(np.linspace(0,data_max,6,dtype=np.int_),0)
  lists2=np.append(np.append(lists1[::-1],[0]),lists1)
  print(lists2)
  self.ax.set_xticks(np.linspace(0,data_max,11,dtype=np.int_))
  self.ax.set_xticklabels(lists2)
  return self.ax.barh(np.arange(len(data)),data,left=(data_max-data)/2,height=1)
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