from test_data import *
if __name__=="__main__":
 print(f"{eventdata=}")
 layout=[
  [
   sgg.Eventplot(data=eventdata,title="イベントグラフの基本",xlabel=xlabel,ylabel=ylabel),
   sgg.Eventplot(data=eventdata,title="ラベルを付ける",label=["a","b","c"])
  ],
  [
   sgg.Eventplot(data=eventdata,title="向きを指定する",orientation="horizontal"),
   sgg.Eventplot(data=eventdata,title="線の種類を変更する",linestyle=":")
  ],
  [
   sgg.Eventplot(data=eventdata,title="線の幅を変更する",linelength=0.5),
   sgg.Eventplot(data=eventdata,title="線の高さを変更する",linewidth=2)
  ]
 ]
 win=sgg.window(title="イベントグラフ(デモ)",layout=layout,scroll=True,maxmine=True)
 win.run()