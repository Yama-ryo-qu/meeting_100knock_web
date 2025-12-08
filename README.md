**【Web開発100本ノック】**



以下テーマ4の解答


**課題43**
```
const express = require('express');
const app = express();
const port = 3000;

// GET /api/greet?name=xxx のリクエストを処理
app.get('/api/greet', (req, res) => {
    // クエリパラメータ 'name' を取得
    const name = req.query.name;

    if (name) {
        res.json({ message: `Hello, ${name}!` });
    } else {
        res.json({ message: "Hello!" });
    }
});

// サーバの起動
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
```

結果は以下

<img width="1259" height="586" alt="スクリーンショット (170)" src="https://github.com/user-attachments/assets/c72dbf5d-d536-40e5-a5e8-4bf6ed83594b" />






**課題49**

## ベースURL
`http://localhost:3000`

## エンドポイント一覧

| メソッド | パス | 機能概要 | 課題番号 |
| :--- | :--- | :--- | :--- |
| `GET` | `/api/greet` | 挨拶メッセージを返す | 42, 43 |
| `POST` | `/api/echo` | 送信されたJSONをそのまま返す | 44 |
| `GET` | `/api/items` | アイテム一覧を取得する | 45 |
| `GET` | `/api/items/:id` | 特定のIDのアイテムを取得する | 46 |
| `POST` | `/api/items` | 新しいアイテムを追加する | 47 |
| `DELETE` | `/api/items/:id` | 特定のIDのアイテムを削除する | 48 |

---

## 詳細仕様

### 1. 挨拶API
シンプルな挨拶メッセージを返します。クエリパラメータで名前を指定することが可能。

- **URL:** `/api/greet`
- **メソッド:** `GET`
- **クエリパラメータ:**
  - `name` (任意): 挨拶する相手の名前

#### レスポンス例

**リクエスト 1 (パラメータなし):**
`GET /api/greet`

```json
{
  "message": "Hello!"
}
```

**リクエスト 2 (パラメータあり):**
`GET /api/greet?name=Yamaguchi`

```json
{
  "message": "Hello, Yamaguchi!"
}
```

---

### 2. エコーAPI
クライアントから送信されたJSONデータをそのままレスポンスとして返す。

- **URL:** `/api/echo`
- **メソッド:** `POST`
- **Content-Type:** `application/json`

#### リクエストボディ例
```json
{
  "id": 1,
  "text": "This is a test."
}
```

#### レスポンス例
```json
{
  "id": 1,
  "text": "This is a test."
}
```

---

### 3. アイテム一覧取得API
サーバで管理しているアイテム（配列データ）の全リストを返す。

- **URL:** `/api/items`
- **メソッド:** `GET`

#### レスポンス例
```json
["Apple", "Banana", "Orange"]
```

---

### 4. 個別アイテム取得API
URLパスで指定されたID（インデックス等）に対応するアイテムを返す。

- **URL:** `/api/items/:id`
- **メソッド:** `GET`
- **パスパラメータ:**
  - `id`: 取得したいアイテムのIDまたはインデックス

#### レスポンス例 (例: `/api/items/1`)
```json
"Banana"
```

---

### 5. アイテム追加API
新しいアイテムを追加し、追加後の全リストを返す。

- **URL:** `/api/items`
- **メソッド:** `POST`
- **Content-Type:** `application/json`

#### リクエストボディ例
```json
{
  "item": "Grape"
}
```

#### レスポンス例
```json
["Apple", "Banana", "Orange", "Grape"]
```

---

### 6. アイテム削除API
指定されたIDのアイテムを削除し、削除後の全リストを返す。

- **URL:** `/api/items/:id`
- **メソッド:** `DELETE`
- **パスパラメータ:**
  - `id`: 削除したいアイテムのIDまたはインデックス

#### レスポンス例 (例: `/api/items/0` - "Apple"を削除)
```json
["Banana", "Orange", "Grape"]
```
