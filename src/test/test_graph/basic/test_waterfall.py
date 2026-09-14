import numpy as np

from sgg import Waterfall, guis

rng = np.random.default_rng(seed=42)


def test_main():

    def updates():
        radomdata = rng.integers(-100, 100, 6)
        print(f"{radomdata=}")
        waterfall: Waterfall = win.get("waterfall")
        waterfall.update(y=radomdata)

    waterfallx = ["1月", "2月", "3月", "4月", "5月", "6月"]
    waterfally = [30, -10, 10, 5, 10, -80]
    print(f"{waterfallx=}")
    print(f"{waterfally=}")
    layout = [
        [
            guis.Waterfall(
                x=waterfallx,
                y=waterfally,
                title="滝グラフの基本",
                xlabel="x軸のラベル",
                ylabel="y軸のラベル",
            ),
            guis.Waterfall(
                x=waterfallx, y=waterfally, title="バーの幅を変更する", width=0.5
            ),
        ],
        [
            guis.Waterfall(
                x=waterfallx,
                y=waterfally,
                title="バーとバーを繋ぐ線の種類を変更する",
                width=0.5,
                linestyle="dotted",
            ),
            guis.Waterfall(
                x=waterfallx,
                y=waterfally,
                title="バーとバーを繋ぐ線の色を変更する",
                width=0.5,
                colorline="red",
            ),
        ],
        [
            guis.Waterfall(
                x=waterfallx,
                y=waterfally,
                title="上昇バーの色を変更する",
                ucolor="pink",
            ),
            guis.Waterfall(
                x=waterfallx,
                y=waterfally,
                title="減少バーの色を変更する",
                dcolor="aqua",
            ),
        ],
        [
            guis.Waterfall(
                x=waterfallx, y=waterfally, title="合計を表示させる", sums=True
            ),
            guis.Waterfall(
                x=waterfallx,
                y=waterfally,
                title="合計を表示させる",
                sums=True,
                sumstext="合計",
            ),
        ],
        [
            guis.Waterfall(
                x=waterfallx, y=waterfally, title="グラフを更新する", key="waterfall"
            ),
            guis.Buttons(text="更新ボタン", function=updates),
        ],
    ]
    win = guis.window(title="滝グラフ(test)", layout=layout, scroll=True, maxmine=True)
    win.run()


if __name__ == "__main__":
    test_main()
