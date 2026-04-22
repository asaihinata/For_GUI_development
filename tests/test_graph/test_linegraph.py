from test_data import *
if __name__=="__main__":
 layout=[
  [
   sgg.LineGraph(x=linex1,y=liney1,title="折り線グラフの基本",xlabel="x軸のラベル",ylabel="y軸のラベル"),
   sgg.LineGraph(x=linex2,y=liney2,title="複数の折り線グラフを表示させる")
  ],
  [
   sgg.LineGraph(x=linex2,y=liney2,title="凡例の表示",label=["label1","label2","label3","label4"]),
   sgg.LineGraph(x=linex2,y=liney2,title="線の色の変更",color=["red","green","#eeeeee","rgb(0,0,0)"])
  ],
  [
   sgg.LineGraph(x=linex1,y=liney1,title="マーカーの大きさを変更する",marker="d",markersize=20),
   sgg.LineGraph(x=linex1,y=liney1,title="マーカーを付ける",marker="d")
  ],
  [sgg.LineGraph(x=linex1,y=liney1,title="線の種類を変更する",linestyle="--")]
 ]
 win=sgg.window(title="折り線グラフ(デモ)",layout=layout,scroll_x=True,scroll_y=True,maxmine=True)
 win.run()