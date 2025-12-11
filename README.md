**【Web開発100本ノック】**



以下テーマ5の解答

## 課題58. Webフォームからの入力データをデータベースに登録

### 概要
ExpressサーバとSQLiteデータベースを連携させ、Webフォームから入力されたデータをデータベース（`users` テーブル）に登録する機能を実装した。
フォームデータの受け取りには `express.urlencoded` を使用し、SQLインジェクション対策としてプレースホルダ（`?`）を用いた `INSERT` 文を実行している。

### 実装したソースコード

#### サーバ側 (`app.js`)
POSTリクエストを受け取り、SQLiteへデータを挿入する処理。

```javascript
const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const path = require('path');
const app = express();

const PORT = 3000;
const DB_PATH = './my_database.db';

// POSTデータ解析用設定
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));

// データベース接続とテーブル作成
const db = new sqlite3.Database(DB_PATH, (err) => {
    if (err) {
        console.error('DB接続エラー:', err.message);
    } else {
        db.run(`CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            email TEXT
        )`);
    }
});

// 登録処理
app.post('/register', (req, res) => {
    const { username, email } = req.body;
    const sql = 'INSERT INTO users (username, email) VALUES (?, ?)';
    
    db.run(sql, [username, email], function(err) {
        if (err) {
            console.error(err.message);
            res.status(500).send("DB Error");
        } else {
            res.send(`
                <h1>登録完了</h1>
                <p>以下のデータで登録しました。</p>
                <ul>
                    <li>ID: ${this.lastID}</li>
                    <li>名前: ${username}</li>
                    <li>Email: ${email}</li>
                </ul>
                <a href="/">戻る</a>
            `);
        }
    });
});

app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});
```

#### フロントエンド側 (`public/index.html`)
ユーザ名とメールアドレスを入力し、POSTメソッドで送信するフォーム。

```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>ユーザ登録</title>
</head>
<body>
    <h1>ユーザ登録フォーム</h1>
    <form action="/register" method="POST">
        <p>
            <label>ユーザ名: <input type="text" name="username" required></label>
        </p>
        <p>
            <label>Email: <input type="email" name="email" required></label>
        </p>
        <button type="submit">データベースに登録</button>
    </form>
</body>
</html>
```

### 実行結果（スクリーンショット）

**1. 入力画面**
ブラウザでフォームにデータを入力した状態。
[ここに「入力画面」のスクリーンショットを貼り付けてください]

**2. 登録完了画面**
登録ボタン押下後、登録されたIDとデータが表示された状態。
[ここに「登録完了画面」のスクリーンショットを貼り付けてください]

**3. データベースの確認（コンソール等）**
実際にデータが追加されていることの確認。
[ここに「SELECT文での検索結果」などのスクリーンショットを貼り付けてください]
