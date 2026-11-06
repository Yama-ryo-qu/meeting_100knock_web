# 課題29：GitHub Pagesを用いたWebページの公開

## 1. HTMLファイルの作成

Webページの内容を記述した `index.html` を作成した。

HTMLにはページタイトル、見出し、文章などを記述し、CSSを用いて背景色や文字の大きさなどを設定した。

GitHub Pagesでは、公開対象のディレクトリにある `index.html` がWebサイトのトップページとして表示される。

## 2. GitHubへのアップロード

作成したHTMLファイルをGitHub上のリポジトリに反映するため、Git Bashを使用してGitの操作を行った。

### ① リモートリポジトリの取得

まず、GitHub上にあるリポジトリをローカル環境にコピーする。

```bash
git clone https://github.com/Yama-ryo-qu/web_knock_test.git
```

`git clone` は、GitHubなどのリモートリポジトリをローカル環境に複製するコマンドである。

これにより、リポジトリ内のファイルやコミット履歴を取得できる。

続いて、作業ディレクトリを移動する。

```bash
cd web_knock_test
```

`cd` はディレクトリを移動するためのコマンドである。

### ② HTMLファイルの配置

作成した `index.html` をリポジトリのルートディレクトリに配置する。

今回、別のフォルダで作成していたHTMLファイルをコピーするために、以下のコマンドを使用した。

```bash
cp ../web_knock/index.html ./index.html
```

- `cp`：ファイルをコピーするコマンド
- `../web_knock/index.html`：コピー元のHTMLファイル
- `./index.html`：現在のディレクトリ内のコピー先

コピー後、以下のコマンドでファイルを確認する。

```bash
ls
```

ファイル一覧に `index.html` が表示されれば、配置は完了である。

### ③ ファイルの変更状態を確認

次のコマンドを実行する。

```bash
git status
```

`git status` は、Gitが管理しているファイルの変更状態を確認するコマンドである。

新しく追加した `index.html` は、Gitに登録する前は `Untracked files` として表示される。

これは、ファイル自体は存在しているものの、Gitの管理対象としてまだ登録されていないことを意味する。

### ④ ファイルをステージングする

次のコマンドを実行する。

```bash
git add index.html
```

`git add` は、ファイルの変更内容を次のコミットに含めるためのコマンドである。

この操作をステージングと呼ぶ。

ステージングを行うことで、Gitに対して「このファイルの変更を記録する」という指定ができる。

なお、`git add .` では現在のディレクトリ内の変更をまとめて追加するが、今回は `index.html` のみを追加した。

### ⑤ 変更内容をコミットする

次のコマンドを実行する。

```bash
git commit -m "Add GitHub Pages website"
```

`git commit` は、ステージングした変更内容をローカルリポジトリの履歴として記録するコマンドである。

`-m` オプションでは、変更内容を説明するコミットメッセージを指定できる。

実行結果：

```text
[main f5bee01] Add GitHub Pages website
 1 file changed, 30 insertions(+)
 create mode 100644 index.html
```

この結果から、`index.html` が新しく作成され、30行の内容がコミットされたことが分かる。

ただし、この段階では変更内容はローカル環境に保存されているだけであり、GitHubにはまだ反映されていない。

### ⑥ GitHubにpushする

次のコマンドを実行する。

```bash
git push origin main
```

`git push` は、ローカルリポジトリで作成したコミットをGitHubなどのリモートリポジトリに送信するコマンドである。

- `origin`：リモートリポジトリの登録名
- `main`：変更を反映するブランチ名

今回、最初のpush時にはGitHubの認証エラーが発生したため、認証情報を確認して再実行した。

最終的にpushが成功し、GitHub上に `index.html` が反映された。

### ⑦ GitHub上で確認

GitHubリポジトリをブラウザで開き、ファイル一覧に `index.html` が存在することを確認する。

リポジトリURL：

https://github.com/Yama-ryo-qu/web_knock_test

これにより、ローカルで作成したHTMLファイルをGitHubにアップロードできた。

## 3. GitHub Pagesの設定

GitHub上のリポジトリで、以下の手順によりGitHub Pagesを有効化した。

1. GitHubリポジトリを開く。
2. `Settings` を選択する。
3. 左側メニューから `Pages` を選択する。
4. `Build and deployment` で以下の項目を設定する。

| 設定項目 | 設定値 | 説明 |
|---|---|---|
| Source | Deploy from a branch | 指定したブランチのファイルを公開する |
| Branch | main | 公開対象のブランチ |
| Folder | /(root) | ブランチのルートディレクトリを公開する |

5. `Save` を押して設定を保存する。

この設定により、`main` ブランチのルートディレクトリ内に配置した `index.html` がWebページとして公開される。

## 4. 実行結果

GitHub Pagesを利用して、作成したWebページをインターネット上に公開できた。

### GitHubリポジトリ

https://github.com/Yama-ryo-qu/web_knock_test

### 公開URL

https://yama-ryo-qu.github.io/web_knock_test/

公開URLにアクセスし、作成したHTMLページが正常に表示されることを確認した。

## 5. まとめ

本課題では、HTMLファイルの作成からGitHubへのアップロード、GitHub Pagesを利用したWebページの公開までを実施した。

GitHubへのアップロードでは、`git add` で変更をステージングし、`git commit` で履歴に記録した後、`git push` でリモートリポジトリに反映するという一連の流れを確認した。

また、GitHub Pagesを利用することで、独自のWebサーバーを構築せずに静的なWebページをインターネット上に公開できることが分かった。
