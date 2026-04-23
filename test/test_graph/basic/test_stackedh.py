from test_data import *
if __name__=="__main__":
 print(f"{stackeddata=}")
 print(f"{stackeddataname=}")
 layout=[
  [
   sgg.Stackedh(data=stackeddata,dataname=stackeddataname,title="積み上げ横棒グラフの基本",xlabel=xlabel,ylabel=ylabel),
   sgg.Stackedh(data=stackeddata,dataname=stackeddataname,title="幅を変更する",height=0.5)
  ]
 ]
 win=sgg.window(title="積み上げ横棒グラフ(デモ)",layout=layout,scroll=True,maxmine=True)
 win.run()