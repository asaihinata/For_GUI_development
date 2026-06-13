import pathlib

from _import import *

if __name__ == "__main__":

    def txtchange():
        win.get("txt1").set_text("!!!変わった!!!")

    def files():
        sgg.Popup(message=win.get("file_load").get_path())

    def folders():
        sgg.Popup(message=win.get("folder_load").get_path())

    def colors():
        sgg.Popup(message=win.get("color_select").get_color())

    def progress_start():
        win.get("prigress").start()

    Lennapath = pathlib.Path(__file__).parent.parent.parent / "data/img/Lenna.png"
    print(Lennapath)
    menus = [
        [
            "ファイル",
            [
                "開く",
                [
                    ["SubmenuのMenu"],
                    "メニュー2",
                    ["メニュー2のMenu"],
                    "メニュー3",
                    "メニュー4",
                ],
                "---",
                {"label": "閉じる", "function": lambda: win.close()},
            ],
        ],
        ["ヘルプ", [{"label": "バージョン"}]],
    ]
    list_val = ["赤", "青", "黄"]
    list_val2 = ["赤", "青", "黄", "赤", "青", "黄", "赤", "青", "黄", "赤", "青", "黄"]
    tree_values = [
        "あ行",
        ["あ", "い", "う", "え", "お"],
        "か行",
        ["か", "き", "く", "け", "こ"],
        "が行",
        ["が", "ぎ", "ぐ", "げ", "ご"],
    ]
    layout = [
        [sgg.Menus(list=menus, key="menus")],
        [sgg.Texts(text="Textウィジェット")],
        [
            sgg.Texts(text="keyがtxt1のTextウィジェット", key="txt1"),
            sgg.Texts(
                key="txt2",
                text="文字色が水色,背景色が赤色,\nサイズが50文字の幅で高さが3文字分の\nTextウィジェット",
                bg="red",
                fg="aqua",
                size=(50, 3),
            ),
        ],
        [sgg.Buttons(text="ボタンウィジェット", key="btn1")],
        [
            sgg.Texts(text="keyがtxt1のTextのテキストを変えるボタン->"),
            sgg.Buttons(text="!!変える!!", function=[txtchange], key="btn2"),
        ],
        [sgg.Link(link="https://www.google.com/", text="googleのサイトを開く")],
        [sgg.Images(path=Lennapath)],
        [sgg.Texts(text="↑画像表示(PGM,PPM,GIF,PNG,XBMでしか表示されない)")],
        [
            sgg.Imagelink(
                link="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg48GxlSXF_4b4XZmtOALPhe3mD5iREyN-Ks6Q2hdviWeDHOcG_AUOS3nn2i-E9g5jD1_7-2o9PZF5MUQEanceM7b07viAr9M6h4C7jDqGhKdF0LzHzn2IBS_A2Fvpv605wIRf9ohIPiv-HStNDjk8JdN2hU-0GTI-OsjRraMo1HnGkTALf6v7qBbHufj04/s400/pose_galpeace_schoolgirl.png"
            )
        ],
        [sgg.Texts(text="↑URL画像も読み取れる")],
        [sgg.Texts(text="入力欄->"), sgg.Input(text="入力欄")],
        [sgg.Texts(text="パスワード入力->"), sgg.Input(show="※")],
        [sgg.Texts(text="複数行表示できる入力欄")],
        [
            sgg.Multiline(text="複数行表示可能の入力欄", key="multiline1"),
            sgg.Multiline(text=["配列でも", "表示可能"], key="multiline2"),
        ],
        [sgg.Texts(text="赤に選択されたリストボックス")],
        [sgg.Listboxs(values=list_val, select=0)],
        [sgg.TCombobox(values=list_val, default="好きな色を選ぼう!")],
        [sgg.Texts(text="数値入力")],
        [sgg.InputNumber(key="number")],
        [sgg.Texts(text="この中で一番好きな色を一つ選ぶ")],
        [
            sgg.Radio(text="赤色", group="color_name"),
            sgg.Radio(text="黄色", group="color_name"),
            sgg.Radio(text="緑色", group="color_name"),
            sgg.Radio(text="黒色", group="color_name"),
            sgg.Radio(text="その他", group="color_name"),
        ],
        [sgg.Texts(text="この中で一番好きな色を複数選ぶ")],
        [
            sgg.Checkbox(text="赤色", group="color_name"),
            sgg.Checkbox(text="黄色", group="color_name"),
            sgg.Checkbox(text="緑色", group="color_name"),
            sgg.Checkbox(text="黒色", group="color_name"),
            sgg.Checkbox(text="その他", group="color_name"),
        ],
        [sgg.Texts(text="この中で一番好きな食べ物を一つ選ぶ")],
        [
            sgg.Radio(text="からあげ", group="food_name"),
            sgg.Radio(text="蕎麦", default=True, group="food_name"),
            sgg.Radio(text="おすし", group="food_name"),
            sgg.Radio(text="おにぎり", group="food_name"),
            sgg.Radio(text="その他", group="food_name"),
        ],
        [sgg.Texts(text="この中で一番好きな食べ物を複数選ぶ")],
        [
            sgg.Checkbox(text="からあげ", group="food_name"),
            sgg.Checkbox(text="蕎麦", default=True, group="food_name"),
            sgg.Checkbox(text="おすし", group="food_name"),
            sgg.Checkbox(text="おにぎり", group="food_name"),
            sgg.Checkbox(text="その他", group="food_name"),
        ],
        [sgg.Texts(text="ファイルを選ぶ")],
        [sgg.FileLoad(key="file_load")],
        [sgg.Buttons(function=[files], text="選択したファイル")],
        [sgg.Texts(text="フォルダを選ぶ")],
        [sgg.FolderLoad(key="folder_load")],
        [sgg.Buttons(text="選択したフォルダ", function=[folders])],
        [sgg.Texts(text="色を選ぶ")],
        [sgg.Colorbtn(key="color_select")],
        [sgg.Buttons(text="選択した色", function=[colors])],
        [sgg.Texts(text="タブ")],
        [
            sgg.Tab(
                tabs=[
                    ["tab1", [[sgg.Texts(text="tab1")]]],
                    ["tab2", [[sgg.Texts(text="tab2")]]],
                ],
                key="tabs1",
            )
        ],
        [sgg.Texts(text="カレンダー")],
        [sgg.Texts(text="スライダー")],
        [sgg.Slidebar(value=20)],
        [sgg.Texts(text="プログレスバー")],
        [sgg.TProgressbar(key="prigress")],
        [sgg.Texts(text="表(縦見出しあり)")],
        [
            sgg.Table(
                header=["列A", "列B"],
                values=[["r1c1", "r1c2"], ["r2c1", "r2c2"]],
                rowheader=["aa", "bb"],
                key="table1",
            )
        ],
        [sgg.Texts(text="表(縦見出しなし)")],
        [
            sgg.Table(
                header=["列A", "列B"],
                values=[["r1c1", "r1c2"], ["r2c1", "r2c2"]],
                key="table2",
            )
        ],
        [sgg.Texts(text="ツリー")],
        [
            sgg.Tree(
                values=tree_values,
                side_header="行",
                header=["あ", "い", "う", "え", "お"],
                key="tree1",
            )
        ],
        [sgg.Texts(text="メニューボタン")],
        [sgg.Menubuttons(list=menus, text="メニューボタン")],
        [
            sgg.Buttons(
                text="Popup(情報)",
                function=lambda: print(sgg.Popup(message="メッセージ")),
            )
        ],
        [
            sgg.Buttons(
                text="Popupwarning(注意)",
                function=lambda: print(sgg.Popupwarning(message="メッセージ")),
            )
        ],
        [
            sgg.Buttons(
                text="Popupwarningyesno(注意)",
                function=lambda: print(sgg.Popupwarningyesno(message="メッセージ")),
            )
        ],
        [
            sgg.Buttons(
                text="Popuperror(エラー)",
                function=lambda: print(sgg.Popuperror(message="メッセージ")),
            )
        ],
        [
            sgg.Buttons(
                text="Popuperror(エラー)",
                function=lambda: print(sgg.Popuperroryesno(message="メッセージ")),
            )
        ],
        [
            sgg.Buttons(
                text="Popupyesno(bool型を返す)",
                function=lambda: print(sgg.Popupyesno(message="メッセージ")),
            )
        ],
        [
            sgg.Buttons(
                text="Popupokcancel(bool型を返す)",
                function=lambda: print(sgg.Popupokcancel(message="メッセージ")),
            )
        ],
        [
            sgg.Buttons(
                text="Popupquestion(YesかNoを返す)",
                function=lambda: print(sgg.Popupquestion(message="メッセージ")),
            )
        ],
        [
            sgg.Buttons(
                text="Popupyesnocancel(bool型とNoneを返す)",
                function=lambda: print(sgg.Popupyesnocancel(message="メッセージ")),
            )
        ],
    ]
    win = sgg.window(
        title="デモ", layout=layout, load=[progress_start], scroll=True, maxmine=True
    )
    win.run()
