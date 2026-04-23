from test_data import *
if __name__=="__main__":
 print(f"{stackeddata=}")
 print(f"{stackeddataname=}")
 layout=[
  [
   sgg.Stacked(data=stackeddata,dataname=stackeddataname,title="積み上げ縦棒グラフの基本",xlabel=xlabel,ylabel=ylabel),
   sgg.Stacked(data=stackeddata,dataname=stackeddataname,title="幅を変更する",width=0.5)
  ]
 ]
 win=sgg.window(title="積み上げ縦棒グラフ(デモ)",layout=layout,scroll=True,maxmine=True)
 win.run()