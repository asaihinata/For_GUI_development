from test_data import *
if __name__=="__main__":
 print(f"{linex1=}")
 print(f"{liney1=}")
 print(f"{linex2=}")
 print(f"{liney2=}")
 layout=[
  [
   sgg.LineGraph(x=linex1,y=liney1,title="折り線グラフの基本",xlabel=xlabel,ylabel=ylabel),
   sgg.LineGraph(x=linex2,y=liney2,title="複数の折り線グラフを表示させる")
  ],
  [
   sgg.LineGraph(x=linex2,y=liney2,title="凡例の表示",label=["label1","label2","label3","label4"]),
   sgg.LineGraph(x=linex2,y=liney2,title="線の色の変更",color=["red","green","#eeeeee","rgb(0,0,0)"])
  ],
  [
   sgg.LineGraph(x=linex1,y=liney1,title="マーカーを変更する",marker="d"),
   sgg.LineGraph(x=linex1,y=liney1,title="マーカーの大きさを変更する",marker="d",markersize=20)
  ],
  [
   sgg.LineGraph(x=linex1,y=liney1,title="線の種類を変更する",linestyle="--")
  ]
 ]
 win=sgg.window(title="折り線グラフ(デモ)",layout=layout,scroll=True,maxmine=True)
 win.run()