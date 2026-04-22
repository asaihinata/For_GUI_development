from test_data import *
if __name__=="__main__":
 layout=[
  [
   sgg.Scatter(x=scatterx1,y=scattery1,title="散布図の基本1",xlabel="x軸のラベル",ylabel="y軸のラベル"),
   sgg.Scatter(x=scatterx2,y=scattery2,title="散布図の基本2",xlabel="x軸のラベル",ylabel="y軸のラベル")
  ],
  [
   sgg.Scatter(x=scatterx1,y=scattery1,title="マーカーの指定",marker="d"),
   sgg.Scatter(x=scatterx1,y=scattery1,title="マーカーサイズの変更",marker="d",markersize=20),
  ]
 ]
 win=sgg.window(title="散布図(デモ)",layout=layout,scroll_x=True,scroll_y=True,maxmine=True)
 win.run()