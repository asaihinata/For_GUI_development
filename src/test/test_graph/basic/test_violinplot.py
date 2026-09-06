import numpy as np

from sgg import Guis, Violinplot

rng = np.random.default_rng(seed=42)


def test_main():

    def updates():
        radomdata = rng.normal((3, 5, 4), (0.75, 1.00, 0.75), (200, 3))
        print(f"{radomdata=}")
        violin: Violinplot = win.get("violin")
        violin.update(radomdata)

    violindata = rng.normal((3, 5, 4), (0.75, 1.00, 0.75), (200, 3))
    print(f"{violindata=}")
    layout = [
        [
            Guis.Violinplot(
                data=violindata,
                title="バイオリングラフの基本",
                xlabel="x軸のラベル",
                ylabel="y軸のラベル",
            ),
            Guis.Violinplot(data=violindata, title="幅を変更する", width=0.6),
        ],
        [
            Guis.Violinplot(
                data=violindata, title="向きを変える", orientation="horizontal"
            ),
            Guis.Violinplot(
                data=violindata, title="曲線の滑らかさを変える", points=1000
            ),
        ],
        [
            Guis.Violinplot(
                data=violindata,
                title="向きを変える",
                orientation="vertical",
                x=[2, 3, 4],
            ),
            Guis.Violinplot(
                data=violindata,
                title="向きを変える",
                orientation="horizontal",
                y=[2, 3, 4],
            ),
        ],
        [
            Guis.Violinplot(
                data=violindata, title="極値を線で示す", showextrema=True, alpha=0.5
            ),
            Guis.Violinplot(
                data=violindata, title="平均線を表示する", showmeans=True, alpha=0.5
            ),
        ],
        [
            Guis.Violinplot(
                data=violindata, title="中央線を表示する", showmedians=True, alpha=0.5
            ),
            Guis.Violinplot(
                data=violindata, title="バイオリンの向きを指定する", side="scale"
            ),
        ],
        [
            Guis.Violinplot(
                data=violindata, title="推定器の帯域幅を指定する", bw_method="silverman"
            )
        ],
        [
            Guis.Violinplot(data=violindata, title="グラフを更新する", key="violin"),
            Guis.Buttons(text="更新ボタン", function=updates),
        ],
    ]
    win = Guis.window(
        title="バイオリングラフ(test)", layout=layout, scroll=True, maxmine=True
    )
    win.run()


if __name__ == "__main__":
    test_main()
