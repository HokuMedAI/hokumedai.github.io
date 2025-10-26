---
title: "１０月定期勉強会開催報告"
description: "１０月定期勉強会開催報告"
date: 2025-10-25
draft: false
showHero: true
layoutBackgroundBlur: true
---

## 開催概要

- **日時**: 2025/10/25 17:15~
- **人数**: オンラインも含め７名

## 内容
10月25日に定期勉強会を行いました。  
発表者: 村上
題名: 「自己教師あり学習手法: DINO」

---
### 概要
「DINO（self-DIstillation with NO labels）」は、正解ラベルのない画像から意味のある特徴を自ら学び取る自己教師あり学習手法です。  
教師あり学習では大量のデータに正解ラベルを付与する必要があり、膨大な時間とコストがかかります。DINOはこの課題を解決し、大規模な学習を可能にする革新的な手法として注目されています。

DINOは、Contrastive Learningの発展形といわれており、同じ画像から生成されたAugmentationのみを学習に使用します。  
Temperature、Centering、Global/Local Cropといった独自の工夫により、TeacherとStudentモデルの出力が一様な分布に陥ることを防ぎ、効果的な特徴抽出を実現しています。

また、DINOv2やDINOv3といった発展系についても紹介しました。  
DINOv2ではDINOとiBOTの損失関数を組み合わせて使用し、DINOv3では大規模学習時の局所的特徴抽出性能の劣化を防ぐためGram損失を導入するなど、継続的な改良が行われています。

