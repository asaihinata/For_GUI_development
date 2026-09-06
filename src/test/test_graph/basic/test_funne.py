import numpy as np

from sgg import Guis,Funne

rng = np.random.default_rng(seed=42)


def test_main():

    def updates():
        radomdata = rng.integers(10, 50, size=3)
        print(f"{radomdata=}")
        funne: Funne = win.get("funne")
        funne.update(radomdata)

    funnedata = rng.integers(10, 50, size=3)
    print(f"{funnedata=}")
    layout = [
        [
            Guis.Funne(
                data=funnedata,
                title="じょうごグラフの基本",
                xlabel="x軸のラベル",
                ylabel="y軸のラベル",
            ),
            Guis.Funne(data=funnedata, title="高さを変更する", height=0.5),
        ],
        [
            Guis.Funne(data=funnedata, title="グラフを更新する", key="funne"),
            Guis.Buttons(text="更新ボタン", function=updates),
        ],
    ]
    win = Guis.window(
        title="じょうごグラフ(test)", layout=layout, scroll=True, maxmine=True
    )
    win.run()


if __name__ == "__main__":
    test_main()
