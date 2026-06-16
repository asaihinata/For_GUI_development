from _import import *

if __name__ == "__main__":

    def updates():
        radomdata = randsint(30, 50, lenght=5)
        print(f"{radomdata=}")
        pies: Pie = win.get("pie")
        pies.update(radomdata)

    print(f"{piedata=}")
    layout = [
        [
            Guis.Pie(data=piedata, title="円グラフの基本", label=pielabel),
            Guis.Pie(
                data=piedata, title="円グラフに影を付ける", label=pielabel, shadow=True
            ),
        ],
        [
            Guis.Pie(
                data=piedata, title="円グラフを90度回す", label=pielabel, startangle=90
            ),
            Guis.Pie(
                data=piedata,
                title="円グラフをpi/2rad回す",
                label=pielabel,
                startangle=np.pi / 2,
                startangletype=False,
            ),
        ],
        [
            Guis.Pie(
                data=piedata,
                title="時計回りに表示させる",
                label=pielabel,
                counterclock=True,
            ),
            Guis.Pie(
                data=piedata,
                title="ラベルの表示位置を変更する",
                label=pielabel,
                labeldistance=1.5,
            ),
        ],
        [
            Guis.Pie(
                data=piedata, title="全体のウェッジを離す", label=pielabel, explode=0.2
            ),
            Guis.Pie(
                data=piedata,
                title="一部のウェッジを離す",
                label=pielabel,
                explode=[0.2, 0, 0, 0, 0],
            ),
        ],
        [
            Guis.Pie(data=piedata, title="グラフを更新する", label=pielabel, key="pie"),
            Guis.Buttons(text="更新ボタン", function=updates),
        ],
    ]
    win = Guis.window(title="円グラフ(test)", layout=layout, scroll=True, maxmine=True)
    win.run()
