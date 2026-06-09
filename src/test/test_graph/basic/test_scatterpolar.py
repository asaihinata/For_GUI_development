from _import import *
if __name__=="__main__":
 def updates():
  radomdata=rng.integers(0,10,5)
  print(f"{radomdata=}")
  scatterpolor:Scatterpolar=win.get("scatterpolor")
  scatterpolor.update(y=radomdata)
 print(f"{scatterpolorx=}")
 print(f"{scatterpolory=}")
 print(f"{scatterpolordata=}")
 layout=[
  [
   sgg.Scatterpolar(x=scatterpolorx,y=scatterpolory,title="極軸散布図の基本1"),
   sgg.Scatterpolar(data=scatterpolordata,title="極軸散布図の基本2")
  ],
  [
   sgg.Scatterpolar(x=scatterpolorx,y=scatterpolory,title="マーカーの指定",marker="d"),
   sgg.Scatterpolar(x=scatterpolorx,y=scatterpolory,title="マーカーサイズの変更",marker="d",markersize=20)
  ],
  [
   sgg.Scatterpolar(x=scatterpolorx,y=scatterpolory,title="グラフを更新する",key="scatterpolor"),
   sgg.Buttons(text="更新ボタン",function=updates)
  ]
 ]
 win=sgg.window(title="極軸散布図(test)",layout=layout,scroll=True,maxmine=True)
 win.run()