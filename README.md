# 【Web開発100本ノック】
対面講義に参加しているため記載してる説明を見ていただけると幸いです🙇

以下テーマ7の解答

## 課題73：useStateによる状態管理
問題：「useStateフックを利用し，ボタン押下で値が増減するカウンターコンポーネントを作成せよ．」


本課題では、React の useState フックを利用し、  ボタン操作によって値が増減するカウンターコンポーネントを作成する。  
状態が変化すると画面が自動的に再描画されることを確認する。


## カウンターコンポーネントのソースコード

```jsx
import { useState } from "react";

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>{count}</p>
      <button onClick={() => setCount(count + 1)}>+1</button>
      <button onClick={() => setCount(count - 1)}>-1</button>
    </div>
  );
}

export default Counter;

```


### useStateの説明

```jsx
const [count, setCount] = useState(0);
```

count は現在の状態を保持する変数であり、
setCount はその状態を更新するための関数である。
初期値として 0 を設定している。



### 状態更新処理の説明

```jsx
setCount(count + 1);
```
count は更新前の状態の値を表し、
前の値を基にして状態を更新できる。



## Appに組み込む（表示確認用）
```js
import Counter from "./Counter";

function App() {
  return (
    <div>
      <Counter />
    </div>

  );
}

export default App;
```
<Counter />の部分でCounter.jsxのCounter()を呼び出している。

## 処理の流れ
1．index.js(Reactアプリが最初に実行されるファイル) が App を呼ぶ

2．App.js が <Counter /> を配置

3．Counter() が実行される

4．useState(0) により count=0

5．JSX が画面に表示される

6．ボタンを押す

7．setCount が呼ばれる

8．Reactが Counter を再実行

9．新しい count が画面に反映される


## 実装結果
<img width="561" height="317" alt="スクリーンショット (223)" src="https://github.com/user-attachments/assets/d1a0b01c-e5fc-4cd6-871e-51d50637acf3" />


<img width="561" height="296" alt="スクリーンショット (224)" src="https://github.com/user-attachments/assets/acb64daf-66a6-4205-a97f-b6922253b1cf" />





# 課題79：Reactアプリの公開（GitHub Pages版）
作成したReactアプリを **GitHub Pages** で公開し、公開URLで表示できることを確認する。

---

## 手順

### 1. GitHubにリポジトリを作成してpushする
（GitHub上で空のリポジトリを作ってから、プロジェクト直下で実行）

```bash
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/<ユーザー名>/<リポジトリ名>.git
git push -u origin main
```

## 2. gh-pages を入れる
```bash
npm install --save-dev gh-pages
```

## 3. package.json を設定する
(1) homepage を追加（最上部付近に入れてOK）
```json
"homepage": "https://<ユーザー名>.github.io/<リポジトリ名>"
```

(2) scripts を追加（既存scriptsに追記）
```json
"predeploy": "npm run build",
"deploy": "gh-pages -d build"
```

## 4. 公開（デプロイ）する
```bash
npm run deploy
```

## 5. GitHub側のPages設定を確認
GitHubのリポジトリ画面 → Settings → Pages

Branch が gh-pages になっていることを確認（なっていなければ gh-pages を選択して保存）

## 実行結果
下記のリンクにアクセスしてみてください。おそらく動作するはずです。

⬇⬇

"https://yama-ryo-qu.github.io/meeting_100knock_web_79"
