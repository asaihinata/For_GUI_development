from ..dev import *
class Pie(twoDElement):
 def __init__(self,master,kw):
  super().__init__(master,kw)
  self.labelplace=self._getlegendplace(kw.get('labelplace'),'upper left')
  self.anchor=self._anchor(kw.get('anchor'),(1.2,1.05))
  self.data=self._dataarr(kw.get('data'))
  self.label=self.pielabel(self.data,kw.get('label'))[0]
  self.startangle=nums(kw.get('startangle'),0)
  self.startangletype=bols(kw.get('startangletype'))
  self.shadow=bols(kw.get('shadow'),False)
  self.counterclock=bols(kw.get('counterclock'),False)
  self.labeldistance=num0(kw.get('labeldistance'),1.1)
  explode=kw.get('explode')
  if isinstance(explode,list|tuple) and all(isinstance(i,int|float)for i in explode):self.explode=list(map(float,explode))
  elif isinstance(explode,int|float):self.explode=[float(explode) for _ in range(self.max_depth)]
  else:self.explode=None
  self.plot(self.data,startangle=self.startangle,shadow=self.shadow,counterclock=self.counterclock,label=self.label,labeldistance=self.labeldistance,explode=self.explode,startangletype=self.startangletype,alpha=self.alpha)
 def plot(self,data,startangle=0.0,shadow=False,counterclock=True,label=None,labeldistance=1.1,explode=None,startangletype=True,alpha=1):
  self.clear()
  if startangletype==False:startangle=Rad(startangle).angle
  pie=np.array(self.ax.pie(data,labels=label,startangle=90-startangle,shadow=shadow,counterclock=counterclock,labeldistance=labeldistance,explode=explode)).T.tolist()
  self.graphdata=[i[0].set_alpha(self.alpha) for i in pie]
  self.legend()
 def update(self,data=None,**kw):
  self._updates(**kw)
  if isinstance(data,np.ndarray|list|tuple):self.data=self._dataarr(data)
  explode=kw.get('explode',self.explode)
  if isinstance(explode,list|tuple) and all(isinstance(i,int|float)for i in explode):self.explode=list(map(float,explode))
  elif isinstance(explode,int|float):self.explode=[float(explode) for _ in range(self.max_depth)]
  else:self.explode=None
  self.label=self.pielabel(self.data,kw.get('label',self.label))[0]
  self.startangle=nums(kw.get('startangle'),self.startangle)
  self.startangletype=bols(kw.get('startangletype'),self.startangletype)
  self.shadow=bols(kw.get('shadow'),self.shadow)
  self.counterclock=bols(kw.get('counterclock'),self.counterclock)
  self.labeldistance=num0(kw.get('labeldistance'),self.labeldistance)
  self.plot(self.data,startangle=self.startangle,shadow=self.shadow,counterclock=self.counterclock,label=self.label,labeldistance=self.labeldistance,explode=self.explode,startangletype=self.startangletype)
  self._redraw()
 def get(self):return self.graphdata
 def getdata(self):return self.data