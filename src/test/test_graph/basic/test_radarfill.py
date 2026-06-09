from _import import *
if __name__=="__main__":
 def updates():
  radomdata=rng.integers(50,100,size=5)
  print(f"{radomdata=}")
  radarfill:RadarFill=win.get("radarfill")
  radarfill.update(data=radomdata)
 print(f"{radarfilldata1=}")
 print(f"{radarfilldata2=}")
 layout=[
  [
   sgg.RadarFill(data=radarfilldata1,title="塗りつぶしレーダーチャートの基本1"),
   sgg.RadarFill(data=radarfilldata2,title="塗りつぶしレーダーチャートの基本2")
  ],
  [
   sgg.RadarFill(data=radarfilldata1,alpha=0.5,title="透明度を変更する")
  ],
  [
   sgg.RadarFill(data=radarfilldata1,title="グラフを更新する",key="radarfill"),
   sgg.Buttons(text="更新ボタン",function=updates)
  ]
 ]
 win=sgg.window(title="塗りつぶしレーダーチャート(test)",layout=layout,scroll=True,maxmine=True)
 win.run()