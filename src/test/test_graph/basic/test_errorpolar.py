from _import import *

if __name__ == "__main__":

    def updates():
        radomdata = rng.integers(0, 3, 5)
        print(f"{radomdata=}")
        errorpolar: Errorpolar = win.get("errorpolar")
        errorpolar.update(y=radomdata)

    print(f"{errorpolarx=}")
    print(f"{errorpolary=}")
    print(f"{polarerr=}")
    print(f"{polarxerr=}")
    print(f"{polaryerr=}")
    layout = [
        [
            Guis.Errorpolar(
                x=errorpolarx,
                y=errorpolary,
                err=polarerr,
                title="極軸エラーグラフの基本1",
            ),
            Guis.Errorpolar(
                x=errorpolarx,
                y=errorpolary,
                polarxerr=polarxerr,
                polaryerr=polaryerr,
                title="極軸エラーグラフの基本2",
            ),
        ],
        [
            Guis.Errorpolar(
                x=errorpolarx,
                y=errorpolary,
                err=polarerr,
                title="xの上向きの誤差に矢印を付ける",
                xuplims=True,
            ),
            Guis.Errorpolar(
                x=errorpolarx,
                y=errorpolary,
                err=polarerr,
                title="xの下向きの誤差に矢印を付ける",
                xlolims=True,
            ),
        ],
        [
            Guis.Errorpolar(
                x=errorpolarx,
                y=errorpolary,
                err=polarerr,
                title="yの上向きの誤差に矢印を付ける",
                yuplims=True,
            ),
            Guis.Errorpolar(
                x=errorpolarx,
                y=errorpolary,
                err=polarerr,
                title="yの下向きの誤差に矢印を付ける",
                ylolims=True,
            ),
        ],
        [
            Guis.Errorpolar(
                x=errorpolarx,
                y=errorpolary,
                err=polarerr,
                title="データ点とデータ点を結ぶ線を指定する",
                linestyle="dashdot",
            ),
            Guis.Errorpolar(
                x=errorpolarx,
                y=errorpolary,
                err=polarerr,
                title="データの点の種類を変更する",
                marker="s",
            ),
        ],
        [
            Guis.Errorpolar(
                x=errorpolarx,
                y=errorpolary,
                err=polarerr,
                title="キャップの長さを指定する",
                capsize=3,
            ),
            Guis.Errorpolar(
                x=errorpolarx,
                y=errorpolary,
                err=polarerr,
                title="キャップの幅を指定する",
                capthick=20,
                capsize=3,
            ),
        ],
        [
            Guis.Errorpolar(
                x=errorpolarx,
                y=errorpolary,
                err=polarerr,
                title="極軸エラーグラフを表示する頻度を変える",
                errorevery=3,
            ),
            Guis.Errorpolar(
                x=errorpolarx,
                y=errorpolary,
                err=polarerr,
                title="極軸エラーグラフを表示する頻度を指定する。",
                errorevery=[2, 4],
            ),
        ],
        [
            Guis.Errorpolar(
                x=errorpolarx,
                y=errorpolary,
                err=polarerr,
                title="極軸エラーグラフの線の幅を変更する",
                linewidth=2,
            )
        ],
        [
            Guis.Errorpolar(
                x=errorpolarx,
                y=errorpolary,
                err=polarerr,
                title="グラフを更新する",
                key="errorpolar",
            ),
            Guis.Buttons(text="更新ボタン", function=updates),
        ],
    ]
    win = Guis.window(
        title="極軸エラーグラフ(test)", layout=layout, scroll=True, maxmine=True
    )
    win.run()
