from test_data import *
if __name__=="__main__":
 print(f"{hatplotx=}")
 print(f"{hatplotdata=}")
 layout=[
  [
   sgg.Hatplot(x=hatplotx,data=hatplotdata,title="ハットグラフの基本",xlabel=xlabel,ylabel=ylabel,yticksrange=5),
  ]
 ]
 win=sgg.window(title="ハットグラフ(デモ)",layout=layout,scroll=True,maxmine=True)
 win.run()