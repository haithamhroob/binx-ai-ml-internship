# Week 4 — Model Evaluation, Tuning & Leak-Free ML Workflows

## Overview

Week 4 focused on making machine-learning evaluation and model selection more reliable.

Using the Breast Cancer Wisconsin classification problem, I progressively moved from a simple validation workflow to a complete end-to-end pipeline that combines feature engineering, preprocessing, cross-validation, and hyperparameter tuning while keeping the final test set independent.

## Daily Work

### Day 1 — Train, Validation and Test Sets

- Split the data into training, validation, and final test sets.
- Used stratification to preserve class proportions.
- Selected KNN hyperparameters using validation data rather than the test set.
- Selected `k = 7` as a tie-breaking choice among the strongest validation results.
- Final Test F1: **0.925**

**Key lesson:**  
The test set must remain independent not only from training, but also from model-selection decisions.

### Day 2 — Cross-Validation

- Replaced dependence on one validation split with 5-fold Stratified K-Fold cross-validation.
- Combined `StandardScaler` and KNN in a Pipeline to keep scaling correct inside each fold.
- Compared mean performance and fold-to-fold variability.

**Result:**

- Mean F1: **0.9575**
- Standard deviation: **0.0116**

**Key lesson:**  
Cross-validation provides stronger evidence about model reliability than a single validation score.

### Day 3 — Bias, Variance and Model Fit

Experimented with Decision Tree complexity to deliberately observe different fitting behaviors.

- Depth 1 → underfitting
- Unrestricted tree → overfitting
- Depth 5 → improved balance between training fit and validation performance

Also reviewed the concepts behind L1 and L2 regularization.

**Key lesson:**  
Model fit should be diagnosed using both the performance level and the train-validation gap, not from either one alone.

### Day 4 — Feature Engineering & Hyperparameter Tuning

Tested engineered features as hypotheses rather than assuming that more features improve the model.

Feature-engineering results:

| Feature Set | Mean F1 |
|---|---:|
| Baseline | 0.9575 |
| Radius ratio | **0.9605** |
| Concavity gap | 0.9546 |
| Both features | 0.9513 |

`radius ratio` was retained for the next stage.

GridSearchCV then tuned:

- `n_neighbors`
- `weights`

The strongest configuration used:

- `n_neighbors = 7`
- `weights = uniform`

Best CV F1: **0.9605 ± 0.0157**

`distance` weighting tied with `uniform` at `k = 7`, while `n_neighbors` had the larger overall effect on performance.

**Key lesson:**  
Feature engineering changes the representation of the problem, while hyperparameter tuning changes how the model uses that representation.

### Day 5 — End-to-End Tuned Pipeline

Built a complete workflow using:

- `FunctionTransformer`
- `ColumnTransformer`
- `StandardScaler`
- `OneHotEncoder`
- `Pipeline`
- `GridSearchCV`
- KNN

The entire preprocessing and modeling workflow was tuned together using cross-validation.

GridSearchCV selected:

- `n_neighbors = 7`
- `weights = uniform`
- categorical radius representation = dropped

**Final results:**

- Best CV F1: **0.9605 ± 0.0157**
- Final Test F1: **0.9231**
- Malignant Recall: **0.8571**
- Malignant Precision: **1.0000**

The final confusion matrix showed that 6 of 42 malignant samples were classified as benign.

The test result was reported without making further modeling changes.

## Tools & Techniques

- Scikit-learn
- Pandas
- Train / Validation / Test Splitting
- Stratified K-Fold Cross-Validation
- F1-score
- Bias–Variance Diagnosis
- Feature Engineering
- StandardScaler
- OneHotEncoder
- FunctionTransformer
- ColumnTransformer
- Pipeline
- GridSearchCV
- RandomizedSearchCV concepts
- Confusion Matrix

## Main Takeaway

The main improvement this week was not simply increasing model scores.

The workflow became more trustworthy:

**Separate evaluation → Cross-validation → Diagnose fit → Engineer features → Tune systematically → Build one leak-free end-to-end pipeline**

A reliable ML workflow requires disciplined evaluation, reproducible preprocessing, evidence-based model decisions, and a final test set that remains independent until development is complete.