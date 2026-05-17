'''マーカーを設定するモジュール'''
from matplotlib.markers import MarkerStyle
from matplotlib.transforms import Affine2D
__all__=['Marker']
class Marker:
 marker_dict={'.':'point',',':'pixel','o':'circle','v':'triangle_down','^':'triangle_up','<':'triangle_left','>':'triangle_right','1':'tri_down','2':'tri_up','3':'tri_left','4':'tri_right','8':'octagon','s':'square','p':'pentagon','*':'star','h':'hexagon1','H':'hexagon2','+':'plus','x':'x','D':'diamond','d':'thin_diamond','|':'vline','_':'hline','P':'plus_filled','X':'x_filled',0:'tickleft',1:'tickright',2:'tickup',3:'tickdown',4:'caretleft',5:'caretright',6:'caretup',7:'caretdown',8:'caretleftbase',9:'caretrightbase',10:'caretupbase',11:'caretdownbase','None':'nothing','none':'nothing',' ':'nothing','':'nothing'}
 marker_list=['.',',','o','v','^','<','>','1','2','3','4','8','s','p','*','h','H','+','x','D','d','|','_','P','X',0,1,2,3,4,5,6,7,8,9,10,11,'None','none',' ','']
 def __init__(self,marker,*,fill=None,cap=None,transform=None,join=None):
  if fill not in ['full','left','right','bottom','top','none']:fill=None
  if cap not in ['butt','round','projecting']:cap=None
  if join not in ['miter','round','bevel']:join=None
  if not isinstance(transform,int|float):transform=0
  self.marker=MarkerStyle(marker,fillstyle=fill,transform=Affine2D().rotate_deg(transform),joinstyle=join,capstyle=cap)
 def __iter__(self):return iter(self.marker_list)
 def __len__(self):return len(self.marker_list)
 def __contains__(self,item):return item in self.marker_list
 def get_marker(self):return self.marker.get_marker()