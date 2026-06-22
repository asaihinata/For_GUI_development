from _import import *

if __name__ == "__main__":

    def updates():
        radomdata = rng.integers(1, 10, (3, 3)) + 2
        print(f"{radomdata=}")
        stack: Stacked = win.get("stacked")
        stack.update(radomdata)

    print(f"{stackeddata=}")
    print(f"{stackeddataname=}")
    layout = [
        [
            Guis.Stacked(
                data=stackeddata,
                dataname=stackeddataname,
                title="積み上げ棒グラフの基本",
                xlabel=xlabel,
                ylabel=ylabel,
            ),
            Guis.Stacked(
                data=stackeddata,
                dataname=stackeddataname,
                title="幅を変更する",
                width=0.5,
            ),
        ],
        [
            Guis.Stacked(
                data=stackeddata,
                dataname=stackeddataname,
                title="グラフを更新する",
                key="stacked",
            ),
            Guis.Buttons(text="更新ボタン", function=updates),
        ],
    ]
    win = Guis.window(
        title="積み上げ棒グラフ(test)", layout=layout, scroll=True, maxmine=True
    )
    win.run()
