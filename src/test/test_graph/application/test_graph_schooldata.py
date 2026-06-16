from _import import *

if __name__ == "__main__":
    data = np.array(getcsv("school_test_demo_data.csv"))
    layout = []
    for i in range(6):
        tabs = []
        for j in range(1, 6):
            datas = data[j + i * 5]
            tabs.append(
                [
                    datas[0],
                    [
                        [
                            Guis.BarGraph(
                                x=["国語", "社会", "数学", "理科"],
                                y=datas[1::].astype(np.int64),
                                title="教科別の点数",
                                xlabel="教科名",
                                ylabel="点数",
                            )
                        ]
                    ],
                ]
            )
        layout.append([Guis.Tab(tabs=tabs)])
    win = Guis.window(
        title="テストの結果(test)", layout=layout, scroll=True, maxmine=True
    )
    win.run()
