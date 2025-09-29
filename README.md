# CNN vs ViT on SpaceNet (Balanced vs Imbalanced)

This repo accompanies the paper:

- **Convolutional Neural Nets vs Vision Transformers: A SpaceNet Case Study with Balanced vs Imbalanced Regimes**
- PDF: `paper/Research_paper_Neural_Nets_vs_Vision_Transformer.pdf`

## Frozen Kaggle Notebooks (v1.0)
- Imbalanced — EfficientNetB0 (40 ep): https://www.kaggle.com/code/akshar27/new-dataset-cnn-epoch-40
- Imbalanced — ViT-Base (40 ep): https://www.kaggle.com/code/akshar27/new-dataset-vit-epoch-40
- Balanced — EfficientNetB0 (40 ep): https://www.kaggle.com/code/akshargothi27/space-balance-efficienet
- Balanced — ViT-Base (40 ep): https://www.kaggle.com/code/akshargothi27/space-balance-vit-base

> Each **Version** page includes seed, GPU (P100), and the dataset snapshot.

## Minimal Artifacts (to verify metrics)
Small, text-first artifacts are included for each run:
- `outputs/<run>/metrics.json` — accuracy, macro-F1, precision/recall
- `outputs/<run>/predictions.csv` — per-image predictions + per-class probs
- `outputs/<run>/confusion_matrix.csv` (+ `figures/confusion_matrix.png`)

## Data
- SpaceNet (Kaggle): https://www.kaggle.com/datasets/razaimam45/spacenet-an-optimally-distributed-astronomy-data  
- Balanced dataset: https://www.kaggle.com/datasets/akshargothi27/spacenet-balance-dataset  
- Imbalanced dataset: https://www.kaggle.com/datasets/arunamarkurali/spacenet  
- Deterministic 70:20:10 manifests live in `manifests/` for both splits.

## How to Reproduce
1) Open a pinned Kaggle notebook above → **Copy & Edit** → **Run All**.  
2) Artifacts appear under `/kaggle/working/outputs/<run>/`.  
3) Manifests are emitted to `/kaggle/working/manifests/<split>/`.

## Citation
See `CITATION.cff`. If you use this work, please cite the paper.
