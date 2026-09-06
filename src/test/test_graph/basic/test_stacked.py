import numpy as np

from sgg import Guis,Stacked

rng = np.random.default_rng(seed=42)


def test_main():

    def updates():
        radomdata = rng.integers(1, 10, (3, 3)) + 2
        print(f"{radomdata=}")
        stack: Stacked = win.get("stacked")
        stack.update(radomdata)

    stackeddata = rng.integers(1, 10, (3, 3)) + 2
    stackeddataname = ["dataname1", "dataname2", "dataname3"]
    print(f"{stackeddata=}")
    print(f"{stackeddataname=}")
    layout = [
        [
            Guis.Stacked(
                data=stackeddata,
                dataname=stackeddataname,
                title="積み上げ棒グラフの基本",
                xlabel="x軸のラベル",
                ylabel="y軸のラベル",
            ),
            Guis.Stacked(
                data=stackeddata,
                dataname=stackeddataname,
                title="幅を変更する",
                width=0.5,
            ),
        ],
        [
            Guis.Stacked(
                data=stackeddata,
                dataname=stackeddataname,
                title="グラフを更新する",
                key="stacked",
            ),
            Guis.Buttons(text="更新ボタン", function=updates),
        ],
    ]
    win = Guis.window(
        title="積み上げ棒グラフ(test)", layout=layout, scroll=True, maxmine=True
    )
    win.run()


if __name__ == "__main__":
    test_main()
