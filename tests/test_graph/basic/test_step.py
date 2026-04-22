from test_data import *
if __name__=="__main__":
 layout=[
  [
   sgg.Step(data=stepdata,title="階段グラフの基本",xlabel="x軸のラベル",ylabel="y軸のラベル"),
   sgg.Step(data=stepdata,title="階段の範囲を指定する",range=5)
  ],
  [
   sgg.Step(data=stepdata,title="階段を塗りつぶす",fill=True),
   sgg.Step(data=stepdata,title="階段の基準を指定する",baseline=3)
  ],
  [
   sgg.Step(data=stepdata,title="階段の向きを変更する",orientation="horizontal")
  ]
 ]
 win=sgg.window(title="階段グラフ(デモ)",layout=layout,scroll_x=True,scroll_y=True,maxmine=True)
 win.run()