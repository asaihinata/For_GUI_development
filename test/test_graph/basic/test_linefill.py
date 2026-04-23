from test_data import *
if __name__=="__main__":
 print(f"{linefillx=}")
 print(f"{linefillymax=}")
 print(f"{linefillymin=}")
 layout=[
  [
   sgg.Linefill(x=linefillx,ymax=linefillymax,ymin=linefillymin,title="積上げ面グラフの基本",xlabel=xlabel,ylabel=ylabel),
   sgg.Linefill(x=linefillx,ymax=linefillymax,ymin=linefillymin,title="中心の線の太さを変更する",centerlinewidth=5)
  ]
 ]
 win=sgg.window(title="積上げ面グラフ(デモ)",layout=layout,scroll=True,maxmine=True)
 win.run()