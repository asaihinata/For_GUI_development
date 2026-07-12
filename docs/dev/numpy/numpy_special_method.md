# numpy配列で使用できる特殊メソッド一覧

## 1. Python標準の特殊メソッド(numpyでオーバーライドされているもの)

### 算術演算子

| メソッド名      | numpyで対応する関数            | メソッドの実行内容                            |
| --------------- | ------------------------------ | --------------------------------------------- |
| `__add__`       | `np.add`                       | 加算 `a + b` を実行する                       |
| `__radd__`      | `np.add`                       | 右辺加算(左辺がndarrayでない場合)を実行する   |
| `__iadd__`      | `np.add(out=a)`                | 加算結果をその場(in-place)で代入する `a += b` |
| `__sub__`       | `np.subtract`                  | 減算 `a - b` を実行する                       |
| `__rsub__`      | `np.subtract`                  | 右辺減算 `b - a` を実行する                   |
| `__isub__`      | `np.subtract(out=a)`           | 減算結果をその場で代入する `a -= b`           |
| `__mul__`       | `np.multiply`                  | 乗算 `a * b` を実行する                       |
| `__rmul__`      | `np.multiply`                  | 右辺乗算を実行する                            |
| `__imul__`      | `np.multiply(out=a)`           | 乗算結果をその場で代入する `a *= b`           |
| `__truediv__`   | `np.true_divide` / `np.divide` | 除算 `a / b` を実行する                       |
| `__rtruediv__`  | `np.true_divide`               | 右辺除算を実行する                            |
| `__itruediv__`  | `np.true_divide(out=a)`        | 除算結果をその場で代入する `a /= b`           |
| `__floordiv__`  | `np.floor_divide`              | 切り捨て除算 `a // b` を実行する              |
| `__rfloordiv__` | `np.floor_divide`              | 右辺切り捨て除算を実行する                    |
| `__ifloordiv__` | `np.floor_divide(out=a)`       | 切り捨て除算結果をその場で代入する `a //= b`  |
| `__mod__`       | `np.mod` / `np.remainder`      | 剰余 `a % b` を計算する                       |
| `__rmod__`      | `np.mod`                       | 右辺剰余を計算する                            |
| `__imod__`      | `np.mod(out=a)`                | 剰余結果をその場で代入する `a %= b`           |
| `__pow__`       | `np.power`                     | べき乗 `a ** b` を計算する                    |
| `__rpow__`      | `np.power`                     | 右辺べき乗を計算する                          |
| `__ipow__`      | `np.power(out=a)`              | べき乗結果をその場で代入する `a **= b`        |
| `__matmul__`    | `np.matmul`                    | 行列積 `a @ b` を計算する                     |
| `__rmatmul__`   | `np.matmul`                    | 右辺行列積を計算する                          |
| `__imatmul__`   | `np.matmul(out=a)`             | 行列積結果をその場で代入する `a @= b`         |
| `__divmod__`    | `np.divmod`                    | 商と剰余を同時に計算する `divmod(a, b)`       |
| `__neg__`       | `np.negative`                  | 符号反転 `-a` を計算する                      |
| `__pos__`       | `np.positive`                  | 単項プラス `+a` を返す                        |
| `__abs__`       | `np.abs` / `np.absolute`       | 絶対値 `abs(a)` を計算する                    |

### ビット演算子

| メソッド名    | numpyで対応する関数            | メソッドの実行内容                   |
| ------------- | ------------------------------ | ------------------------------------ |
| `__and__`     | `np.bitwise_and`               | ビットAND `a & b` を計算する         |
| `__rand__`    | `np.bitwise_and`               | 右辺ビットANDを計算する              |
| `__iand__`    | `np.bitwise_and(out=a)`        | ビットANDをその場で代入する `a &= b` |
| `__or__`      | `np.bitwise_or`                | ビットOR `a \| b` を計算する         |
| `__ror__`     | `np.bitwise_or`                | 右辺ビットORを計算する               |
| `__ior__`     | `np.bitwise_or(out=a)`         | ビットORをその場で代入する `a \|= b` |
| `__xor__`     | `np.bitwise_xor`               | ビットXOR `a ^ b` を計算する         |
| `__rxor__`    | `np.bitwise_xor`               | 右辺ビットXORを計算する              |
| `__ixor__`    | `np.bitwise_xor(out=a)`        | ビットXORをその場で代入する `a ^= b` |
| `__invert__`  | `np.invert` / `np.bitwise_not` | ビット反転 `~a` を計算する           |
| `__lshift__`  | `np.left_shift`                | 左シフト `a << b` を計算する         |
| `__rlshift__` | `np.left_shift`                | 右辺左シフトを計算する               |
| `__ilshift__` | `np.left_shift(out=a)`         | 左シフトをその場で代入する `a <<= b` |
| `__rshift__`  | `np.right_shift`               | 右シフト `a >> b` を計算する         |
| `__rrshift__` | `np.right_shift`               | 右辺右シフトを計算する               |
| `__irshift__` | `np.right_shift(out=a)`        | 右シフトをその場で代入する `a >>= b` |

### 比較演算子

| メソッド名 | numpyで対応する関数 | メソッドの実行内容                   |
| ---------- | ------------------- | ------------------------------------ |
| `__eq__`   | `np.equal`          | 要素ごとの等価比較 `a == b` を行う   |
| `__ne__`   | `np.not_equal`      | 要素ごとの非等価比較 `a != b` を行う |
| `__lt__`   | `np.less`           | 要素ごとの未満比較 `a < b` を行う    |
| `__le__`   | `np.less_equal`     | 要素ごとの以下比較 `a <= b` を行う   |
| `__gt__`   | `np.greater`        | 要素ごとの超過比較 `a > b` を行う    |
| `__ge__`   | `np.greater_equal`  | 要素ごとの以上比較 `a >= b` を行う   |

### 型変換・コンテナ系

| メソッド名     | numpyで対応する関数 | メソッドの実行内容                                        |
| -------------- | ------------------- | --------------------------------------------------------- |
| `__len__`      | なし                | 先頭軸(axis=0)の要素数を返す                              |
| `__getitem__`  | なし                | インデックスやスライスによる要素・部分配列の取得を行う    |
| `__setitem__`  | なし                | インデックスやスライスを指定して値を代入する              |
| `__iter__`     | なし                | 先頭軸に沿ったイテレータを返す                            |
| `__contains__` | なし                | 値が配列内に存在するか判定する `x in a`                   |
| `__bool__`     | なし                | 要素数が1の配列を真偽値に変換する(複数要素だとValueError) |
| `__int__`      | なし                | 要素数が1の配列を`int`に変換する                          |
| `__float__`    | なし                | 要素数が1の配列を`float`に変換する                        |
| `__index__`    | なし                | 整数インデックスとして使用可能な整数値を返す              |
| `__repr__`     | なし                | `repr(a)` 用の文字列表現を返す                            |
| `__str__`      | なし                | `str(a)` 用の文字列表現を返す                             |
| `__copy__`     | `np.copy`           | 浅いコピーを返す(`copy.copy`から呼ばれる)                 |
| `__deepcopy__` | なし                | 深いコピーを返す(`copy.deepcopy`から呼ばれる)             |
| `__reduce__`   | なし                | pickle化のための再構築情報を返す                          |

---

## 2. numpy専用の特殊メソッド(プロトコル)

| メソッド名            | numpyで対応する関数                                  | メソッドの実行内容                                                                                     |
| --------------------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `__array__`           | `np.array` / `np.asarray`                            | オブジェクトをndarrayに変換する際に呼び出され、変換後の配列を返す                                      |
| `__array_ufunc__`     | ufunc全般(`np.add`, `np.exp`など)                    | ufuncが自身のインスタンスに適用された際の挙動をカスタマイズする                                        |
| `__array_function__`  | ufunc以外のnumpy関数(`np.sum`, `np.concatenate`など) | numpyの高水準関数が呼ばれた際の挙動をカスタマイズする                                                  |
| `__array_wrap__`      | ufunc全般                                            | ufuncの計算結果を、元のサブクラスの型に包み直す(post-process)                                          |
| `__array_prepare__`   | ufunc全般(廃止予定)                                  | ufuncの計算前に出力配列を準備する(`__array_wrap__`に統合されつつある)                                  |
| `__array_finalize__`  | なし(`view`,`__new__`,`slice`等から自動呼出)         | ndarrayサブクラスの新規生成・ビュー生成・テンプレートコピー時に属性を引き継ぐ                          |
| `__array_interface__` | `np.asarray`等                                       | 配列プロトコル(shape, dtype, dataポインタ等)を辞書形式で提供する                                       |
| `__array_struct__`    | `np.asarray`等                                       | Cレベルの配列インターフェース(`PyArrayInterface`構造体)を提供する                                      |
| `__array_priority__`  | 二項演算全般                                         | 異なるndarrayサブクラス同士の演算時、どちらの`__array_ufunc__`等を優先するかを決定する優先度を指定する |

---

### 補足
- `__array_ufunc__`を`None`に設定すると、そのクラスに対するufunc適用を明示的に無効化できる。
- `__array_function__`はNEP 18で導入されたプロトコルで、`np.sum`や`np.reshape`のようなufunc以外の関数をサブクラス向けにオーバーライドする際に使用する。
- `__array_priority__`は新しいコードでは`__array_ufunc__`によるディスパッチに置き換えられつつある。