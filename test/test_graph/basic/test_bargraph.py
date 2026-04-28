from _import import *
if __name__=="__main__":
 def updates():
  radomdata=rand.randint(30,60,size=5)
  print(f"{radomdata=}")
  barGraph:BarGraph=win.get("BarGraph")
  barGraph.update(y=radomdata)
 print(f"{bargraphx1=}")
 print(f"{bargraphx2=}")
 print(f"{bargraphy1=}")
 print(f"{bargraphy2=}")
 layout=[
  [
   sgg.BarGraph(x=bargraphx1,y=bargraphy1,title="縦軸棒グラフの基本1",xlabel=xlabel,ylabel=ylabel),
   sgg.BarGraph(x=bargraphx2,y=bargraphy2,title="縦軸棒グラフの基本2",xlabel=xlabel,ylabel=ylabel)
  ],
  [
   sgg.BarGraph(x=bargraphx1,y=bargraphy1,title="y軸を対数スケールにする",logs=True),
   sgg.BarGraph(x=bargraphx1,y=bargraphy1,title="グラフの開始位置の変更",align="edge")
  ],
  [
   sgg.BarGraph(x=bargraphx1,y=bargraphy1,title="グラフの幅の変更",width=0.4)
  ],
  [
   sgg.BarGraph(x=bargraphx1,y=bargraphy1,title="グラフを更新する",key="BarGraph"),
   sgg.Buttons(text="更新ボタン",function=updates)
  ]
 ]
 win=sgg.window(title="縦軸棒グラフ(test)",layout=layout,scroll=True,maxmine=True)
 win.run()