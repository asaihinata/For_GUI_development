from test_data import *
if __name__=="__main__":
 def updates():
  radomdata1=rand.randn(5000)
  radomdata2=1.4*radomdata1+rand.randn(5000)/3
  print(f"{radomdata1=}")
  print(f"{radomdata2=}")
  hist2d:Hist2d=win.get("hist2d")
  hist2d.update(x=radomdata1,y=radomdata2)
 print(f"{hist2dx}")
 print(f"{hist2dy}")
 layout=[
  [
   sgg.Hist2d(x=hist2dx,y=hist2dy,title="2次元ヒストグラムの基本",xlabel=xlabel,ylabel=ylabel),
   sgg.Hist2d(x=hist2dx,y=hist2dy,title="2次元ヒストグラムを正規化する",density=True)
  ],
  [
   sgg.Hist2d(x=hist2dx,y=hist2dy,title="x軸に表示させる範囲を指定する",xmax=5,xmin=-5),
   sgg.Hist2d(x=hist2dx,y=hist2dy,title="y軸に表示させる範囲を指定する",ymax=5,ymin=-5)
  ],
  [
   sgg.Hist2d(x=hist2dx,y=hist2dy,title="binsを指定する",bins=5)
  ],
  [
   sgg.Hist2d(x=hist2dx,y=hist2dy,title="グラフを更新する",key="hist2d"),
   sgg.Buttons(text="更新ボタン",function=updates)
  ]
 ]
 win=sgg.window(title="2次元ヒストグラム(デモ)",layout=layout,scroll=True,maxmine=True)
 win.run()