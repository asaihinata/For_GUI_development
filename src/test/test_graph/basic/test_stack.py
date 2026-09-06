import numpy as np

from sgg import Guis,Stack

rng = np.random.default_rng(seed=42)


def test_main():

    def updates():
        radomdata = rng.integers(low=50, high=80, size=(2, 3))
        print(f"{radomdata=}")
        stack: Stack = win.get("stack")
        stack.update(y=radomdata)

    stackx = np.arange(1, 4, 1)
    stacky = rng.integers(50, 80, size=(2, 3))
    print(f"{stackx=}")
    print(f"{stacky=}")
    layout = [
        [
            Guis.Stack(
                x=stackx,
                y=stacky,
                title="積み上げグラフの基本",
                xlabel="x軸のラベル",
                ylabel="y軸のラベル",
            ),
            Guis.Stack(
                x=stackx, y=stacky, title="塗りつぶす領域内の模様を指定する", hatch="-"
            ),
        ],
        [
            Guis.Stack(
                x=stackx,
                y=stacky,
                title="積み上げグラフの積み上げる基準を指定する",
                baseline="weighted_wiggle",
            )
        ],
        [
            Guis.Stack(x=stackx, y=stacky, title="グラフを更新する", key="stack"),
            Guis.Buttons(text="更新ボタン", function=updates),
        ],
    ]
    win = Guis.window(
        title="積み上げエリアチャート(test)", layout=layout, scroll=True, maxmine=True
    )
    win.run()


if __name__ == "__main__":
    test_main()
