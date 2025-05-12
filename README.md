# 北医AI研究会ホームページ
北医AI研究会のホームページです。[こちらからアクセス](https://hokumedai.github.io/)


## プロジェクトのセットアップ

このプロジェクトは Git サブモジュールを利用しています。最初にクローンするときは以下の手順を踏んでください。

```bash
# 1. リポジトリをクローン
git clone https://github.com/hokumedai/hokumedai.github.io.git
cd hokumedai.github.io

# 2. サブモジュールを初期化・更新
git submodule update --init --recursive
```

## ブランチ運用ルール

### 個人用作業ブランチ

- 各自、自分専用の作業ブランチを持つことを推奨します。
- ブランチ名は `名前/ブランチ名` 形式（例: `yamada/develop`）
- 使いまわし可能。別の作業に入る場合はリセットまたはブランチを切り直す。

### 一時的なブランチ

- 作業内容が明確に分かれている場合は新しくブランチを切る。
- 例: `yamada/update-README`, `yamada/fix-navbar`
- マージ後は必ず削除する。

## Pull Request（PR）のルール

- PRは必ず `main` ブランチに向けて作成。
- マージされたらGitHub Actionsが自動でビルド・公開を実行。
- レビューを必須とし、自己マージは原則禁止（例外があれば明記）。

## HTMLビルドの扱い

- HTMLやビルド成果物を手元で生成してPushするのは禁止。
- HTMLは全てGitHub Actionsで自動生成される。
- 手動で生成したHTMLや関連ファイルは `.gitignore` によって無視。
