---
title: "EBRAINSのWSIデータをダウンロードするCLIツールを作った"
description: "EBRAINSのGUIダウンロードが不安定な問題を解消するため、タイムアウト時の自動再試行機能を備えたCLIツールを作成した"
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
[The Digital Brain Tumour Atlas](https://search.kg.ebrains.eu/instances/8fc108ab-e2b4-406f-8999-60269dc1f994)から脳腫瘍のHE染色のWSIがダウンロードできる。

## EBRAINSの問題点

**試みたこと**

- ZIPでダウンロード  
ダウンロードが途中で中断されるためか、zipファイルが破損していて解凍できず。

- GUIで複数ファイルを一度にダウンロード  
最初は30ファイルほどダウンロードしようとしたがやはりうまくいかず、最大2,3ファイルが一度にできる限度のようだ。  
このままでは画面の前にかじりついたまま作業しなければならない。

**なぜうまくいかないか**

根本的な原因は、**EBRAINSのデータが裏側のストレージ（`rgw.cscs.ch`、スイスのCSCSが運営）から配信されていて、このバックエンドが一時的に不安定**なことにあるようだ。

```
ブラウザ
    ↓
data-proxy.ebrains.eu
    ↓
rgw.cscs.ch  ← ここが不安定
```

## 作成したCLIツールの紹介：[ebrains-downloader](https://github.com/HokuMedAI/ebrains-downloader)

**Usage**

uvxの場合:

```bash
uvx --from git+https://github.com/HokuMedAI/ebrains-downloader ebrains-downloader --diagnosis Haemangiopericytoma --output /path/to/output

# 複数指定
uvx --from git+https://github.com/HokuMedAI/ebrains-downloader ebrains-downloader --diagnosis Haemangiopericytoma Schwannoma
# スペースを含む場合はクォートで囲む
uvx --from git+https://github.com/HokuMedAI/ebrains-downloader ebrains-downloader --diagnosis "Fibrous meningioma"
```

git clone + uv runを使う場合:

```bash
git clone https://github.com/HokuMedAI/ebrains-downloader
cd ebrains-downloader
uv run ebrains-downloader --diagnosis Haemangiopericytoma --output /path/to/output 
```

**Arguments**

| オプション | 説明 | デフォルト |
|---|---|---|
| `--diagnosis` | 診断名（必須、複数指定可） | — |
| `--output` | 出力ディレクトリ | `downloads` |

**Output structure**

```
downloads/
├── annotation.csv
├── Haemangiopericytoma/
│   ├── <uuid>.ndpi
│   └── ...
└── Fibrous meningioma/
    ├── <uuid>.ndpi
    └── ...
```

**Auto-resume**
![実際の動作ログ](/images/screenshot/Screenshot_20260428_161445.jpg)
2番目のファイルで465MBのところでタイムアウトが発生したが、そこから自動で再開して無事完了している。

## おわりに
CLIツールを自作(?)したのは初めてだったが、手作業でダウンロードを行う手間を考えると作ってよかったと思う。  
課題として、6時間ほどでアクセスが途切れてしまうため、100ファイル程度しかダウンロードできない点が挙げられる。
