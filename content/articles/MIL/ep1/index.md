---
title: "論文紹介(SSR-Mam2MIL)"
description: "論文紹介～SSR-Mam2MIL: Spatial sequence reordering Mamba2 based multiple instance learning for computational pathology"
date: 2025-11-12T17:20:11+09:00
draft: true
showHero: true
layoutBackgroundBlur: true
categories: ["MIL"]
tags: ["MIL", "Mamba"]
author: "yamada"
---

### 背景
MIL課題に対して、今までのモデルたちはIlseに代表されるように  
インスタンスを、
- 独立している(independent)
- 理想的に分布している(indentically distributed)
  
ものとして考えてきた (i.i.d.というらしい)

#### 紹介されているMILモデル ↓
1.  [AB-MIL](https://proceedings.mlr.press/v80/ilse18a/ilse18a.pdf)
2.  [CLAM](https://www.nature.com/articles/s41551-020-00682-w)
3.  [DSMIL](https://openaccess.thecvf.com/content/CVPR2021/papers/Li_Dual-Stream_Multiple_Instance_Learning_Network_for_Whole_Slide_Image_Classification_CVPR_2021_paper.pdf)
4.  [DTFD-MIL](https://openaccess.thecvf.com/content/CVPR2022/papers/Zhang_DTFD-MIL_Double-Tier_Feature_Distillation_Multiple_Instance_Learning_for_Histopathology_Whole_CVPR_2022_paper.pdf)


#### Transformer系のMILモデル
[Transformer](https://proceedings.neurips.cc/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf) を踏襲したものもいくつか存在する
1. [TransMIL](https://proceedings.neurips.cc/paper_files/paper/2021/file/10c272d06794d3e5785d5e7c5356e9ff-Paper.pdf)
2. [MMP](https://arxiv.org/pdf/2407.00224)： WSIの形態的特徴 ＋ トランスクリプトームというmahmoodお手製のなんかすごいやつ

#### Mambaモデルの台頭
State Space Models (SSMs)という状態方程式を用いたモデルが、長いコンテキストの課題においていいパフォーマンスを発揮するらしい    
アーキテクチャはよくわからないが、トランスフォーマー同様でMIL課題用のaggregatorも色々出現しているようだ
- [Mambaモデル](https://openreview.net/pdf?id=tEYskw1VY2)
- Mamba系のMILモデル
    1. [MamMIL](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10822552)
    2. [MambaMIL](https://github.com/isyangshu/MambaMIL)

けれど、上記のモデルも位置情報はロスしてしまっているらしい

---
### 方法
#### SSR-Mam2MILモデル
先程のMambaMILをベースに座標から、位置情報を特徴量に組み込んでaggregateするモデルである。
座標からk-meansでクラスタリングして、各パッチの順番について

- クラスター内のものは連続するようにするか、クラスターを無視して座標の値に従うようにするか
- 縦に進むか横に進むか

以上の観点に基づいて特徴量を”連結する”(のだと思う)

詳しいアーキテクチャや実装はまた後日





