import numpy as np

from sgg import Waterfallh, guis

rng = np.random.default_rng(seed=42)


def test_main():

    def updates():
        radomdata = rng.integers(-100, 100, 6)
        print(f"{radomdata=}")
        waterfallh: Waterfallh = win.get("waterfallh")
        waterfallh.update(y=radomdata)

    waterfallx = ["1月", "2月", "3月", "4月", "5月", "6月"]
    waterfally = [30, -10, 10, 5, 10, -80]
    print(f"{waterfallx=}")
    print(f"{waterfally=}")
    layout = [
        [
            guis.Waterfallh(
                x=waterfallx,
                y=waterfally,
                title="横向き滝グラフの基本",
                xlabel="x軸のラベル",
                ylabel="y軸のラベル",
            ),
            guis.Waterfallh(
                x=waterfallx, y=waterfally, title="バーの幅を変更する", height=0.5
            ),
        ],
        [
            guis.Waterfallh(
                x=waterfallx,
                y=waterfally,
                title="バーとバーを繋ぐ線の種類を変更する",
                height=0.5,
                linestyle="dotted",
            ),
            guis.Waterfallh(
                x=waterfallx,
                y=waterfally,
                title="バーとバーを繋ぐ線の色を変更する",
                height=0.5,
                colorline="red",
            ),
        ],
        [
            guis.Waterfallh(
                x=waterfallx,
                y=waterfally,
                title="上昇バーの色を変更する",
                ucolor="pink",
            ),
            guis.Waterfallh(
                x=waterfallx,
                y=waterfally,
                title="減少バーの色を変更する",
                dcolor="aqua",
            ),
        ],
        [
            guis.Waterfallh(
                x=waterfallx, y=waterfally, title="合計を表示させる", sums=True
            ),
            guis.Waterfallh(
                x=waterfallx,
                y=waterfally,
                title="合計を表示させる",
                sums=True,
                sumstext="合計",
            ),
        ],
        [
            guis.Waterfallh(
                x=waterfallx, y=waterfally, title="グラフを更新する", key="waterfallh"
            ),
            guis.Buttons(text="更新ボタン", function=updates),
        ],
    ]
    win = guis.window(
        title="横向き滝グラフ(test)",
        layout=layout,
        scroll=True,
        maxmine=True,
    )
    win.run()


if __name__ == "__main__":
    test_main()
