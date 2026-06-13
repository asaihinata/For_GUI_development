from _import import *

if __name__ == "__main__":

    def updates():
        radomdata = rng.integers(1, 10, 5)
        print(f"{radomdata=}")
        step: Step = win.get("step")
        step.update(radomdata)

    print(f"{stepdata=}")
    layout = [
        [
            sgg.Step(
                data=stepdata, title="階段グラフの基本", xlabel=xlabel, ylabel=ylabel
            ),
            sgg.Step(data=stepdata, title="階段の範囲を指定する", range=5),
        ],
        [
            sgg.Step(data=stepdata, title="階段を塗りつぶす", fill=True),
            sgg.Step(data=stepdata, title="階段の基準を指定する", baseline=3),
        ],
        [
            sgg.Step(
                data=stepdata, title="階段の向きを変更する", orientation="horizontal"
            )
        ],
        [
            sgg.Step(data=stepdata, title="グラフを更新する", key="step"),
            sgg.Buttons(text="更新ボタン", function=updates),
        ],
    ]
    win = sgg.window(title="階段グラフ(test)", layout=layout, scroll=True, maxmine=True)
    win.run()
