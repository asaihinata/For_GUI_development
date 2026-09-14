import pathlib

from sgg import guis


def test_main():
    def txtchange():
        win.get("txt1").set_text("!!!変わった!!!")

    def files():
        guis.Popup(message=win.get("file_load").get_path())

    def folders():
        guis.Popup(message=win.get("folder_load").get_path())

    def colors():
        guis.Popup(message=win.get("color_select").get_color())

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
        [guis.Menus(list=menus, key="menus")],
        [guis.Texts(text="Textウィジェット")],
        [
            guis.Texts(text="keyがtxt1のTextウィジェット", key="txt1"),
            guis.Texts(
                key="txt2",
                text="文字色が水色,背景色が赤色,\nサイズが50文字の幅で高さが3文字分の\nTextウィジェット",
                bg="red",
                fg="aqua",
                size=(50, 3),
            ),
        ],
        [guis.Buttons(text="ボタンウィジェット", key="btn1")],
        [
            guis.Texts(text="keyがtxt1のTextのテキストを変えるボタン->"),
            guis.Buttons(text="!!変える!!", function=[txtchange], key="btn2"),
        ],
        [guis.Link(link="https://www.google.com/", text="googleのサイトを開く")],
        [guis.Images(path=Lennapath)],
        [guis.Texts(text="↑画像表示(PGM,PPM,GIF,PNG,XBMでしか表示されない)")],
        [
            guis.Imagelink(
                link="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg48GxlSXF_4b4XZmtOALPhe3mD5iREyN-Ks6Q2hdviWeDHOcG_AUOS3nn2i-E9g5jD1_7-2o9PZF5MUQEanceM7b07viAr9M6h4C7jDqGhKdF0LzHzn2IBS_A2Fvpv605wIRf9ohIPiv-HStNDjk8JdN2hU-0GTI-OsjRraMo1HnGkTALf6v7qBbHufj04/s400/pose_galpeace_schoolgirl.png"
            )
        ],
        [guis.Texts(text="↑URL画像も読み取れる")],
        [guis.Texts(text="入力欄->"), guis.Input(text="入力欄")],
        [guis.Texts(text="パスワード入力->"), guis.Input(show="※")],
        [guis.Texts(text="複数行表示できる入力欄")],
        [
            guis.Multiline(text="複数行表示可能の入力欄", key="multiline1"),
            guis.Multiline(text=["配列でも", "表示可能"], key="multiline2"),
        ],
        [guis.Texts(text="赤に選択されたリストボックス")],
        [guis.Listboxs(values=list_val, select=0)],
        [guis.TCombobox(values=list_val, default="好きな色を選ぼう!")],
        [guis.Texts(text="数値入力")],
        [guis.InputNumber(key="number")],
        [guis.Texts(text="この中で一番好きな色を一つ選ぶ")],
        [
            guis.Radio(text="赤色", group="color_name"),
            guis.Radio(text="黄色", group="color_name"),
            guis.Radio(text="緑色", group="color_name"),
            guis.Radio(text="黒色", group="color_name"),
            guis.Radio(text="その他", group="color_name"),
        ],
        [guis.Texts(text="この中で一番好きな色を複数選ぶ")],
        [
            guis.Checkbox(text="赤色", group="color_name"),
            guis.Checkbox(text="黄色", group="color_name"),
            guis.Checkbox(text="緑色", group="color_name"),
            guis.Checkbox(text="黒色", group="color_name"),
            guis.Checkbox(text="その他", group="color_name"),
        ],
        [guis.Texts(text="この中で一番好きな食べ物を一つ選ぶ")],
        [
            guis.Radio(text="からあげ", group="food_name"),
            guis.Radio(text="蕎麦", default=True, group="food_name"),
            guis.Radio(text="おすし", group="food_name"),
            guis.Radio(text="おにぎり", group="food_name"),
            guis.Radio(text="その他", group="food_name"),
        ],
        [guis.Texts(text="この中で一番好きな食べ物を複数選ぶ")],
        [
            guis.Checkbox(text="からあげ", group="food_name"),
            guis.Checkbox(text="蕎麦", default=True, group="food_name"),
            guis.Checkbox(text="おすし", group="food_name"),
            guis.Checkbox(text="おにぎり", group="food_name"),
            guis.Checkbox(text="その他", group="food_name"),
        ],
        [guis.Texts(text="ファイルを選ぶ")],
        [guis.FileLoad(key="file_load")],
        [guis.Buttons(function=[files], text="選択したファイル")],
        [guis.Texts(text="フォルダを選ぶ")],
        [guis.FolderLoad(key="folder_load")],
        [guis.Buttons(text="選択したフォルダ", function=[folders])],
        [guis.Texts(text="色を選ぶ")],
        [guis.Colorbtn(key="color_select")],
        [guis.Buttons(text="選択した色", function=[colors])],
        [guis.Texts(text="タブ")],
        [
            guis.Tab(
                tabs=[
                    ["tab1", [[guis.Texts(text="tab1")]]],
                    ["tab2", [[guis.Texts(text="tab2")]]],
                ],
                key="tabs1",
            )
        ],
        [guis.Texts(text="スライダー")],
        [guis.Slidebar(value=20)],
        [guis.Texts(text="プログレスバー")],
        [guis.TProgressbar(key="prigress")],
        [guis.Texts(text="表(縦見出しあり)")],
        [
            guis.Table(
                header=["列A", "列B"],
                values=[["r1c1", "r1c2"], ["r2c1", "r2c2"]],
                rowheader=["aa", "bb"],
                key="table1",
            )
        ],
        [guis.Texts(text="表(縦見出しなし)")],
        [
            guis.Table(
                header=["列A", "列B"],
                values=[["r1c1", "r1c2"], ["r2c1", "r2c2"]],
                key="table2",
            )
        ],
        [guis.Texts(text="ツリー")],
        [
            guis.Tree(
                values=tree_values,
                side_header="行",
                header=["あ", "い", "う", "え", "お"],
                key="tree1",
            )
        ],
        [guis.Texts(text="メニューボタン")],
        [guis.Menubuttons(list=menus, text="メニューボタン")],
        [
            guis.Buttons(
                text="Popup(情報)",
                function=lambda: print(guis.Popup(message="メッセージ")),
            )
        ],
        [
            guis.Buttons(
                text="Popupwarning(注意)",
                function=lambda: print(guis.Popupwarning(message="メッセージ")),
            )
        ],
        [
            guis.Buttons(
                text="Popupwarningyesno(注意)",
                function=lambda: print(guis.Popupwarningyesno(message="メッセージ")),
            )
        ],
        [
            guis.Buttons(
                text="Popuperror(エラー)",
                function=lambda: print(guis.Popuperror(message="メッセージ")),
            )
        ],
        [
            guis.Buttons(
                text="Popuperror(エラー)",
                function=lambda: print(guis.Popuperroryesno(message="メッセージ")),
            )
        ],
        [
            guis.Buttons(
                text="Popupyesno(bool型を返す)",
                function=lambda: print(guis.Popupyesno(message="メッセージ")),
            )
        ],
        [
            guis.Buttons(
                text="Popupokcancel(bool型を返す)",
                function=lambda: print(guis.Popupokcancel(message="メッセージ")),
            )
        ],
        [
            guis.Buttons(
                text="Popupquestion(YesかNoを返す)",
                function=lambda: print(guis.Popupquestion(message="メッセージ")),
            )
        ],
        [
            guis.Buttons(
                text="Popupyesnocancel(bool型とNoneを返す)",
                function=lambda: print(guis.Popupyesnocancel(message="メッセージ")),
            )
        ],
    ]
    win = guis.window(
        title="デモ", layout=layout, load=[progress_start], scroll=True, maxmine=True
    )
    win.run()


if __name__ == "__main__":
    test_main()
