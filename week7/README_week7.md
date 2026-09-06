# Week 7 — CNNs, RNNs, Attention & Transformers

## Overview

Week 7 focused on selecting and evaluating suitable deep-learning architectures for different data types: images, sequential signals, and text. The week covered CNNs, RNNs, LSTMs, attention, Transformers, transfer learning, model comparison, and Sprint 2 evaluation.

## Daily Progress

### Day 1 — Sprint 2 Planning & CNN Fundamentals

- Defined the Sprint 2 goal and backlog.
- Explored the melanoma image dataset: **13,879 images** across Benign and Malignant classes.
- Applied manual edge-detection filters to understand convolution and feature maps.
- Examined padding, stride, and parameter sharing.
- Selected a **2D CNN** as the appropriate architecture for image classification.

### Day 2 — CNNs & Transfer Learning

- Built a CNN from scratch for melanoma classification.
- Added pooling and image augmentation.
- Tested transfer learning and fine-tuning with **MobileNetV2**.
- Compared models using validation F2 and malignant recall.
- Selected the CNN from scratch and evaluated it once on the untouched test set.

| Metric | Test Result |
|---|---:|
| Accuracy | 0.8970 |
| Precision | 0.9161 |
| Malignant Recall | 0.8740 |
| F1 Score | 0.8946 |
| F2 Score | 0.8821 |

### Day 3 — RNNs & LSTMs

- Used the **MIT-BIH ECG Heartbeat** dataset with five heartbeat classes.
- Compared a Dense baseline, Simple RNN, and LSTM.
- Applied class weights to address class imbalance.
- Tested whether the LSTM learned temporal order by shuffling the sequence steps.
- The Dense baseline achieved the best validation result and was selected.

| Metric | Final Test Result |
|---|---:|
| Accuracy | 0.7632 |
| Balanced Accuracy | 0.7985 |
| Macro Recall | 0.7985 |
| Macro F1 | 0.5448 |
| Macro F2 | 0.6182 |

### Day 4 — Attention & Transformers

- Studied attention, self-attention, and Query–Key–Value concepts.
- Explained positional encoding and Transformer parallelism.
- Used a balanced **IMDb sentiment** split: 4,000 training, 1,000 validation, and 1,000 test reviews.
- Compared a trained Text LSTM with pretrained DistilBERT.

| Model | Accuracy | Precision | Recall | F1 |
|---|---:|---:|---:|---:|
| Text LSTM | 0.7880 | 0.7726 | 0.8187 | 0.7950 |
| DistilBERT | 0.8200 | 0.8411 | 0.7908 | 0.8152 |

**DistilBERT** was selected based on its higher F1 score.

### Day 5 — Core Model Improvement & Sprint 2 Review

- Rebuilt a TF-IDF and Logistic Regression baseline.
- Fine-tuned DistilBERT gradually on the IMDb domain.
- Tuned classification thresholds using validation data only.
- Combined TF-IDF and DistilBERT using a soft-voting ensemble.
- Evaluated the final model once on the untouched test set.

| Final Configuration | Value |
|---|---:|
| TF-IDF weight | 0.775 |
| DistilBERT weight | 0.225 |
| Classification threshold | 0.495 |
| Test Accuracy | 0.8920 |
| Test Precision | 0.8818 |
| Test Recall | 0.9064 |
| Test F1 | **0.8939** |

The final ensemble improved F1 by **0.0787** over the initial DistilBERT result.

## Datasets Used

| Task | Dataset | Data Type |
|---|---|---|
| Melanoma classification | Skin-lesion images | Images |
| Heartbeat classification | MIT-BIH ECG Heartbeat | Sequential signals |
| Sentiment classification | IMDb movie reviews | Text |

## Main Tools

- Python and Jupyter/Google Colab
- NumPy, Pandas, Matplotlib, and Seaborn
- Scikit-learn
- TensorFlow and Keras
- Hugging Face Transformers and Datasets
- Git and GitHub

## Key Conclusions

- The architecture should match the data type and evaluation objective.
- A more complex model does not always produce a better result.
- Validation data must be used for model and threshold selection.
- The test set should remain untouched until final evaluation.
- Combining classical machine learning with a Transformer produced the strongest Week 7 result.

## Final Outcome

Sprint 2 produced complete experiments for image, sequence, and text classification. The selected core architecture was **DistilBERT**, and the final **TF-IDF + fine-tuned DistilBERT ensemble** achieved a test F1 score of **0.8939**.
