from _import import *

if __name__ == "__main__":

    def updates():
        radomdata = randsint(50, 80, lenght=3, hierarchy=2)
        print(f"{radomdata=}")
        stemplot: Stem = win.get("stem")
        stemplot.update(x=radomdata)

    print(f"{stemx1=}")
    print(f"{stemx2=}")
    print(f"{stemy=}")
    layout = [
        [
            Guis.Stem(
                x=stemx1, y=stemy, title="幹図の基本1", xlabel=xlabel, ylabel=ylabel
            ),
            Guis.Stem(
                x=stemx2, y=stemy, title="幹図の基本2", xlabel=xlabel, ylabel=ylabel
            ),
        ],
        [
            Guis.Stem(x=stemx1, y=stemy, title="マーカーを変更する", markerfmt="go"),
            Guis.Stem(
                x=stemx1,
                y=stemy,
                title="幹図の向きを指定する",
                orientation="horizontal",
            ),
        ],
        [
            Guis.Stem(x=stemx1, y=stemy, title="ベースラインを変更する", bottom=30),
            Guis.Stem(
                x=stemx1,
                y=stemy,
                title="ベースラインを変更する",
                bottom=30,
                orientation="horizontal",
            ),
        ],
        [
            Guis.Stem(x=stemx1, y=stemy, title="幹図の色を変更する", linefmt="g"),
            Guis.Stem(x=stemx1, y=stemy, title="幹図の線を変更する", basefmt="--"),
        ],
        [
            Guis.Stem(x=stemx2, y=stemy, title="グラフを更新する", key="stem"),
            Guis.Buttons(text="更新ボタン", function=updates),
        ],
    ]
    win = Guis.window(title="幹図(test)", layout=layout, scroll=True, maxmine=True)
    win.run()
