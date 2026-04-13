from .._graphhelp import *
__all__=['Hatplot']
class Hatplot(twoDElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.x=self._dataarr(kw.get('x'))
  self.y=self._dataarr(kw.get('y'))
  self.label=self.labels(kw.get('label'))[0]
  self.plot(self.x,self.y)
 def plot(self,x,y):
  self.clear()
  self.graphdata=self.hat_graph(x,y,self.label)
  self._apply_labels(self.xlabel,self.ylabel)
  self.legend()
 def update(self,x=None,y=None,**kw):
  self._updates(**kw)
  if isinstance(x,NpArraytype):self.x=self._onearr(x)
  if isinstance(y,NpArraytype):self.y=self._onearr(y)
  self.plot(self.x,self.y)
  self._redraw()
 def get(self):return self.graphdata
 def getx(self):return self.x
 def gety(self):return self.y
 def hat_graph(self,x,y,group_labels):
  x,y=np.array(x),np.array(y)
  values=np.vstack([x,y])
  xlen=np.arange(values.shape[1])
  width=0.7/values.shape[0]
  returns=[]
  for i,(heights,group_label) in enumerate(zip(values,group_labels)):
   style={'fill':False} if i==0 else {'edgecolor':'black'}
   rects=self.ax.bar(xlen-0.15+i*width,heights-x,width,bottom=x,label=group_label,**style)
   for height,rect in zip(heights,rects):
    self.ax.annotate(
height,
xy=(rect.get_x()+rect.get_width()/2,height),
xytext=(0,4),
textcoords='offset points',
ha='center',va='bottom')
   returns.append(rects)
  return returns