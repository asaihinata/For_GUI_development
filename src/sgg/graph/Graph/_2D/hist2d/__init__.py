from ...dev import *
__all__=['Hist2d']
class Hist2d(twoElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.x=NPNumber(kw.get('x'),depth_limit=2)
  self.y=NPNumber(kw.get('y'),depth_limit=2)
  self.max,self.min=nums(kw.get('max')),nums(kw.get('min'))
  if isinstance(self.max,int|float) and isinstance(self.min,int|float) and self.max<self.min:
   self.max,self.min=self.min,self.max
  self.xmax=self._powsmax(nums(kw.get('xmax')),self.x)
  self.xmin=self._powsmin(nums(kw.get('xmin')),self.x)
  self.ymax=self._powsmax(nums(kw.get('ymax')),self.y)
  self.ymin=self._powsmin(nums(kw.get('ymin')),self.y)
  if self.xmax<self.xmin:self.xmin,self.xmax=self.xmax,self.xmin
  if self.ymax<self.ymin:self.ymin,self.ymax=self.ymax,self.ymin
  self.range=((self.xmin,self.xmax),(self.ymin,self.ymax))
  self.bins=self._bins(kw.get('bins',10))
  self.density=bols(kw.get('density'),False)
  self.plot(self.x,self.y,bins=self.bins,alpha=self.alpha,density=self.density,range=self.range,max=self.max,min=self.min)
 def plot(self,x,y,bins=10,alpha=1,density=False,range=None,min=None,max=None):
  self.clear()
  self.graphdata=[self.ax.hist2d(x,y,bins=bins,alpha=alpha,density=density,range=range,cmax=max,cmin=min)]
  self._apply_labels(self.xlabel,self.ylabel)
  self._adjustment()
 def update(self,x=None,y=None,**kw):
  self._updates(**kw)
  if isinstance(x,nListlike):self.x=NPNumber(x,depth_limit=2)
  if isinstance(y,nListlike):self.y=NPNumber(y,depth_limit=2)
  self.max=nums(kw.get('max'),self.max)
  self.min=nums(kw.get('min'),self.min)
  if isinstance(self.max,int|float) and isinstance(self.min,int|float) and self.max<self.min:
   self.max,self.min=self.min,self.max
  self.xmax=self._powsmax(nums(kw.get('xmax'),self.xmax),self.x)
  self.xmin=self._powsmin(nums(kw.get('xmin'),self.xmin),self.x)
  self.ymax=self._powsmax(nums(kw.get('ymax'),self.ymax),self.y)
  self.ymin=self._powsmin(nums(kw.get('ymin'),self.ymin),self.y)
  if self.xmax<self.xmin:self.xmin,self.xmax=self.xmax,self.xmin
  if self.ymax<self.ymin:self.ymin,self.ymax=self.ymax,self.ymin
  self.range=((self.xmin,self.xmax),(self.ymin,self.ymax))
  self.bins=self._bins(kw.get('bins',self.bins))
  self.density=bols(kw.get('density'),self.density)
  self.alpha=range_num(num0s(kw.get('alpha'),self.alpha),0,1,self.alpha)
  self.plot(self.x,self.y,bins=self.bins,alpha=self.alpha,density=self.density,range=self.range,max=self.max,min=self.min)
  self._redraw()
 def get(self):return self.graphdata
 def getx(self):return self.x
 def gety(self):return self.y
 def _powsmax(self,val,range):
  if val==None:
   maxs=range.max
   if maxs<0:return np.pow(10,np.ceil(np.log10(np.abs(maxs)))-1)*-1
   return np.pow(10,np.ceil(np.log10(maxs)))
  return val
 def _powsmin(self,val,range):
  if val==None:
   mins=range.min
   if mins<0:return np.pow(10,np.ceil(np.log10(np.abs(mins))))*-1
   return np.pow(10,np.ceil(np.log10(mins))-1)
  return val
 def _bins(self,val):
  if(isinstance(val,int)or(isinstance(val,np.ndarray)and len(val.shape)==1 and 2<=val.shape[0])or(isinstance(val,list|tuple)and((len(val)==2 and all(isinstance(val[i],list|tuple)for i in range(2)))or(1<=len(val)and all(isinstance(i,int)for i in val))))):return val
  return 10