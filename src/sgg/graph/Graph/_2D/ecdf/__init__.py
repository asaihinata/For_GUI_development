from ...dev import *
__all__=['Ecdf']
class Ecdf(twoElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.data=NPNumber(kw.get('data'))
  self.complementary=bols(kw.get('complementary'),False)
  self.compress=bols(kw.get('compress'),False)
  self.orientation=listchose(kw.get('orientation'),['vertical','horizontal'])
  self.line=Solidlist(kw.get('linestyle','-'))
  self.linewidth=num0(kw.get('linewidth'),1.5)
  self.plot(self.data,complementary=self.complementary,compress=self.compress,orientation=self.orientation,linewidth=self.linewidth,line=self.line,alpha=self.alpha)
 def plot(self,data,complementary=False,compress=False,orientation='vertical',linewidth=1.5,line='-',alpha=1):
  self.clear()
  self.graphdata=[self.ax.ecdf(ds,compress=compress,complementary=complementary,orientation=orientation,linewidth=linewidth,linestyle=line[i],alpha=alpha)for i,ds in enumerate(data)]
  self._apply_labels(self.xlabel,self.ylabel)
  self._adjustment()
 def update(self,data=None,**kw):
  self._updates(**kw)
  if isinstance(data,nListlike):self.data=NPNumber(data)
  self.complementary=bols(kw.get('complementary'),self.complementary)
  self.compress=bols(kw.get('compress'),self.compress)
  self.orientation=listchose(kw.get('orientation'),['vertical','horizontal'],self.orientation)
  lines=kw.get('linestyle',None)
  self.line=parameters(lines,self.line,Solidlist(lines))
  self.linewidth=num0(kw.get('linewidth'),self.linewidth)
  self.plot(self.data,complementary=self.complementary,compress=self.compress,orientation=self.orientation,linewidth=self.linewidth,line=self.line)
  self._redraw()
 def get(self):return self.graphdata
 def getdata(self):return self.data.tonp()