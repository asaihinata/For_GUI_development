from test_data import *
if __name__=="__main__":
 layout=[
  [
   sgg.Stack(x=stackx,y=stacky,title="積み上げグラフの基本",xlabel="x軸のラベル",ylabel="y軸のラベル"),
   sgg.Stack(x=stackx,y=stacky,title="塗りつぶす領域内の模様を指定する",hatch="-")
  ],
  [
   sgg.Stack(x=stackx,y=stacky,title="積み上げグラフの積み上げる基準を指定する",baseline="weighted_wiggle"),
  ],
 ]
 win=sgg.window(title="積み上げエリアチャート(デモ)",layout=layout,scroll_x=True,scroll_y=True,maxmine=True)
 win.run()