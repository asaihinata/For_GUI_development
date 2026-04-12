class clearsave:
 clea=None
 def __init__(self,v=None):
  if v!=None:
   if clearsave.clea==None:clearsave.clea=v
  else:pass
 def __str__(self):return str(self.clea)