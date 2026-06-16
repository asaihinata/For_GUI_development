from _import import *

if __name__ == "__main__":

    def updates():
        radomdata = rng.gamma(4, size=(3, 50))
        print(f"{radomdata=}")
        event: Eventplot = win.get("event")
        event.update(radomdata)

    print(f"{eventdata=}")
    layout = [
        [
            Guis.Eventplot(
                data=eventdata,
                title="イベントグラフの基本",
                xlabel=xlabel,
                ylabel=ylabel,
            ),
            Guis.Eventplot(
                data=eventdata, title="ラベルを付ける", label=["a", "b", "c"]
            ),
        ],
        [
            Guis.Eventplot(
                data=eventdata, title="向きを指定する", orientation="horizontal"
            ),
            Guis.Eventplot(data=eventdata, title="線の種類を変更する", linestyle=":"),
        ],
        [
            Guis.Eventplot(data=eventdata, title="線の幅を変更する", linelength=0.5),
            Guis.Eventplot(data=eventdata, title="線の高さを変更する", linewidth=2),
        ],
        [
            Guis.Eventplot(data=eventdata, title="グラフを更新する", key="event"),
            Guis.Buttons(text="更新ボタン", function=updates),
        ],
    ]
    win = Guis.window(
        title="イベントグラフ(test)", layout=layout, scroll=True, maxmine=True
    )
    win.run()
