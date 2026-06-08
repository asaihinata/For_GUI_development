from _import import *
if __name__=="__main__":
 def updates():
  radomdata=rng.integers(10,15,size=5)
  print(f"{radomdata=}")
  radarplots:Radarplot=win.get("radarplot")
  radarplots.update(data=radomdata)
 print(f"{radarplotdata=}")
 layout=[
  [
   sgg.Radarplot(data=radarplotdata,title="レーダーチャートの基本"),
   sgg.Radarplot(data=radarplotdata,linewidth=10,title="線の太さを変更する")
  ],
  [
   sgg.Radarplot(data=radarplotdata,marker="+",title="マーカーを表示させる"),
   sgg.Radarplot(data=radarplotdata,marker="+",markersize=20,title="マーカーの大きさを変える")
  ],
  [
   sgg.Radarplot(data=radarplotdata,title="グラフを更新する",key="radarplot"),
   sgg.Buttons(text="更新ボタン",function=updates)
  ]
 ]
 win=sgg.window(title="レーダーチャート(test)",layout=layout,scroll=True,maxmine=True)
 win.run()