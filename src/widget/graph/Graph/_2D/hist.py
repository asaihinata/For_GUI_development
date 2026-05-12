from ...dev import *
class Hist(twoDElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.data=self._dataarr(kw.get('data'))
  self.label=self.labels(kw.get('label'))[0]
  if len(self.data.shape)!=1:
   raise ValueError('配列に多次元配列で指定されています')
  bins=kw.get('bins')
  if isinstance(bins,list|range|tuple|np.ndarray) or bins in ['auto','fd','doane','scott','stone','rice','sturges','sqrt']:self.bins=bins
  elif isinstance(bins,int):self.bins=num1s(bins,round(np.log2(len(self.data))+1))
  else:self.bins=round(np.log2(len(self.data))+1)
  self.min=nums(kw.get('min'),np.min(self.data))
  self.max=nums(kw.get('max'),np.max(self.data))
  self.range=(self.min,self.max)
  self.bottom=num0s(kw.get('bottom'))
  self.decimalpoint=num0s(kw.get('decimalpoint'),0)
  self.orientation=listchose(kw.get('orientation'),['vertical','horizontal'])
  self.width=range_num(num0s(kw.get('width'),1),0,1,1)
  self.plot(self.data,label=self.label,bins=self.bins,ranges=self.range,bottom=self.bottom,orientation=self.orientation,width=self.width,alpha=self.alpha)
 def plot(self,data,label=None,bins=10,ranges=None,bottom=0,orientation='vertical',width=None,alpha=1):
  self.clear()
  self.graphdata=self.ax.hist(data,label=label,bins=bins,range=ranges,bottom=bottom,rwidth=width,orientation=orientation,alpha=alpha)
  self.tickslist,self.tickslists,pows=[],[],np.pow(10,self.decimalpoint)
  for i in self.graphdata[1]:
   self.tickslist.append(i)
   self.tickslists.append(np.floor(i*pows)/pows)
  self._apply_labels(self.xlabel,self.ylabel)
  if orientation=='vertical':self.ax.set_xticks(self.tickslist,self.tickslists)
  else:self.ax.set_yticks(self.tickslist,self.tickslists)
  self.legend()
  self._adjustment()
 def update(self,data=None,**kw):
  self._updates(**kw)
  if isinstance(data,np.ndarray|list|tuple):self.data=self._dataarr(data)
  bins=kw.get('bins',self.bins)
  if isinstance(bins,list|range|tuple|np.ndarray) or bins in ['auto','fd','doane','scott','stone','rice','sturges','sqrt']:self.bins=bins
  elif isinstance(bins,int):self.bins=num1s(bins,round(np.log2(len(self.data))+1))
  else:self.bins=round(np.log2(len(self.data))+1)
  self.min=nums(kw.get('min'),np.min(self.data))
  self.max=nums(kw.get('max'),np.max(self.data))
  self.range=(self.min,self.max)
  self.bottom=num0s(kw.get('bottom'),self.bottom)
  self.orientation=listchose(kw.get('orientation'),['vertical','horizontal'],self.orientation)
  self.decimalpoint=num0s(kw.get('decimalpoint'),self.decimalpoint)
  self.width=range_num(num0s(kw.get('width'),self.width),0,1,self.width)
  self.plot(self.data,label=self.label,bins=self.bins,ranges=self.range,bottom=self.bottom,orientation=self.orientation,width=self.width)
  self._redraw()
 def get(self):return list(self.graphdata)
 def getrange(self,num=True):return self.range if num else (self.range[0].item(),self.range[1].item())
 def getmin(self,num=True):return self.min if num else self.min.item()
 def getmax(self,num=True):return self.max if num else self.max.item()
 def getdata(self):return self.data