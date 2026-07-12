import numpy as np

from sgg import *

rng = np.random.default_rng(seed=42)


def test_main():

    def updates():
        radomdata = rng.integers(0, 10, 5)
        print(f"{radomdata=}")
        scatter: Scatter = win.get("scatter")
        scatter.update(y=radomdata)

    scatterx1 = ["1月", "2月", "3月", "4月", "5月"]
    scattery1 = rng.integers(0, 10, size=5)
    scatterx2 = np.arange(1, 4, 1)
    scattery2 = rng.integers(100, 400, size=(2, 3))
    print(f"{scatterx1=}")
    print(f"{scattery1=}")
    print(f"{scatterx2=}")
    print(f"{scattery2=}")
    layout = [
        [
            Guis.Scatter(
                x=scatterx1,
                y=scattery1,
                title="散布図の基本1",
                xlabel="x軸のラベル",
                ylabel="y軸のラベル",
            ),
            Guis.Scatter(
                x=scatterx2,
                y=scattery2,
                title="散布図の基本2",
                xlabel="x軸のラベル",
                ylabel="y軸のラベル",
            ),
        ],
        [
            Guis.Scatter(x=scatterx1, y=scattery1, title="マーカーの指定", marker="d"),
            Guis.Scatter(
                x=scatterx1,
                y=scattery1,
                title="マーカーサイズの変更",
                marker="d",
                markersize=20,
            ),
        ],
        [
            Guis.Scatter(
                x=scatterx1, y=scattery1, title="回帰直線1", regression_bool=True
            ),
            Guis.Scatter(
                x=scatterx2, y=scattery2, title="回帰直線2", regression_bool=True
            ),
        ],
        [
            Guis.Scatter(
                x=scatterx1, y=scattery1, title="グラフを更新する", key="scatter"
            ),
            Guis.Buttons(text="更新ボタン", function=updates),
        ],
    ]
    win = Guis.window(title="散布図(test)", layout=layout, scroll=True, maxmine=True)
    win.run()


if __name__ == "__main__":
    test_main()
