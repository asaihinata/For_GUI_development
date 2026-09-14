import numpy as np

from sgg import RadarLine, guis

rng = np.random.default_rng(seed=42)


def test_main():

    def updates():
        radomdata = rng.integers(10, 15, size=5)
        print(f"{radomdata=}")
        radarline: RadarLine = win.get("radarline")
        radarline.update(data=radomdata)

    radarplotdata1 = rng.integers(10, 15, size=5)
    radarplotdata2 = rng.integers(10, 15, size=(2, 5))
    print(f"{radarplotdata1=}")
    print(f"{radarplotdata2=}")
    layout = [
        [
            guis.RadarLine(data=radarplotdata1, title="折線レーダーチャートの基本1"),
            guis.RadarLine(data=radarplotdata2, title="折線レーダーチャートの基本2"),
        ],
        [
            guis.RadarLine(
                data=radarplotdata1, linewidth=10, title="線の太さを変更する"
            ),
            guis.RadarLine(
                data=radarplotdata1, marker="+", title="マーカーを表示させる"
            ),
        ],
        [
            guis.RadarLine(
                data=radarplotdata1,
                marker="+",
                markersize=20,
                title="マーカーの大きさを変える",
            )
        ],
        [
            guis.RadarLine(
                data=radarplotdata1, title="グラフを更新する", key="radarline"
            ),
            guis.Buttons(text="更新ボタン", function=updates),
        ],
    ]
    win = guis.window(
        title="折線レーダーチャート(test)", layout=layout, scroll=True, maxmine=True
    )
    win.run()


if __name__ == "__main__":
    test_main()
