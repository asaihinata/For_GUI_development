from _import import *

if __name__ == "__main__":

    def updates():
        radomdata = rng.integers(0, 10, 5)
        print(f"{radomdata=}")
        scatterpolor: Scatterpolar = win.get("scatterpolor")
        scatterpolor.update(y=radomdata)

    print(f"{scatterpolarx=}")
    print(f"{scatterpolary=}")
    print(f"{scatterpolardata=}")
    layout = [
        [
            Guis.Scatterpolar(
                x=scatterpolarx, y=scatterpolary, title="極軸散布図の基本1"
            ),
            Guis.Scatterpolar(data=scatterpolardata, title="極軸散布図の基本2"),
        ],
        [
            Guis.Scatterpolar(
                x=scatterpolarx, y=scatterpolary, title="マーカーの指定", marker="d"
            ),
            Guis.Scatterpolar(
                x=scatterpolarx,
                y=scatterpolary,
                title="マーカーサイズの変更",
                marker="d",
                markersize=20,
            ),
        ],
        [
            Guis.Scatterpolar(
                x=scatterpolarx,
                y=scatterpolary,
                title="グラフを更新する",
                key="scatterpolor",
            ),
            Guis.Buttons(text="更新ボタン", function=updates),
        ],
    ]
    win = Guis.window(
        title="極軸散布図(test)", layout=layout, scroll=True, maxmine=True
    )
    win.run()
