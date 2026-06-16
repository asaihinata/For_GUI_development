from _import import *

if __name__ == "__main__":

    def updates():
        radomdata = randsint(50, 80, lenght=3)
        print(f"{radomdata=}")
        stemplot: Stempolar = win.get("stempolar")
        stemplot.update(x=radomdata)

    print(f"{stempolarx=}")
    print(f"{stempolary=}")
    print(f"{stempolardata=}")
    layout = [
        [
            Guis.Stempolar(x=stempolarx, y=stempolary, title="極軸幹図の基本1"),
            Guis.Stempolar(data=stempolardata, title="極軸幹図の基本2"),
        ],
        [
            Guis.Stempolar(
                x=stempolarx, y=stempolary, title="マーカーを変更する", fmarker="^"
            ),
            Guis.Stempolar(
                x=stempolarx, y=stempolary, title="ベースラインを変更する", bottom=30
            ),
        ],
        [
            Guis.Stempolar(
                x=stempolarx, y=stempolary, title="極軸幹図の色を変更する", fcolor="b"
            ),
            Guis.Stempolar(
                x=stempolarx, y=stempolary, title="極軸幹図の線を変更する", fline="--"
            ),
        ],
        [
            Guis.Stempolar(
                x=stempolarx, y=stempolary, title="グラフを更新する", key="stempolar"
            ),
            Guis.Buttons(text="更新ボタン", function=updates),
        ],
    ]
    win = Guis.window(title="極軸幹図(test)", layout=layout, scroll=True, maxmine=True)
    win.run()
