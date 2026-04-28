from _import import *
if __name__=="__main__":
 def updates():
  radomdata=rand.randint(10,50,size=3)
  print(f"{radomdata=}")
  funne:Funne=win.get("funne")
  funne.update(radomdata)
 print(f"{funnedata=}")
 layout=[
  [
   sgg.Funne(data=funnedata,title="じょうごグラフの基本",xlabel=xlabel,ylabel=ylabel),
   sgg.Funne(data=funnedata,title="高さを変更する",height=0.5)
  ],
  [
   sgg.Funne(data=funnedata,title="グラフを更新する",key="funne"),
   sgg.Buttons(text="更新ボタン",function=updates)
  ]
 ]
 win=sgg.window(title="じょうごグラフ(test)",layout=layout,scroll=True,maxmine=True)
 win.run()