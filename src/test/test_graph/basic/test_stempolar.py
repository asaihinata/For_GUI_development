import numpy as np

from sgg import Guis,Stempolar

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
            Guis.Stempolar(x=stempolarx, y=stempolary, title="極軸幹図の基本1"),
            Guis.Stempolar(data=stempolardata, title="極軸幹図の基本2"),
        ],
        [
            Guis.Stempolar(
                x=stempolarx, y=stempolary, title="マーカーを変更する", fmarker="^"
            ),
            Guis.Stempolar(
                x=stempolarx, y=stempolary, title="ベースラインを変更する", bottom=30
            ),
        ],
        [
            Guis.Stempolar(
                x=stempolarx, y=stempolary, title="極軸幹図の色を変更する", fcolor="b"
            ),
            Guis.Stempolar(
                x=stempolarx, y=stempolary, title="極軸幹図の線を変更する", fline="--"
            ),
        ],
        [
            Guis.Stempolar(
                x=stempolarx, y=stempolary, title="グラフを更新する", key="stempolar"
            ),
            Guis.Buttons(text="更新ボタン", function=updates),
        ],
    ]
    win = Guis.window(title="極軸幹図(test)", layout=layout, scroll=True, maxmine=True)
    win.run()


if __name__ == "__main__":
    test_main()
