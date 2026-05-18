from _import import *
if __name__=="__main__":
 def updates():
  radomdata=rng.integers(-100,100,6)
  print(f"{radomdata=}")
  waterfallh:Waterfallh=win.get("waterfallh")
  waterfallh.update(y=radomdata)
 print(f"{waterfallx=}")
 print(f"{waterfally=}")
 layout=[
  [
   sgg.Waterfallh(x=waterfallx,y=waterfally,title="横向きのウォーターフォールの基本",xlabel=xlabel,ylabel=ylabel),
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
  ],
  [
   sgg.Waterfallh(x=waterfallx,y=waterfally,title="グラフを更新する",key="waterfallh"),
   sgg.Buttons(text="更新ボタン",function=updates)
  ]
 ]
 win=sgg.window(title="横向きのウォーターフォール(test)",layout=layout,scroll=True,maxmine=True)
 win.run()