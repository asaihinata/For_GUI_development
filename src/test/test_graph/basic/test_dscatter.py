from _import import *

if __name__ == "__main__":

    def updates():
        radomdata = rng.integers(30, 60, size=4)
        print(f"{radomdata=}")
        dscatter: DScatter = win.get("dscatter")
        dscatter.update(y=radomdata)

    print(f"{dscatterx=}")
    print(f"{dscattery=}")
    print(f"{dscatterz=}")
    layout = [
        [
            Guis.DScatter(
                x=dscatterx,
                y=dscattery,
                z=dscatterz,
                title="3D散布図の基本",
                xlabel=xlabel,
                ylabel=ylabel,
                zlabel=zlabel,
            ),
            Guis.DScatter(
                x=dscatterx,
                y=dscattery,
                z=dscatterz,
                title="グラフを動かす",
                xlabel=xlabel,
                ylabel=ylabel,
                zlabel=zlabel,
                mouse_rotation=False,
            ),
        ],
        [
            Guis.DScatter(
                x=dscatterx,
                y=dscattery,
                z=dscatterz,
                title="マーカーを指定する",
                marker="*",
            ),
            Guis.DScatter(
                x=dscatterx,
                y=dscattery,
                z=dscatterz,
                title="マーカーサイズを変更する",
                marker=2,
                markersize=20,
            ),
        ],
        [
            Guis.DScatter(
                x=dscatterx,
                y=dscattery,
                z=dscatterz,
                title="グラフを更新する",
                key="dscatter",
            ),
            Guis.Buttons(text="更新ボタン", function=updates),
        ],
    ]
    win = Guis.window(title="3D散布図(test)", layout=layout, scroll=True, maxmine=True)
    win.run()
