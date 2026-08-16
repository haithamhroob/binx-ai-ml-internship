# Week 5 - Day 1: Unsupervised Learning & K-Means

## Overview

Day 1 introduced **unsupervised learning** and K-Means clustering.

The Cleveland Heart Disease dataset from Project 1 was reused, but this time the diagnosis target was excluded. The goal changed from predicting heart disease to discovering natural patient profiles from clinical measurements.

## What I Learned

* Supervised vs. unsupervised learning.
* How K-Means uses distance, centroids, and the assignment-update loop.
* Why scaling is essential for distance-based clustering.
* The meaning of `n_init` and inertia.
* How the Elbow Method helps identify reasonable values of `k`.
* How the Silhouette Score evaluates cluster compactness and separation.
* Why cluster IDs must be interpreted rather than treated as predefined classes.

## What I Applied

* Selected six appropriate numeric/discrete clinical features.
* Handled missing values with median imputation.
* Standardized features using `StandardScaler`.
* Tested K-Means across multiple values of `k`.
* Used Elbow and Silhouette analysis to select the final cluster count.
* Fitted the final K-Means model with `k=2`.
* Compared cluster profiles using the original clinical units.
* Visualized both a 2D view and the six-feature standardized profiles.

## Key Result

K-Means identified **two broad patient profiles** with systematic differences across age, blood pressure, cholesterol, maximum heart rate, ST depression, and number of major vessels.

The clusters still showed noticeable overlap, so they were interpreted as patient profiles rather than sharply separated clinical or diagnostic groups.

## Key Lesson

Clustering can discover useful structure without a target label, but the output should not be trusted from the algorithm alone.

A useful clustering result requires:

**appropriate features → proper scaling → quantitative validation → meaningful interpretation**
