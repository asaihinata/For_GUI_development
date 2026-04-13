from matplotlib import font_manager as fm,rcParams
from ..._function import listchose
class pltFont:
 variantlist=['normal','small-caps']
 stretchlist=['ultra-condensed','extra-condensed','condensed','semi-condensed','normal','semi-expanded','expanded','extra-expanded','ultra-expanded']
 weightlist=['ultralight','light','normal','regular','book','medium','roman','semibold','demibold','demi','bold','heavy','extra bold','black']
 sizelist=['xx-small','x-small','small','medium','large','x-large','xx-large']
 stylelist=['normal','italic','oblique']
 rcparams=rcParams
 def __init__(self,family='sans-serif',size=10,stretch='normal',style='normal',variant='normal',weight='normal'):
  if family in fm.findSystemFonts():self.family=family
  else:self.family='sans-serif'
  if size in self.sizelist or isinstance(size,(int,float)):self.size=size
  else:self.size=10
  if (isinstance(stretch,(int,float)) and 0<=stretch<=1000) or stretch in self.stretchlist:self.stretch=stretch
  else:self.stretch='normal'
  if (isinstance(weight,(int,float)) and 0<=weight<=1000) or weight in self.weightlist:self.weight=weight
  else:self.weight='normal'
  self.style=listchose(style,self.stylelist)
  self.variant=listchose(variant,self.variantlist)
  self.rcparams.update({'font.family':self.family,'font.size':self.size,'font.stretch':self.stretch,'font.style':self.style,'font.variant':self.variant,'font.weight':self.weight})
 def familys(self):return fm.findSystemFonts()
 def familylist(self):return[fm.FontProperties(fname=f).get_name() for f in fm.findSystemFonts()]
 @staticmethod
 def familys():return fm.findSystemFonts()
 @staticmethod
 def familylist():return[fm.FontProperties(fname=f).get_name() for f in fm.findSystemFonts()]
 def items(self):return self.rcparams.items()
 def __getitem__(self,key):return self.rcparams[key]
 @classmethod
 def __instancecheck__(cls,ins):return isinstance(ins,pltFont)