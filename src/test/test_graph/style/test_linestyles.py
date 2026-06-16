from _import import *

if __name__ == "__main__":
    linestyle = ["solid", "dotted", "dashed", "dashdot", "None"]
    x = np.arange(1, 10)
    y = [
        [count for _ in range(1, 10)]
        for count, _ in enumerate(range(1, len(linestyle) + 1))
    ]
    layout = [[Guis.LineGraph(x=x, y=y, label=linestyle, linestyle=linestyle)]]
    win = Guis.window(
        title="線のスタイルの種類", layout=layout, scroll=True, maxmine=True
    )
    win.run()
