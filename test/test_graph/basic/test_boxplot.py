from test_data import *
if __name__=="__main__":
 layout=[
  [
   sgg.Boxplot(data=boxdata1,title="箱ひげ図の基本1",xlabel="x軸のラベル",ylabel="y軸のラベル"),
   sgg.Boxplot(data=boxdata2,title="箱ひげ図の基本2",xlabel="x軸のラベル",ylabel="y軸のラベル")
  ],
  [
   sgg.Boxplot(data=boxdata1,title="凡例を非表示にする",legend=False),
   sgg.Boxplot(data=boxdata1,title="箱ひげ図に窪みを入れる",notch=True)
  ],
  [
   sgg.Boxplot(data=boxdata1,title="外れ値を非表示にする",showfliers=False),
   sgg.Boxplot(data=boxdata1,title="箱ひげ図の向きを変える",orientation="horizontal")
  ],
  [
   sgg.Boxplot(data=boxdata1,title="箱ひげ図の髭の開始位置を変更する1",whis=2),
   sgg.Boxplot(data=boxdata1,title="箱ひげ図の髭の開始位置を変更する2",whis=[10,90])
  ],
  [
   sgg.Boxplot(data=boxdata1,title="箱ひげ図の幅を変更する",width=0.5)
  ]
 ]
 win=sgg.window(title="箱ひげ図(デモ)",layout=layout,scroll_x=True,scroll_y=True,maxmine=True)
 win.run()