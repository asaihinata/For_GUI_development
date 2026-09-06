import numpy as np

from sgg import Guis,BarhGraph

rng = np.random.default_rng(seed=42)


def test_main():

    def updates():
        radomdata = rng.integers(30, 60, size=5)
        print(f"{radomdata=}")
        barhGraph: BarhGraph = win.get("BarhGraph")
        barhGraph.update(x=radomdata)

    barhgraphx1 = ["1月", "2月", "3月", "4月", "5月"]
    barhgraphy1 = rng.integers(30, 60, size=5)
    barhgraphx2 = ["1月", "2月", "3月"]
    barhgraphy2 = rng.integers(30, 60, size=(2, 3))
    print(f"{barhgraphx1=}")
    print(f"{barhgraphx2=}")
    print(f"{barhgraphy1=}")
    print(f"{barhgraphy2=}")
    layout = [
        [
            Guis.BarhGraph(
                x=barhgraphy1,
                y=barhgraphx1,
                title="横向き棒グラフの基本1",
                xlabel="x軸のラベル",
                ylabel="y軸のラベル",
                label=["bar1"],
            ),
            Guis.BarhGraph(
                x=barhgraphy2,
                y=barhgraphx2,
                title="横向き棒グラフの基本2",
                xlabel="x軸のラベル",
                ylabel="y軸のラベル",
                label=["bar1", "bar2"],
            ),
        ],
        [
            Guis.BarhGraph(
                x=barhgraphy1, y=barhgraphx1, title="x軸を対数スケールにする", logs=True
            ),
            Guis.BarhGraph(
                x=barhgraphy1, y=barhgraphx1, title="グラフの開始位置の変更", align="edge"
            ),
        ],
        [
            Guis.BarhGraph(
                x=barhgraphy1, y=barhgraphx1, title="グラフの幅の変更", height=0.4
            )
        ],
        [
            Guis.BarhGraph(
                x=barhgraphy1, y=barhgraphx1, title="グラフを更新する", key="BarhGraph"
            ),
            Guis.Buttons(text="更新ボタン", function=updates),
        ],
    ]
    win = Guis.window(
        title="横向き棒グラフ(test)", layout=layout, scroll=True, maxmine=True
    )
    win.run()


if __name__ == "__main__":
    test_main()
