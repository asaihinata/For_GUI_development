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
            sgg.DScatter(
                x=dscatterx,
                y=dscattery,
                z=dscatterz,
                title="3D散布図の基本",
                xlabel=xlabel,
                ylabel=ylabel,
                zlabel=zlabel,
            ),
            sgg.DScatter(
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
            sgg.DScatter(
                x=dscatterx,
                y=dscattery,
                z=dscatterz,
                title="マーカーを指定する",
                marker="*",
            ),
            sgg.DScatter(
                x=dscatterx,
                y=dscattery,
                z=dscatterz,
                title="マーカーサイズを変更する",
                marker=2,
                markersize=20,
            ),
        ],
        [
            sgg.DScatter(
                x=dscatterx,
                y=dscattery,
                z=dscatterz,
                title="グラフを更新する",
                key="dscatter",
            ),
            sgg.Buttons(text="更新ボタン", function=updates),
        ],
    ]
    win = sgg.window(title="3D散布図(test)", layout=layout, scroll=True, maxmine=True)
    win.run()
