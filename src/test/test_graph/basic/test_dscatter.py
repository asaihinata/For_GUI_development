import numpy as np

from sgg import *

rng = np.random.default_rng(seed=42)


def test_main():

    def updates():
        radomdata = rng.integers(30, 60, size=4)
        print(f"{radomdata=}")
        dscatter: DScatter = win.get("dscatter")
        dscatter.update(y=radomdata)

    dscatterx = np.arange(0, 4, 1)
    dscattery = [3, 4, 9, 10]
    dscatterz = [10, 20, 30, 40]
    print(f"{dscatterx=}")
    print(f"{dscattery=}")
    print(f"{dscatterz=}")
    layout = [
        [
            Guis.DScatter(
                x=dscatterx,
                y=dscattery,
                z=dscatterz,
                title="立体散布図の基本",
                xlabel="x軸のラベル",
                ylabel="y軸のラベル",
                zlabel="z軸のラベル",
            ),
            Guis.DScatter(
                x=dscatterx,
                y=dscattery,
                z=dscatterz,
                title="グラフを動かす",
                xlabel="x軸のラベル",
                ylabel="y軸のラベル",
                zlabel="z軸のラベル",
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
    win = Guis.window(
        title="立体散布図(test)", layout=layout, scroll=True, maxmine=True
    )
    win.run()


if __name__ == "__main__":
    test_main()
