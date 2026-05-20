from _import import *
if __name__=="__main__":
 def updates():
  radomdata=randrange(50,80,size=(4,3))
  print(f"{radomdata=}")
  lineplot:LineGraph=win.get("lineplot")
  lineplot.update(y=radomdata)
 print(f"{linex=}")
 print(f"{liney1=}")
 print(f"{liney2=}")
 layout=[
  [
   sgg.LineGraph(x=linex,y=liney1,title="折り線グラフの基本",xlabel=xlabel,ylabel=ylabel),
   sgg.LineGraph(x=linex,y=liney2,title="複数の折り線グラフを表示させる")
  ],
  [
   sgg.LineGraph(x=linex,y=liney2,title="凡例の表示",label=["label1","label2","label3","label4"]),
   sgg.LineGraph(x=linex,y=liney2,title="線の色の変更",color=["red","green","#eeeeee","rgb(0,0,0)"])
  ],
  [
   sgg.LineGraph(x=linex,y=liney1,title="マーカーを変更する",marker="d"),
   sgg.LineGraph(x=linex,y=liney1,title="マーカーの大きさを変更する",marker="d",markersize=20)
  ],
  [
   sgg.LineGraph(x=linex,y=liney1,title="線の種類を変更する",linestyle="--")
  ],
  [
   sgg.LineGraph(x=linex,y=liney2,title="グラフを更新する",key="lineplot"),
   sgg.Buttons(text="更新ボタン",function=updates)
  ]
 ]
 win=sgg.window(title="折り線グラフ(test)",layout=layout,scroll=True,maxmine=True)
 win.run()