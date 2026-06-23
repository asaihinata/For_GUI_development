import pathlib

from _import import *


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


if __name__ == "__main__":
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
    list_val2 = ["赤", "青", "黄", "赤", "青", "黄", "赤", "青", "黄", "赤", "青", "黄"]
    tree_values = [
        "あ行",
        ["あ", "い", "う", "え", "お"],
        "か行",
        ["か", "き", "く", "け", "こ"],
        "が行",
        ["が", "ぎ", "ぐ", "げ", "ご"],
    ]
    rng = np.random.default_rng(seed=42)
    xlabel = "x軸のラベル"
    ylabel = "y軸のラベル"
    zlabel = "z軸のラベル"
    linex = np.arange(1, 4, 1)
    liney1 = rng.integers(50, 80, size=3)
    liney2 = rng.integers(50, 80, size=(4, 3))
    stemx1 = rng.integers(50, 80, size=3)
    stemx2 = rng.integers(50, 80, size=(2, 3))
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
    boxdata2 = rng.normal(20, 90, size=(2, 150))
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
        [Guis.Link(link=HTMLFILE, text="htmlファイルを開く")],
        [Guis.Images(path=LENNAPATH)],
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
        [
            Guis.LineGraph(
                x=linex,
                y=liney1,
                title="折線グラフ",
                xlabel="xlabel",
                ylabel="ylabel",
            )
        ],
        [Guis.Pie(data=piedata, title="円グラフ", label=pielabel)],
        [
            Guis.BarGraph(
                x=bargraphx2,
                y=bargraphy2,
                title="棒グラフ(縦)",
                xlabel="xlabel",
                ylabel="ylabel",
                width=0.5,
            )
        ],
        [
            Guis.BarhGraph(
                x=bargraphy1,
                y=bargraphx1,
                title="棒グラフ(横)",
                xlabel="xlabel",
                ylabel="ylabel",
                height=0.5,
            )
        ],
        [
            Guis.Scatter(
                x=scatterx1,
                y=scattery1,
                title="散布図",
                xlabel="xlabel",
                ylabel="ylabel",
            )
        ],
        [Guis.Scatter(x=scatterx2, y=scattery2, title="散布図")],
        [
            Guis.DScatter(
                x=dscatterx,
                y=dscattery,
                z=dscatterz,
                title="3D 散布図",
                xlabel="x",
                ylabel="y",
                zlabel="z",
            )
        ],
        [Guis.Hist(data=histdata, title="ヒストグラフ")],
        [Guis.Stem(x=stemx1, y=stemy, title="ステムグラフ")],
        [Guis.Boxplot(data=boxdata1, title="箱ひげ図", whis=1.5)],
        [
            Guis.Waterfall(
                x=waterfallx,
                y=waterfally,
                width=0.5,
                title="ウォーターフォール",
                linestyle="dotted",
            )
        ],
        [
            Guis.Waterfallh(
                x=waterfallx, y=waterfally, height=0.5, title="ウォーターフォール"
            )
        ],
        [Guis.Step(data=stepdata, title="階段グラフ")],
        [Guis.Stack(x=stackx, y=stacky, title="積み上げグラフ")],
        [
            Guis.Eventplot(
                data=eventdata,
                linestyle="dashed",
                label=["a", "b", "c"],
                title="イベントグラフ",
            )
        ],
        [Guis.Errorbar(x=errorbarx, y=errorbary, err=err, title="エラーグラフ")],
        [
            Guis.Errorbar(
                x=errorbarx, y=errorbary, xerr=xerr, yerr=yerr, title="エラーグラフ"
            )
        ],
        [Guis.Errorbar(x=errorbarx, y=errorbary, xerr=xerr, title="エラーグラフ")],
        [Guis.Errorbar(x=errorbarx, y=errorbary, yerr=yerr, title="エラーグラフ")],
        [Guis.Ecdf(data=ecdfdata, title="経験的累積分布関数のグラフ")],
        [
            Guis.Stacked(
                data=stackeddata,
                dataname=stackeddataname,
                title="積み上げ縦棒グラフ",
            )
        ],
        [
            Guis.Stackedh(
                data=stackeddata,
                dataname=stackeddataname,
                title="積み上げ横棒グラフ",
            )
        ],
        [
            Guis.Violinplot(
                data=violindata,
                title="バイオリングラフ",
                xlabel=xlabel,
                ylabel=ylabel,
            )
        ],
        [
            Guis.Hatplot(
                x=hatplotx,
                data=hatplotdata,
                title="ハットグラフ",
                xlabel=xlabel,
                ylabel=ylabel,
                yticksrange=5,
            )
        ],
        [
            Guis.Hexbin(
                x=hexbinx1,
                y=hexbiny1,
                title="2次元六角形グラフ",
                xlabel=xlabel,
                ylabel=ylabel,
            )
        ],
        [
            Guis.Hist2d(
                x=hist2dx,
                y=hist2dy,
                title="2次元ヒストグラム",
                xlabel=xlabel,
                ylabel=ylabel,
            )
        ],
        [
            Guis.Linefill(
                x=linefillx,
                ymax=linefillymax,
                ymin=linefillymin,
                title="積上げ面グラフ",
                xlabel=xlabel,
                ylabel=ylabel,
            )
        ],
        [Guis.Funne(data=funnedata, title="じょうごグラフ")],
        [Guis.Barpolar(x=barpolarx, y=barpolary, title="極軸棒グラフ")],
        [
            Guis.Errorpolar(
                x=errorpolarx, y=errorpolary, err=polarerr, title="極軸エラーグラフ"
            )
        ],
        [
            Guis.Errorpolar(
                x=errorpolarx,
                y=errorpolary,
                xerr=polarxerr,
                yerr=polaryerr,
                title="極軸エラーグラフ",
            )
        ],
        [Guis.Eventpolar(data=eventdata, title="極軸イベントグラフ")],
        [Guis.Linepolar(x=linepolarx, y=linepolary, title="極軸折線グラフ")],
        [Guis.Scatterpolar(x=scatterpolarx, y=scatterpolary, title="極軸散布図")],
        [Guis.Stempolar(x=stempolarx, y=stempolary, title="極軸幹図")],
        [Guis.RadarFill(data=radarfilldata, title="塗りつぶしレーダーチャート")],
        [Guis.RadarLine(data=radarlinedata, title="塗りつぶし折線チャート")],
    ]
    win: WindowController = Guis.window(
        title="デモ", layout=layout, load=[progress_start], scroll=True, maxmine=True
    )
    win.run()
