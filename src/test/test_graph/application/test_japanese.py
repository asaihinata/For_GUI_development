from _import import *

if __name__ == "__main__":
    data = np.array(getcsv("japan_population.csv"))[1:4, 2:8].astype(np.int64)
    layout = [
        [
            Guis.LineGraph(
                x=[2015, 2016, 2017, 2018, 2019, 2020],
                y=data,
                label=["総合", "女", "男"],
                xlabel="年",
                ylabel="人数",
                title="人口の変化",
            )
        ]
    ]
    win = Guis.window(
        title="人口の変化(test)", layout=layout, scroll=True, maxmine=True
    )
    win.run()
