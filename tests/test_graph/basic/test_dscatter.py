from test_data import *
if __name__=="__main__":
 layout=[
  [
   sgg.DScatter(x=dscatterx,y=dscattery,z=dscatterz,title="3D散布図の基本",xlabel="x軸のラベル",ylabel="y軸のラベル",zlabel="z軸のラベル"),
   sgg.DScatter(x=dscatterx,y=dscattery,z=dscatterz,title="グラフを動かす",xlabel="x軸のラベル",ylabel="y軸のラベル",zlabel="z軸のラベル",mouse_rotation=False),
  ],
  [
   sgg.DScatter(x=dscatterx,y=dscattery,z=dscatterz,title="マーカーを指定する",marker="*"),
   sgg.DScatter(x=dscatterx,y=dscattery,z=dscatterz,title="マーカーサイズを変更する",marker=2,markersize=20)
  ]
 ]
 win=sgg.window(title="3D 散布図(デモ)",layout=layout,scroll_x=True,scroll_y=True,maxmine=True)
 win.run()