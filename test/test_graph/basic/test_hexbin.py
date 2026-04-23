from test_data import *
if __name__=="__main__":
 print(f"{hexbinx1=}")
 print(f"{hexbiny1=}")
 print(f"{hexbinx2=}")
 print(f"{hexbiny2=}")
 layout=[
  [
   sgg.Hexbin(x=hexbinx1,y=hexbiny1,title="2次元六角形グラフの基本",xlabel=xlabel,ylabel=ylabel),
   sgg.Hexbin(x=hexbinx1,y=hexbiny1,title="binsの細かさを指定する",gridsize=300)
  ],
  [
   sgg.Hexbin(x=hexbinx1,y=hexbiny1,title="表示させる範囲を指定する",extent=[-1.0,1.0,-1.0,1.0]),
   sgg.Hexbin(x=hexbinx1,y=hexbiny1,title="描画するbinsの最小を指定する",mincnt=3)
  ],
  [
   sgg.Hexbin(x=hexbinx2,y=hexbiny2,title="x軸を対数にする",xscale="log"),
   sgg.Hexbin(x=hexbinx2,y=hexbiny2,title="y軸を対数にする",yscale="log")
  ],
  [
   sgg.Hexbin(x=hexbinx1,y=hexbiny1,title="binsを指定する",bins="log")
  ]
 ]
 win=sgg.window(title="2次元六角形グラフ(デモ)",layout=layout,scroll=True,maxmine=True)
 win.run()