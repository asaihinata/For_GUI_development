from _import import *

if __name__ == "__main__":

    def updates():
        radomdata = randsint(50, 80, lenght=3, hierarchy=2)
        print(f"{radomdata=}")
        stack: Stack = win.get("stack")
        stack.update(y=radomdata)

    print(f"{stackx=}")
    print(f"{stacky=}")
    layout = [
        [
            Guis.Stack(
                x=stackx,
                y=stacky,
                title="積み上げグラフの基本",
                xlabel=xlabel,
                ylabel=ylabel,
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
