from .._graphhelp import *
class Violinplot(twoDElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.data=self._dataarr(kw.get('data'),False)
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
  self.side=listchose(kw.get('side'),['both','low','high'])
  self.plot(self.data,self.x,self.y,alpha=self.alpha,width=self.width,points=self.points,showextrema=self.showextrema,showmeans=self.showmeans,showmedians=self.showmedians,side=self.side,orientation=self.orientation,bwmethod=self.bwmethod)
 def plot(self,data,x,y,alpha=1,width=1,points=100,showextrema=True,showmeans=False,showmedians=False,side='both',orientation='vertical',bwmethod='scott'):
  self.clear()
  if orientation=='vertical' and x.size!=0:positions=x
  elif orientation=='horizontal' and y.size!=0:positions=y
  else:positions=np.arange(1,data.shape[1]+1)
  self.graphdata=self.ax.violinplot(data,positions=positions,widths=width,points=points,showextrema=showextrema,showmedians=showmedians,showmeans=showmeans,side=side,orientation=orientation,bw_method=bwmethod)
  for i in self.graphdata['bodies']:i.set_alpha(alpha)
  self._adjustment()
 def update(self,data=None,x=None,y=None,**kw):
  self._updates(**kw)
  if isinstance(data,np.ndarray|list|tuple):self.data=self._dataarr(data)
  if isinstance(x,np.ndarray|list|tuple):self.data=self._dataarr(x)
  if isinstance(y,np.ndarray|list|tuple):self.data=self._dataarr(y)
  self.orientation=listchose(kw.get('orientation'),['vertical','horizontal'],self.orientation)
  self.width=range_num(num0s(kw.get('width'),self.width),0,1,self.width)
  self.showextrema=bols(kw.get('showextrema'),self.showextrema)
  self.showmeans=bols(kw.get('showmeans'),self.showmeans)
  self.showmedians=bols(kw.get('showmedians'),self.showmedians)
  self.points=num1s(kw.get('points'),self.points)
  bwmethod=kw.get('bw_method',self.bwmethod)
  if bwmethod in ['scott','silverman'] or isinstance(bwmethod,int|float|FunctionType):self.bwmethod=bwmethod
  else:self.bwmethod=self.bwmethod
  self.side=listchose(kw.get('side'),['both','low','high'],self.side)
  self.plot(self.data,self.x,self.y,alpha=self.alpha,width=self.width,points=self.points,showextrema=self.showextrema,showmeans=self.showmeans,showmedians=self.showmedians,side=self.side,orientation=self.orientation,bwmethod=self.bwmethod)
  self._redraw()
 def get(self):return [self.graphdata]
 def getdata(self):return self.data