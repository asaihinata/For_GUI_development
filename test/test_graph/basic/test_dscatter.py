from test_data import *
if __name__=="__main__":
 print(f"{dscatterx=}")
 print(f"{dscattery=}")
 print(f"{dscatterz=}")
 layout=[
  [
   sgg.DScatter(x=dscatterx,y=dscattery,z=dscatterz,title="3D散布図の基本",xlabel=xlabel,ylabel=ylabel,zlabel=zlabel),
   sgg.DScatter(x=dscatterx,y=dscattery,z=dscatterz,title="グラフを動かす",xlabel=xlabel,ylabel=ylabel,zlabel=zlabel,mouse_rotation=False)
  ],
  [
   sgg.DScatter(x=dscatterx,y=dscattery,z=dscatterz,title="マーカーを指定する",marker="*"),
   sgg.DScatter(x=dscatterx,y=dscattery,z=dscatterz,title="マーカーサイズを変更する",marker=2,markersize=20)
  ]
 ]
 win=sgg.window(title="3D散布図(デモ)",layout=layout,scroll=True,maxmine=True)
 win.run()