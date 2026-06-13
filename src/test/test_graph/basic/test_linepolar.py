from _import import *

if __name__ == "__main__":

    def updates():
        radomdata = randrange(50, 80, size=3)
        print(f"{radomdata=}")
        linepolar: Linepolar = win.get("linepolar")
        linepolar.update(y=radomdata)

    print(f"{linepolarx=}")
    print(f"{linepolary=}")
    print(f"{linepolardata=}")
    layout = [
        [
            sgg.Linepolar(x=linepolarx, y=linepolary, title="極軸折線グラフの基本1"),
            sgg.Linepolar(data=linepolardata, title="極軸折線グラフの基本2"),
        ],
        [
            sgg.Linepolar(
                x=linepolarx, y=linepolary, title="マーカーを変更する", marker="d"
            ),
            sgg.Linepolar(
                x=linepolarx,
                y=linepolary,
                title="マーカーの大きさを変更する",
                marker="d",
                markersize=20,
            ),
        ],
        [
            sgg.Linepolar(
                x=linepolarx, y=linepolary, title="線の色の変更", color="red"
            ),
            sgg.Linepolar(
                x=linepolarx, y=linepolary, title="線の種類を変更する", linestyle="--"
            ),
        ],
        [
            sgg.Linepolar(
                x=linepolarx, y=linepolary, title="グラフを更新する", key="linepolar"
            ),
            sgg.Buttons(text="更新ボタン", function=updates),
        ],
    ]
    win = sgg.window(
        title="極軸折線グラフ(test)", layout=layout, scroll=True, maxmine=True
    )
    win.run()
