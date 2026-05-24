from ...dev import *
__all__=['Boxplot']
class Boxplot(twoElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.data=self._manyarr(kw.get('data'))
  label=getLabel(kw.get('label')).label
  if label==None:self.label=[f'box{i}'for i in range(self.max_depth)]
  else:self.label=label
  self.legends=bols(kw.get('legend'))
  self.width=range_num(num0s(kw.get('width'),0.15),0,1,0.15)
  self.whis=self._boxplot_whis(kw.get('whis'))
  self.fill=bols(kw.get('fill'),False)
  self.notch=bols(kw.get('notch'),False)
  self.showfliers=bols(kw.get('showfliers'))
  self.orientation=listchose(kw.get('orientation'),['vertical','horizontal'])
  self.plot(self.data,label=self.label,width=self.width,legend=self.legends,whis=self.whis,fill=self.fill,showfliers=self.showfliers,notch=self.notch,orientation=self.orientation,alpha=self.alpha)
 def plot(self,data,label=None,width=0.15,whis=1.5,fill=False,legend=True,showfliers=True,notch=False,orientation='vertical',alpha=1):
  self.clear()
  boxplot=self.ax.boxplot(data.T,showfliers=showfliers,label=label,widths=width,whis=whis,patch_artist=fill,notch=notch,orientation=orientation)
  for i in range(data.shape[0]):boxplot['boxes'][i].set_alpha(alpha)
  self.graphdata=[boxplot]
  if orientation=='vertical':self.ax.set_xticklabels(label)
  else:self.ax.set_yticklabels(label)
  self._apply_labels(self.xlabel,self.ylabel)
  if legend:self.legend()
  self._adjustment()
 def update(self,data=None,**kw):
  self._updates(**kw)
  if isinstance(data,nListlike):self.data=self._manyarr(data)
  label=kw.get('label',self.label)
  if label==None:label=[f'box{i}'for i in range(self.max_depth)]
  self.legends=bols(kw.get('legend'),self.legends)
  self.fill=bols(kw.get('fill'),self.fill)
  self.notch=bols(kw.get('notch'),self.notch)
  self.showfliers=bols(kw.get('showfliers'),self.showfliers)
  self.orientation=listchose(kw.get('orientation'),['vertical','horizontal'],self.orientation)
  self.width=range_num(num0s(kw.get('width'),self.width),0,1,self.width)
  self.whis=self._boxplot_whis(kw.get('whis',self.whis))
  self.plot(self.data,label=self.label,width=self.width,legend=self.legends,whis=self.whis,fill=self.fill,showfliers=self.showfliers,notch=self.notch,orientation=self.orientation,alpha=self.alpha)
  self._redraw()
 def get(self):return self.graphdata
 def getdata(self):return self.data
 def _boxplot_whis(self,data):
  if isinstance(data,list|tuple):
   x,y=data[0],data[1]
   if isinstance(x,int|float)and isinstance(y,int|float):
    if y<x:x,y=y,x
    if not 0<=x<=100:x=0
    if not 0<=y<=100:y=100
    return(float(x),float(y))
  elif isinstance(data,int|float):return float(data)
  return 1.5