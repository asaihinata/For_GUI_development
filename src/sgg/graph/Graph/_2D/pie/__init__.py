from ...dev import *
__all__=['Pie']
class Pie(twoElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.labelplace=self._getlegendplace(kw.get('labelplace'),'upper left')
  self.anchor=self._anchor(kw.get('anchor'),(1.2,1.05))
  self.data=NPNumber(kw.get('data'))
  self.startangle=nums(kw.get('startangle'),0)
  self.startangletype=bols(kw.get('startangletype'))
  self.shadow=bols(kw.get('shadow'),False)
  self.counterclock=bols(kw.get('counterclock'),False)
  self.labeldistance=num0(kw.get('labeldistance'),1.1)
  explode=kw.get('explode')
  if isinstance(explode,list|tuple) and all(isinstance(i,int|float)for i in explode):self.explode=list(map(float,explode))
  elif isinstance(explode,int|float):self.explode=[float(explode) for _ in range(self.data.size)]
  else:self.explode=None
  self.plot(self.data,startangle=self.startangle,shadow=self.shadow,counterclock=self.counterclock,label=self.label,labeldistance=self.labeldistance,explode=self.explode,startangletype=self.startangletype,alpha=self.alpha)
 def plot(self,data,startangle=0.0,shadow=False,counterclock=True,label=None,labeldistance=1.1,explode=None,startangletype=True,alpha=1):
  self.clear()
  if startangletype==False:startangle=np.rad2deg(startangle)
  pie=self.ax.pie(data,labels=None if label else list(label),startangle=90-startangle,shadow=shadow,counterclock=counterclock,labeldistance=labeldistance,explode=explode)
  for i in np.array(pie).T:i[0].set_alpha(alpha)
  self.graphdata=[pie]
  self.legend()
 def update(self,data=None,**kw):
  self._updates(**kw)
  if isinstance(data,nListlike):self.data=NPNumber(data)
  explode=kw.get('explode',self.explode)
  if isinstance(explode,list|tuple) and all(isinstance(i,int|float)for i in explode):self.explode=list(map(float,explode))
  elif isinstance(explode,int|float):self.explode=[float(explode) for _ in range(self.data.size)]
  else:self.explode=None
  self.startangle=nums(kw.get('startangle'),self.startangle)
  self.startangletype=bols(kw.get('startangletype'),self.startangletype)
  self.shadow=bols(kw.get('shadow'),self.shadow)
  self.counterclock=bols(kw.get('counterclock'),self.counterclock)
  self.labeldistance=num0(kw.get('labeldistance'),self.labeldistance)
  self.plot(self.data,startangle=self.startangle,shadow=self.shadow,counterclock=self.counterclock,label=self.label,labeldistance=self.labeldistance,explode=self.explode,startangletype=self.startangletype)
  self._redraw()
 def get(self):return self.graphdata
 def getdata(self):return self.data