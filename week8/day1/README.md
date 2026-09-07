# Week 8 — Day 1

## Sprint 3 Planning & NLP Preprocessing

### Project: IMDB Movie Review Sentiment Analysis

## Overview

During Week 7, the IMDB dataset was used to compare multiple sentiment-analysis approaches:

| Model                        | Test F1 |
| ---------------------------- | ------: |
| Text LSTM                    |  0.7950 |
| Pretrained DistilBERT        |  0.8152 |
| TF-IDF + Logistic Regression |  0.8617 |
| Final Weighted Ensemble      |  0.8939 |

Therefore, Week 8 does not treat IMDB as a new dataset. Instead, Sprint 3 continues the previous work by studying how text preprocessing affects classical and deep-learning representations.

The main question for Day 1 is:

> How can raw reviews be cleaned consistently without removing information that is important for sentiment classification?

Two separate text representations were created because different models require different levels of preprocessing.

---

## Day 1 Objectives

* Define the Sprint 3 goal and backlog.
* Reconstruct the exact Week 7 data split.
* Remove duplicate reviews before sampling.
* Audit overlap between training, validation, and test data.
* Explain word and sub-word tokenization.
* Demonstrate the real DistilBERT tokenizer.
* Apply minimal and classical text preprocessing.
* Preserve sentiment-critical negation words.
* Compare stemming and lemmatization.
* Build reusable preprocessing functions.
* Verify preprocessing quality.
* Save the processed data for Day 2.

---

## Sprint 3 Goal

The goal of Sprint 3 is to transform the Week 7 sentiment models into a reproducible end-to-end system with:

* Model-specific preprocessing.
* Consistent training and prediction inputs.
* Fair model comparison.
* Proper validation and test separation.
* Error analysis.
* Explainability using SHAP.
* Full pipeline integration.

---

## Sprint 3 Backlog

1. Reconstruct and verify the Week 7 dataset split.
2. Build reusable preprocessing functions.
3. Compare TF-IDF and word embeddings.
4. Prevent preprocessing differences between training and prediction.
5. Integrate preprocessing and prediction into one function.
6. Select configurations using validation data.
7. Evaluate the final configuration once on the test set.
8. Analyze false-positive and false-negative predictions.
9. Apply SHAP explainability where appropriate.

---

## Dataset

The Stanford IMDB Large Movie Review Dataset contains:

* 25,000 official training reviews.
* 25,000 official test reviews.
* Binary sentiment labels.
* `0` for negative reviews.
* `1` for positive reviews.

Dataset source:

https://huggingface.co/datasets/stanfordnlp/imdb

---

## Reproducing the Week 7 Split

To ensure a fair comparison with the previous experiments, the same Week 7 splitting procedure was reused.

The final experiment contains:

| Split      | Number of Reviews |
| ---------- | ----------------: |
| Training   |             4,000 |
| Validation |             1,000 |
| Test       |             1,000 |

Exact duplicate reviews are removed before sampling.

The validation set is used to select preprocessing and model settings. The test set remains reserved for one final evaluation.

This prevents a score change from being incorrectly attributed to preprocessing when it may actually be caused by using different reviews.

---

## Data Integrity Audit

The notebook checks:

* Duplicate reviews inside the training set.
* Duplicate reviews inside the validation set.
* Duplicate reviews inside the test set.
* Normalized-text overlap between training and validation.
* Normalized-text overlap between training and test.
* Normalized-text overlap between validation and test.

The overlap check applies basic normalization before comparison because two reviews may differ only in:

* Capitalization.
* HTML tags.
* Repeated spaces.
* Formatting differences.

---

## Why Text Needs Preprocessing

Raw IMDB reviews may contain:

* HTML tags such as `<br />`.
* Capitalization differences.
* Punctuation.
* Numerical ratings.
* Repeated spaces.
* Contractions such as `wasn't`.
* Common words with limited lexical value.

However, these elements are not automatically useless.

For example:

```text
good
not good
wasn't good
```

These phrases have different meanings. Removing `not` would destroy the sentiment signal.

The objective is therefore not to delete as much text as possible. The objective is to reduce unnecessary variation while preserving meaning.

---

## Word and Sub-word Tokenization

### Word Tokenization

NLTK word tokenization separates text into words and punctuation.

Example:

```text
The movie was not great!
```

may become:

```text
["The", "movie", "was", "not", "great", "!"]
```

This tokenization is used in the classical preprocessing pipeline.

### Sub-word Tokenization

DistilBERT uses WordPiece tokenization. Common words may remain complete, while uncommon words may be divided into smaller known pieces.

The notebook uses the actual pretrained DistilBERT tokenizer:

```python
AutoTokenizer.from_pretrained("distilbert-base-uncased")
```

A transformer's tokenizer should not be manually replaced because it must match the vocabulary used during pretraining.

---

## Model-specific Preprocessing

One preprocessing strategy is not appropriate for every model.

The notebook creates three text columns:

| Column           | Description                   | Intended Use                   |
| ---------------- | ----------------------------- | ------------------------------ |
| `text`           | Original review               | Inspection and traceability    |
| `minimal_text`   | Lightly normalized review     | LSTM and DistilBERT            |
| `classical_text` | Linguistically cleaned review | TF-IDF and Logistic Regression |

---

## Minimal Preprocessing

The minimal pipeline performs:

```text
Raw text
→ HTML decoding
→ HTML tag removal
→ Lowercasing
→ Whitespace normalization
```

Minimal preprocessing preserves:

* Natural word order.
* Punctuation.
* Numbers.
* Most sentence structure.
* Contextual information.

This representation is intended for the LSTM and DistilBERT pipelines.

Transformers already contain a pretrained tokenizer and contextual embeddings, so aggressive cleaning may remove useful language information.

---

## Classical Preprocessing

The classical pipeline performs:

```text
Minimal text
→ Negation expansion
→ URL removal
→ Punctuation and number removal
→ Word tokenization
→ Task-aware stop-word removal
→ POS tagging
→ Lemmatization
```

This representation is designed for TF-IDF and classical machine-learning models.

The goal is to reduce vocabulary variation while preserving words that help distinguish positive and negative reviews.

---

## Negation Expansion

Negation is expanded before punctuation removal.

Examples:

```text
wasn't → was not
can't   → can not
won't   → will not
```

If punctuation were removed first, `wasn't` could become:

```text
wasn t
```

The negative meaning would then be lost.

---

## Task-aware Stop-word Removal

Standard stop-word lists may include words that are essential for sentiment analysis.

The notebook protects the following words:

```text
not
no
nor
never
neither
nobody
nothing
nowhere
hardly
barely
scarcely
without
```

Words such as `the`, `is`, and `a` may be removed, while expressions such as `not good` and `hardly enjoyable` remain available.

This demonstrates that preprocessing decisions must depend on the task.

---

## Stemming vs. Lemmatization

### Stemming

Stemming removes word endings using simple rules.

Examples:

```text
studying → studi
movies   → movi
```

It is fast, but it may produce forms that are not real English words.

### Lemmatization

Lemmatization returns a dictionary base form and can use grammatical information.

Examples:

```text
studying → study
running  → run
movies   → movie
better   → good
```

The notebook uses POS-aware lemmatization because its output is more meaningful and easier to interpret when examining TF-IDF features.

---

## Pipeline Verification

The preprocessing functions are tested using examples such as:

```text
The movie was good.
The movie was not good.
The movie wasn't good!
The movie was never good.
The story was hardly enjoyable.
<br /> An AMAZING movie — I loved it!!!
```

Assertions verify that:

* Explicit `not` remains.
* Contracted negation becomes `not`.
* `never` remains.
* `hardly` remains.
* HTML tags are removed.
* No test sentence becomes empty.

---

## Preprocessing Quality Checks

After preprocessing, the notebook checks:

1. Missing values.
2. Empty reviews.
3. Average review length.
4. Negation preservation.
5. Total token count.
6. Unique vocabulary size.
7. Differences between raw, minimal, and classical text.

The vocabulary comparison uses training data only.

A smaller vocabulary is not automatically better. Day 2 will determine whether vocabulary reduction improves validation performance.

---

## Saved Outputs

The notebook creates the following directory:

```text
outputs/week8_day1/
```

It saves three files:

```text
imdb_train_preprocessed.csv
imdb_validation_preprocessed.csv
imdb_test_preprocessed.csv
```

Each file contains:

| Column           | Meaning                   |
| ---------------- | ------------------------- |
| `text`           | Original review           |
| `minimal_text`   | Lightly cleaned review    |
| `classical_text` | Fully cleaned review      |
| `label`          | Numerical sentiment label |
| `sentiment`      | Negative or Positive      |

---

## Day 1 Acceptance Criteria

Day 1 is considered complete when:

* The Week 7 split is successfully reconstructed.
* Exact duplicates are removed before sampling.
* Cross-split overlap is audited.
* Minimal and classical preprocessing functions work.
* Negation-preservation tests pass.
* No cleaned review is missing.
* No cleaned review is empty.
* Training, validation, and test outputs are saved separately.

---

## Day 2 Handoff

Day 2 will use the saved files to:

1. Fit TF-IDF using training data only.
2. Transform validation data using the fitted vectorizer.
3. Compare TF-IDF using `minimal_text` and `classical_text`.
4. Test unigrams and bigrams such as `not good`.
5. Select the best configuration using validation F1.
6. Examine the most important positive and negative features.
7. Compare the selected model with the Week 7 TF-IDF baseline.
8. Evaluate the final configuration once on the untouched test set.
9. Compare TF-IDF with word embeddings.

---

## How to Run

Open the notebook and run all cells from top to bottom:

```text
week8_day1_revised.ipynb
```

The POS-tagging and lemmatization stage may require several minutes when running on a CPU.

The first execution may also download:

* The IMDB dataset.
* NLTK language resources.
* The DistilBERT tokenizer.

---

## Tools Used

* Python
* Jupyter Notebook
* Hugging Face Datasets
* Hugging Face Transformers
* NLTK
* Scikit-learn
* Pandas
* NumPy
* Matplotlib
* Seaborn
* TQDM

---

## Conclusion

Day 1 completed the Sprint 3 planning and NLP preprocessing requirements while maintaining continuity with Week 7.

Instead of applying one aggressive cleaning pipeline to every model, the notebook created two model-specific representations:

* Minimal text for LSTM and DistilBERT.
* Classical text for TF-IDF and Logistic Regression.

The notebook also preserved negation, verified preprocessing behavior, reproduced the previous experiment split, audited data integrity, and prepared reusable outputs for Day 2.
