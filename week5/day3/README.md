# Week 5 - Day 3: Dimensionality Reduction with PCA

## Overview

Day 3 focused on dimensionality reduction using Principal Component Analysis (PCA). PCA was applied to all 13 predictor features from the Cleveland Heart Disease dataset to determine how many components were needed to retain approximately 95% of the standardized variance.

A separate two-component PCA representation was also created to visualize the patients in two dimensions.

## What I Learned

* Why high-dimensional data can become difficult to analyze and visualize.
* How PCA creates principal components from combinations of the original features.
* Why PCA must be applied to standardized data.
* How to interpret individual and cumulative explained variance.
* How to choose the number of components using a variance threshold.
* How PCA loadings describe the contribution of the original features.
* When PCA is useful and when its loss of interpretability may be a disadvantage.

## What I Applied

* Selected all 13 predictors while keeping the diagnosis target separate.
* handled missing values using median imputation.
* standardized the predictors using `StandardScaler`.
* compared PCA behavior before and after scaling.
* fitted PCA using all available components.
* plotted individual and cumulative explained variance.
* selected the minimum number of components that exceeded the 95% threshold.
* created a 12-component reduced representation.
* created a two-component representation for visualization.
* colored and marked the 2D points using the known diagnosis groups only after PCA fitting.
* inspected the feature loadings for the first two principal components.

## Key Result

Without scaling, the first component explained approximately **74.65%** of the variance and was almost completely dominated by cholesterol because of its larger numerical range.

After standardization:

* PC1 explained approximately **23.69%** of the variance.
* PC2 explained approximately **12.31%** of the variance.
* The two-component visualization retained approximately **35.99%** of the total standardized variance.
* 11 components retained approximately **94.12%**, which was below the selected threshold.
* 12 components retained approximately **97.28%**, making 12 the minimum number of components that satisfied the 95% requirement.

The 2D visualization showed a directional tendency between the diagnosis groups, especially along PC1, but the groups still overlapped substantially.

## Key Lesson

PCA can reduce dimensionality while preserving the major directions of variation, but the amount of useful compression depends on the structure of the dataset.

For this dataset, retaining at least 95% of the variance required 12 of the original 13 dimensions, so PCA provided only modest compression at this strict threshold. The two-component representation was useful for visualization, but it retained only 35.99% of the variance and should not replace the fuller representation.

Scaling was essential because PCA is variance-based, and unscaled features with large numerical ranges can dominate the components. PCA also introduces an interpretability trade-off because each component combines several original features rather than preserving their direct clinical meanings.
