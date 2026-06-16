from _import import *

if __name__ == "__main__":
    marker1 = [",", "1", "2", "3", "4", "+", "x", "|", "_"]
    marker2 = list(range(1, 12, 1))
    x = np.arange(1, 2)
    y1 = [[count] for count, _ in enumerate(range(1, len(marker1) + 1))]
    y2 = [[count] for count, _ in enumerate(range(1, len(marker2) + 1))]
    layout = [
        [
            Guis.Scatter(
                x=x,
                y=y1,
                label=marker1,
                marker=marker1,
                markersize=50,
                grid_xy=False,
                ticksshow=True,
            ),
            Guis.Scatter(
                x=x,
                y=y2,
                label=marker2,
                marker=marker2,
                markersize=50,
                grid_xy=False,
                ticksshow=True,
            ),
        ]
    ]
    win = Guis.window(
        title="線のスタイルの種類", layout=layout, scroll=True, maxmine=True
    )
    win.run()
