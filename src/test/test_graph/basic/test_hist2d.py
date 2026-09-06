import numpy as np

from sgg import Guis,Hist2d

rng = np.random.default_rng(seed=42)


def test_main():

    def updates():
        radomdata1 = rng.standard_normal(5000)
        radomdata2 = 1.4 * radomdata1 + rng.standard_normal(5000) / 3
        print(f"{radomdata1=}")
        print(f"{radomdata2=}")
        hist2d: Hist2d = win.get("hist2d")
        hist2d.update(x=radomdata1, y=radomdata2)

    hist2dx = rng.standard_normal(5000)
    hist2dy = 1.2 * hist2dx + rng.standard_normal(5000) / 3
    print(f"{hist2dx}")
    print(f"{hist2dy}")
    layout = [
        [
            Guis.Hist2d(
                x=hist2dx,
                y=hist2dy,
                title="2次元ヒストグラムの基本",
                xlabel="x軸のラベル",
                ylabel="y軸のラベル",
            ),
            Guis.Hist2d(
                x=hist2dx,
                y=hist2dy,
                title="2次元ヒストグラムを正規化する",
                density=True,
            ),
        ],
        [
            Guis.Hist2d(
                x=hist2dx,
                y=hist2dy,
                title="x軸に表示させる範囲を指定する",
                xmax=5,
                xmin=-5,
            ),
            Guis.Hist2d(
                x=hist2dx,
                y=hist2dy,
                title="y軸に表示させる範囲を指定する",
                ymax=5,
                ymin=-5,
            ),
        ],
        [Guis.Hist2d(x=hist2dx, y=hist2dy, title="binsを指定する", bins=5)],
        [
            Guis.Hist2d(x=hist2dx, y=hist2dy, title="グラフを更新する", key="hist2d"),
            Guis.Buttons(text="更新ボタン", function=updates),
        ],
    ]
    win = Guis.window(
        title="2次元ヒストグラム(test)", layout=layout, scroll=True, maxmine=True
    )
    win.run()


if __name__ == "__main__":
    test_main()
