# Week 6 — Day 5

## Tuning, Evaluation and Sprint Review

This day completed the tuning and final evaluation of the multi-label neural network for PTB-XL ECG classification.

## Work Completed

* Added `EarlyStopping` and `ModelCheckpoint`.
* Tuned one variable at a time:

  * Learning rate
  * Network size
  * Dropout rate
  * Batch size
* Selected the prediction threshold using validation Macro F2.
* Evaluated the final model once on the official test fold.
* Compared the tuned network with Logistic Regression.
* Completed the Sprint Review and Retrospective.

## Final Configuration

* Architecture: `72 → 64 → 32 → 4`
* Learning rate: `0.002`
* Dropout: `0.0`
* Batch size: `32`
* Threshold: `0.15`
* Loss: Binary Cross-Entropy
* Optimizer: Adam

## Final Test Results

| Model                | Precision | Recall |     F1 |     F2 |
| -------------------- | --------: | -----: | -----: | -----: |
| Logistic Regression  |    0.4086 | 0.6642 | 0.5037 | 0.5879 |
| Tuned Neural Network |    0.3827 | 0.8035 | 0.5166 | 0.6561 |

The tuned neural network outperformed the baseline in Recall, F1, and F2. It detected more true disease cases at the cost of lower precision.

## Main Conclusion

Systematic tuning and validation-based threshold selection increased Test Macro Recall from `0.3821` at threshold `0.5` to `0.8035` at threshold `0.15`.
