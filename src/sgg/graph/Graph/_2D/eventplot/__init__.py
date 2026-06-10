from ...dev import *

__all__=['Eventplot']
class Eventplot(twoElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.data=NPNumber(kw.get('data'))
  self.x=np.arange(self.data.shape[0])
  self.orientation=listchose(kw.get('orientation'),['vertical','horizontal'])
  self.linewidth=num0(kw.get('linewidth'),1)
  self.linelength=num0(kw.get('linelength'),1)
  self.linestyle=Solidlist(kw.get('linestyle','-'))
  self.plot(self.data,label=self.label,orientation=self.orientation,linewidth=self.linewidth,linelength=self.linelength,alpha=self.alpha,linestyle=self.linestyle)
 def plot(self,data,label,orientation='vertical',linewidth=1,linelength=1,alpha=1,linestyle=None):
  self.clear()
  self.graphdata=[self.ax.eventplot(ds,alpha=alpha,lineoffsets=i,linelengths=linelength,linewidths=linewidth,orientation=orientation,linestyles=linestyle[i],label=label[i])[0]for i,ds in enumerate(data)]
  self._apply_labels(self.xlabel,self.ylabel)
  if not label:
   if orientation=='vertical':self.ax.set_xticks(self.x,label.tolist())
   else:self.ax.set_yticks(self.x,label.tolist())
  self.legend()
  self._adjustment()
 def update(self,data=None,**kw):
  self._updates(**kw)
  if isinstance(data,nListlike):self.data=NPNumber(data)
  self.orientation=listchose(kw.get('orientation'),['vertical','horizontal'],self.orientation)
  self.linewidth=num0(kw.get('linewidth'),self.linewidth)
  self.linelength=num0(kw.get('linelength'),self.linelength)
  self.alpha=range_num(num0s(kw.get('alpha'),self.alpha),0,1,self.alpha)
  lines=kw.get('linestyle',None)
  self.linestyle=parameters(lines,self.linestyle,Solidlist('-'))
  self.plot(self.data,label=self.label,orientation=self.orientation,linewidth=self.linewidth,linelength=self.linelength,alpha=self.alpha,linestyle=self.linestyle)
  self._redraw()
 def get(self):return self.graphdata
 def getdata(self):return self.data