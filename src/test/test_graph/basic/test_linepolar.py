import numpy as np

from sgg import *

rng = np.random.default_rng(seed=42)


def test_main():

    def updates():
        radomdata = rng.random(3) * 30 + 50
        print(f"{radomdata=}")
        linepolar: Linepolar = win.get("linepolar")
        linepolar.update(y=radomdata)

    linepolarx = np.arange(1, 4, 1)
    linepolary = rng.integers(50, 80, size=3)
    linepolardata = np.arange(1, 4, 1)
    print(f"{linepolarx=}")
    print(f"{linepolary=}")
    print(f"{linepolardata=}")
    layout = [
        [
            Guis.Linepolar(x=linepolarx, y=linepolary, title="極軸折線グラフの基本1"),
            Guis.Linepolar(data=linepolardata, title="極軸折線グラフの基本2"),
        ],
        [
            Guis.Linepolar(
                x=linepolarx, y=linepolary, title="マーカーを変更する", marker="d"
            ),
            Guis.Linepolar(
                x=linepolarx,
                y=linepolary,
                title="マーカーの大きさを変更する",
                marker="d",
                markersize=20,
            ),
        ],
        [
            Guis.Linepolar(
                x=linepolarx, y=linepolary, title="線の色の変更", color="red"
            ),
            Guis.Linepolar(
                x=linepolarx, y=linepolary, title="線の種類を変更する", linestyle="--"
            ),
        ],
        [
            Guis.Linepolar(
                x=linepolarx, y=linepolary, title="グラフを更新する", key="linepolar"
            ),
            Guis.Buttons(text="更新ボタン", function=updates),
        ],
    ]
    win = Guis.window(
        title="極軸折線グラフ(test)", layout=layout, scroll=True, maxmine=True
    )
    win.run()


if __name__ == "__main__":
    test_main()
