from test_data import *
if __name__=="__main__":
 layout=[
  [
   sgg.BarhGraph(x=bargraphx1,y=bargraphy1,title="横軸棒グラフの基本1",xlabel="x軸のラベル",ylabel="y軸のラベル"),
   sgg.BarhGraph(x=bargraphx2,y=bargraphy2,title="横軸棒グラフの基本2")
  ],
  [
   sgg.BarhGraph(x=bargraphx1,y=bargraphy1,title="x軸を対数スケールにする",logs=True),
   sgg.BarhGraph(x=bargraphx1,y=bargraphy1,title="グラフの開始位置の変更",align="edge")
  ],
  [sgg.BarhGraph(x=bargraphx1,y=bargraphy1,title="グラフの幅の変更",height=0.4)]
 ]
 win=sgg.window(title="横軸棒グラフ(デモ)",layout=layout,scroll_x=True,scroll_y=True,maxmine=True)
 win.run()