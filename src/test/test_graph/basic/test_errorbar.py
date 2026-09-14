import numpy as np

from sgg import Errorbar, guis

rng = np.random.default_rng(seed=42)


def test_main():

    def updates():
        radomdata = rng.integers(0, 3, 5)
        print(f"{radomdata=}")
        error: Errorbar = win.get("errorbar")
        error.update(y=radomdata)

    errorbarx = np.arange(2, 12, 2)
    errorbary = rng.integers(0, 3, 5)
    err = rng.integers(3, size=5)
    xerr = rng.integers(3, size=5)
    yerr = rng.integers(3, size=5)
    print(f"{errorbarx=}")
    print(f"{errorbary=}")
    print(f"{err=}")
    print(f"{xerr=}")
    print(f"{yerr=}")
    layout = [
        [
            guis.Errorbar(
                x=errorbarx,
                y=errorbary,
                err=err,
                title="エラーグラフの基本1",
                xlabel="x軸のラベル",
                ylabel="y軸のラベル",
            ),
            guis.Errorbar(
                x=errorbarx,
                y=errorbary,
                xerr=xerr,
                yerr=yerr,
                title="エラーグラフの基本2",
                xlabel="x軸のラベル",
                ylabel="y軸のラベル",
            ),
        ],
        [
            guis.Errorbar(
                x=errorbarx,
                y=errorbary,
                err=err,
                title="xの上向きの誤差に矢印を付ける",
                xuplims=True,
            ),
            guis.Errorbar(
                x=errorbarx,
                y=errorbary,
                err=err,
                title="xの下向きの誤差に矢印を付ける",
                xlolims=True,
            ),
        ],
        [
            guis.Errorbar(
                x=errorbarx,
                y=errorbary,
                err=err,
                title="yの上向きの誤差に矢印を付ける",
                yuplims=True,
            ),
            guis.Errorbar(
                x=errorbarx,
                y=errorbary,
                err=err,
                title="yの下向きの誤差に矢印を付ける",
                ylolims=True,
            ),
        ],
        [
            guis.Errorbar(
                x=errorbarx,
                y=errorbary,
                err=err,
                title="データ点とデータ点を結ぶ線を指定する",
                linestyle="dashdot",
            ),
            guis.Errorbar(
                x=errorbarx,
                y=errorbary,
                err=err,
                title="データの点の種類を変更する",
                marker="s",
            ),
        ],
        [
            guis.Errorbar(
                x=errorbarx,
                y=errorbary,
                err=err,
                title="キャップの長さを指定する",
                capsize=3,
            ),
            guis.Errorbar(
                x=errorbarx,
                y=errorbary,
                err=err,
                title="キャップの幅を指定する",
                capthick=20,
                capsize=3,
            ),
        ],
        [
            guis.Errorbar(
                x=errorbarx,
                y=errorbary,
                err=err,
                title="エラーグラフを表示する頻度を変える",
                errorevery=3,
            ),
            guis.Errorbar(
                x=errorbarx,
                y=errorbary,
                err=err,
                title="エラーグラフを表示する頻度を指定する。",
                errorevery=[2, 4],
            ),
        ],
        [
            guis.Errorbar(
                x=errorbarx,
                y=errorbary,
                err=err,
                title="エラーグラフの線の幅を変更する",
                linewidth=2,
            )
        ],
        [
            guis.Errorbar(
                x=errorbarx,
                y=errorbary,
                err=err,
                title="グラフを更新する",
                key="errorbar",
            ),
            guis.Buttons(text="更新ボタン", function=updates),
        ],
    ]
    win = guis.window(
        title="エラーグラフ(test)", layout=layout, scroll=True, maxmine=True
    )
    win.run()


if __name__ == "__main__":
    test_main()
