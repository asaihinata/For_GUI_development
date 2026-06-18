"""
郵便番号から住所を調べるテスト

郵便番号検索API使用

郵便番号検索APIの詳細
https://zipcloud.ibsnet.co.jp/doc/api
"""

import json

from _import import *
import requests

if __name__ == "__main__":

    def ztoy():
        zyuusyo: Listboxs = win.get("zyuusyo")
        Yuubin: Input = win.get("yuubin")
        Yget = Yuubin.get_text()
        response = requests.get(
            f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={Yget}&limit=100"
        )
        getyubinz = json.loads(response.text)
        status = getyubinz["status"]
        message = getyubinz["message"]
        if status in [400, 500]:
            zyuusyo_txt = [message]
        elif status == 200:
            result = getyubinz["results"]
            zyuusyo.set_height(len(result))
            zyuusyo_txt = [
                f"{i["address1"]}{i["address2"]}{i["address3"]}" for i in result
            ]
        zyuusyo.set(zyuusyo_txt)

    layout = [
        [Guis.Texts(text="郵便番号から住所")],
        [
            Guis.Texts(text="郵便番号"),
            Guis.Input(text="1000000", key="yuubin"),
            Guis.Buttons(text="変換", function=ztoy),
        ],
        [
            Guis.Texts(text="住所"),
            Guis.Listboxs(values=["東京都千代田区"], height=1, key="zyuusyo"),
        ],
    ]
    win = Guis.window(layout=layout, maxmine=True, scroll=True)
    win.run()
