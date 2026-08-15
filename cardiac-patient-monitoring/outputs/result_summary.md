# Result Summary

## Model selection

The initial single validation split slightly favored Random Forest:

- Logistic Regression validation F1: **0.786**
- Random Forest validation F1: **0.807**

However, 5-fold stratified cross-validation on the training subset reversed that conclusion:

- Logistic Regression mean CV F1: **0.792**
- Random Forest mean CV F1: **0.750**

Random Forest achieved a training F1 of **1.000**, while its cross-validated F1 dropped to **0.750**, supporting the overfitting concern. Logistic Regression showed a smaller generalization gap and achieved the higher validation ROC-AUC (**0.936 vs. 0.893**).

**Decision:** Logistic Regression was selected.

## Feature engineering

Two interaction features were tested:

- `oldpeak × exang`
- `age × thalach`

Mean CV F1 changed from **0.792** to **0.796**, while validation F1 and validation ROC-AUC remained unchanged.

**Decision:** The engineered features were rejected because the improvement was too small and was not consistently supported by the other evaluation measures.

## Final test evaluation

The selected Logistic Regression pipeline was refitted on all **242 development samples** and evaluated once on the untouched **61-sample final test set**.

| Metric | Score |
|---|---:|
| Accuracy | 0.869 |
| Precision | 0.812 |
| Recall | 0.929 |
| F1 | 0.867 |
| ROC-AUC | 0.958 |

Final confusion-matrix counts:

- True Negatives: **27**
- False Positives: **6**
- False Negatives: **2**
- True Positives: **26**

The final test result was used only as an estimate of the already-selected workflow and was not used to revise model, feature, preprocessing, or configuration decisions.
