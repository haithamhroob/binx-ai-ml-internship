# Week 8 - Day 2: Text Representation

## Overview

This notebook continues the Week 8 Day 1 IMDB sentiment-analysis pipeline. The preprocessed training, validation, and test splits are converted into numerical representations using TF-IDF and pretrained GloVe word embeddings.

The goal is to compare a task-specific sparse representation with a general semantic dense representation while preventing data leakage.

## Dataset

The notebook reuses the files produced on Day 1:

- Training: 4,000 reviews
- Validation: 1,000 reviews
- Test: 1,000 reviews
- Labels: Negative (`0`) and Positive (`1`)
- Text versions: `minimal_text` and `classical_text`

## Topics Covered

- Converting text into numeric vectors
- Bag of Words and TF-IDF
- `fit`, `transform`, and data-leakage prevention
- Sparse matrices
- Unigrams and bigrams
- `max_features`, `min_df`, `max_df`, and `sublinear_tf`
- Logistic Regression feature weights
- Word embeddings and semantic geometry
- Word2Vec: CBOW and Skip-gram
- Pretrained GloVe embeddings
- OOV words and cosine similarity
- Mean pooling for complete-review vectors
- Fixed embeddings versus BERT contextual embeddings

## TF-IDF Experiment

TF-IDF configurations were trained on the training split and selected using validation F1 only. The best configuration used:

- `minimal_text`
- Unigrams and bigrams
- 10,000 maximum features
- `min_df=2`
- `max_df=0.95`
- `sublinear_tf=True`

### TF-IDF Results

| Metric | Score |
|---|---:|
| Validation F1 | 0.8808 |
| Test Accuracy | 0.8590 |
| Test Precision | 0.8519 |
| Test Recall | 0.8705 |
| Test F1 | 0.8611 |
| Test ROC-AUC | 0.9441 |

The model correctly classified 422 negative and 437 positive test reviews. Its strongest features included negative terms such as `bad`, `worst`, and `poor`, and positive terms such as `great`, `excellent`, and `wonderful`.

## GloVe Experiment

Pretrained `glove-wiki-gigaword-100` embeddings were used. The model contains 400,000 vocabulary terms, with 100 dimensions per word. Each review was represented by the mean of its known word vectors, while OOV words were skipped.

### GloVe Results

| Metric | Score |
|---|---:|
| Validation F1 | 0.7972 |
| Test Accuracy | 0.7860 |
| Test Precision | 0.7975 |
| Test Recall | 0.7689 |
| Test F1 | 0.7830 |
| Test ROC-AUC | 0.8645 |

## Representation Comparison

| Representation | Validation F1 | Test F1 |
|---|---:|---:|
| Tuned TF-IDF | 0.8808 | 0.8611 |
| Averaged pretrained GloVe | 0.7972 | 0.7830 |

TF-IDF performed better because it learned sentiment-specific word and bigram importance directly from the IMDB training reviews. GloVe captured useful semantic relationships, but averaging the word vectors removed order and diluted important sentiment signals.

## Week 7 Comparison

| Model | Test F1 |
|---|---:|
| Final Weighted Ensemble | 0.8939 |
| Week 7 TF-IDF + Logistic Regression | 0.8617 |
| Week 8 Tuned TF-IDF + Logistic Regression | 0.8611 |
| Pretrained DistilBERT | 0.8152 |
| Text LSTM | 0.7950 |

The Week 8 tuning improved validation performance but did not produce a meaningful test improvement over the Week 7 TF-IDF result. The weighted ensemble remained the strongest overall model.

## Running the Notebook

Place the notebook inside `week8/day2`. The Day 1 CSV files are expected at:

```text
../day1/outputs/week8_day1
```

Then run all cells in order. The first GloVe run downloads the pretrained embedding model. Day 2 output tables are saved under:

```text
outputs/week8_day2
```

## Conclusion

TF-IDF was selected as the better standalone representation for this IMDB experiment. Pretrained embeddings provide semantic knowledge, while contextual embeddings such as BERT improve on fixed embeddings by representing words according to their sentence context.
