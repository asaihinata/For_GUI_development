from ..dev import *
class Step(twoDElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.data=self._manyarr(kw.get('data'))
  self.range=self._steprange(kw.get('range'),self.data)
  self.fill=bols(kw.get('fill'),False)
  self.baseline=num0s(kw.get('baseline'))
  self.orientation=listchose(kw.get('orientation'),['vertical','horizontal'])
  self.label=self.labels(kw.get('label'))[0]
  self.linewidth=num0(kw.get('linewidth'),2)
  self.plot(self.data,range=self.range,fill=self.fill,baseline=self.baseline,orientation=self.orientation,alpha=self.alpha)
 def plot(self,data,linewidth=2,range=None,fill=False,baseline=0,orientation='vertical',alpha=1):
  self.clear()
  self.graphdata=[self.ax.stairs(d,linewidth=linewidth,baseline=baseline,fill=fill,orientation=orientation,label=self.label[i],alpha=alpha)for i,d in enumerate(data)]
  self._apply_labels(self.xlabel,self.ylabel)
  if orientation=='vertical':self.ax.set_xticks(np.arange(data.shape[1]+1),labels=range.astype('U5'))
  else:self.ax.set_yticks(np.arange(data.shape[1]+1),labels=range.astype('U5'))
  self.legend()
  self._adjustment()
 def update(self,data=None,**kw):
  self._updates(**kw)
  if isinstance(data,np.ndarray|list|tuple):self.data=self._manyarr(data)
  self.range=self._steprange(kw.get('range',self.range),self.data)
  self.linewidth=num0(kw.get('linewidth'),self.linewidth)
  self.fill=bols(kw.get('fill'),self.fill)
  self.baseline=num0s(kw.get('baseline'),self.baseline)
  self.orientation=listchose(kw.get('orientation'),['vertical','horizontal'],self.orientation)
  self.plot(self.data,linewidth=self.linewidth,range=self.range,fill=self.fill,baseline=self.baseline,orientation=self.orientation)
  self._redraw()
 def get(self):return self.graphdata
 def getdata(self):return self.data
 def _steprange(self,ranges=None,data=None):
  len1=data.shape[1]+1
  def _array(min,max):
   if max<min:min,max=max,min
   return np.array([float((max-min)*i/(len1-1)+min)for i in range(len1)],dtype=object)
  if isinstance(ranges,np.ndarray) and len(ranges.shape)==1 and ranges.shape[0]==len1:return ranges
  elif isinstance(ranges,tuple|list):
   lens=len(ranges)
   if lens==2 and all(isinstance(ranges[i],int|float)for i in range(2)):return _array(ranges[0],ranges[1])
   elif len1==lens:return np.array([str(i) for i in ranges],dtype=np.str_)
  elif isinstance(ranges,int|float):return _array(0,ranges)
  return np.arange(len1)