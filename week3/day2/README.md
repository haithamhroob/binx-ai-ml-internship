# Week 3 — Day 2: Linear Regression

## Overview

This project applies Linear Regression to the scikit-learn Diabetes dataset.

The notebook covers:
- BMI-only Linear Regression
- Multiple Linear Regression using all features
- Coefficient and intercept interpretation
- MAE, RMSE, and $R^2$
- Mean baseline comparison
- Residual analysis

---

## Key Results

| Model | RMSE |
|---|---:|
| Mean Baseline | 73.22 |
| BMI-only Linear Regression | 63.73 |
| All-features Linear Regression | 53.85 |

The all-features model achieved:

- MAE ≈ **42.79**
- RMSE ≈ **53.85**
- $R^2 \approx 0.453$

This shows that using all features improves prediction performance compared with BMI alone and the mean baseline.

---

## Linear Regression Equation

For multiple features:

$\hat{y} = Xw + b$

where $w$ represents the learned coefficients and $b$ is the intercept.

The strongest coefficient by absolute magnitude in the fitted model was `s1`, but coefficients represent model relationships and should not be interpreted as causal effects.

---

## Residual Analysis

Residuals are calculated as:

$Residual = Actual - Predicted$

The residual plot shows errors around zero, but some relatively large residuals remain. This suggests that Linear Regression captures useful structure in the data but does not explain all variation.

---

## Conclusion

Linear Regression provided a clear improvement over the baseline while remaining simple and interpretable. The all-features model performed better than the BMI-only model, although the residual analysis indicates that some structure remains unexplained.