from _import import *
if __name__=="__main__":
 def updates():
  radomdata=rng.gamma(4,size=(5,50))
  print(f"{radomdata=}")
  eventpolar:Eventpolar=win.get("eventpolar")
  eventpolar.update(data=radomdata)
 print(f"{eventdata=}")
 layout=[
  [
   sgg.Eventpolar(data=eventdata,title="極軸イベントグラフの基本"),
   sgg.Eventpolar(data=eventdata,title="ラベルを付ける",label=["a","b","c"])
  ],
  [
   sgg.Eventpolar(data=eventdata,title="向きを指定する",orientation="horizontal"),
   sgg.Eventpolar(data=eventdata,title="線の種類を変更する",linestyle=":")
  ],
  [
   sgg.Eventpolar(data=eventdata,title="線の幅を変更する",linelength=0.5),
   sgg.Eventpolar(data=eventdata,title="線の高さを変更する",linewidth=2)
  ],
  [
   sgg.Eventpolar(data=eventdata,title="グラフを更新する",key="eventpolar"),
   sgg.Buttons(text="更新ボタン",function=updates)
  ]
 ]
 win=sgg.window(title="極軸イベントグラフ(test)",layout=layout,scroll=True,maxmine=True)
 win.run()