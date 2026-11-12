# 課題37：動的なリスト表示

## 1. 実装内容

JavaScriptの配列に格納した果物の名前を、`forEach()` を用いて1つずつ取り出し、HTML上にリスト形式で動的に表示するプログラムを作成した。

リストの各要素は `document.createElement()` を使用して生成し、`appendChild()` によってHTMLに追加する。

## 2. HTMLファイル（index.html）

HTML側では、リストの表示先となる `<ul>` 要素を用意する。

```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>課題37：動的なリスト表示</title>
</head>
<body>
    <h1>果物リスト</h1>

    <!-- JavaScriptでリストを追加する場所 -->
    <ul id="fruit-list"></ul>

    <!-- JavaScriptファイルを読み込む -->
    <script src="main.js"></script>
</body>
</html>
```

## 3. JavaScriptファイル（main.js）

```javascript
// 果物の名前を配列に格納する
const fruits = ["りんご", "バナナ", "みかん", "ぶどう", "いちご"];

// HTML内のリスト要素を取得する
const fruitList = document.getElementById("fruit-list");

// 配列内の果物を1つずつ処理する
fruits.forEach(function(fruit) {

    // 新しい<li>要素を生成する
    const listItem = document.createElement("li");

    // <li>要素に果物の名前を設定する
    listItem.textContent = fruit;

    // <ul>要素の中に<li>要素を追加する
    fruitList.appendChild(listItem);

});
```

## 4. 処理の説明

### ① 配列の定義

```javascript
const fruits = ["りんご", "バナナ", "みかん", "ぶどう", "いちご"];
```

5種類の果物を配列 `fruits` に格納する。

### ② HTML要素の取得

```javascript
const fruitList = document.getElementById("fruit-list");
```

`document.getElementById()` を使用し、HTML内の `id="fruit-list"` が指定された `<ul>` 要素を取得する。

### ③ 配列の繰り返し処理

```javascript
fruits.forEach(function(fruit) {
    // 処理
});
```

`forEach()` は、配列の各要素に対して順番に処理を実行するメソッドである。

今回の場合、「りんご」「バナナ」「みかん」「ぶどう」「いちご」が順番に変数 `fruit` に代入される。

### ④ HTML要素の生成

```javascript
const listItem = document.createElement("li");
```

`document.createElement()` を用いて、新しい `<li>` 要素を生成する。

`<li>` はリストの各項目を表すHTML要素である。

### ⑤ テキストの設定

```javascript
listItem.textContent = fruit;
```

生成した `<li>` 要素に、現在処理している果物の名前を設定する。

### ⑥ HTMLへの追加

```javascript
fruitList.appendChild(listItem);
```

`appendChild()` を使って、生成した `<li>` 要素を `<ul>` 要素の末尾に追加する。

これらの処理をすべての果物に対して繰り返すことで、リストが動的に生成される。

## 5. 実行結果

ブラウザで `index.html` を開くと、次の内容が箇条書きで表示される。

**果物リスト**

- りんご
- バナナ
- みかん
- ぶどう
- いちご

### 表示結果のスクリーンショット


<img width="959" height="485" alt="image" src="https://github.com/user-attachments/assets/bf001cd0-9615-453a-b7b7-73f2fc85743d" />


## 6. まとめ

今回の課題では、JavaScriptの配列と `forEach()` を使用して、複数のデータを順番に処理する方法を学んだ。

また、`document.createElement()` によってHTML要素を生成し、`appendChild()` を使ってWebページに追加することで、HTMLファイルに各項目を直接記述しなくても、JavaScriptから動的にリストを作成できることを確認した。
