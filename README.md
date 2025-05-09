# 🌐 プロジェクト名

このリポジトリは、[Hugo](https://gohugo.io/) を使用して構築された北医AI研究会のホームページのソースコードです。  
GitHub Pages を利用してサイトを公開しており、複数のブランチで開発・公開を管理しています。
[https://hokumedai.github.io/](https://hokumedai.github.io/)

---

## 📦 使用技術：Hugo（静的サイトジェネレータ）

このプロジェクトでは Hugo を使用して、MarkdownファイルからHTMLサイトを生成しています。

- **高速ビルド**：数千ページでも一瞬で生成
- **Markdownで簡単に記述**：エンジニア以外でも記事編集が可能
- **テーマが豊富**：レイアウトやデザインを素早く適用可能

### Hugo のローカル開発

```bash
# 開発用サーバー起動（変更を即反映）
hugo server -D
```

### 本番用ビルド

```bash
# 最適化されたHTMLを生成
hugo --minify
```

出力結果は `public/` ディレクトリに生成されます。

---

## 🌿 ブランチ運用ルール

このリポジトリでは、以下の3つのブランチを使って開発・公開を行っています。

### 🧪 `develop` ブランチ（開発用）

- **すべての開発作業はこのブランチで行います**
- 記事追加、デザイン調整、バグ修正などの編集はここで行います
- テスト・レビュー後に `main` にマージします

### 🚀 `main` ブランチ（リリース用）

- `develop`で完成した機能をまとめる安定ブランチです
- このブランチの内容をもとに **Hugoでビルド** を行います
- 原則として `develop` からマージのみ行い、直接編集しません

### 🌐 `gh-pages` ブランチ（公開用）

- GitHub Pages で公開される静的ファイルを管理
- `main` でビルドした成果物（`public/`）を反映します
- Webサイトは以下のURLで公開されます：

```
https://<ユーザー名>.github.io/<リポジトリ名>/
```

---

## 📄 運用の流れ（Hugo + Git）

1. `develop` ブランチで作業
2. 完成したら `main` にマージ
3. `main` 上で以下のコマンドでビルド：

```bash
hugo --minify
```

4. `gh-pages` ブランチに切り替え
5. `public/` フォルダの中身をコピー＆コミットして push

---

## 🔧 公開手順（手動デプロイ）

```bash
# mainブランチでビルド
git switch main
hugo --minify

# gh-pagesに切り替え
git switch gh-pages

# public/ の内容をコピー（上書き）
cp -r ../public/* ./

# コミット & プッシュ
git add .
git commit -m "公開用にビルド成果物を更新"
git push origin gh-pages
```

---

## 🛠 今後の予定

- GitHub Actions による自動ビルド & デプロイの導入予定
- `main` にマージされたタイミングで自動反映

---

## 💡 補足

- Hugo のテーマや設定ファイルは `config.toml` で管理しています
- コンテンツは `content/` ディレクトリ配下にMarkdown形式で記述します
- デザインやテンプレートは `layouts/` に配置します

---

## 🧑‍💻 開発者向けメモ

Hugo のインストール（Mac例）：

```bash
brew install hugo
```

他の環境のインストール方法は公式サイトをご覧ください：  
[https://gohugo.io/getting-started/installing/](https://gohugo.io/getting-started/installing/)

---

