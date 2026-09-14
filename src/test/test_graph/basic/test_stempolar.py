import numpy as np

from sgg import Stempolar, guis

rng = np.random.default_rng(seed=42)


def test_main():

    def updates():
        radomdata = rng.integers(low=50, high=80, size=3)
        print(f"{radomdata=}")
        stemplot: Stempolar = win.get("stempolar")
        stemplot.update(x=radomdata)

    stempolarx = rng.integers(50, 80, size=3)
    stempolary = np.arange(1, 4, 1)
    stempolardata = rng.integers(50, 80, size=3)
    print(f"{stempolarx=}")
    print(f"{stempolary=}")
    print(f"{stempolardata=}")
    layout = [
        [
            guis.Stempolar(x=stempolarx, y=stempolary, title="極軸幹図の基本1"),
            guis.Stempolar(data=stempolardata, title="極軸幹図の基本2"),
        ],
        [
            guis.Stempolar(
                x=stempolarx, y=stempolary, title="マーカーを変更する", fmarker="^"
            ),
            guis.Stempolar(
                x=stempolarx, y=stempolary, title="ベースラインを変更する", bottom=30
            ),
        ],
        [
            guis.Stempolar(
                x=stempolarx, y=stempolary, title="極軸幹図の色を変更する", fcolor="b"
            ),
            guis.Stempolar(
                x=stempolarx, y=stempolary, title="極軸幹図の線を変更する", fline="--"
            ),
        ],
        [
            guis.Stempolar(
                x=stempolarx, y=stempolary, title="グラフを更新する", key="stempolar"
            ),
            guis.Buttons(text="更新ボタン", function=updates),
        ],
    ]
    win = guis.window(title="極軸幹図(test)", layout=layout, scroll=True, maxmine=True)
    win.run()


if __name__ == "__main__":
    test_main()
