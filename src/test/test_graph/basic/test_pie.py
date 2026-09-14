import numpy as np

from sgg import Pie, guis

rng = np.random.default_rng(seed=42)


def test_main():

    def updates():
        radomdata = rng.random(5) * 30 + 50
        print(f"{radomdata=}")
        pies: Pie = win.get("pie")
        pies.update(radomdata)

    piedata = rng.integers(30, 50, size=5)
    pielabel = ["1月", "2月", "3月", "4月", "5月"]
    print(f"{piedata=}")
    layout = [
        [
            guis.Pie(data=piedata, title="円グラフの基本", label=pielabel),
            guis.Pie(
                data=piedata, title="円グラフに影を付ける", label=pielabel, shadow=True
            ),
        ],
        [
            guis.Pie(
                data=piedata, title="円グラフを90度回す", label=pielabel, startangle=90
            ),
            guis.Pie(
                data=piedata,
                title="円グラフをpi/2rad回す",
                label=pielabel,
                startangle=np.pi / 2,
                startangletype=False,
            ),
        ],
        [
            guis.Pie(
                data=piedata,
                title="時計回りに表示させる",
                label=pielabel,
                counterclock=True,
            ),
            guis.Pie(
                data=piedata,
                title="ラベルの表示位置を変更する",
                label=pielabel,
                labeldistance=1.5,
            ),
        ],
        [
            guis.Pie(
                data=piedata, title="全体のウェッジを離す", label=pielabel, explode=0.2
            ),
            guis.Pie(
                data=piedata,
                title="一部のウェッジを離す",
                label=pielabel,
                explode=[0.2, 0, 0, 0, 0],
            ),
        ],
        [
            guis.Pie(data=piedata, title="グラフを更新する", label=pielabel, key="pie"),
            guis.Buttons(text="更新ボタン", function=updates),
        ],
    ]
    win = guis.window(title="円グラフ(test)", layout=layout, scroll=True, maxmine=True)
    win.run()


if __name__ == "__main__":
    test_main()
