from _import import *
from data.csv import getcsv
if __name__=='__main__':
 data=np.array(getcsv('school_test_demo_data.csv'))
 layout=[]
 for i in range(6):
  tab=[]
  for j in range(1,6):
   datas=data[j+i*5]
   tab.append([datas[0],[[sgg.BarGraph(x=['国語','社会','数学','理科'],y=datas[1::].astype(np.int64),title='教科別の点数',xlabel='教科名',ylabel='点数')]]])
  layout.append([sgg.Tab(tabs=tab)])
 win=sgg.window(title='テストの結果(デモ)',layout=layout,scroll_x=True,scroll_y=True,maxmine=True)
 win.run()