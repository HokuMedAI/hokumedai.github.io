# 北医AI研究会ホームページ
北医AI研究会のホームページです。[こちらからアクセス](https://hokumedai.github.io/)

---
## プロジェクトのセットアップ

このプロジェクトは Git サブモジュールを利用しています。最初にクローンするときは以下の手順を踏んでください。

```bash
# 1. リポジトリをクローン
git clone https://github.com/hokumedai/hokumedai.github.io.git
cd hokumedai.github.io

# 2. サブモジュールを初期化・更新
git submodule update --init --recursive
```

---
## 記事の作成

### 基本操作の流れ
1. プロジェクトディレクトリに移動
2. 上記コマンドを実行
3. 作成されたMarkdownファイルを編集

### 基本構文
```bash
hugo new [パス] --kind [テンプレートタイプ]
```

### 利用可能なテンプレートタイプ

| タイプ | 用途 | コマンド例 |
|--------|------|-----------|
| `mokumoku` | もくもく会 | `hugo new content/activities/mokumoku/2024-01-15/index.md --kind mokumoku` |
| `seminar` | セミナー | `hugo new content/activities/seminar/2024-01-20/index.md --kind seminar` |
| `meeting` | ミーティング | `hugo new content/activities/meeting/2024-01-25/index.md --kind meeting` |
| `article` | 記事 | `hugo new content/articles/research/index.md --kind article` |
| `other(default)` | その他 |  |

### 補足：自動化スクリプト
Pythonスクリプト `new_page.py` を使用可能。

#### 使用方法
```bash
# new_page.py を実行して、新しい記事ページを作成
python -m new_page 
# 下の２つでもOK
python new_page.py
/new_page.py
```

実行後、以下の流れで記事を作成します：

1. **ページタイプの選択**
   ```
   Select page type:
   1. Article
   2. Seminar  
   3. Mokumoku
   4. Meeting
   5. Other (default)
   
   Enter number (1-5): 
   ```

2. **記事の詳細入力**
   - **Article の場合**: パス名を入力（例：`new_series/new_page`）
   - **その他の場合**: 日付を入力（デフォルト：今日の日付）

3. **実行確認**
   - 実行されるHugoコマンドが表示され、確認後に記事が作成されます

#### 実行例
```bash
$ python new_page.py

Select page type:
1. Article
2. Seminar
3. Mokumoku
4. Meeting
5. Other (default)

Enter number (1-5): 3

Enter date (YYYY-MM-DD) [default: 2025-07-30]: 

Will execute the following command:
hugo new content/activities/mokumoku/2025-07-30/index.md --kind mokumoku

Proceed? (y/n): y

Page created: content/activities/mokumoku/2025-07-30/index.md
```

---
## ブランチ運用ルール

### 個人用作業ブランチ
- 各自、自分専用の作業ブランチを持つことを推奨します。
- ブランチ名は `名前/ブランチ名` 形式（例: `yamada/develop`）
- 使いまわし可能。別の作業に入る場合はリベースする。
```bash
# 個人作業の流れ（個人用開発ブランチ）
# 1.新しい個人用ブランチを作成してチェックアウト
git checkout -b yamada/dev

# 2.変更をステージ、コミット、PR（コマンド略）

# 3.マージされた後はmainを更新
git checkout main
git pull origin main

# 4.自分のブランチをrebase
git checkout yamada/dev
git rebase main
```

### 一時的なブランチ
- 作業内容が明確に分かれている場合は新しくブランチを切る。(例: `yamada/feat-newarticle`, `yamada/bug-fix`)
- マージ後は必ず削除する。
```bash
# 個人作業の流れ（一時的なブランチ）
# 1.新機能開発のためのブランチを作成してチェックアウト
git checkout -b yamada/feat-new

# 2.変更をステージ、コミット、PR（コマンド略）

# 3.ローカルの古いブランチは削除して整理する
git branch -d yamada/feat-new

# 4.リモートブランチも不要であれば削除する（必要に応じて）
git push origin --delete yamada/feat-new
```

---
## Pull Request（PR）のルール

- PRは必ず `main` ブランチに向けて作成。
- マージされたらGitHub Actionsが自動でビルド・公開を実行。
- レビューを必須とし、自己マージは原則禁止（例外があれば明記）。
```bash
# PRを作成するための手順
# 0.自分のブランチを切る
git checkout -b yamada/new-feature

# 1.作業ののち、変更内容をステージ
git add .

# 2.コミット
git commit -m "feat: new "

# 3.プッシュ
git push origin yamada/new-feature

# 4.GitHub上でPRを作成
```

## HTMLビルドの扱い
- HTMLやビルド成果物を手元で生成してPushするのは禁止。
- HTMLは全てGitHub Actionsで自動生成される。
- 手動で生成したHTMLや関連ファイルは `.gitignore` によって無視。
```bash
# 手動で生成したHTMLを無視するための.gitignore設定(例)
/public/
/resources/_gen/
/assets/jsconfig.json
hugo_stats.json
.hugo_build.lock
```
