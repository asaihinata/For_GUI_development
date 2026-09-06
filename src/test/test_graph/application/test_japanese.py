from pathlib import Path

import numpy as np
import pandas as pd

from sgg import Guis


def test_main():
    data = (
        pd.read_csv(Path(__file__).parent / "data" / "japan_population.csv")
        .to_numpy()[1:4, 2:8]
        .astype(np.int64)
    )
    layout = [
        [
            Guis.LineGraph(
                x=[2015, 2016, 2017, 2018, 2019, 2020],
                y=data,
                label=["女", "男", "総合"],
                xlabel="年",
                ylabel="人数",
                title="人口の変化",
            )
        ]
    ]
    win = Guis.window(
        title="人口の変化(test)", layout=layout, scroll=True, maxmine=True
    )
    win.run()


if __name__ == "__main__":
    test_main()
