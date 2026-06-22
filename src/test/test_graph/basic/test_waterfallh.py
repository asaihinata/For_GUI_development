from _import import *

if __name__ == "__main__":

    def updates():
        radomdata = rng.integers(-100, 100, 6)
        print(f"{radomdata=}")
        waterfallh: Waterfallh = win.get("waterfallh")
        waterfallh.update(y=radomdata)

    print(f"{waterfallx=}")
    print(f"{waterfally=}")
    layout = [
        [
            Guis.Waterfallh(
                x=waterfallx,
                y=waterfally,
                title="横向き滝グラフの基本",
                xlabel=xlabel,
                ylabel=ylabel,
            ),
            Guis.Waterfallh(
                x=waterfallx, y=waterfally, title="バーの幅を変更する", width=0.5
            ),
        ],
        [
            Guis.Waterfallh(
                x=waterfallx,
                y=waterfally,
                title="バーとバーを繋ぐ線の種類を変更する",
                width=0.5,
                linestyle="dotted",
            ),
            Guis.Waterfallh(
                x=waterfallx,
                y=waterfally,
                title="バーとバーを繋ぐ線の色を変更する",
                width=0.5,
                colorline="green",
            ),
        ],
        [
            Guis.Waterfallh(
                x=waterfallx,
                y=waterfally,
                title="上昇バーの色を変更する",
                ucolor="pink",
            ),
            Guis.Waterfallh(
                x=waterfallx,
                y=waterfally,
                title="減少バーの色を変更する",
                dcolor="aqua",
            ),
        ],
        [
            Guis.Waterfallh(
                x=waterfallx, y=waterfally, title="合計を表示させる", sums=True
            ),
            Guis.Waterfallh(
                x=waterfallx,
                y=waterfally,
                title="合計を表示させる",
                sums=True,
                sumstext="合計",
            ),
        ],
        [
            Guis.Waterfallh(
                x=waterfallx, y=waterfally, title="グラフを更新する", key="waterfallh"
            ),
            Guis.Buttons(text="更新ボタン", function=updates),
        ],
    ]
    win = Guis.window(
        title="横向き滝グラフ(test)",
        layout=layout,
        scroll=True,
        maxmine=True,
    )
    win.run()
