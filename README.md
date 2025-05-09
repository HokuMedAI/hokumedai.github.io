# 🌐 北医AI研究会 [https://hokumedai.github.io/](https://hokumedai.github.io/)


このリポジトリは、[Hugo](https://gohugo.io/) を使用して構築された北医AI研究会のホームページのソースコードです。  
GitHub Pages を利用してサイトを公開しており、複数のブランチで開発・公開を管理しています。

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

このリポジトリでは、以下の2つのブランチを使って開発・公開を行っています。

### 🧪 `develop` ブランチ（開発用）

- **すべての開発作業はこのブランチで行います**
- 記事追加、デザイン調整、バグ修正などの編集はここで行います
- テスト・レビュー後に `main` にマージします

### 🚀 `main` ブランチ（公開用）

- `develop`で完成した機能をまとめる安定ブランチです
- このブランチの内容をもとに **Hugoでビルド** を行い、ビルド成果物をこのブランチに含めて公開します。（５/９現在ではまだ公開していません）
- GitHub Pagesは、この`main`ブランチ（またはその中の`/docs`フォルダ）からサイトを公開するように設定します。（管理者が行います）
- 原則として `develop` からマージのみ行い、直接編集しません（ビルド成果物のコミットを除く）。

---

## 📄 運用の流れ（Hugo + Git）

1. `develop` ブランチで作業
2. 完成したら PullRequest
3.  `main` にマージして `main` 上で以下のコマンドでビルド（管理者が行います）：

```bash
hugo --minify
```

4. ビルドされた `public/` ディレクトリの中身を、`main` ブランチの公開ディレクトリ（例：ルートまたは `/docs`）にコピー＆コミットして push

---

## 🔧 公開手順（手動デプロイ）

```bash
# developブランチでの作業が完了したらmainブランチにマージ
git switch main
git merge develop

# mainブランチでビルド
hugo --minify

# public/ の内容を公開ディレクトリにコピー（例：ルートに公開する場合）
# 注意: 既存のファイルを上書きします。必要に応じてバックアップや調整を行ってください。
#      .gitディレクトリなどを消さないように注意。
#      もしルートに .gitignore があれば、public/* を無視する設定は一時的にコメントアウトするか、
#      cp -r public/* ./ の代わりに、必要なファイルだけを慎重にコピーしてください。
#      より安全な方法としては、一旦別の場所に public の中身を移し、
#      不要なファイルを削除してからルートに移動するなどの手段があります。
# 例:
# rm -rf !(public|.git|.gitignore|README.md|その他の管理ファイル) # publicと管理ファイル以外を削除
# cp -r public/* ./                                          # publicの中身をコピー
# git add .
# git commit -m "公開用にビルド成果物を更新"
# git push origin main

# (よりシンプルな例: GitHub Pagesが /docs から配信する設定の場合)
# rm -rf docs/* # docsフォルダの中身をクリア
# cp -r public/* docs/
# git add docs/
# git commit -m "公開用にビルド成果物を更新 (docs/)"
# git push origin main
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

