"""
住所から郵便番号を調べるテスト

ExcelAPI使用

ExcelAPIの詳細
https://excelapi.org/docs/post/zipcode/
"""

from _import import *
import requests

if __name__ == "__main__":

    def ytoz():
        zyuusyo: Input = win.get("zyuusyo")
        Zget = zyuusyo.get_text()
        yuubin: Input = win.get("yuubin")
        response = requests.get(f"https://api.excelapi.org/post/zipcode?address={Zget}")
        getyubinz = response.text
        if getyubinz == "":
            yubin_txt = f"{Zget}には郵便番号が存在しません"
        else:
            yubin_txt = response.text
        yuubin.set_text(yubin_txt)

    layout = [
        [Guis.Texts(text="住所から郵便番号")],
        [
            Guis.Texts(text="住所"),
            Guis.Input(text="東京都千代田区", key="zyuusyo"),
            Guis.Buttons(text="変換", function=ytoz),
        ],
        [
            Guis.Texts(text="郵便番号"),
            Guis.Input(text="1000000", key="yuubin"),
        ],
    ]
    win = Guis.window(layout=layout, maxmine=True, scroll=True)
    win.run()
