from _import import *

if __name__ == "__main__":

    def updates():
        radomdata = rng.integers(30, 60, size=5)
        print(f"{radomdata=}")
        barhGraph: BarhGraph = win.get("BarhGraph")
        barhGraph.update(x=radomdata)

    print(f"{bargraphx1=}")
    print(f"{bargraphx2=}")
    print(f"{bargraphy1=}")
    print(f"{bargraphy2=}")
    layout = [
        [
            Guis.BarhGraph(
                x=bargraphy1,
                y=bargraphx1,
                title="横軸棒グラフの基本1",
                xlabel=xlabel,
                ylabel=ylabel,
                label=["bar1"],
            ),
            Guis.BarhGraph(
                x=bargraphy2,
                y=bargraphx2,
                title="横軸棒グラフの基本2",
                xlabel=xlabel,
                ylabel=ylabel,
                label=["bar1", "bar2"],
            ),
        ],
        [
            Guis.BarhGraph(
                x=bargraphy1, y=bargraphx1, title="x軸を対数スケールにする", logs=True
            ),
            Guis.BarhGraph(
                x=bargraphy1, y=bargraphx1, title="グラフの開始位置の変更", align="edge"
            ),
        ],
        [
            Guis.BarhGraph(
                x=bargraphy1, y=bargraphx1, title="グラフの幅の変更", height=0.4
            )
        ],
        [
            Guis.BarhGraph(
                x=bargraphy1, y=bargraphx1, title="グラフを更新する", key="BarhGraph"
            ),
            Guis.Buttons(text="更新ボタン", function=updates),
        ],
    ]
    win = Guis.window(
        title="横軸棒グラフ(test)", layout=layout, scroll=True, maxmine=True
    )
    win.run()
