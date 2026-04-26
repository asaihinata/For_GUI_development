from test_data import *
if __name__=="__main__":
 def updates():
  radomdata1=3+4*linefillx/8+rand.rands(0.0,0.5,len(linefillx))
  radomdata2=1+2*linefillx/8+rand.rands(0.0,0.5,len(linefillx))
  print(f"{radomdata1=}")
  print(f"{radomdata2=}")
  linefill:Linefill=win.get("linefill")
  linefill.update(x=linefillx,ymax=radomdata1,ymin=radomdata2)
 print(f"{linefillx=}")
 print(f"{linefillymax=}")
 print(f"{linefillymin=}")
 layout=[
  [
   sgg.Linefill(x=linefillx,ymax=linefillymax,ymin=linefillymin,title="積上げ面グラフの基本",xlabel=xlabel,ylabel=ylabel),
   sgg.Linefill(x=linefillx,ymax=linefillymax,ymin=linefillymin,title="中心の線の太さを変更する",centerlinewidth=5)
  ],
  [
   sgg.Linefill(x=linefillx,ymax=linefillymax,ymin=linefillymin,title="グラフを更新する",key="linefill"),
   sgg.Buttons(text="更新ボタン",function=updates)
  ]
 ]
 win=sgg.window(title="積上げ面グラフ(デモ)",layout=layout,scroll=True,maxmine=True)
 win.run()