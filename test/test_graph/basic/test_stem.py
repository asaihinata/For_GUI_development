from test_data import *
if __name__=="__main__":
 def updates():
  radomdata=rand.randrange(50,80,size=(2,3))
  print(f"{radomdata=}")
  stemplot:Stem=win.get("stem")
  stemplot.update(x=radomdata)
 print(f"{stemx1=}")
 print(f"{stemx2=}")
 print(f"{stemy=}")
 layout=[
  [
   sgg.Stem(x=stemx1,y=stemy,title="幹図の基本1",xlabel=xlabel,ylabel=ylabel),
   sgg.Stem(x=stemx2,y=stemy,title="幹図の基本2",xlabel=xlabel,ylabel=ylabel)
  ],
  [
   sgg.Stem(x=stemx1,y=stemy,title="マーカーを変更する",marker="^"),
   sgg.Stem(x=stemx1,y=stemy,title="幹図の向きを指定する",orientation="horizontal")
  ],
  [
   sgg.Stem(x=stemx1,y=stemy,title="ベースラインを変更する",bottom=30),
   sgg.Stem(x=stemx1,y=stemy,title="ベースラインを変更する",bottom=30,orientation="horizontal")
  ],
  [
   sgg.Stem(x=stemx1,y=stemy,title="幹図の色を変更する",color="b"),
   sgg.Stem(x=stemx1,y=stemy,title="幹図の線を変更する",line="--")
  ],
  [
   sgg.Stem(x=stemx2,y=stemy,title="グラフを更新する",key="stem"),
   sgg.Buttons(text="更新ボタン",function=updates)
  ]
 ]
 win=sgg.window(title="幹図(デモ)",layout=layout,scroll=True,maxmine=True)
 win.run()