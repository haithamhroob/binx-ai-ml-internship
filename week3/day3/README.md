# BinX Tech AI & ML Internship

## Week 3 - Day 3: Logistic Regression & Classification Metrics

### Summary

Built and evaluated a binary Logistic Regression classifier using the Breast Cancer Wisconsin dataset from Scikit-learn. The workflow connects the mathematical idea behind Logistic Regression to a complete classification pipeline: probability estimation, threshold-based prediction, confusion-matrix analysis, classification metrics, baseline comparison, and ROC-AUC evaluation.

The positive class was intentionally defined as **Malignant (`1`)** so that false negatives and recall have a clear real-world interpretation.

### Dataset

- **Source:** Scikit-learn Breast Cancer Wisconsin dataset
- **Samples:** 569
- **Features:** 30 numeric features
- **Target used in this notebook:**
  - `0` = Benign
  - `1` = Malignant
- **Class distribution:**
  - Benign: 357 samples (~62.7%)
  - Malignant: 212 samples (~37.3%)

### Workflow

- Loaded the dataset and defined the clinically important class as the positive class.
- Inspected the target distribution before training.
- Performed an 80/20 train/test split using `random_state=42` and `stratify=y`.
- Standardized the features without data leakage:
  - `fit_transform()` on the training set.
  - `transform()` only on the test set.
- Trained `LogisticRegression(max_iter=1000)`.
- Inspected learned coefficients and the intercept.
- Compared `predict()` with `predict_proba()`.
- Verified the default probability-to-class threshold behavior.
- Evaluated predictions using a confusion matrix.
- Calculated accuracy, precision, recall, F1-score, and ROC-AUC.
- Compared the model against a majority-class `DummyClassifier` baseline.
- Plotted and interpreted the ROC curve.

### Results

| Metric | Logistic Regression | Majority Baseline |
|---|---:|---:|
| Accuracy | 0.9649 | 0.6316 |
| Precision | 0.9750 | 0.0000 |
| Recall | 0.9286 | 0.0000 |
| F1-score | 0.9512 | 0.0000 |
| ROC-AUC | 0.9960 | 0.5000 |

### Confusion Matrix

The test-set confusion matrix was:

```text
[[71,  1],
 [ 3, 39]]
```

- **TN = 71:** benign cases correctly classified as benign.
- **FP = 1:** one benign case incorrectly flagged as malignant.
- **FN = 3:** three malignant cases incorrectly classified as benign.
- **TP = 39:** malignant cases correctly detected.

### Interpretation

The classifier performs strongly and clearly beats the majority-class baseline. Precision is very high, which means most cases predicted as malignant are actually malignant.

Recall is slightly lower because the model missed three malignant cases. In a screening-style problem, these false negatives are especially important, so model quality should not be judged by accuracy alone.

The ROC-AUC of approximately **0.996** indicates excellent separation between malignant and benign cases across decision thresholds. If threshold tuning were required for deployment, it should be performed using validation data or cross-validation rather than repeatedly optimizing against the test set.

### Visualizations

#### Target Class Distribution
- **Why:** checks whether class imbalance may affect metric interpretation.
- **X-axis:** class.
- **Y-axis:** number of samples.
- **Decision:** use richer classification metrics rather than relying only on accuracy.

#### Confusion Matrix
- **Why:** exposes the exact types of correct and incorrect predictions.
- **X-axis:** predicted class.
- **Y-axis:** true class.
- **Decision:** focus on false negatives when the positive class is clinically important.

#### ROC Curve
- **Why:** evaluates the classifier across multiple decision thresholds.
- **X-axis:** False Positive Rate.
- **Y-axis:** True Positive Rate / Recall.
- **Decision:** assess the model's discrimination independently of one fixed threshold.

### Key Learning Outcomes

- Logistic Regression performs classification by applying a sigmoid function to a linear score.
- `predict_proba()` returns class probabilities while `predict()` returns final class decisions.
- A confusion matrix provides the foundation for interpreting TP, TN, FP, and FN.
- Accuracy can be misleading when classes are imbalanced.
- Precision measures the reliability of positive predictions.
- Recall measures how many actual positive cases are detected.
- F1-score balances precision and recall.
- ROC-AUC measures discrimination across thresholds.
- Metric selection should reflect the real-world cost of mistakes.
- Preprocessing must be fit on training data only to prevent data leakage.
- A model should be compared against a simple baseline before claiming useful predictive value.

### Tools Used

- Python
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- Jupyter Notebook

### Files

- `day3.ipynb` — complete narrated Day 3 workflow.
- `README.md` — summary, results, interpretation, and learning outcomes.
