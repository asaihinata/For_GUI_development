from _import import *

if __name__ == "__main__":

    def updates():
        radomdata = rng.integers(20, 30, size=5, endpoint=True)
        print(f"{radomdata=}")
        hat: Hatplot = win.get("hat")
        hat.update(x=radomdata, data=radomdata + 2)

    print(f"{hatplotx=}")
    print(f"{hatplotdata=}")
    layout = [
        [
            Guis.Hatplot(
                x=hatplotx,
                data=hatplotdata,
                title="ハットグラフの基本",
                xlabel=xlabel,
                ylabel=ylabel,
                yticksrange=5,
            ),
            Guis.Hatplot(
                x=hatplotx,
                data=hatplotdata,
                title="ハットの色を変える",
                color="red",
                yticksrange=5,
            ),
        ],
        [
            Guis.Hatplot(
                x=hatplotx, data=hatplotdata, title="ハットグラフの基本", yticksrange=5
            ),
        ],
        [
            Guis.Hatplot(
                x=hatplotx,
                data=hatplotdata,
                title="グラフを更新する",
                yticksrange=5,
                key="hat",
            ),
            Guis.Buttons(text="更新ボタン", function=updates),
        ],
    ]
    win = Guis.window(
        title="ハットグラフ(test)", layout=layout, scroll=True, maxmine=True
    )
    win.run()
