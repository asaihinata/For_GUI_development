from test_data import *
if __name__=="__main__":
 layout=[
  [
   sgg.Eventplot(data=eventdata,title="イベントグラフの基本",xlabel="x軸のラベル",ylabel="y軸のラベル"),
   sgg.Eventplot(data=eventdata,title="ラベル付き",label=["a","b","c"])
  ],
  [
   sgg.Eventplot(data=eventdata,title="イベントグラフの基本",),
   sgg.Eventplot(data=eventdata,title="ラベル付き",label=["a","b","c"])
  ],
 ]
 win=sgg.window(title="箱ひげ図(デモ)",layout=layout,scroll_x=True,scroll_y=True,maxmine=True)
 win.run()