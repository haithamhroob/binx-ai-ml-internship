# Week 4 - Day 3: Bias-Variance & Diagnosing Model Fit

## Focus
Diagnosing underfitting and overfitting using training vs validation F1-score and understanding the bias-variance trade-off.

## What I Applied
- Deliberately created underfit and overfit Decision Trees.
- Compared training F1, validation F1, and their gap.
- Tested different tree depths to study the effect of model complexity.
- Reduced overfitting by constraining `max_depth`.
- Reviewed Ridge (L2) and Lasso (L1) regularization and their effect on coefficients.

## Key Result
The unrestricted tree achieved **1.0000 training F1** but only **0.8764 validation F1** with a **0.1236 gap**.

Limiting the tree to `max_depth=5` improved validation F1 to **0.9091** and reduced the gap to **0.0870**, while keeping training F1 high at **0.9960**.

## Key Lesson
A small train-validation gap does not automatically mean a good model. Both the performance level and the gap must be considered when diagnosing model fit.

Model complexity should be high enough to capture the pattern, but not so high that it fits training-specific details.

The final test set remained untouched during all model-fit and complexity decisions.