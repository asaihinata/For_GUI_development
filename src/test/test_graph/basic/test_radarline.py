from _import import *

if __name__ == "__main__":

    def updates():
        radomdata = rng.integers(10, 15, size=5)
        print(f"{radomdata=}")
        radarline: RadarLine = win.get("radarline")
        radarline.update(data=radomdata)

    print(f"{radarplotdata=}")
    layout = [
        [
            Guis.RadarLine(data=radarplotdata, title="折れ線レーダーチャートの基本"),
            Guis.RadarLine(
                data=radarplotdata, linewidth=10, title="線の太さを変更する"
            ),
        ],
        [
            Guis.RadarLine(
                data=radarplotdata, marker="+", title="マーカーを表示させる"
            ),
            Guis.RadarLine(
                data=radarplotdata,
                marker="+",
                markersize=20,
                title="マーカーの大きさを変える",
            ),
        ],
        [
            Guis.RadarLine(
                data=radarplotdata, title="グラフを更新する", key="radarline"
            ),
            Guis.Buttons(text="更新ボタン", function=updates),
        ],
    ]
    win = Guis.window(
        title="折れ線レーダーチャート(test)", layout=layout, scroll=True, maxmine=True
    )
    win.run()
