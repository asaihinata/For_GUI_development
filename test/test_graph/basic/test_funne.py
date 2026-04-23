from test_data import *
if __name__=="__main__":
 print(f"{funnedata=}")
 layout=[
  [
   sgg.Funne(data=funnedata,title="じょうごグラフの基本",xlabel=xlabel,ylabel=ylabel),
   sgg.Funne(data=funnedata,title="高さを変更する",height=0.5)
  ]
 ]
 win=sgg.window(title="じょうごグラフ(デモ)",layout=layout,scroll=True,maxmine=True)
 win.run()