from _import import *

if __name__ == "__main__":

    def updates():
        radomdata = rng.integers(30, 60, size=5)
        print(f"{radomdata=}")
        barpolar: Barpolar = win.get("Barpolar")
        barpolar.update(y=radomdata)

    print(f"{barpolarx=}")
    print(f"{barpolary=}")
    print(f"{barpolardata=}")
    layout = [
        [
            sgg.Barpolar(x=barpolarx, y=barpolary, title="極軸棒グラフの基本1"),
            sgg.Barpolar(data=barpolardata, title="極軸棒グラフの基本2"),
        ],
        [
            sgg.Barpolar(
                x=barpolarx,
                y=barpolary,
                align="edge",
                title="極軸棒グラフの配置を変更する",
            ),
            sgg.Barpolar(
                x=barpolarx,
                y=barpolary,
                width=0.4,
                title="極軸棒グラフのバーの幅を変更する",
            ),
        ],
        [
            sgg.Barpolar(
                x=barpolarx, y=barpolary, title="グラフを更新する", key="Barpolar"
            ),
            sgg.Buttons(text="更新ボタン", function=updates),
        ],
    ]
    win = sgg.window(
        title="極軸棒グラフ(test)", layout=layout, scroll=True, maxmine=True
    )
    win.run()
