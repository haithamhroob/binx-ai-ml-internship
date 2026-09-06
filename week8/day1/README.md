# Week 8 — Day 1: Sprint 3 Planning & NLP Preprocessing

## Overview

This notebook begins Sprint 3 by building a reusable text-preprocessing pipeline for sentiment analysis using the Stanford IMDB Movie Review Dataset.

The main goal is to convert inconsistent raw reviews into clean and standardized text without removing words that are essential to sentiment. In particular, negation words such as `not`, `no`, and `nor` are preserved because they can reverse the meaning of a sentence.

## Learning Objectives

By the end of this day, the following objectives were completed:

- Defined the Sprint 3 goal and the integration and evaluation backlog.
- Explained why raw text requires preprocessing.
- Demonstrated word tokenization and explained sub-word tokenization.
- Applied lowercasing, HTML removal, and punctuation removal.
- Removed low-signal stop words while preserving negation.
- Compared stemming with lemmatization.
- Applied POS-aware lemmatization.
- Built and tested a reusable preprocessing pipeline.
- Saved the cleaned training and test data for Day 2.

## Dataset

The project uses the [Stanford IMDB Large Movie Review Dataset](https://huggingface.co/datasets/stanfordnlp/imdb), which contains:

- 25,000 labeled training reviews.
- 25,000 labeled test reviews.
- Two classes: negative (`0`) and positive (`1`).

To keep POS tagging and lemmatization practical on a CPU, balanced subsets were selected:

| Split | Negative | Positive | Total |
|---|---:|---:|---:|
| Training | 5,000 | 5,000 | 10,000 |
| Test | 2,500 | 2,500 | 5,000 |

The inspection found no missing text. It also identified 18 duplicated reviews inside the training sample and 8 inside the test sample. These duplicates are documented and will be handled with a train-test overlap check before model evaluation on Day 2.

## Sprint 3 Backlog

1. Build and verify a reusable text-cleaning pipeline.
2. Compare TF-IDF and word embeddings using the same cleaned data.
3. Integrate preprocessing and prediction into one end-to-end function.
4. Keep training-time and prediction-time preprocessing consistent.
5. Evaluate the final model against the previous baseline.
6. Analyze the confusion matrix and misclassified examples.
7. Explain predictions using SHAP where applicable.

## Preprocessing Workflow

The raw reviews pass through the following ordered pipeline:

1. Decode HTML entities and remove HTML tags.
2. Convert text to lowercase.
3. Expand negation contractions such as `wasn't` into `was not`.
4. Remove URLs, punctuation, numbers, and repeated spaces.
5. Split the text into word tokens.
6. Remove common stop words while preserving `not`, `no`, and `nor`.
7. Identify each token's part of speech.
8. Apply POS-aware lemmatization.

The order is important. Negation is expanded before punctuation removal so that a word such as `wasn't` does not become `wasn t` and lose its negative meaning.

## Word and Sub-word Tokenization

Word tokenization separates a sentence into words and punctuation. It is suitable for the TF-IDF pipeline planned for Day 2.

Sub-word tokenization divides unfamiliar words into smaller known pieces. It is commonly used by pretrained transformers and should be performed using the tokenizer that belongs to the selected transformer model.

## Stemming vs. Lemmatization

Stemming removes word endings using simple rules and may produce non-dictionary forms. For example, `studies` and `studying` were reduced to `studi`.

Lemmatization aims to return valid base forms. With part-of-speech information:

- `studies` became `study`.
- `running` became `run`.
- `better` became `good`.
- `movies` became `movie`.

Lemmatization was selected because it produces more interpretable text and better preserves meaning.

## Task-specific Stop-word Decision

The default NLTK English stop-word list contains the word `not`. Removing it would make `good` and `not good` appear too similar.

Therefore, the stop-word list was customized to preserve:

```text
not, no, nor
```

Automated assertions verified that explicit negation and contractions remained after preprocessing.

## Results

The preprocessing pipeline completed successfully for all selected reviews.

| Result | Value |
|---|---:|
| Training reviews processed | 10,000 |
| Test reviews processed | 5,000 |
| Missing cleaned reviews | 0 |
| Empty cleaned reviews | 0 |
| Average raw words per training review | 232.20 |
| Average cleaned words per training review | 121.56 |
| Average-length reduction | 47.65% |
| Cleaned training reviews containing `not` | 8,266 |

For a sample of 1,000 training reviews:

| Stage | Total Tokens | Unique Tokens |
|---|---:|---:|
| Raw text | 239,839 | 17,729 |
| Cleaned text | 121,693 | 14,610 |

The total token count decreased by approximately 49.26%, while the number of unique tokens decreased by approximately 17.59%. The most frequent cleaned words remained relevant to movie reviews, including `movie`, `film`, `good`, `character`, `watch`, and `story`.

## Output Files

Running the final notebook cell creates:

```text
outputs/week8_day1/imdb_train_cleaned.csv
outputs/week8_day1/imdb_test_cleaned.csv
```

Each file contains:

- `text`: original review.
- `cleaned_text`: processed review.
- `label`: numerical sentiment label.
- `sentiment`: readable class name.

## Tools Used

- Python
- NLTK
- Hugging Face Datasets
- Pandas and NumPy
- Matplotlib and Seaborn
- Jupyter Notebook
- Git and GitHub

## How to Run

1. Open `week8_day1_complete.ipynb` in Jupyter Notebook or Visual Studio Code.
2. Select the project's Python environment.
3. Run all cells in order.
4. Confirm that all pipeline assertions pass.
5. Verify that the two cleaned CSV files are created in `outputs/week8_day1/`.

## Conclusion

Day 1 produced a documented and reusable text-cleaning pipeline that tokenizes and standardizes IMDB reviews, applies task-aware stop-word removal, and uses POS-aware lemmatization while preserving sentiment-critical negation.

The cleaned training and test data are now ready for Day 2, where TF-IDF and word embeddings will be compared using the same sentiment-classification task.
