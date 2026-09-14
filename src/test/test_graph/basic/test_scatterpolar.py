import numpy as np

from sgg import Scatterpolar, guis

rng = np.random.default_rng(seed=42)


def test_main():

    def updates():
        radomdata = rng.integers(0, 10, 5)
        print(f"{radomdata=}")
        scatterpolor: Scatterpolar = win.get("scatterpolor")
        scatterpolor.update(y=radomdata)

    scatterpolarx = rng.integers(0, 10, size=5)
    scatterpolary = rng.integers(0, 10, size=5)
    scatterpolardata = rng.integers(0, 10, size=5)
    print(f"{scatterpolarx=}")
    print(f"{scatterpolary=}")
    print(f"{scatterpolardata=}")
    layout = [
        [
            guis.Scatterpolar(
                x=scatterpolarx, y=scatterpolary, title="極軸散布図の基本1"
            ),
            guis.Scatterpolar(data=scatterpolardata, title="極軸散布図の基本2"),
        ],
        [
            guis.Scatterpolar(
                x=scatterpolarx, y=scatterpolary, title="マーカーの指定", marker="d"
            ),
            guis.Scatterpolar(
                x=scatterpolarx,
                y=scatterpolary,
                title="マーカーサイズの変更",
                marker="d",
                markersize=20,
            ),
        ],
        [
            guis.Scatterpolar(
                x=scatterpolarx,
                y=scatterpolary,
                title="グラフを更新する",
                key="scatterpolor",
            ),
            guis.Buttons(text="更新ボタン", function=updates),
        ],
    ]
    win = guis.window(
        title="極軸散布図(test)", layout=layout, scroll=True, maxmine=True
    )
    win.run()


if __name__ == "__main__":
    test_main()
