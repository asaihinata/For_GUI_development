********
numpy用語集
********



(`n`,)
    括弧で囲まれた数字の後にカンマが続く場合、要素数1のタプルを表す。
    末尾のカンマによって、要素数1のタプルと単に括弧で囲まれた ``n`` とを区別している。


-1
    - **次元(dimension)の指定において**、NumPyに対して「配列全体の要素数が変わらないように」
      その次元の長さを自動的に決定させることを意味する。

        >>> np.arange(12).reshape(4, -1).shape
        (4, 3)

    - **インデックスにおいて**、負の値は
      `右側からのインデックス <https://docs.python.org/dev/faq/programming.html#what-s-a-negative-index>`_
      を意味する。

. . .
    :py:data:`Ellipsis` (省略記号)。

    - **配列のインデックス参照時**には、存在する場合、省略された軸がすべて全体スライス
      (full slice)であることを示す省略表記。

        >>> a = np.arange(24).reshape(2,3,4)

        >>> a[...].shape
        (2, 3, 4)


        >>> a[...,0].shape
        (2, 3)

        >>> a[0,...].shape
        (3, 4)

        >>> a[0,...,0].shape
        (3,)

      1つのインデックス式の中で使用できるのは最大1回まで。``a[...,0,...]`` は
      :exc:`IndexError` を送出する。

    - **表示(printout)において**、NumPyは大きな配列の中間の要素を ``...`` に置き換えて
      表示する。配列全体を表示したい場合は `numpy.printoptions` を使用する。


:
    Python の :term:`python:slice` 演算子。ndarray においては、スライスは
    すべての軸に対して適用できる。

        >>> a = np.arange(24).reshape(2,3,4)
        >>> a
        array([[[ 0,  1,  2,  3],
                [ 4,  5,  6,  7],
                [ 8,  9, 10, 11]],
        <BLANKLINE>
               [[12, 13, 14, 15],
                [16, 17, 18, 19],
                [20, 21, 22, 23]]])
        <BLANKLINE>
        >>> a[1:,-2:,:-1]
        array([[[16, 17, 18],
                [20, 21, 22]]])

    末尾のスライスは省略できる。 ::

        >>> a[1] == a[1,:,:]
        array([[ True,  True,  True,  True],
               [ True,  True,  True,  True],
               [ True,  True,  True,  True]])

    Pythonではスライスがコピーを作るのに対し、NumPyのスライスは
    :term:`view`(ビュー)を作る点が異なる。

    詳細は :ref:`combining-advanced-and-basic-indexing` を参照。


<
    dtype 宣言において、データが :term:`little-endian`(リトルエンディアン)
    であることを示す(括弧が右側で大きくなる形)。 ::

        >>> dt = np.dtype('<f')  # リトルエンディアンの単精度浮動小数点数


>
    dtype 宣言において、データが :term:`big-endian`(ビッグエンディアン)
    であることを示す(括弧が左側で大きくなる形)。 ::

        >>> dt = np.dtype('>H')  # ビッグエンディアンの符号なしshort


advanced indexing(高度なインデックス参照)
    :doc:`スカラー <reference/arrays.scalars>` やスライスをインデックスとして使う代わりに、
    軸を配列でインデックス参照することで、きめ細かい要素選択が可能になる。これを
    :ref:`高度なインデックス参照(advanced indexing)<advanced-indexing>` または
    「ファンシーインデックス参照(fancy indexing)」と呼ぶ。


along an axis(軸に沿って)
    配列 ``a`` の「軸 n に沿った」操作は、その引数が軸 `n` の連続したインデックスを持つ
    ``a`` のスライスの配列であるかのように振る舞う。

    例えば、``a`` が 3 x `N` の配列であれば、軸0に沿った操作は、その引数が各行の
    スライスを含む配列であるかのように振る舞う。

        >>> np.array((a[0,:], a[1,:], a[2,:])) #doctest: +SKIP

    具体的に示すため、``axis`` 引数を受け取る配列反転関数 :func:`numpy.flip` を
    例にとる。3 x 4 の配列 ``a`` を作成する。

        >>> a = np.arange(12).reshape(3,4)
        >>> a
        array([[ 0,  1,  2,  3],
               [ 4,  5,  6,  7],
               [ 8,  9, 10, 11]])

    軸0(行の軸)に沿って反転すると次のようになる。

        >>> np.flip(a,axis=0)
        array([[ 8,  9, 10, 11],
               [ 4,  5,  6,  7],
               [ 0,  1,  2,  3]])

    「軸に沿って」の定義を思い出すと、軸0に沿った ``flip`` は、その引数を
    以下であるかのように扱っている。

        >>> np.array((a[0,:], a[1,:], a[2,:]))
        array([[ 0,  1,  2,  3],
               [ 4,  5,  6,  7],
               [ 8,  9, 10, 11]])

    そして ``np.flip(a,axis=0)`` の結果は、このスライスを反転したものになる。

        >>> np.array((a[2,:],a[1,:],a[0,:]))
        array([[ 8,  9, 10, 11],
               [ 4,  5,  6,  7],
               [ 0,  1,  2,  3]])


array(配列)
    NumPyのドキュメントでは :term:`ndarray` と同義で使われる。


array_like(array_like型)
    ndarray として解釈できる任意の :doc:`スカラー <reference/arrays.scalars>` や
    :term:`python:sequence`(シーケンス)。ndarray やスカラーに加えて、リスト
    (ネストしていてもよく、要素の型が異なっていてもよい)やタプルもこのカテゴリに含まれる。
    :doc:`numpy.array <reference/generated/numpy.array>` が受け付ける引数は
    すべて array_like である。 ::

        >>> a = np.array([[1, 2.0], [0, 0], (1+1j, 3.)])

        >>> a
        array([[1.+0.j, 2.+0.j],
               [0.+0.j, 0.+0.j],
               [1.+1.j, 3.+0.j]])


array scalar(配列スカラー)
    :doc:`配列スカラー <reference/arrays.scalars>` とは、float32、float64などの
    型/クラスのインスタンスである。オペランドの扱いを統一するため、NumPyは
    スカラーを0次元の配列として扱う。対照的に、0次元配列は正確に1つの値を
    含む :doc:`ndarray <reference/arrays.ndarray>` のインスタンスである。


axis(軸)
    配列の次元(dimension)を表す別の用語。軸は左から右に番号が振られ、
    軸0は shape タプルの最初の要素である。

    2次元のベクトルでは、軸0の要素は行(row)、軸1の要素は列(column)である。

    次元がさらに高くなると、様子が変わる。NumPyは高次元のベクトルを、
    行×列の構成ブロックの繰り返しとして表示する。以下は3次元ベクトルの例である。

        >>> a = np.arange(12).reshape(2,2,3)
        >>> a
        array([[[ 0,  1,  2],
                [ 3,  4,  5]],
               [[ 6,  7,  8],
                [ 9, 10, 11]]])

    ``a`` は、2x3のベクトルを要素とする2要素の配列として表現されている。
    この観点から見ると、行と列は、どの shape においても常に最後の2つの軸である。

    このルールを知っておくと、ベクトルがどのように表示されるかを予測しやすくなり、
    逆に表示された要素のインデックスを見つける手がかりにもなる。例えば上の例では、
    8のインデックスの末尾2つの値は0と1でなければならない。8は2つある2x3の
    2番目に現れているので、最初のインデックスは1になるはずである。

        >>> a[1,0,2]
        8

    表示されたベクトルの次元数を数える簡便な方法は、開き括弧の後に続く ``[``
    記号の数を数えることである。これは例えば (1,2,3) の shape と (2,3) の
    shape を区別するのに役立つ。

        >>> a = np.arange(6).reshape(2,3)
        >>> a.ndim
        2
        >>> a
        array([[0, 1, 2],
               [3, 4, 5]])

        >>> a = np.arange(6).reshape(1,2,3)
        >>> a.ndim
        3
        >>> a
        array([[[0, 1, 2],
                [3, 4, 5]]])


.base

    配列が自身のメモリを所有していない場合、その
    :doc:`base <reference/generated/numpy.ndarray.base>` 属性は、その配列が
    参照しているメモリを持つオブジェクトを返す。そのオブジェクト自体がさらに別の
    オブジェクトのメモリを参照している場合もあるため、所有元のオブジェクトは
    ``a.base.base.base...`` のようになることもある。``base`` を調べれば配列が
    :term:`view`(ビュー)かどうか判定できると誤って主張する文献もあるが、
    正しい判定方法については :func:`numpy.shares_memory` を参照のこと。


big-endian(ビッグエンディアン)
    `エンディアン(Endianness) <https://en.wikipedia.org/wiki/Endianness>`_ を参照。


BLAS
    `Basic Linear Algebra Subprograms(基本線形代数サブプログラム) <https://en.wikipedia.org/wiki/Basic_Linear_Algebra_Subprograms>`_


broadcast(ブロードキャスト)
    *broadcasting(ブロードキャスティング)* とは、サイズの異なる ndarray を、
    あたかもすべて同じサイズであるかのように処理できるNumPyの機能である。

    これにより、例えばスカラーとベクトルを足すと、そのスカラー値がすべての要素に
    加算される、という「意図をくみ取った」挙動が実現される。

        >>> a = np.arange(3)
        >>> a
        array([0, 1, 2])

        >>> a + [3, 3, 3]
        array([3, 4, 5])

        >>> a + 3
        array([3, 4, 5])

    通常、ベクトルのオペランドはすべて同じサイズでなければならない。なぜなら
    NumPyは要素ごとに処理するからである。例えば ``c = a * b`` は次のように
    実行される。 ::

        c[0,0,0] = a[0,0,0] * b[0,0,0]
        c[0,0,1] = a[0,0,1] * b[0,0,1]
       ...

    しかし、ある種の有用なケースでは、NumPyは「欠けている」軸や「短すぎる」次元に
    沿ってデータを複製し、shapeを一致させることができる。この複製にメモリや
    時間のコストはかからない。詳細は
    :doc:`ブロードキャスティング。 <user/basics.broadcasting>` を参照。


C order(C順序)
    :term:`row-major`(行優先)と同じ。

casting(キャスト)
    配列のデータをあるdtypeから別のdtypeへ変換する処理。以下のキャストルールで
    定義される、いくつかのキャストモードが存在する。

    - ``no``: データ型は一切キャストされない。配列間でデータ型に不一致があれば
      `TypeError` が送出される。
    - ``equiv``: バイトオーダーの変更のみが許可される。
    - ``safe``: 値を保持できるキャストのみが許可される。アップキャスト
      (例: intからfloat)は許可されるが、ダウンキャストは許可されない。
    - ``same_kind``: 'same_kind' キャストオプションは、safeキャストに加えて、
      float64からfloat32のような同種内でのキャストを許可する。
    - ``unsafe``: 任意のデータ変換が許可される。

column-major(列優先)
    `行優先・列優先の順序(Row- and column-major order) <https://en.wikipedia.org/wiki/Row-_and_column-major_order>`_ を参照。


contiguous(連続)

    以下を満たす場合、配列は連続(contiguous)であるという。

    - 途切れのない1つのメモリブロックを占有していること
    - より大きいインデックスを持つ配列要素が、より大きいアドレスを占有していること
      (すなわち、:term:`stride`(ストライド)が負でないこと)

    適切に連続しているNumPy配列には2種類ある。

    - Fortran連続(Fortran-contiguous)配列は、列方向に格納されたデータを指す。
      すなわち、メモリに格納されたデータのインデックス付けは、最も低い次元から
      始まる。
    - C連続(C-contiguous)配列、または単に連続(contiguous)配列は、行方向に
      格納されたデータを指す。すなわち、メモリに格納されたデータのインデックス
      付けは、最も高い次元から始まる。

    1次元配列では、この2つの概念は一致する。

    例えば、2x2の配列 ``A`` は、その要素が以下の順序でメモリに格納されている
    場合にFortran連続である。 ::

        A[0,0] A[1,0] A[0,1] A[1,1]

    以下の順序であればC連続である。 ::

        A[0,0] A[0,1] A[1,0] A[1,1]

    配列がC連続かどうかを調べるには、NumPy配列の ``.flags.c_contiguous``
    属性を使用する。Fortran連続かどうかを調べるには、``.flags.f_contiguous``
    属性を使用する。


copy(コピー)
    :term:`view` を参照。


dimension(次元)
    :term:`axis` を参照。


dtype
    ndarray内の(すべて同じ型の)要素を記述するデータ型。配列の内容を再解釈するために
    変更することができる。詳細は
    :doc:`データ型オブジェクト(dtype)。 <reference/arrays.dtypes>` を参照。


fancy indexing(ファンシーインデックス参照)
    :term:`advanced indexing` の別名。


field(フィールド)
    :term:`structured data type`(構造化データ型)において、各サブタイプは
    `field`(フィールド)と呼ばれる。`field` には名前(文字列)、型(任意の有効な
    dtype)、および任意で `title`(タイトル)がある。:ref:`arrays.dtypes` を参照。


Fortran order(Fortran順序)
    :term:`column-major`(列優先)と同じ。


flattened(平坦化された)
    :term:`ravel` を参照。


homogeneous(均質)
    均質な配列のすべての要素は同じ型を持つ。ndarrayは、Pythonのリストとは対照的に
    均質である。この型は :term:`structured array`(構造化配列)のように複雑な
    場合もあるが、すべての要素はその型を持つ。

    Pythonオブジェクトへの参照を含む NumPy の
    `オブジェクト配列(object arrays) <#term-object-array>`_ は、
    異種混在配列(heterogeneous array)の役割を果たす。


itemsize
    dtypeの要素のバイト単位でのサイズ。


little-endian(リトルエンディアン)
    `エンディアン(Endianness) <https://en.wikipedia.org/wiki/Endianness>`_ を参照。


mask(マスク)
    ある演算のために特定の要素だけを選択するために使われるブール配列。

        >>> x = np.arange(5)
        >>> x
        array([0, 1, 2, 3, 4])

        >>> mask = (x > 2)
        >>> mask
        array([False, False, False, True,  True])

        >>> x[mask] = -1
        >>> x
        array([ 0,  1,  2,  -1, -1])


masked array(マスク配列)
    不正なデータや欠損データは、マスク配列に格納することでクリーンに無視できる。
    マスク配列は、無効なエントリを示す内部的なブール配列を持つ。マスク配列を用いた
    演算では、これらのエントリは無視される。 ::

      >>> a = np.ma.masked_array([np.nan, 2, np.nan], [True, False, True])
      >>> a
      masked_array(data=[--, 2.0, --],
                   mask=[ True, False,  True],
             fill_value=1e+20)

      >>> a + [1, 2, 3]
      masked_array(data=[--, 4.0, --],
                   mask=[ True, False,  True],
             fill_value=1e+20)

    詳細は :doc:`マスク配列。 <reference/maskedarray>` を参照。


matrix(行列)
    NumPyの2次元 :doc:`matrix クラス <reference/generated/numpy.matrix>` は
    もはや使用すべきではない。通常の ndarray を使用すること。


ndarray
   :doc:`NumPyの基本構造 <reference/arrays>`。


object array(オブジェクト配列)
    dtype が ``object`` である配列。すなわち、Pythonオブジェクトへの参照を
    含む配列。この配列のインデックス参照はPythonオブジェクトを間接参照(dereference)
    するため、他のndarrayとは異なり、オブジェクト配列は異種混在オブジェクトを
    保持できる。


ravel(平坦化)
    :doc:`numpy.ravel \
    <reference/generated/numpy.ravel>` と
    :doc:`numpy.flatten \
    <reference/generated/numpy.ndarray.flatten>` は、どちらもndarrayを
    平坦化する。``ravel`` は可能であればビューを返し、``flatten`` は常に
    コピーを返す。

    平坦化(Flattening)は、多次元配列を1次元に折りたたむ操作である。この処理の
    詳細(例えば ``a[n+1]`` が次の行になるべきか、次の列になるべきか)は
    パラメータで決まる。


record array(レコード配列)
    ``a['field']`` に加えて、属性形式(``a.field``)でのアクセスを許可する
    :term:`structured array`(構造化配列)。詳細は
    :doc:`numpy.recarray。 <reference/generated/numpy.recarray>` を参照。


row-major(行優先)
    `行優先・列優先の順序(Row- and column-major order) <https://en.wikipedia.org/wiki/Row-_and_column-major_order>`_ を参照。
    NumPyはデフォルトで行優先の順序で配列を作成する。


scalar(スカラー)
    NumPyでは、通常 :term:`array scalar`(配列スカラー)の同義語として使われる。


shape
    ndarrayの各次元の長さを示すタプル。このタプル自体の長さが次元数
    (:doc:`numpy.ndim <reference/generated/numpy.ndarray.ndim>`)である。
    タプルの要素の積が配列内の要素数である。詳細は
    :doc:`numpy.ndarray.shape <reference/generated/numpy.ndarray.shape>` を参照。


stride(ストライド)
    物理メモリは1次元であるため、ストライドは特定のインデックスをメモリ上の
    アドレスに対応付ける仕組みを提供する。N次元配列の場合、その ``strides``
    属性はN要素のタプルであり、軸 ``n`` でインデックス ``i`` から ``i+1``
    へ進むことは、アドレスに ``a.strides[n]`` バイトを加算することを意味する。

    ストライドは配列のdtypeとshapeから自動的に計算されるが、
    :doc:`as_strided <reference/generated/numpy.lib.stride_tricks.as_strided>`
    を使って直接指定することもできる。境界検証(bounds validation)は
    ``check_bounds`` パラメータで有効にできる。

    詳細は
    :doc:`numpy.ndarray.strides <reference/generated/numpy.ndarray.strides>` を参照。

    ストライドがNumPyのビューの強力さをどのように支えているかについては、
    `NumPy配列:効率的な数値計算のための構造。 \
    <https://arxiv.org/pdf/1102.1523.pdf>`_ を参照。


structured array(構造化配列)
    :term:`dtype` が :term:`structured data type`(構造化データ型)である配列。


structured data type(構造化データ型)
    ユーザーは、他の配列やdtypeを含む、任意に複雑な :term:`dtypes <dtype>`
    (データ型)を作成できる。このような複合的なdtypeは
    :doc:`構造化データ型。 <user/basics.rec>` と呼ばれる。


subarray(サブ配列)
   :term:`structured data type`(構造化データ型)の中にネストされた配列。
   以下の例における ``b`` がそれにあたる。

     >>> dt = np.dtype([('a', np.int32), ('b', np.float32, (3,))])
     >>> np.zeros(3, dtype=dt)
     array([(0, [0., 0., 0.]), (0, [0., 0., 0.]), (0, [0., 0., 0.])],
           dtype=[('a', '<i4'), ('b', '<f4', (3,))])


subarray data type(サブ配列データ型)
    ndarrayのように振る舞う、構造化データ型の要素。


title(タイトル)
    構造化データ型におけるフィールド名の別名(エイリアス)。


type(型)
    NumPyでは、通常 :term:`dtype` の同義語として使われる。より一般的な
    Pythonでの意味については :term:`こちらを参照。 <python:type>`


ufunc
    NumPyの高速な要素ごとの計算(:term:`vectorization`、ベクトル化)では、
    どの関数を適用するかを選択できる。この関数を表す一般的な用語が ``ufunc``
    であり、``universal function``(汎用関数)の略である。NumPyのルーチンには
    組み込みのufuncがあるが、ユーザーは
    :doc:`自分でufuncを書くこともできる。 <reference/ufuncs>`


vectorization(ベクトル化)
    NumPyは配列処理をCに委譲するため、ループや計算がPythonよりもはるかに
    高速になる。これを活用するため、NumPyを使うプログラマーはPythonの
    ループを排除し、配列同士の演算に置き換える。:term:`vectorization`
    (ベクトル化)は、このCへの処理委譲そのものを指す場合もあれば、それを
    活かすようにNumPyのコードを構成することを指す場合もある。

view(ビュー)
    元となるデータに手を加えることなく、NumPyはある配列のデータ型や
    shapeを変化させたように見せることができる。

    このようにして作られた配列を `view`(ビュー)と呼び、NumPyは新しい配列を
    作る代わりにビューを使うことによる性能上の恩恵をしばしば活用している。

    潜在的な欠点として、ビューへの書き込みは元の配列も変更してしまう
    可能性があるという点が挙げられる。これが問題になる場合は、物理的に
    独立した配列、すなわち `copy`(コピー)を作成する必要がある。

    一部のNumPyルーチンは常にビューを返し、一部は常にコピーを返し、一部は
    どちらを返すか選べず、一部は選択を指定できる。ビューとコピーの管理責任は
    プログラマーにある。``b`` が ``a`` のビューであるかどうかは
    :func:`numpy.shares_memory` で確認できるが、ドキュメントページで
    説明されているとおり、常に厳密な答えが得られるとは限らない。

      >>> x = np.arange(5)
      >>> x
      array([0, 1, 2, 3, 4])

      >>> y = x[::2]
      >>> y
      array([0, 2, 4])

      >>> x[0] = 3 # xを変更するとyも変更される。yはxのビューであるため
      >>> y
      array([3, 2, 4])