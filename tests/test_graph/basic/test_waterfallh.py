from test_data import *
if __name__=="__main__":
 layout=[
  [
   sgg.Waterfallh(x=waterfallx,y=waterfally,title="ウォーターフォールの基本",xlabel="x軸のラベル",ylabel="y軸のラベル"),
   sgg.Waterfallh(x=waterfallx,y=waterfally,title="バーの幅を変更する",width=0.5)
  ],
  [
   sgg.Waterfallh(x=waterfallx,y=waterfally,title="バーとバーを繋ぐ線の種類を変更する",width=0.5,linestyle="dotted"),
   sgg.Waterfallh(x=waterfallx,y=waterfally,title="バーとバーを繋ぐ線の色を変更する",width=0.5,colorline="green")
  ],
  [
   sgg.Waterfallh(x=waterfallx,y=waterfally,title="上昇バーの色を変更する",ucolor="pink"),
   sgg.Waterfallh(x=waterfallx,y=waterfally,title="減少バーの色を変更する",dcolor="aqua")
  ],
  [
   sgg.Waterfallh(x=waterfallx,y=waterfally,title="合計を表示させる",sums=True),
   sgg.Waterfallh(x=waterfallx,y=waterfally,title="合計を表示させる",sums=True,sumstext="合計")
  ]
 ]
 win=sgg.window(title="横向きのウォーターフォール(デモ)",layout=layout,scroll_x=True,scroll_y=True,maxmine=True)
 win.run()