# Week 5 - Day 2: DBSCAN & Hierarchical Clustering

## Overview

Day 2 focused on the limitations of K-Means and compared it with DBSCAN and hierarchical clustering using the same Cleveland Heart Disease features prepared on Day 1.

## What I Learned

* Why K-Means may struggle with noise and irregular cluster shapes.
* How DBSCAN uses density to identify core, border, and noise points.
* How `eps` and `min_samples` affect DBSCAN results.
* How hierarchical clustering builds nested groups.
* How to read a dendrogram and select a cut height.
* How to compare clustering methods based on their results and intended use.

## What I Applied

* Selected `eps` using a nearest-neighbor distance plot.
* Tested several `eps` and `min_samples` values.
* Fitted DBSCAN and identified core, border, and noise patients.
* Built a hierarchical dendrogram using Ward linkage.
* Selected a cut height that produced two hierarchical clusters.
* Compared K-Means, DBSCAN, and hierarchical clustering on the same standardized data.

## Key Result

K-Means produced two clusters with a Silhouette Score of **0.232**.

DBSCAN found one dense region containing 285 patients and identified 18 noise points.

Hierarchical clustering produced two clusters with a Silhouette Score of **0.192**.

K-Means provided the strongest complete segmentation, while DBSCAN was more useful for detecting isolated observations and hierarchical clustering revealed the nested structure.

## Key Lesson

The best clustering method depends on the data shape and analysis objective. A useful decision should combine parameter behavior, quantitative metrics, interpretability, and the purpose of clustering.
