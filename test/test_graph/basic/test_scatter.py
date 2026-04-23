from test_data import *
if __name__=="__main__":
 print(f"{scatterx1=}")
 print(f"{scattery1=}")
 print(f"{scatterx2=}")
 print(f"{scattery2=}")
 layout=[
  [
   sgg.Scatter(x=scatterx1,y=scattery1,title="散布図の基本1",xlabel=xlabel,ylabel=ylabel),
   sgg.Scatter(x=scatterx2,y=scattery2,title="散布図の基本2",xlabel=xlabel,ylabel=ylabel)
  ],
  [
   sgg.Scatter(x=scatterx1,y=scattery1,title="マーカーの指定",marker="d"),
   sgg.Scatter(x=scatterx1,y=scattery1,title="マーカーサイズの変更",marker="d",markersize=20)
  ]
 ]
 win=sgg.window(title="散布図(デモ)",layout=layout,scroll=True,maxmine=True)
 win.run()