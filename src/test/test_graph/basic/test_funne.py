from _import import *

if __name__ == "__main__":

    def updates():
        radomdata = rng.integers(10, 50, size=3)
        print(f"{radomdata=}")
        funne: Funne = win.get("funne")
        funne.update(radomdata)

    print(f"{funnedata=}")
    layout = [
        [
            Guis.Funne(
                data=funnedata,
                title="じょうごグラフの基本",
                xlabel=xlabel,
                ylabel=ylabel,
            ),
            Guis.Funne(data=funnedata, title="高さを変更する", height=0.5),
        ],
        [
            Guis.Funne(data=funnedata, title="グラフを更新する", key="funne"),
            Guis.Buttons(text="更新ボタン", function=updates),
        ],
    ]
    win = Guis.window(
        title="じょうごグラフ(test)", layout=layout, scroll=True, maxmine=True
    )
    win.run()
