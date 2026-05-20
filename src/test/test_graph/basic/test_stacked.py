from _import import *
if __name__=="__main__":
 def updates():
  radomdata=rng.integers(1,10,(3,3))+2
  print(f"{radomdata=}")
  stack:Stacked=win.get("stacked")
  stack.update(radomdata)
 print(f"{stackeddata=}")
 print(f"{stackeddataname=}")
 layout=[
  [
   sgg.Stacked(data=stackeddata,dataname=stackeddataname,title="積み上げ縦棒グラフの基本",xlabel=xlabel,ylabel=ylabel),
   sgg.Stacked(data=stackeddata,dataname=stackeddataname,title="幅を変更する",width=0.5)
  ],
  [
   sgg.Stacked(data=stackeddata,dataname=stackeddataname,title="グラフを更新する",key="stacked"),
   sgg.Buttons(text="更新ボタン",function=updates)
  ]
 ]
 win=sgg.window(title="積み上げ縦棒グラフ(test)",layout=layout,scroll=True,maxmine=True)
 win.run()