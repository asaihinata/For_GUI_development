import numpy as np

from sgg import Eventplot, guis

rng = np.random.default_rng(seed=42)


def test_main():

    def updates():
        radomdata = rng.gamma(4, size=(3, 50))
        print(f"{radomdata=}")
        event: Eventplot = win.get("event")
        event.update(radomdata)

    eventdata = rng.gamma(4, size=(3, 50))
    print(f"{eventdata=}")
    layout = [
        [
            guis.Eventplot(
                data=eventdata,
                title="イベントグラフの基本",
                xlabel="x軸のラベル",
                ylabel="y軸のラベル",
            ),
            guis.Eventplot(
                data=eventdata, title="ラベルを付ける", label=["a", "b", "c"]
            ),
        ],
        [
            guis.Eventplot(
                data=eventdata, title="向きを指定する", orientation="horizontal"
            ),
            guis.Eventplot(data=eventdata, title="線の種類を変更する", linestyle=":"),
        ],
        [
            guis.Eventplot(data=eventdata, title="線の幅を変更する", linelength=0.5),
            guis.Eventplot(data=eventdata, title="線の高さを変更する", linewidth=2),
        ],
        [
            guis.Eventplot(data=eventdata, title="グラフを更新する", key="event"),
            guis.Buttons(text="更新ボタン", function=updates),
        ],
    ]
    win = guis.window(
        title="イベントグラフ(test)", layout=layout, scroll=True, maxmine=True
    )
    win.run()


if __name__ == "__main__":
    test_main()
