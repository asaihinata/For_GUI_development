from test_data import *
if __name__=="__main__":
 print(f"{histdata=}")
 layout=[
  [
   sgg.Hist(data=histdata,title="ヒストグラフの基本",xlabel=xlabel,ylabel=ylabel),
   sgg.Hist(data=histdata,title="表示される範囲を指定する",min=50,max=75)
  ],
  [
   sgg.Hist(data=histdata,title="表示する小数点を指定する",decimalpoint=1),
   sgg.Hist(data=histdata,title="表示される向きを指定する",orientation="horizontal")
  ],
  [
   sgg.Hist(data=histdata,title="binsを指定する",bins=5),
   sgg.Hist(data=histdata,title="binsを指定する",bins="doane")
  ],
  [
   sgg.Hist(data=histdata,title="binsを指定する",bins=[30,40,50]),
   sgg.Hist(data=histdata,title="幅を指定する",width=0.4)
  ]
 ]
 win=sgg.window(title="ヒストグラフ(デモ)",layout=layout,scroll=True,maxmine=True)
 win.run()