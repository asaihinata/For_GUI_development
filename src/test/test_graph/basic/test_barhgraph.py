from _import import *
if __name__=="__main__":
 def updates():
  radomdata=rng.integers(30,60,size=5)
  print(f"{radomdata=}")
  barhGraph:BarhGraph=win.get("BarhGraph")
  barhGraph.update(y=radomdata)
 print(f"{bargraphx1=}")
 print(f"{bargraphx2=}")
 print(f"{bargraphy1=}")
 print(f"{bargraphy2=}")
 layout=[
  [
   sgg.BarhGraph(x=bargraphx1,y=bargraphy1,title="横軸棒グラフの基本1",xlabel=xlabel,ylabel=ylabel,label=["bar1"]),
   sgg.BarhGraph(x=bargraphx2,y=bargraphy2,title="横軸棒グラフの基本2",xlabel=xlabel,ylabel=ylabel,label=["bar1","bar2"])
  ],
  [
   sgg.BarhGraph(x=bargraphx1,y=bargraphy1,title="x軸を対数スケールにする",logs=True),
   sgg.BarhGraph(x=bargraphx1,y=bargraphy1,title="グラフの開始位置の変更",align="edge")
  ],
  [
   sgg.BarhGraph(x=bargraphx1,y=bargraphy1,title="グラフの幅の変更",height=0.4)
  ],
  [
   sgg.BarhGraph(x=bargraphx1,y=bargraphy1,title="グラフを更新する",key="BarhGraph"),
   sgg.Buttons(text="更新ボタン",function=updates)
  ]
 ]
 win=sgg.window(title="横軸棒グラフ(test)",layout=layout,scroll=True,maxmine=True)
 win.run()