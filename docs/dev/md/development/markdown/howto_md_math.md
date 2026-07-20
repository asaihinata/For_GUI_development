# Markdownで数式の書き方
Markdownは,LaTeXを使用して数式を埋め込むことができ技術文書,学術論文,教材に専門的な数学表現機能を提供します。

## 基本的なLaTeX数式構文
```$```で囲むと数式が表示できる。
```
$4+2=6$
$a \times b = ab$
二次方程式の解:$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$
```
$4+2=6$
$a \times b = ab$
二次方程式の解:$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$

## ブロック数式
ブロック数式は二重のドル記号`$$`で数式を囲み,別の中央行に表示する。
```
$$\int_{-\infty}^{\infty}e^{-x^2}dx$$
$$\sum_{n=1}^{\infty}\frac{1}{n^2}$$
$$\lim_{x\to0}\frac{\sin x}{x}$$
```
$$\int_{-\infty}^{\infty}e^{-x^2}dx$$
$$\sum_{n=1}^{\infty}\frac{1}{n^2}$$
$$\lim_{x\to0}\frac{\sin x}{x}$$
## 基本的な数学要素
### 四則演算
| 項目           | 表示         | コード             |
| -------------- | ------------ | ------------------ |
| 足し算（加算） | $a+b$        | ```$a+b$```        |
| 引き算         | $a-b$        | ```$a-b$```        |
| 掛け算         | $a \times b$ | ```$a \times b$``` |
| 割り算         | $a \div b$   | ```$a \div b$```   |
### 上付き文字と下付き文字
```
上付き文字
$x^2$,$e^{i\pi}$,$2^{10}$
下付き文字
$x_1$,$a_{ij}$,$\log_2 n$
組み合わせ
$x_1^2$,$a_{i,j}^{(k)}$,$\sum_{i=1}^n x_i^2$
```
上付き文字
$x^2$,$e^{i\pi}$,$2^{10}$
下付き文字
$x_1$,$a_{ij}$,$\log_2 n$
組み合わせ
$x_1^2$,$a_{i,j}^{(k)}$,$\sum_{i=1}^n x_i^2$
### 分数
```
基本的な分数
$\frac{1}{2}$,$\frac{a}{b}$,$\frac{x+y}{x-y}$
連分数
$\frac{1}{1+\frac{1}{2+\frac{1}{3+\cdots}}}$
複雑な分数
$\frac{\partial^2 f}{\partial x^2}$,$\frac{d}{dx}\left(\frac{1}{x}\right)$
```
基本的な分数
$\frac{1}{2}$,$\frac{a}{b}$,$\frac{x+y}{x-y}$
連分数
$\frac{1}{1+\frac{1}{2+\frac{1}{3+\cdots}}}$
複雑な分数
$\frac{\partial^2 f}{\partial x^2}$,$\frac{d}{dx}\left(\frac{1}{x}\right)$
### 平方根
```
平方根
$\sqrt{2}$,$\sqrt{x^2+y^2}$
n乗根
$\sqrt[3]{8}$,$\sqrt[n]{x}$
複雑な根
$\sqrt{\frac{a}{b}}$,$\sqrt{1+\sqrt{1+\sqrt{1+\cdots}}}$
```
平方根
$\sqrt{2}$,$\sqrt{x^2+y^2}$
n乗根
$\sqrt[3]{8}$,$\sqrt[n]{x}$
複雑な根
$\sqrt{\frac{a}{b}}$,$\sqrt{1+\sqrt{1+\sqrt{1+\cdots}}}$
### 記号と演算子
```
小文字のギリシャ文字
$\alpha$,$\beta$,$\gamma$,$\delta$,$\epsilon$,$\zeta$,$\eta$,$\theta$
$\iota$,$\kappa$,$\lambda$,$\mu$,$\nu$,$\xi$,$\pi$,$\rho$
$\sigma$,$\tau$,$\upsilon$,$\phi$,$\chi$,$\psi$,$\omega$
大文字のギリシャ文字
$\Alpha$,$\Beta$,$\Gamma$,$\Delta$,$\Epsilon$,$\Zeta$,$\Eta$,$\Theta$
$\Lambda$,$\Xi$,$\Pi$,$\Sigma$,$\Phi$,$\Psi$,$\Omega$
```
小文字のギリシャ文字
$\alpha$,$\beta$,$\gamma$,$\delta$,$\epsilon$,$\zeta$,$\eta$,$\theta$
$\iota$,$\kappa$,$\lambda$,$\mu$,$\nu$,$\xi$,$\pi$,$\rho$
$\sigma$,$\tau$,$\upsilon$,$\phi$,$\chi$,$\psi$,$\omega$
大文字のギリシャ文字
$\Alpha$,$\Beta$,$\Gamma$,$\Delta$,$\Epsilon$,$\Zeta$,$\Eta$,$\Theta$
$\Lambda$,$\Xi$,$\Pi$,$\Sigma$,$\Phi$,$\Psi$,$\Omega$
```
基本的な演算
$+$,$-$,$\times$,$\div$,$\pm$,$\mp$
関係演算
$=$,$\neq$,$<$,$>$,$\leq$,$\geq$,$\ll$,$\gg$
論理演算
$\land$,$\lor$,$\lnot$,$\implies$,$\iff$
集合演算
$\in$,$\notin$,$\subset$,$\supset$,$\cup$,$\cap$,$\emptyset$
その他の記号
$\infty$,$\partial$,$\nabla$,$\propto$,$\approx$,$\equiv$
```
基本的な演算
$+$,$-$,$\times$,$\div$,$\pm$,$\mp$
関係演算
$=$,$\neq$,$<$,$>$,$\leq$,$\geq$,$\ll$,$\gg$
論理演算
$\land$,$\lor$,$\lnot$,$\implies$,$\iff$
集合演算
$\in$,$\notin$,$\subset$,$\supset$,$\cup$,$\cap$,$\emptyset$
その他の記号
$\infty$,$\partial$,$\nabla$,$\propto$,$\approx$,$\equiv$
### 高度な数学構造
```
総和
$$\sum_{i=1}^{n}i$$
$$\sum_{k=0}^{\infty}\frac{x^k}{k!}$$
積分
$$\int_a^b f(x)dx$$
$$\oint_C \mathbf{F} \cdot d\mathbf{r}$$
$$\iint_D f(x,y) \,dx \,dy$$
$$\iiint_V f(x,y,z)\,dx\,dy \,dz$$
極限
$$\lim_{n \to \infty} \left(1+\frac{1}{n}\right)^n$$
$$\lim_{x \to 0^+} \frac{1}{x}$$
```
総和
$$\sum_{i=1}^{n} i$$
$$\sum_{k=0}^{\infty} \frac{x^k}{k!}$$
積分
$$\int_a^b f(x) dx$$
$$\oint_C \mathbf{F} \cdot d\mathbf{r}$$
$$\iint_D f(x,y) \,dx \,dy$$
$$\iiint_V f(x,y,z) \,dx \,dy \,dz$$
極限
$$\lim_{n \to \infty} \left(1+\frac{1}{n}\right)^n$$
$$\lim_{x \to 0^+} \frac{1}{x}$$
### 数式フォント
```
太字
$\mathbf{A}$,$\mathbf{x}$,$\boldsymbol{\alpha}$
イタリック
$A$,$x$,$\alpha$
黒板太字
$\mathbb{R}$,$\mathbb{C}$,$\mathbb{N}$,$\mathbb{Z}$,$\mathbb{Q}$
コールグラフ
$\mathcal{A}$,$\mathcal{B}$,$\mathcal{F}$,$\mathcal{L}$
スクリプト
$\mathscr{A}$,$\mathscr{B}$,$\mathscr{F}$,$\mathscr{L}$
等幅
$\mathtt{text}$,$\mathtt{ABC}$
ローマン
$\mathrm{d}x$,$\mathrm{sin}$,$\mathrm{cos}$
```
太字
$\mathbf{A}$,$\mathbf{x}$,$\boldsymbol{\alpha}$
イタリック
$A$,$x$,$\alpha$
黒板太字
$\mathbb{R}$,$\mathbb{C}$,$\mathbb{N}$,$\mathbb{Z}$,$\mathbb{Q}$
コールグラフ
$\mathcal{A}$,$\mathcal{B}$,$\mathcal{F}$,$\mathcal{L}$
スクリプト
$\mathscr{A}$,$\mathscr{B}$,$\mathscr{F}$,$\mathscr{L}$
等幅
$\mathtt{text}$,$\mathtt{ABC}$
ローマン
$\mathrm{d}x$,$\mathrm{sin}$,$\mathrm{cos}$
### サイズ制御
```
$\tiny{tiny}$
$\small{small}$
$\normalsize{normal}$
$\large{large}$
$\Large{Large}$
$\LARGE{LARGE}$
$\huge{huge}$
```
$\tiny{tiny}$
$\small{small}$
$\normalsize{normal}$
$\large{large}$
$\Large{Large}$
$\LARGE{LARGE}$
$\huge{huge}$
### 特殊マーク
```
単一矢印
$\leftarrow$,$\rightarrow$,$\uparrow$,$\downarrow$
二重矢印
$\leftrightarrow$,$\updownarrow$
長い矢印
$\longleftarrow$,$\longrightarrow$,$\longleftrightarrow$
二重線矢印
$\Leftarrow$,$\Rightarrow$,$\Leftrightarrow$
特殊矢印
$\mapsto$,$\to$,$\gets$,$\hookrightarrow$,$\leadsto$
```
単一矢印
$\leftarrow$,$\rightarrow$,$\uparrow$,$\downarrow$
二重矢印
$\leftrightarrow$,$\updownarrow$
長い矢印
$\longleftarrow$,$\longrightarrow$,$\longleftrightarrow$
二重線矢印
$\Leftarrow$,$\Rightarrow$,$\Leftrightarrow$
特殊矢印
$\mapsto$,$\to$,$\gets$,$\hookrightarrow$,$\leadsto$
### 矢印
```
ハット
$\hat{a}$,$\widehat{abc}$
チルダ
$\tilde{a}$,$\widetilde{abc}$
バー
$\bar{a}$,$\overline{abc}$
アンダーライン
$\underline{abc}$
ベクトル矢印
$\vec{a}$,$\overrightarrow{AB}$
ドット
$\dot{a}$,$\ddot{a}$,$\dddot{a}$
```
ハット
$\hat{a}$,$\widehat{abc}$
チルダ
$\tilde{a}$,$\widetilde{abc}$
バー
$\bar{a}$,$\overline{abc}$
アンダーライン
$\underline{abc}$
ベクトル矢印
$\vec{a}$,$\overrightarrow{AB}$
ドット
$\dot{a}$,$\ddot{a}$,$\dddot{a}$
