import numpy as np

from sgg import *

rng = np.random.default_rng(seed=42)


def test_main():

    def updates():
        radomdata = rng.random((4, 3)) * 30 + 50
        print(f"{radomdata=}")
        lineplot: LineGraph = win.get("lineplot")
        lineplot.update(y=radomdata)

    linex = np.arange(1, 4, 1)
    liney1 = rng.integers(50, 80, size=3)
    liney2 = rng.integers(50, 80, size=(4, 3))
    print(f"{linex=}")
    print(f"{liney1=}")
    print(f"{liney2=}")
    layout = [
        [
            Guis.LineGraph(
                x=linex,
                y=liney1,
                title="折り線グラフの基本",
                xlabel="x軸のラベル",
                ylabel="y軸のラベル",
            ),
            Guis.LineGraph(x=linex, y=liney2, title="複数の折り線グラフを表示させる"),
        ],
        [
            Guis.LineGraph(
                x=linex,
                y=liney2,
                title="凡例の表示",
                label=["label1", "label2", "label3", "label4"],
            ),
            Guis.LineGraph(
                x=linex,
                y=liney2,
                title="線の色の変更",
                color=["red", "green", "#eeeeee", "rgb(0,0,0)"],
            ),
        ],
        [
            Guis.LineGraph(x=linex, y=liney1, title="マーカーを変更する", marker="d"),
            Guis.LineGraph(
                x=linex,
                y=liney1,
                title="マーカーの大きさを変更する",
                marker="d",
                markersize=20,
            ),
        ],
        [Guis.LineGraph(x=linex, y=liney1, title="線の種類を変更する", linestyle="--")],
        [
            Guis.LineGraph(x=linex, y=liney2, title="グラフを更新する", key="lineplot"),
            Guis.Buttons(text="更新ボタン", function=updates),
        ],
    ]
    win = Guis.window(
        title="折り線グラフ(test)", layout=layout, scroll=True, maxmine=True
    )
    win.run()


if __name__ == "__main__":
    test_main()
