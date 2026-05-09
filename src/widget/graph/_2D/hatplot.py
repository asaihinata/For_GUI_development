from ..dev import *
class Hatplot(twoDElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.x=self._dataarr(kw.get('x'))
  self.data=self._dataarr(kw.get('data'))
  self.color=parsecolor(kw.get('color'),'#4477aa')
  self.label=self.labels(kw.get('label'),2)[0]
  self.plot(self.x,self.data,label=self.label,color=self.color,alpha=self.alpha)
 def plot(self,x,data,label=None,color=None,alpha=1):
  self.clear()
  self.graphdata=self.hat_graph(x,data,label=label,color=color,alpha=alpha)
  self._apply_labels(self.xlabel,self.ylabel)
  self.legend()
  self._adjustment()
 def hat_graph(self,x,data,label,color=None,alpha=1):
  x,data=np.array(x),np.array(data)
  values=np.vstack([x,data])
  xlen=np.arange(x.shape[0])
  for i,(heights,group_label) in enumerate(zip(values,label)):
   style={'fill':False} if i==0 else {'edgecolor':'black'}
   rects=self.ax.bar(xlen-0.15+i*0.35,heights-x,width=0.35,bottom=x,label=group_label,color=color,alpha=alpha,**style)
   annotate=[self.ax.annotate(f'{height}',xy=(rect.get_x()+rect.get_width()/2,height),xytext=(0,4),textcoords='offset points',ha='center',va='bottom',alpha=alpha)for height,rect in zip(heights,rects)]
  return[rects,annotate]
 def update(self,x=None,data=None,**kw):
  self._updates(**kw)
  if isinstance(x,np.ndarray|list|tuple):self.x=self._dataarr(x)
  if isinstance(data,np.ndarray|list|tuple):self.data=self._dataarr(data)
  self.color=parsecolor(kw.get('color'),self.color)
  self.label=self.labels(kw.get('label',self.label),2)[0]
  self.plot(self.x,self.data,label=self.label,color=self.color,alpha=self.alpha)
  self._redraw()
 def get(self):return self.graphdata
 def getx(self):return self.x
 def gety(self):return self.y