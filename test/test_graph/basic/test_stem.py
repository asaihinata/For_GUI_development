from test_data import *
if __name__=="__main__":
 print(f"{stemx1=}")
 print(f"{stemy1=}")
 print(f"{stemx2=}")
 print(f"{stemy2=}")
 layout=[
  [
   sgg.Stem(x=stemx1,y=stemy1,title="幹図の基本1",xlabel=xlabel,ylabel=ylabel),
   sgg.Stem(x=stemx2,y=stemy2,title="幹図の基本2",xlabel=xlabel,ylabel=ylabel)
  ],
  [
   sgg.Stem(x=stemx1,y=stemy1,title="マーカーを変更する",marker="^"),
   sgg.Stem(x=stemx1,y=stemy1,title="幹図の向きを指定する",orientation="horizontal")
  ],
  [
   sgg.Stem(x=stemx1,y=stemy1,title="ベースラインを変更する",bottom=30),
   sgg.Stem(x=stemx1,y=stemy1,title="ベースラインを変更する",bottom=30,orientation="horizontal")
  ],
  [
   sgg.Stem(x=stemx1,y=stemy1,title="幹図の色を変更する",color="b"),
   sgg.Stem(x=stemx1,y=stemy1,title="幹図の線を変更する",line="--")
  ]
 ]
 win=sgg.window(title="幹図(デモ)",layout=layout,scroll=True,maxmine=True)
 win.run()