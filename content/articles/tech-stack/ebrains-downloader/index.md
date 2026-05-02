---
title: "EBRAINSのWSIデータをダウンロードするCLIツールを作った"
description: "EBRAINSのWSIデータをダウンロードするCLIツールを作った"
date: 2026-04-28
draft: false
showHero: true
layoutBackgroundBlur: true
authors:
  - "ymd000"
---

## TL;DR

- **EBRAINSからのWSI(Whole Slide Image)のダウンロードを自動で行うコマンドラインツール[ebrains-downloader](https://github.com/HokuMedAI/ebrains-downloader)** を作成した
- 背景：**EBRAINSのGUIダウンロードはバックエンド（`rgw.cscs.ch`）の不安定さでタイムアウトしやすい**

## EBRAINSとは

[EBRAINS](https://ebrains.eu/) は欧州の神経科学データプラットフォームで、脳画像や病理データなどの研究データが公開されている。

### やりたかったこと

病理画像のWSIデータ（`.ndpi`形式、1ファイル数GB、500ファイルほど）をダウンロードしたかった。

## EBRAINSの問題点

### 試みたこと

- ZIPでダウンロード  
ファイル破損していて解凍できず。

- GUIで複数ファイルを一度にダウンロード  
最初は30ファイルほどダウンロードしようとしたがもちろんうまくいかず、最大2,3ファイルが一度にできる限度のようだ。  
このままでは画面の前にかじりついたまま作業しなければならない。

### なぜうまくいかないか

根本的な原因は、**EBRAINSのデータが裏側のストレージ（`rgw.cscs.ch`、スイスのCSCSが運営）から配信されていて、このバックエンドが一時的に不安定**なことにあるようだ。

```
ブラウザ
    ↓
data-proxy.ebrains.eu
    ↓
rgw.cscs.ch  ← ここが不安定
```

## 作成したCLIツールの紹介：[ebrains-downloader](https://github.com/HokuMedAI/ebrains-downloader)

### インストール

インストールは不要。[uvx](https://docs.astral.sh/uv/)から実行可能:

```bash
uvx --from git+https://github.com/HokuMedAI/ebrains-downloader ebrains-downloader --diagnosis <DIAGNOSIS>
```

### 使い方

```bash
alias ebrains="uvx --from git+https://github.com/HokuMedAI/ebrains-downloader ebrains-downloader"
ebrains --diagnosis Meningioma
ebrains --diagnosis Meningioma Schwannoma
ebrains --diagnosis "Fibrous meningioma" --output /data/ebrains
```

| オプション | 説明 | デフォルト |
|---|---|---|
| `--diagnosis` | 診断名（必須、複数指定可） | — |
| `--output` | 出力ディレクトリ | `downloads` |

### 出力

```
downloads/
├── annotation.csv
├── Meningioma/
│   ├── <uuid>.ndpi
│   └── ...
└── Fibrous meningioma/
    ├── <uuid>.ndpi
    └── ...
```

**途中で中断しても自動でレジューム**するので、タイムアウトが発生しても最初からやり直す必要はない。

### 実際に使ってみる

![実際の動作ログ](/images/screenshot/Screenshot_20260428_161445.jpg)
2番目のファイルで465MBのところでタイムアウトが発生したが、そこから自動で再開して無事完了している。
