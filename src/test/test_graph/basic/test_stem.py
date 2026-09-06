import numpy as np

from sgg import Guis,Stem

rng = np.random.default_rng(seed=42)


def test_main():

    def updates():
        radomdata = rng.integers(low=50, high=80, size=(2, 3))
        print(f"{radomdata=}")
        stemplot: Stem = win.get("stem")
        stemplot.update(x=radomdata)

    stemx1 = rng.integers(50, 80, size=3)
    stemx2 = rng.integers(50, 80, size=(2, 3))
    stemy = np.arange(1, 4, 1)
    print(f"{stemx1=}")
    print(f"{stemx2=}")
    print(f"{stemy=}")
    layout = [
        [
            Guis.Stem(
                x=stemx1,
                y=stemy,
                title="幹図の基本1",
                xlabel="x軸のラベル",
                ylabel="y軸のラベル",
            ),
            Guis.Stem(
                x=stemx2,
                y=stemy,
                title="幹図の基本2",
                xlabel="x軸のラベル",
                ylabel="y軸のラベル",
            ),
        ],
        [
            Guis.Stem(x=stemx1, y=stemy, title="マーカーを変更する", markerfmt="go"),
            Guis.Stem(
                x=stemx1,
                y=stemy,
                title="幹図の向きを指定する",
                orientation="horizontal",
            ),
        ],
        [
            Guis.Stem(x=stemx1, y=stemy, title="ベースラインを変更する", bottom=30),
            Guis.Stem(
                x=stemx1,
                y=stemy,
                title="ベースラインを変更する",
                bottom=30,
                orientation="horizontal",
            ),
        ],
        [
            Guis.Stem(x=stemx1, y=stemy, title="幹図の色を変更する", linefmt="g"),
            Guis.Stem(x=stemx1, y=stemy, title="幹図の線を変更する", basefmt="--"),
        ],
        [
            Guis.Stem(x=stemx2, y=stemy, title="グラフを更新する", key="stem"),
            Guis.Buttons(text="更新ボタン", function=updates),
        ],
    ]
    win = Guis.window(title="幹図(test)", layout=layout, scroll=True, maxmine=True)
    win.run()


if __name__ == "__main__":
    test_main()
