from test_data import *
if __name__=="__main__":
 print(f"{stackx=}")
 print(f"{stacky=}")
 layout=[
  [
   sgg.Stack(x=stackx,y=stacky,title="積み上げグラフの基本",xlabel=xlabel,ylabel=ylabel),
   sgg.Stack(x=stackx,y=stacky,title="塗りつぶす領域内の模様を指定する",hatch="-")
  ],
  [
   sgg.Stack(x=stackx,y=stacky,title="積み上げグラフの積み上げる基準を指定する",baseline="weighted_wiggle")
  ]
 ]
 win=sgg.window(title="積み上げエリアチャート(デモ)",layout=layout,scroll=True,maxmine=True)
 win.run()