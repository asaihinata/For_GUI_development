import numpy as np

from sgg import Guis,Boxplot

rng = np.random.default_rng(seed=42)


def test_main():

    def updates():
        radomdata = rng.normal(100, 10, size=100)
        print(f"{radomdata=}")
        boxplot: Boxplot = win.get("boxplot")
        boxplot.update(radomdata)

    boxdata1 = rng.normal(20, 90, 100)
    boxdata2 = rng.normal(20, 90, size=(2, 150))
    print(f"{boxdata1=}")
    print(f"{boxdata2=}")
    layout = [
        [
            Guis.Boxplot(
                data=boxdata1,
                title="箱ひげ図の基本1",
                xlabel="x軸のラベル",
                ylabel="y軸のラベル",
            ),
            Guis.Boxplot(
                data=boxdata2,
                title="箱ひげ図の基本2",
                xlabel="x軸のラベル",
                ylabel="y軸のラベル",
            ),
        ],
        [
            Guis.Boxplot(data=boxdata1, title="凡例を非表示にする", legend=False),
            Guis.Boxplot(data=boxdata1, title="箱ひげ図に窪みを入れる", notch=True),
        ],
        [
            Guis.Boxplot(data=boxdata1, title="外れ値を非表示にする", showfliers=False),
            Guis.Boxplot(
                data=boxdata1, title="箱ひげ図の向きを変える", orientation="horizontal"
            ),
        ],
        [
            Guis.Boxplot(
                data=boxdata1, title="箱ひげ図の髭の開始位置を変更する1", whis=2
            ),
            Guis.Boxplot(
                data=boxdata1, title="箱ひげ図の髭の開始位置を変更する2", whis=[10, 90]
            ),
        ],
        [
            Guis.Boxplot(data=boxdata1, title="箱ひげ図の幅を変更する", width=0.5),
            Guis.Boxplot(data=boxdata1, title="ラベル名を変更する", label=["ラベル1"]),
        ],
        [Guis.Boxplot(data=boxdata1, title="凡例を表示する", legend=True)],
        [
            Guis.Boxplot(data=boxdata1, title="グラフを更新する", key="boxplot"),
            Guis.Buttons(text="更新ボタン", function=updates),
        ],
    ]
    win = Guis.window(title="箱ひげ図(test)", layout=layout, scroll=True, maxmine=True)
    win.run()


if __name__ == "__main__":
    test_main()
