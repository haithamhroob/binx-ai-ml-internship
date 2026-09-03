# Week 7 - Day 5: Advancing the Core Model and Sprint 2 Review

## Overview

This notebook completes Day 5 of Week 7 and closes Sprint 2 of the IMDb sentiment-classification project.

Day 4 compared a Text LSTM with a pre-trained DistilBERT model. DistilBERT achieved the stronger overall result and was selected as the project's core text architecture.

During Day 5, the project was advanced by:

* Building a reproducible TF-IDF and Logistic Regression baseline.
* Partially fine-tuning DistilBERT on IMDb reviews.
* Selecting the best checkpoint using validation data.
* Tuning the classification threshold.
* Combining TF-IDF and DistilBERT using a weighted ensemble.
* Comparing the final model with the baseline, Sprint 1, and the initial Sprint 2 models.
* Completing the Sprint Review and Retrospective.

## Learning Objectives

* Select an architecture appropriate for natural-language text.
* Build a fast and reproducible classical baseline.
* Apply transfer learning and gradual unfreezing to DistilBERT.
* Tune model decisions using validation data only.
* Log experiment configurations, timings, and metrics.
* Compare Sprint 2 results with previous models.
* Complete the Sprint Review and Retrospective.

## Dataset

The project uses the IMDb Movie Reviews dataset for binary sentiment classification.

| Label | Sentiment |
| ----: | --------- |
|     0 | Negative  |
|     1 | Positive  |

A CPU-friendly subset was used:

| Split      | Samples | Negative | Positive |
| ---------- | ------: | -------: | -------: |
| Training   |   4,000 |    1,997 |    2,003 |
| Validation |   1,000 |      499 |      501 |
| Test       |   1,000 |      498 |      502 |

The same deterministic split used during Day 4 was retained to keep the historical model comparison consistent.

The test set remained isolated during training, checkpoint selection, threshold tuning, and ensemble-weight selection.

## Experimental Workflow

The experiment followed these stages:

1. Load and clean the IMDb dataset.
2. Reproduce the Day 4 data split.
3. Audit missing values and normalized-text overlap.
4. Build a TF-IDF and Logistic Regression baseline.
5. Load the saved Day 4 LSTM and DistilBERT results.
6. Fine-tune the DistilBERT classification head.
7. Unfreeze the final Transformer block.
8. Select the best checkpoint using validation F1-score.
9. Tune the DistilBERT classification threshold.
10. Evaluate the fine-tuned model on the untouched test set.
11. Build a weighted TF-IDF and DistilBERT ensemble.
12. Compare all models and save the experiment evidence.

## Evaluation Metrics

The following metrics were used:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix
* Training time
* Inference time

F1-score was used as the main model-selection metric because it balances Precision and Recall:

$$
F1 =
2 \times
\frac{\text{Precision} \times \text{Recall}}
{\text{Precision} + \text{Recall}}
$$

## Reconstructed Baseline

The reconstructed Week 6-style baseline used:

* TF-IDF unigram features.
* Maximum vocabulary size of `20,000`.
* Logistic Regression.
* Validation-tuned decision threshold of `0.47`.

This baseline was fast, reproducible, and provided a strong classical reference for evaluating the added complexity of the Transformer model.

Its test results were:

* Accuracy: `0.8520`
* Precision: `0.8116`
* Recall: `0.9183`
* F1-score: `0.8617`

## Sprint 1 Model

The Sprint 1 neural-network reference was the Text LSTM developed during Day 4.

Its saved test results were:

* Accuracy: `0.7880`
* Precision: `0.7726`
* Recall: `0.8187`
* F1-score: `0.7950`

## Initial Sprint 2 DistilBERT

The initial Transformer model was:

```text
distilbert-base-uncased-finetuned-sst-2-english
```

Before adapting it to the IMDb training subset, it achieved:

* Accuracy: `0.8200`
* Precision: `0.8411`
* Recall: `0.7908`
* F1-score: `0.8152`

## Partial DistilBERT Fine-Tuning

Training the complete DistilBERT model on CPU would be expensive and could increase overfitting on only `4,000` training reviews.

Gradual unfreezing was therefore used.

| Stage      | Trainable components                   | Epochs | Learning rate |
| ---------- | -------------------------------------- | -----: | ------------: |
| Head only  | Pre-classifier and classifier          |      1 |        0.0005 |
| Last block | Final Transformer block and classifier |      2 |       0.00002 |

The head-only stage produced the best validation result:

* Validation Accuracy: `0.8550`
* Validation Precision: `0.8463`
* Validation Recall: `0.8683`
* Validation F1-score: `0.8571`

Unfreezing the final Transformer block reduced validation F1 slightly. Therefore, the notebook correctly restored the head-only checkpoint instead of keeping the final epoch.

After threshold tuning, the selected DistilBERT threshold was `0.51`.

The partially fine-tuned DistilBERT achieved:

* Accuracy: `0.8450`
* Precision: `0.8305`
* Recall: `0.8685`
* F1-score: `0.8491`

Fine-tuning improved DistilBERT F1-score from `0.8152` to `0.8491`.

## Final Ensemble

The TF-IDF baseline achieved strong lexical Recall, while DistilBERT provided contextual predictions.

A weighted soft-voting ensemble was used:

$$
p_{\text{ensemble}}
=
\alpha p_{\text{DistilBERT}}
+
(1-\alpha)p_{\text{TF-IDF}}
$$

The ensemble weight and threshold were selected using validation data only.

The selected configuration was:

* DistilBERT weight: `0.225`
* TF-IDF weight: `0.775`
* Classification threshold: `0.500`
* Validation F1-score: `0.8975`

The final ensemble achieved the following test results:

* Accuracy: `0.8920`
* Precision: `0.8833`
* Recall: `0.9044`
* F1-score: `0.8937`

## Final Model Comparison

| Stage               | Model                           |   Accuracy |  Precision |     Recall |   F1-score |
| ------------------- | ------------------------------- | ---------: | ---------: | ---------: | ---------: |
| Week 6 baseline     | TF-IDF + Logistic Regression    |     0.8520 |     0.8116 |     0.9183 |     0.8617 |
| Sprint 1            | Text LSTM                       |     0.7880 |     0.7726 |     0.8187 |     0.7950 |
| Sprint 2 initial    | Pre-trained DistilBERT          |     0.8200 |     0.8411 |     0.7908 |     0.8152 |
| Sprint 2 fine-tuned | Partially fine-tuned DistilBERT |     0.8450 |     0.8305 |     0.8685 |     0.8491 |
| Sprint 2 final      | TF-IDF + DistilBERT Ensemble    | **0.8920** | **0.8833** | **0.9044** | **0.8937** |

## Main Findings

* Fine-tuning improved DistilBERT F1-score by `0.0339`.
* The classical TF-IDF baseline remained stronger than DistilBERT alone.
* Combining lexical and contextual predictions produced the strongest result.
* The ensemble improved F1-score over the TF-IDF baseline by `0.0320`.
* The ensemble improved F1-score over the Sprint 1 LSTM by `0.0987`.
* The ensemble improved F1-score over the initial DistilBERT by `0.0785`.
* Validation F1-score was `0.8975`, while test F1-score was `0.8937`.
* The small validation-test difference indicates stable generalization.
* The final ensemble provided a better Precision-Recall balance than TF-IDF alone.

## Error Analysis

The final ensemble's most confident errors included:

* Reviews containing mixed positive and negative statements.
* Sarcastic or indirect sentiment.
* Negative reviews containing many positive descriptive words.
* Reviews whose final opinion differed from their opening description.
* Long reviews where important information may occur after the `128`-token limit.

This analysis demonstrates that high model confidence does not always mean the prediction is correct.

## Experiment Logging

The notebook records:

* Dataset split statistics.
* Data-integrity checks.
* Baseline threshold search.
* DistilBERT training configurations.
* Training loss for each epoch.
* Validation metrics for each checkpoint.
* DistilBERT threshold search.
* Ensemble weight and threshold search.
* Final model comparison.
* Confusion matrices.
* High-confidence classification errors.
* Training and inference times.

The generated evidence is saved under:

```text
outputs/week7_day5/
```

The output files include:

```text
split_summary.csv
baseline_threshold_search.csv
distilbert_threshold_search.csv
ensemble_search.csv
training_log.csv
final_model_comparison.csv
most_confident_errors.csv
```

## Sprint Review

Sprint 2 successfully produced a final model that outperformed:

* The reconstructed Week 6-style baseline.
* The Sprint 1 Text LSTM.
* The initial Sprint 2 DistilBERT.
* The partially fine-tuned DistilBERT.

The final TF-IDF and DistilBERT ensemble achieved the highest test F1-score of `0.8937`.

The experiment also demonstrated that the most complex standalone model is not automatically the strongest. The best result came from combining the lexical strength of TF-IDF with the contextual understanding of DistilBERT.

## Sprint Retrospective

### What Went Well

* All models were evaluated on the same deterministic test subset.
* The validation set was used for checkpoint and threshold selection.
* The test set remained isolated until final evaluation.
* Gradual unfreezing kept Transformer training practical on CPU.
* The best checkpoint was restored automatically.
* Experiment configurations and metrics were logged clearly.
* The final ensemble exceeded all previous results.

### What Can Be Improved

* Only `4,000` reviews were used for training.
* Reviews were truncated to `128` tokens.
* Training was completed without GPU acceleration.
* Only the final Transformer block was tested during gradual unfreezing.
* A wider hyperparameter search may improve DistilBERT further.
* Model weights were not saved because of their large size.

### Sprint 3 Action

Use GPU-backed experiments to compare sequence lengths of `128` and `256`, test additional fine-tuning configurations, and evaluate probability calibration before extending the project toward NLP/CV integration.

## Repository Workflow

The completed notebook and small generated result files are uploaded directly to GitHub.

No Pull Request or supervisor-approval step is required for this workflow.

Large model-weight files should not be committed unless Git LFS or external model storage is configured.

## Conclusion

Day 5 completed the full Sprint 2 model-development cycle.

The final TF-IDF and DistilBERT ensemble achieved:

* Accuracy: `0.8920`
* Precision: `0.8833`
* Recall: `0.9044`
* F1-score: `0.8937`

This was the strongest result across all evaluated models and successfully satisfied the Sprint 2 improvement objective.
