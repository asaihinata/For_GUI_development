import numpy as np

from sgg import Guis, RadarFill

rng = np.random.default_rng(seed=42)


def test_main():

    def updates():
        radomdata = rng.integers(50, 100, size=5)
        print(f"{radomdata=}")
        radarfill: RadarFill = win.get("radarfill")
        radarfill.update(data=radomdata)

    radarfilldata1 = rng.integers(50, 100, size=5)
    radarfilldata2 = rng.integers(50, 100, size=(3, 5))
    print(f"{radarfilldata1=}")
    print(f"{radarfilldata2=}")
    layout = [
        [
            Guis.RadarFill(
                data=radarfilldata1, title="塗りつぶしレーダーチャートの基本1"
            ),
            Guis.RadarFill(
                data=radarfilldata2, title="塗りつぶしレーダーチャートの基本2"
            ),
        ],
        [Guis.RadarFill(data=radarfilldata1, alpha=0.5, title="透明度を変更する")],
        [
            Guis.RadarFill(
                data=radarfilldata1, title="グラフを更新する", key="radarfill"
            ),
            Guis.Buttons(text="更新ボタン", function=updates),
        ],
    ]
    win = Guis.window(
        title="塗りつぶしレーダーチャート(test)",
        layout=layout,
        scroll=True,
        maxmine=True,
    )
    win.run()


if __name__ == "__main__":
    test_main()
