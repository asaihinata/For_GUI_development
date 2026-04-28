from _import import *
if __name__=="__main__":
 def updates():
  radomdata=rand.normal(low=100,high=10,lenght=100)
  print(f"{radomdata=}")
  boxplot:Boxplot=win.get("boxplot")
  boxplot.update(radomdata)
 print(f"{boxdata1=}")
 print(f"{boxdata2=}")
 layout=[
  [
   sgg.Boxplot(data=boxdata1,title="箱ひげ図の基本1",xlabel=xlabel,ylabel=ylabel),
   sgg.Boxplot(data=boxdata2,title="箱ひげ図の基本2",xlabel=xlabel,ylabel=ylabel)
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
  ],
  [
   sgg.Boxplot(data=boxdata1,title="グラフを更新する",key="boxplot"),
   sgg.Buttons(text="更新ボタン",function=updates)
  ]
 ]
 win=sgg.window(title="箱ひげ図(test)",layout=layout,scroll=True,maxmine=True)
 win.run()