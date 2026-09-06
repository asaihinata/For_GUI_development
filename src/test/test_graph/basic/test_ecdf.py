import numpy as np

from sgg import Ecdf, Guis

rng = np.random.default_rng(seed=42)


def test_main():

    def updates():
        radomdata = 4 + rng.normal(0, 1.5, size=100)
        print(f"{radomdata=}")
        ecdf: Ecdf = win.get("ecdf")
        ecdf.update(radomdata)

    ecdfdata = 4 + rng.normal(0, 1.5, size=100)
    print(f"{ecdfdata=}")
    layout = [
        [
            Guis.Ecdf(
                data=ecdfdata,
                title="経験的累積分布関数の基本",
                xlabel="x軸のラベル",
                ylabel="y軸のラベル",
            ),
            Guis.Ecdf(
                data=ecdfdata, title="同一値のデータをまとめて最適化する", compress=True
            ),
        ],
        [
            Guis.Ecdf(
                data=ecdfdata,
                title="経験的累積分布関数の向きを変える",
                orientation="horizontal",
            ),
            Guis.Ecdf(data=ecdfdata, title="補累積分布を描画する", complementary=True),
        ],
        [
            Guis.Ecdf(data=ecdfdata, title="線の幅を変える", linewidth=3),
            Guis.Ecdf(data=ecdfdata, title="線の種類を変える", linestyle="dotted"),
        ],
        [
            Guis.Ecdf(data=ecdfdata, title="グラフを更新する", key="ecdf"),
            Guis.Buttons(text="更新ボタン", function=updates),
        ],
    ]
    win = Guis.window(
        title="経験的累積分布関数(test)", layout=layout, scroll=True, maxmine=True
    )
    win.run()


if __name__ == "__main__":
    test_main()
