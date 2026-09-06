import numpy as np

from sgg import Guis,Step

rng = np.random.default_rng(seed=42)


def test_main():

    def updates():
        radomdata = rng.integers(1, 10, 5)
        print(f"{radomdata=}")
        step: Step = win.get("step")
        step.update(radomdata)

    stepdata = rng.integers(1, 10, size=5)
    print(f"{stepdata=}")
    layout = [
        [
            Guis.Step(
                data=stepdata,
                title="階段グラフの基本",
                xlabel="x軸のラベル",
                ylabel="y軸のラベル",
            ),
            Guis.Step(data=stepdata, title="階段の範囲を指定する", range=5),
        ],
        [
            Guis.Step(data=stepdata, title="階段を塗りつぶす", fill=True),
            Guis.Step(data=stepdata, title="階段の基準を指定する", baseline=3),
        ],
        [
            Guis.Step(
                data=stepdata, title="階段の向きを変更する", orientation="horizontal"
            )
        ],
        [
            Guis.Step(data=stepdata, title="グラフを更新する", key="step"),
            Guis.Buttons(text="更新ボタン", function=updates),
        ],
    ]
    win = Guis.window(
        title="階段グラフ(test)", layout=layout, scroll=True, maxmine=True
    )
    win.run()


if __name__ == "__main__":
    test_main()
