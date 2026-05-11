'''ウィジェットの型ヒント'''
from basic import *
from graph import *
__all__=['allwidget','graphtype','widgettype']
type graphtype=BarGraph|BarhGraph|Boxplot|LineGraph|Scatter|Stem|Hist|Pie|Waterfall|Waterfallh|DScatter
'''graphtype型

グラフウィジェットの型ヒント'''
type widgettype=Colorbtn|FileLoad|FolderLoad|Savebtn|Calendars|Buttons|Checkbox|Column|Frames|Input|InputNumber|Listboxs|Menubuttons|Menus|Multiline|Radio|Slidebar|Tab|Table|Texts|Tree|Barcode|Images|QRcode|Link|TCombobox|TProgressbar
'''widgettype型

基本的なウィジェットの型ヒント'''
type allwidget=widgettype|graphtype
'''allwidget型

基本的なウィジェットとグラフウィジェットの型ヒント'''