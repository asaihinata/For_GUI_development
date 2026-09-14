import numpy as np

from sgg import Linepolar, guis

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
            guis.Linepolar(x=linepolarx, y=linepolary, title="極軸折線グラフの基本1"),
            guis.Linepolar(data=linepolardata, title="極軸折線グラフの基本2"),
        ],
        [
            guis.Linepolar(
                x=linepolarx, y=linepolary, title="マーカーを変更する", marker="d"
            ),
            guis.Linepolar(
                x=linepolarx,
                y=linepolary,
                title="マーカーの大きさを変更する",
                marker="d",
                markersize=20,
            ),
        ],
        [
            guis.Linepolar(
                x=linepolarx, y=linepolary, title="線の色の変更", color="red"
            ),
            guis.Linepolar(
                x=linepolarx, y=linepolary, title="線の種類を変更する", linestyle="--"
            ),
        ],
        [
            guis.Linepolar(
                x=linepolarx, y=linepolary, title="グラフを更新する", key="linepolar"
            ),
            guis.Buttons(text="更新ボタン", function=updates),
        ],
    ]
    win = guis.window(
        title="極軸折線グラフ(test)", layout=layout, scroll=True, maxmine=True
    )
    win.run()


if __name__ == "__main__":
    test_main()
