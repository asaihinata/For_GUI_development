import numpy as np

from sgg import Hist, guis

rng = np.random.default_rng(seed=42)


def test_main():

    def updates():
        radomdata = rng.normal(50, 10, size=1000)
        print(f"{radomdata=}")
        hist: Hist = win.get("hist")
        hist.update(radomdata)

    histdata = rng.normal(10, 50, size=1000)
    print(f"{histdata=}")
    layout = [
        [
            guis.Hist(
                data=histdata,
                title="ヒストグラフの基本",
                xlabel="x軸のラベル",
                ylabel="y軸のラベル",
            ),
            guis.Hist(data=histdata, title="表示される範囲を指定する", min=50, max=75),
        ],
        [
            guis.Hist(data=histdata, title="表示する小数点を指定する", decimalpoint=1),
            guis.Hist(
                data=histdata,
                title="表示される向きを指定する",
                orientation="horizontal",
            ),
        ],
        [
            guis.Hist(data=histdata, title="binsを指定する", bins=5),
            guis.Hist(data=histdata, title="binsを指定する", bins="doane"),
        ],
        [
            guis.Hist(data=histdata, title="binsを指定する", bins=[30, 40, 50]),
            guis.Hist(data=histdata, title="幅を指定する", width=0.4),
        ],
        [
            guis.Hist(data=histdata, title="グラフを更新する", key="hist"),
            guis.Buttons(text="更新ボタン", function=updates),
        ],
    ]
    win = guis.window(
        title="ヒストグラフ(test)", layout=layout, scroll=True, maxmine=True
    )
    win.run()


if __name__ == "__main__":
    test_main()
