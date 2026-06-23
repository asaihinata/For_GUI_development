import pathlib

from _import import *

if __name__ == "__main__":

    def txtchange():
        win.get("txt1").set_text("!!!変わった!!!")

    def files():
        Guis.Popup(message=win.get("file_load").get_path())

    def folders():
        Guis.Popup(message=win.get("folder_load").get_path())

    def colors():
        Guis.Popup(message=win.get("color_select").get_color())

    def progress_start():
        win.get("prigress").start()

    Lennapath = pathlib.Path(__file__).parent.parent.parent / "data/img/Lenna.png"
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
        [Guis.Menus(list=menus, key="menus")],
        [Guis.Texts(text="Textウィジェット")],
        [
            Guis.Texts(text="keyがtxt1のTextウィジェット", key="txt1"),
            Guis.Texts(
                key="txt2",
                text="文字色が水色,背景色が赤色,\nサイズが50文字の幅で高さが3文字分の\nTextウィジェット",
                bg="red",
                fg="aqua",
                size=(50, 3),
            ),
        ],
        [Guis.Buttons(text="ボタンウィジェット", key="btn1")],
        [
            Guis.Texts(text="keyがtxt1のTextのテキストを変えるボタン->"),
            Guis.Buttons(text="!!変える!!", function=[txtchange], key="btn2"),
        ],
        [Guis.Link(link="https://www.google.com/", text="googleのサイトを開く")],
        [Guis.Images(path=Lennapath)],
        [Guis.Texts(text="↑画像表示(PGM,PPM,GIF,PNG,XBMでしか表示されない)")],
        [
            Guis.Imagelink(
                link="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg48GxlSXF_4b4XZmtOALPhe3mD5iREyN-Ks6Q2hdviWeDHOcG_AUOS3nn2i-E9g5jD1_7-2o9PZF5MUQEanceM7b07viAr9M6h4C7jDqGhKdF0LzHzn2IBS_A2Fvpv605wIRf9ohIPiv-HStNDjk8JdN2hU-0GTI-OsjRraMo1HnGkTALf6v7qBbHufj04/s400/pose_galpeace_schoolgirl.png"
            )
        ],
        [Guis.Texts(text="↑URL画像も読み取れる")],
        [Guis.Texts(text="入力欄->"), Guis.Input(text="入力欄")],
        [Guis.Texts(text="パスワード入力->"), Guis.Input(show="※")],
        [Guis.Texts(text="複数行表示できる入力欄")],
        [
            Guis.Multiline(text="複数行表示可能の入力欄", key="multiline1"),
            Guis.Multiline(text=["配列でも", "表示可能"], key="multiline2"),
        ],
        [Guis.Texts(text="赤に選択されたリストボックス")],
        [Guis.Listboxs(values=list_val, select=0)],
        [Guis.TCombobox(values=list_val, default="好きな色を選ぼう!")],
        [Guis.Texts(text="数値入力")],
        [Guis.InputNumber(key="number")],
        [Guis.Texts(text="この中で一番好きな色を一つ選ぶ")],
        [
            Guis.Radio(text="赤色", group="color_name"),
            Guis.Radio(text="黄色", group="color_name"),
            Guis.Radio(text="緑色", group="color_name"),
            Guis.Radio(text="黒色", group="color_name"),
            Guis.Radio(text="その他", group="color_name"),
        ],
        [Guis.Texts(text="この中で一番好きな色を複数選ぶ")],
        [
            Guis.Checkbox(text="赤色", group="color_name"),
            Guis.Checkbox(text="黄色", group="color_name"),
            Guis.Checkbox(text="緑色", group="color_name"),
            Guis.Checkbox(text="黒色", group="color_name"),
            Guis.Checkbox(text="その他", group="color_name"),
        ],
        [Guis.Texts(text="この中で一番好きな食べ物を一つ選ぶ")],
        [
            Guis.Radio(text="からあげ", group="food_name"),
            Guis.Radio(text="蕎麦", default=True, group="food_name"),
            Guis.Radio(text="おすし", group="food_name"),
            Guis.Radio(text="おにぎり", group="food_name"),
            Guis.Radio(text="その他", group="food_name"),
        ],
        [Guis.Texts(text="この中で一番好きな食べ物を複数選ぶ")],
        [
            Guis.Checkbox(text="からあげ", group="food_name"),
            Guis.Checkbox(text="蕎麦", default=True, group="food_name"),
            Guis.Checkbox(text="おすし", group="food_name"),
            Guis.Checkbox(text="おにぎり", group="food_name"),
            Guis.Checkbox(text="その他", group="food_name"),
        ],
        [Guis.Texts(text="ファイルを選ぶ")],
        [Guis.FileLoad(key="file_load")],
        [Guis.Buttons(function=[files], text="選択したファイル")],
        [Guis.Texts(text="フォルダを選ぶ")],
        [Guis.FolderLoad(key="folder_load")],
        [Guis.Buttons(text="選択したフォルダ", function=[folders])],
        [Guis.Texts(text="色を選ぶ")],
        [Guis.Colorbtn(key="color_select")],
        [Guis.Buttons(text="選択した色", function=[colors])],
        [Guis.Texts(text="タブ")],
        [
            Guis.Tab(
                tabs=[
                    ["tab1", [[Guis.Texts(text="tab1")]]],
                    ["tab2", [[Guis.Texts(text="tab2")]]],
                ],
                key="tabs1",
            )
        ],
        [Guis.Texts(text="スライダー")],
        [Guis.Slidebar(value=20)],
        [Guis.Texts(text="プログレスバー")],
        [Guis.TProgressbar(key="prigress")],
        [Guis.Texts(text="表(縦見出しあり)")],
        [
            Guis.Table(
                header=["列A", "列B"],
                values=[["r1c1", "r1c2"], ["r2c1", "r2c2"]],
                rowheader=["aa", "bb"],
                key="table1",
            )
        ],
        [Guis.Texts(text="表(縦見出しなし)")],
        [
            Guis.Table(
                header=["列A", "列B"],
                values=[["r1c1", "r1c2"], ["r2c1", "r2c2"]],
                key="table2",
            )
        ],
        [Guis.Texts(text="ツリー")],
        [
            Guis.Tree(
                values=tree_values,
                side_header="行",
                header=["あ", "い", "う", "え", "お"],
                key="tree1",
            )
        ],
        [Guis.Texts(text="メニューボタン")],
        [Guis.Menubuttons(list=menus, text="メニューボタン")],
        [
            Guis.Buttons(
                text="Popup(情報)",
                function=lambda: print(Guis.Popup(message="メッセージ")),
            )
        ],
        [
            Guis.Buttons(
                text="Popupwarning(注意)",
                function=lambda: print(Guis.Popupwarning(message="メッセージ")),
            )
        ],
        [
            Guis.Buttons(
                text="Popupwarningyesno(注意)",
                function=lambda: print(Guis.Popupwarningyesno(message="メッセージ")),
            )
        ],
        [
            Guis.Buttons(
                text="Popuperror(エラー)",
                function=lambda: print(Guis.Popuperror(message="メッセージ")),
            )
        ],
        [
            Guis.Buttons(
                text="Popuperror(エラー)",
                function=lambda: print(Guis.Popuperroryesno(message="メッセージ")),
            )
        ],
        [
            Guis.Buttons(
                text="Popupyesno(bool型を返す)",
                function=lambda: print(Guis.Popupyesno(message="メッセージ")),
            )
        ],
        [
            Guis.Buttons(
                text="Popupokcancel(bool型を返す)",
                function=lambda: print(Guis.Popupokcancel(message="メッセージ")),
            )
        ],
        [
            Guis.Buttons(
                text="Popupquestion(YesかNoを返す)",
                function=lambda: print(Guis.Popupquestion(message="メッセージ")),
            )
        ],
        [
            Guis.Buttons(
                text="Popupyesnocancel(bool型とNoneを返す)",
                function=lambda: print(Guis.Popupyesnocancel(message="メッセージ")),
            )
        ],
    ]
    win = Guis.window(
        title="デモ", layout=layout, load=[progress_start], scroll=True, maxmine=True
    )
    win.run()
