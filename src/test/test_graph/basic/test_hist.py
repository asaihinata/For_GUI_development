from _import import *

if __name__ == "__main__":

    def updates():
        radomdata = rng.normal(50, 10, size=1000)
        print(f"{radomdata=}")
        hist: Hist = win.get("hist")
        hist.update(radomdata)

    print(f"{histdata=}")
    layout = [
        [
            Guis.Hist(
                data=histdata, title="ヒストグラフの基本", xlabel=xlabel, ylabel=ylabel
            ),
            Guis.Hist(data=histdata, title="表示される範囲を指定する", min=50, max=75),
        ],
        [
            Guis.Hist(data=histdata, title="表示する小数点を指定する", decimalpoint=1),
            Guis.Hist(
                data=histdata,
                title="表示される向きを指定する",
                orientation="horizontal",
            ),
        ],
        [
            Guis.Hist(data=histdata, title="binsを指定する", bins=5),
            Guis.Hist(data=histdata, title="binsを指定する", bins="doane"),
        ],
        [
            Guis.Hist(data=histdata, title="binsを指定する", bins=[30, 40, 50]),
            Guis.Hist(data=histdata, title="幅を指定する", width=0.4),
        ],
        [
            Guis.Hist(data=histdata, title="グラフを更新する", key="hist"),
            Guis.Buttons(text="更新ボタン", function=updates),
        ],
    ]
    win = Guis.window(
        title="ヒストグラフ(test)", layout=layout, scroll=True, maxmine=True
    )
    win.run()
