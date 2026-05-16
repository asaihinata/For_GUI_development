from ..dev import *
class Violinpolar(polarElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.data=self._dataarr(kw.get('data'),False).T
  self.x=self._dataarr(kw.get('x',[]),False)
  self.y=self._dataarr(kw.get('y',[]),False)
  self.orientation=listchose(kw.get('orientation'),['vertical','horizontal'])
  self.width=range_num(num0s(kw.get('width'),1),0,1,1)
  self.showextrema=bols(kw.get('showextrema'))
  self.showmeans=bols(kw.get('showmeans'),False)
  self.showmedians=bols(kw.get('showmedians'),False)
  self.points=num1s(kw.get('points'),100)
  bwmethod=kw.get('bw_method')
  if bwmethod in ['scott','silverman'] or isinstance(bwmethod,int|float|FunctionType):self.bwmethod=bwmethod
  else:self.bwmethod='scott'
  if self.orientation=='vertical' and self.x.size!=0:self.positions=self.x
  elif self.orientation=='horizontal' and self.y.size!=0:self.positions=self.y
  else:self.positions=self._places(self.data.shape[1])
  self.side=listchose(kw.get('side'),['both','low','high'])
  self.plot(self.data,positions=self.positions,alpha=self.alpha,width=self.width,points=self.points,showextrema=self.showextrema,showmeans=self.showmeans,showmedians=self.showmedians,side=self.side,orientation=self.orientation,bwmethod=self.bwmethod)
 def plot(self,data,positions=None,alpha=1,width=1,points=100,showextrema=True,showmeans=False,showmedians=False,side='both',orientation='vertical',bwmethod='scott'):
  self.clear()
  self.graphdata=self.ax.violinplot(data,positions=positions,widths=width,points=points,showextrema=showextrema,showmedians=showmedians,showmeans=showmeans,side=side,orientation=orientation,bw_method=bwmethod)
  for i in self.graphdata['bodies']:
   i.set_alpha(alpha)
  self._adjustment()
 def update(self,x=None,y=None,data=None,**kw):
  self._updates(**kw)
  if not isinstance(x,nListlike):x=self.x
  if not isinstance(y,nListlike):y=self.y
  self.x,self.y=self._xyd(x,y,data)
  self.width=range_num(num0s(kw.get('width'),self.width),0,1,self.width)
  self.align=listchose(kw.get('align'),['center','edge'],self.align)
  self.logs=bols(kw.get('logs'),self.logs)
  self.plot(self.x,self.y,alpha=self.alpha,width=self.width,align=self.align,logs=self.logs,color=self.color)
  self._redraw()
 def get(self):return [self.graphdata]
 def getx(self):return self.x
 def gety(self):return self.y