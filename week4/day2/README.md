# Week 4 — Day 2: Cross-Validation

## Focus
Today I improved model evaluation by moving from a single validation split to **5-fold cross-validation**.

## What I Applied
- 5-fold cross-validation using `cross_val_score`
- `StratifiedKFold` to preserve class proportions
- Mean and standard deviation of F1-scores
- A Pipeline with `StandardScaler` and KNN to avoid leakage during cross-validation
- Comparison with the single validation result from Day 1

## Key Result
The KNN model with `k=7` achieved:

- **CV Mean F1:** 0.9707
- **Standard Deviation:** 0.0159
- **Day 1 Single Validation F1:** 0.9639

The cross-validation results were consistent across the five folds.

## Key Lesson
A single validation score may depend on one particular split. Cross-validation provides stronger evidence about both the model's expected performance and its consistency across different subsets of the data.

Stratification also kept the class distribution consistent across folds, while the final test set remained untouched.