from _import import *
if __name__=="__main__":
 def updates():
  radomdata=rng.integers(1,10,(3,3))+2
  print(f"{radomdata=}")
  stackh:Stackedh=win.get("stackedh")
  stackh.update(radomdata)
 print(f"{stackeddata=}")
 print(f"{stackeddataname=}")
 layout=[
  [
   sgg.Stackedh(data=stackeddata,dataname=stackeddataname,title="積み上げ横棒グラフの基本",xlabel=xlabel,ylabel=ylabel),
   sgg.Stackedh(data=stackeddata,dataname=stackeddataname,title="幅を変更する",height=0.5)
  ],
  [
   sgg.Stackedh(data=stackeddata,dataname=stackeddataname,title="グラフを更新する",key="stackedh"),
   sgg.Buttons(text="更新ボタン",function=updates)
  ]
 ]
 win=sgg.window(title="積み上げ横棒グラフ(test)",layout=layout,scroll=True,maxmine=True)
 win.run()