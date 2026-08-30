# Pythonのドキュメントのテンプレートの書き方
VScodeでautoDocstringの拡張機能を使用したPython関数のドキュメント文字列を素早く生成するための機能

## カスタムドキュメント文字列テンプレート

この拡張機能はカスタムテンプレートをサポートするようになりました。この拡張機能はmustache.jsテンプレートエンジンを使用します。カスタムテンプレートを使用するには、.mustacheファイルを作成し、customTemplatePath設定でそのパスを指定します。使用例については、付属のGoogleドキュメント文字列テンプレートを参照してください。カスタムテンプレートでは、以下のタグを使用できます。
### 変数(Variables)
```
{{name}}                        - 関数名
{{summaryPlaceholder}}          - 概要のプレースホルダー
{{extendedSummaryPlaceholder}}  - 詳細な要約のプレースホルダー
```

### セクション(Sections)
```
{{#args}}                       - 関数の引数の反復処理
    {{var}}                     - 変数名
    {{typePlaceholder}}         - 引数や戻り値の型のプレースホルダ
    {{descriptionPlaceholder}}  - 説明のプレースホルダー
{{/args}}

{{#kwargs}}                     - 関数のキーワード引数の反復処理
    {{var}}                     - 変数名
    {{typePlaceholder}}         - 引数や戻り値の型のプレースホルダ
    {{&default}}                - デフォルト値(および変数のエスケープ解除)
    {{descriptionPlaceholder}}  - 説明のプレースホルダー
{{/kwargs}}

{{#exceptions}}                 - 例外の反復処理
    {{type}}                    - 例外の種類
    {{descriptionPlaceholder}}  - 説明のプレースホルダー
{{/exceptions}}

{{#yields}}                     - yield（生成された値）を順に処理する
    {{typePlaceholder}}         - 引数や戻り値の型のプレースホルダ
    {{descriptionPlaceholder}}  - 説明のプレースホルダー
{{/yields}}

{{#returns}}                    - 戻り値
    {{typePlaceholder}}         - 引数や戻り値の型のプレースホルダ
    {{descriptionPlaceholder}}  - 説明のプレースホルダー
{{/returns}}
```

### 追加セクション(Additional Sections)
```
{{#argsExist}}          - 引数が存在する場合、内容を表示する
{{/argsExist}}

{{#kwargsExist}}        - kwargs が存在する場合にコンテンツを表示
{{/kwargsExist}}

{{#parametersExist}}    - args または kwargs が存在する場合にコンテンツを表示
{{/parametersExist}}

{{#exceptionsExist}}    - 例外が存在する場合にコンテンツを表示
{{/exceptionsExist}}

{{#yieldsExist}}        - 戻り値（yield）が存在する場合にコンテンツを表示
{{/yieldsExist}}

{{#returnsExist}}       - 戻り値（return）が存在する場合にコンテンツを表示
{{/returnsExist}}

{{#placeholder}}        - コンテンツをプレースホルダーにする
{{/placeholder}}
```

(引用)[https://open-vsx.org/extension/njpwerner/autodocstring]