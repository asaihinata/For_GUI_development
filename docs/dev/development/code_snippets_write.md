# .code-snippets ファイルの書き方まとめ

参考: [Snippets in Visual Studio Code (公式ドキュメント)](https://code.visualstudio.com/docs/editing/userdefinedsnippets)

## 1. 基本概念

`.code-snippets` は複数言語・グローバルスコープに対応した「グローバルスニペットファイル」で,JSON形式(Cスタイルコメント可)で記述します。特定言語専用の `javascript.json` のような言語別ファイルとは異なり,`scope` プロパティで対象言語を指定できます。

作成方法: **File > Preferences > Configure Snippets** から「New Global Snippets file」または「New Snippets file for '<folder-name>'...」(プロジェクト単位)を選択します。

## 2. 基本構造

```jsonc
{
  "スニペット名": {
    "prefix": ["for", "for-const"],   // 入力トリガー文字列(複数可)
    "body": [
      "for (const ${2:element} of ${1:array}) {",
      "\t$0",
      "}"
    ],
    "description": "A for loop.",     // IntelliSenseに表示される説明
    "scope": "javascript,typescript", // 対象言語(省略時は全言語)
    "isFileTemplate": false           // ファイルテンプレートとして使うか
  }
}
```

- **prefix**: 入力してスニペットを呼び出すトリガー文字列。部分一致するため,`"fc"` でも `"for-const"` にマッチ可能。
- **body**: 挿入されるコード本体。配列の場合は改行で結合される。
- **description**: 省略時はスニペット名がIntelliSenseに表示される。

## 3. スコープの指定方法

| 種類 | 説明 |
|---|---|
| **言語スコープ** | `scope` プロパティに[言語識別子](https://code.visualstudio.com/docs/languages/identifiers)(例: `python`, `javascript`)を指定。省略時は全言語で有効。 |
| **プロジェクトスコープ** | `.vscode` フォルダ内に配置し,そのプロジェクトを開いている全員と共有可能。 |
| **ファイルパターンスコープ** | `include`/`exclude` でファイルパターン(globパターン)による絞り込みが可能。両方に一致する場合は `exclude` が優先。 |

```jsonc
{
  "Test Block": {
    "prefix": "test",
    "body": ["test('${1:description}', () => {", "\t${0}", "});"],
    "scope": "typescript",
    "include": ["**/*.test.ts", "**/*.spec.ts"],
    "exclude": ["**/dist/**", "**/node_modules/**"]
  }
}
```

## 4. `body` 内で使える構文

### タブストップ

`$1`, `$2`... の順にTabキーでカーソル移動。`$0` は最終カーソル位置(常に最後)。

### プレースホルダー(デフォルト値付き)

`${1:foo}` のように書くと,`foo` が選択状態で挿入される。ネストも可能: `${1:another ${2:placeholder}}`

### 選択肢(Choice)

```
${1|one,two,three|}
```

挿入時にドロップダウンで選択できる。

### 変数

`$name` または `${name:default}` の形式。主な変数:

| カテゴリ | 変数例 |
|---|---|
| 選択・文脈 | `TM_SELECTED_TEXT`, `TM_CURRENT_LINE`, `TM_CURRENT_WORD` |
| ファイル情報 | `TM_FILENAME`, `TM_FILENAME_BASE`, `TM_DIRECTORY`, `TM_FILEPATH`, `RELATIVE_FILEPATH` |
| ワークスペース | `WORKSPACE_NAME`, `WORKSPACE_FOLDER` |
| 日時 | `CURRENT_YEAR`, `CURRENT_MONTH`, `CURRENT_DATE`, `CURRENT_HOUR` など |
| ランダム値 | `RANDOM`(6桁10進), `RANDOM_HEX`(6桁16進), `UUID` |
| コメント記法 | `BLOCK_COMMENT_START`, `BLOCK_COMMENT_END`, `LINE_COMMENT`(言語に応じて自動変換) |
| その他 | `CLIPBOARD`, `CURSOR_INDEX`, `CURSOR_NUMBER` |

### 変数変換(Variable Transform)

正規表現で変数の値を加工できます。

```
${TM_FILENAME/(.*)\..+$/$1/}
```

→ `foo.txt` から拡張子を除いた `foo` を取り出す例。

変換例(ファイル名 `example-123.456-TEST.js` に対して):

| 記述 | 結果 |
|---|---|
| `${TM_FILENAME/[\.]/_/}` | `example-123_456-TEST.js`(最初の`.`のみ置換) |
| `${TM_FILENAME/[\.-]/_/g}` | `example_123_456_TEST_js`(全置換) |
| `${TM_FILENAME/(.*)/${1:/upcase}/}` | `EXAMPLE-123.456-TEST.JS`(大文字化) |

書式変換オプション: `/upcase`, `/downcase`, `/capitalize`, `/camelcase`, `/pascalcase`, `/snakecase`, `/kebabcase`

### プレースホルダー変換

プレースホルダーにも同様の変換構文を使用でき,次のタブストップに移動する際にテキストが変換されます。

## 5. エスケープ

`\`(バックスラッシュ)で `$`, `}`, `\` をエスケープ可能。変数として解釈させたくない `$` はエスケープする必要があります。

```jsonc
{
  "VariableSnippet": {
    "prefix": "_Var",
    "body": "\\$MyVar = 2",
    "description": "$の後に変数名を続けたい場合"
  }
}
```

→ 挿入結果: `$MyVar = 2`

## 6. キーバインドへの割り当て

`keybindings.json` にスニペットをインライン指定,または既存スニペットを `langId` と `name` で参照可能。

```jsonc
{
  "key": "cmd+k 1",
  "command": "editor.action.insertSnippet",
  "when": "editorTextFocus",
  "args": {
    "langId": "python",
    "name": "myFavSnippet"
  }
}
```

---

## 付録: Python + Sphinx環境での活用例

docstringスニペットを `.code-snippets`(プロジェクト単位)に用意しておくと便利です。

```jsonc
{
  "Sphinx docstring": {
    "prefix": "docstring",
    "scope": "python",
    "body": [
      "\"\"\"${1:概要}",
      "",
      ":param ${2:name}: ${3:説明}",
      ":type ${2:name}: ${4:型}",
      ":return: ${5:戻り値の説明}",
      ":rtype: ${6:型}",
      "\"\"\"$0"
    ],
    "description": "Sphinx形式のdocstringを挿入"
  }
}
```

このようなプロジェクト用スニペットは `.vscode/*.code-snippets` に置くと,開発チーム内で共有できます。