# 【Web開発100本ノック】
対面講義に参加しているため記載してる説明を見ていただけると幸いです🙇

以下テーマ8の解答

## 課題88：APIデータのページネーション表示

この課題では、Avascriptの`fetch()` を使って API からデータを取得し、`_page` と `_limit` でページごとに分割して表示。  
さらに「前へ」「次へ」ボタンでページを切り替えられるようにした。

---

## 画面（HTML）の構成

- **前へボタン**：1ページ戻る
- **次へボタン**：1ページ進む
- **Page表示**：今が何ページ目か
- **メッセージ**：Loading... や エラー表示
- **リスト（ul）**：取得した投稿データ（posts）を表示

コード全体は以下の通り。

```html
<!doctype html>
<html lang="ja">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>課題88: ページネーション</title>
  <style>
    body { font-family: system-ui, sans-serif; margin: 24px; }
    .toolbar { display: flex; gap: 8px; align-items: center; flex-wrap: wrap; margin-bottom: 12px; }
    button { padding: 8px 12px; cursor: pointer; }
    button:disabled { opacity: 0.5; cursor: not-allowed; }
    .status { margin-left: 8px; }
    ul { padding-left: 18px; }
    li { margin: 10px 0; }
    .title { font-weight: 700; }
    .meta { color: #666; font-size: 12px; margin-top: 2px; }
    .error { color: #b00020; font-weight: 700; }
    .loading { color: #0b57d0; font-weight: 700; }
  </style>
</head>
<body>
  <h1>課題88：APIデータのページネーション表示</h1>

  <div class="toolbar">
    <button id="prevBtn">前へ</button>
    <button id="nextBtn">次へ</button>

    <span class="status" id="pageInfo">Page - / -</span>
    <span class="status" id="message"></span>
  </div>

  <ul id="list"></ul>

  <script>
    const API_URL = "https://jsonplaceholder.typicode.com/posts";
    const LIMIT = 10;

    let currentPage = 1;
    let totalPages = null;

    const $list = document.getElementById("list");
    const $prev = document.getElementById("prevBtn");
    const $next = document.getElementById("nextBtn");
    const $pageInfo = document.getElementById("pageInfo");
    const $message = document.getElementById("message");

    function setMessage(text, kind = "") {
      $message.textContent = text;
      $message.className = kind; // "", "loading", "error"
    }

    function updateButtons() {
      $prev.disabled = currentPage <= 1;
      $next.disabled = totalPages !== null ? currentPage >= totalPages : false;
      $pageInfo.textContent = `Page ${currentPage} / ${totalPages ?? "?"}`;
    }

    function renderPosts(posts) {
      $list.innerHTML = "";
      for (const p of posts) {
        const li = document.createElement("li");

        const title = document.createElement("div");
        title.className = "title";
        title.textContent = p.title;

        const body = document.createElement("div");
        body.textContent = p.body;

        const meta = document.createElement("div");
        meta.className = "meta";
        meta.textContent = `id: ${p.id}, userId: ${p.userId}`;

        li.appendChild(title);
        li.appendChild(body);
        li.appendChild(meta);
        $list.appendChild(li);
      }
    }

    async function fetchPage(page) {
      try {
        setMessage("Loading...", "loading");
        updateButtons();

        const url = new URL(API_URL);
        url.searchParams.set("_page", page);
        url.searchParams.set("_limit", LIMIT);

        const res = await fetch(url);
        if (!res.ok) throw new Error(`HTTP Error: ${res.status}`);

        // 総件数（JSONPlaceholderは x-total-count を返す）
        const totalCount = Number(res.headers.get("x-total-count"));
        if (!Number.isNaN(totalCount) && totalCount > 0) {
          totalPages = Math.ceil(totalCount / LIMIT);
        } else {
          // 万一ヘッダーが取れない場合の保険
          totalPages = totalPages ?? page;
        }

        const data = await res.json();
        renderPosts(data);

        currentPage = page;
        setMessage("");
        updateButtons();
      } catch (err) {
        setMessage(`エラー: ${err.message}`, "error");
      }
    }

    $prev.addEventListener("click", () => {
      if (currentPage > 1) fetchPage(currentPage - 1);
    });

    $next.addEventListener("click", () => {
      if (totalPages === null || currentPage < totalPages) fetchPage(currentPage + 1);
    });

    // 初回表示
    fetchPage(currentPage);
  </script>
</body>
</html>
```

## Javascript部分の解説
### 変数の役割（状態管理）

```Javascript
const API_URL = "https://jsonplaceholder.typicode.com/posts";
const LIMIT = 10;


let currentPage = 1;
let totalPages = null;
```

- `API_URL`：取得元の API

- `LIMIT`：1ページに表示する件数（10件）

- `currentPage`：現在表示しているページ番号

- `totalPages`：全ページ数（ヘッダーから計算して入れる）

---

### DOM要素の取得（画面部品を操作できるようにする）

```Javascript
const $list = document.getElementById("list");
const $prev = document.getElementById("prevBtn");
const $next = document.getElementById("nextBtn");
const $pageInfo = document.getElementById("pageInfo");
const $message = document.getElementById("message");
```

- `document.getElementById()` は HTML の要素を取得する関数

- 取得した要素に対して `textContent` や `innerHTML` を使い、画面を書き換える。

---

### 関数①：setMessage（画面メッセージ表示）

```Javascript
function setMessage(text, kind = "") {
  $message.textContent = text;
  $message.className = kind; // "", "loading", "error"
}
```

#### 役割

- 取得中に `Loading...` を出したり、エラー時に `エラー: ...` を出したりするための関数

#### 引数

- `text`：表示したい文章

- `kind`：CSSのclass名（例：loading, error）

---

### 関数②：updateButtons（ボタンの有効/無効・ページ表示更新）

```Javascript
function updateButtons() {
  $prev.disabled = currentPage <= 1;
  $next.disabled = totalPages !== null ? currentPage >= totalPages : false;
  $pageInfo.textContent = `Page ${currentPage} / ${totalPages ?? "?"}`;
}
```

#### 役割

-「前へ」「次へ」が押せる状況かを判断して `disabled` を切り替える。今のページ番号を画面に出す

#### ポイント

- `currentPage <= 1` のときは 1ページ目なので「前へ」は無効

- `currentPage >= totalPages` のときは最終ページなので「次へ」は無効

- `totalPages ?? "?"` :totalPages がまだ不明なら ? を表示する（null合体演算子）

---

### 関数③：renderPosts（取得したデータをulに表示）

```Javascript
function renderPosts(posts) {
  $list.innerHTML = "";
  for (const p of posts) {
    const li = document.createElement("li");


    const title = document.createElement("div");
    title.className = "title";
    title.textContent = p.title;


    const body = document.createElement("div");
    body.textContent = p.body;


    const meta = document.createElement("div");
    meta.className = "meta";
    meta.textContent = `id: ${p.id}, userId: ${p.userId}`;


    li.appendChild(title);
    li.appendChild(body);
    li.appendChild(meta);
    $list.appendChild(li);
  }
}
```

#### 役割

APIから取得した配列 `posts` をもとにHTMLを作り、画面に一覧表示する

#### 処理の流れ

- `ul` を一旦空にする（`innerHTML = ""`）

- `posts` を1件ずつ取り出す

- `li` 要素を作る

- title/body/meta の要素を作って `li` に入れる

- できた `li` を `ul` に追加する

---

### 関数④：fetchPage（APIから指定ページを取得して表示）

```Javascript
async function fetchPage(page) {
  try {
    setMessage("Loading...", "loading");
    updateButtons();


    const url = new URL(API_URL);
    url.searchParams.set("_page", page);
    url.searchParams.set("_limit", LIMIT);


    const res = await fetch(url);
    if (!res.ok) throw new Error(`HTTP Error: ${res.status}`);


    const totalCount = Number(res.headers.get("x-total-count"));
    if (!Number.isNaN(totalCount) && totalCount > 0) {
      totalPages = Math.ceil(totalCount / LIMIT);
    } else {
      totalPages = totalPages ?? page;
    }


    const data = await res.json();
    renderPosts(data);


    currentPage = page;
    setMessage("");
    updateButtons();
  } catch (err) {
    setMessage(`エラー: ${err.message}`, "error");
  }
}
```

#### 役割

指定ページ `page` のデータを API から取得して表示する中心関数

#### ポイント

- `setMessage("Loading...")` :Loading表示

- `_page=page`, `_limit=10` :URL作成（クエリ付ける）

- fetchで取得

- HTTPエラーチェック :`res.ok` が `false` なら `throw` して `catch` へ

総件数から全ページ数を計算

x-total-count ヘッダーに総件数が入っている

Math.ceil(totalCount / LIMIT) でページ数

JSONに変換して表示

res.json() → renderPosts()

状態更新

currentPage = page

メッセージ消す

ボタン状態更新

async / await の意味

fetch() は非同期（時間がかかる）ので await で待つ

関数を async function にすると await が使える
