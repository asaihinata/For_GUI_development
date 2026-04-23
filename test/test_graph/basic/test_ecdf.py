from test_data import *
if __name__=="__main__":
 print(f"{ecdfdata=}")
 layout=[
  [
   sgg.Ecdf(data=ecdfdata,title="経験的累積分布関数の基本",xlabel=xlabel,ylabel=ylabel),
   sgg.Ecdf(data=ecdfdata,title="同一値のデータをまとめて最適化する",compress=True)
  ],
  [
   sgg.Ecdf(data=ecdfdata,title="経験的累積分布関数の向きを変える",orientation="horizontal"),
   sgg.Ecdf(data=ecdfdata,title="補累積分布を描画する",complementary=True)
  ],
  [
   sgg.Ecdf(data=ecdfdata,title="線の幅を変える",linewidth=3),
   sgg.Ecdf(data=ecdfdata,title="線の種類を変える",linestyle="dotted")
  ]
 ]
 win=sgg.window(title="経験的累積分布関数(デモ)",layout=layout,scroll=True,maxmine=True)
 win.run()