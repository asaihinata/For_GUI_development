from sgg import Guis
from sgg.testing._cursor import testing_CURSOR_LIST

layout_sum = 0
layout = []
for i in range(11):
    layout_set = []
    for j in range(7):
        txt = testing_CURSOR_LIST[layout_sum]
        layout_set.append(Guis.Texts(text=txt, cursor=txt))
        layout_sum += 1
    layout.append(layout_set)
win = Guis.window(layout=layout, maxmine=True, scroll=True)
win.run()
