import numpy as np

from sgg import *

rng = np.random.default_rng(seed=42)


def test_main():

    def updates():
        radomdata1 = rng.standard_normal((1, 5000))
        radomdata2 = 1.2 * radomdata1 + rng.standard_normal((1, 5000)) / 3
        print(f"{radomdata1=}")
        print(f"{radomdata2=}")
        print(radomdata1)
        print(radomdata2)
        hexbin: Hexbin = win.get("hexbin")
        hexbin.update(x=radomdata1, y=radomdata2)

    hexbinx1 = rng.standard_normal((1, 5000))
    hexbiny1 = 1.2 * hexbinx1 + rng.standard_normal((1, 5000)) / 3
    hexbinx2 = 2 + rng.random((1, 5000))
    hexbiny2 = 2 + 1.2 * hexbinx2 + rng.standard_normal((1, 5000)) / 3
    print(f"{hexbinx1=}")
    print(f"{hexbiny1=}")
    print(f"{hexbinx2=}")
    print(f"{hexbiny2=}")
    layout = [
        [
            Guis.Hexbin(
                x=hexbinx1,
                y=hexbiny1,
                title="2次元六角形ビニンググラフの基本",
                xlabel="x軸のラベル",
                ylabel="y軸のラベル",
            ),
            Guis.Hexbin(
                x=hexbinx1, y=hexbiny1, title="binsの細かさを指定する", gridsize=300
            ),
        ],
        [
            Guis.Hexbin(
                x=hexbinx1,
                y=hexbiny1,
                title="表示させる範囲を指定する",
                extent=[-1.0, 1.0, -1.0, 1.0],
            ),
            Guis.Hexbin(
                x=hexbinx1, y=hexbiny1, title="描画するbinsの最小を指定する", mincnt=3
            ),
        ],
        [
            Guis.Hexbin(x=hexbinx2, y=hexbiny2, title="x軸を対数にする", xscale="log"),
            Guis.Hexbin(x=hexbinx2, y=hexbiny2, title="y軸を対数にする", yscale="log"),
        ],
        [Guis.Hexbin(x=hexbinx1, y=hexbiny1, title="binsを指定する", bins="log")],
        [
            Guis.Hexbin(x=hexbinx1, y=hexbiny1, title="グラフを更新する", key="hexbin"),
            Guis.Buttons(text="更新ボタン", function=updates),
        ],
    ]
    win = Guis.window(
        title="2次元六角形ビニンググラフ(test)",
        layout=layout,
        scroll=True,
        maxmine=True,
    )
    win.run()


if __name__ == "__main__":
    test_main()
