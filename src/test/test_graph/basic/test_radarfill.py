from _import import *

if __name__ == "__main__":

    def updates():
        radomdata = rng.integers(50, 100, size=5)
        print(f"{radomdata=}")
        radarfill: RadarFill = win.get("radarfill")
        radarfill.update(data=radomdata)

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
