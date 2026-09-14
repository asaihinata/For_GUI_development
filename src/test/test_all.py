import pathlib

import numpy as np

from sgg import WindowController, guis


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

    NOW_FILE = pathlib.Path(__file__).parent
    LENNAPATH = NOW_FILE / "data/img/Lenna.png"
    HTMLFILE = NOW_FILE / "data/index.html"
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
    tree_values = [
        "あ行",
        ["あ", "い", "う", "え", "お"],
        "か行",
        ["か", "き", "く", "け", "こ"],
        "が行",
        ["が", "ぎ", "ぐ", "げ", "ご"],
    ]
    rng = np.random.default_rng(seed=42)
    linex = np.arange(1, 4, 1)
    liney1 = rng.integers(50, 80, size=3)
    stemx1 = rng.integers(50, 80, size=3)
    stemy = np.arange(1, 4, 1)
    piedata = rng.integers(30, 50, size=5)
    pielabel = ["1月", "2月", "3月", "4月", "5月"]
    bargraphx1 = ["1月", "2月", "3月", "4月", "5月"]
    bargraphy1 = rng.integers(30, 60, size=5)
    bargraphx2 = ["1月", "2月", "3月"]
    bargraphy2 = rng.integers(30, 60, size=(2, 3))
    scatterx1 = ["1月", "2月", "3月", "4月", "5月"]
    scattery1 = rng.integers(0, 10, size=5)
    scatterx2 = np.arange(1, 4, 1)
    scattery2 = rng.integers(100, 400, size=(2, 3))
    waterfallx = ["1月", "2月", "3月", "4月", "5月", "6月"]
    waterfally = [30, -10, 10, 5, 10, -80]
    stackx = np.arange(1, 4, 1)
    stacky = rng.integers(50, 80, size=(2, 3))
    errorbarx = np.arange(2, 12, 2)
    errorbary = rng.integers(0, 3, 5)
    err = rng.integers(3, size=5)
    xerr = rng.integers(3, size=5)
    yerr = rng.integers(3, size=5)
    dscatterx = np.arange(0, 4, 1)
    dscattery = [3, 4, 9, 10]
    dscatterz = [10, 20, 30, 40]
    stepdata = rng.integers(1, 10, size=5)
    histdata = rng.normal(10, 50, size=1000)
    boxdata1 = rng.normal(10, 100, size=100)
    eventdata = rng.gamma(4, size=(3, 50))
    ecdfdata = 4 + rng.normal(0, 1.5, size=100)
    stackeddata = rng.integers(1, 10, (3, 3)) + 2
    stackeddataname = ["dataname1", "dataname2", "dataname3"]
    violindata = rng.normal((3, 5, 4), (0.75, 1.00, 0.75), (200, 3))
    hexbinx1 = rng.standard_normal((1, 5000))
    hexbiny1 = 1.2 * hexbinx1 + rng.standard_normal((1, 5000)) / 3
    hist2dx = rng.standard_normal(5000)
    hist2dy = 1.2 * hist2dx + rng.standard_normal(5000) / 3
    linefillx = np.linspace(0, 8, 16)
    linefillymax = 3 + 4 * linefillx / 8 + rng.uniform(0.0, 0.5, len(linefillx))
    linefillymin = 1 + 2 * linefillx / 8 + rng.uniform(0.0, 0.5, len(linefillx))
    funnedata = rng.integers(10, 50, size=3)
    hatplotx = rng.integers(20, 30, size=5, endpoint=True)
    hatplotdata = hatplotx + 3
    radarfilldata = rng.integers(50, 100, size=5)
    radarlinedata = rng.integers(10, 15, size=5)
    barpolarx = np.linspace(0, np.pi * 2, 5)
    barpolary = rng.integers(30, 60, size=5)
    errorpolarx = np.arange(2, 12, 2)
    errorpolary = rng.integers(0, 3, 5)
    polarerr = rng.integers(2, size=5) + 0.5
    polarxerr = rng.integers(2, size=5) + 0.5
    polaryerr = rng.integers(2, size=5) + 0.5
    linepolarx = np.arange(1, 4, 1)
    linepolary = rng.integers(50, 80, size=3)
    scatterpolarx = rng.integers(0, 10, size=5)
    scatterpolary = rng.integers(0, 10, size=5)
    stempolarx = rng.integers(50, 80, size=3)
    stempolary = np.arange(1, 4, 1)
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
        [guis.Link(link=HTMLFILE, text="htmlファイルを開く")],
        [guis.Images(path=LENNAPATH)],
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
        [
            guis.LineGraph(
                x=linex,
                y=liney1,
                title="折線グラフ",
                xlabel="xlabel",
                ylabel="ylabel",
            )
        ],
        [guis.Pie(data=piedata, title="円グラフ", label=pielabel)],
        [
            guis.BarGraph(
                x=bargraphx2,
                y=bargraphy2,
                title="棒グラフ(縦)",
                xlabel="xlabel",
                ylabel="ylabel",
                width=0.5,
            )
        ],
        [
            guis.BarhGraph(
                x=bargraphy1,
                y=bargraphx1,
                title="棒グラフ(横)",
                xlabel="xlabel",
                ylabel="ylabel",
                height=0.5,
            )
        ],
        [
            guis.Scatter(
                x=scatterx1,
                y=scattery1,
                title="散布図",
                xlabel="xlabel",
                ylabel="ylabel",
            )
        ],
        [guis.Scatter(x=scatterx2, y=scattery2, title="散布図")],
        [
            guis.DScatter(
                x=dscatterx,
                y=dscattery,
                z=dscatterz,
                title="3D 散布図",
                xlabel="x",
                ylabel="y",
                zlabel="z",
            )
        ],
        [guis.Hist(data=histdata, title="ヒストグラフ")],
        [guis.Stem(x=stemx1, y=stemy, title="ステムグラフ")],
        [guis.Boxplot(data=boxdata1, title="箱ひげ図", whis=1.5)],
        [
            guis.Waterfall(
                x=waterfallx,
                y=waterfally,
                width=0.5,
                title="ウォーターフォール",
                linestyle="dotted",
            )
        ],
        [
            guis.Waterfallh(
                x=waterfallx, y=waterfally, height=0.5, title="ウォーターフォール"
            )
        ],
        [guis.Step(data=stepdata, title="階段グラフ")],
        [guis.Stack(x=stackx, y=stacky, title="積み上げグラフ")],
        [
            guis.Eventplot(
                data=eventdata,
                linestyle="dashed",
                label=["a", "b", "c"],
                title="イベントグラフ",
            )
        ],
        [guis.Errorbar(x=errorbarx, y=errorbary, err=err, title="エラーグラフ")],
        [
            guis.Errorbar(
                x=errorbarx, y=errorbary, xerr=xerr, yerr=yerr, title="エラーグラフ"
            )
        ],
        [guis.Errorbar(x=errorbarx, y=errorbary, xerr=xerr, title="エラーグラフ")],
        [guis.Errorbar(x=errorbarx, y=errorbary, yerr=yerr, title="エラーグラフ")],
        [guis.Ecdf(data=ecdfdata, title="経験的累積分布関数のグラフ")],
        [
            guis.Stacked(
                data=stackeddata,
                dataname=stackeddataname,
                title="積み上げ縦棒グラフ",
            )
        ],
        [
            guis.Stackedh(
                data=stackeddata,
                dataname=stackeddataname,
                title="積み上げ横棒グラフ",
            )
        ],
        [
            guis.Violinplot(
                data=violindata,
                title="バイオリングラフ",
                xlabel="x軸のラベル",
                ylabel="y軸のラベル",
            )
        ],
        [
            guis.Hatplot(
                x=hatplotx,
                data=hatplotdata,
                title="ハットグラフ",
                xlabel="x軸のラベル",
                ylabel="y軸のラベル",
                yticksrange=5,
            )
        ],
        [
            guis.Hexbin(
                x=hexbinx1,
                y=hexbiny1,
                title="2次元六角形グラフ",
                xlabel="x軸のラベル",
                ylabel="y軸のラベル",
            )
        ],
        [
            guis.Hist2d(
                x=hist2dx,
                y=hist2dy,
                title="2次元ヒストグラム",
                xlabel="x軸のラベル",
                ylabel="y軸のラベル",
            )
        ],
        [
            guis.Linefill(
                x=linefillx,
                ymax=linefillymax,
                ymin=linefillymin,
                title="積上げ面グラフ",
                xlabel="x軸のラベル",
                ylabel="y軸のラベル",
            )
        ],
        [guis.Funne(data=funnedata, title="じょうごグラフ")],
        [guis.Barpolar(x=barpolarx, y=barpolary, title="極軸棒グラフ")],
        [
            guis.Errorpolar(
                x=errorpolarx, y=errorpolary, err=polarerr, title="極軸エラーグラフ"
            )
        ],
        [
            guis.Errorpolar(
                x=errorpolarx,
                y=errorpolary,
                xerr=polarxerr,
                yerr=polaryerr,
                title="極軸エラーグラフ",
            )
        ],
        [guis.Eventpolar(data=eventdata, title="極軸イベントグラフ")],
        [guis.Linepolar(x=linepolarx, y=linepolary, title="極軸折線グラフ")],
        [guis.Scatterpolar(x=scatterpolarx, y=scatterpolary, title="極軸散布図")],
        [guis.Stempolar(x=stempolarx, y=stempolary, title="極軸幹図")],
        [guis.RadarFill(data=radarfilldata, title="塗りつぶしレーダーチャート")],
        [guis.RadarLine(data=radarlinedata, title="折線レーダーチャート")],
    ]
    win: WindowController = guis.window(
        title="デモ", layout=layout, load=[progress_start], scroll=True, maxmine=True
    )
    win.run()


if __name__ == "__main__":
    test_main()
