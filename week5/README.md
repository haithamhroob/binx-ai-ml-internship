# Week 5 — Unsupervised Learning and Project Discussion

## Overview

This week focused on applying unsupervised machine learning techniques to the Cleveland Heart Disease dataset. The same dataset was used throughout the first four days to maintain continuity and allow a fair comparison between clustering, dimensionality reduction, visualization, and anomaly detection methods.

The diagnosis label was excluded while fitting the unsupervised models. It was used only when needed as a reference for interpreting the discovered patient structure.

On Day 5, the work shifted from notebook implementation to discussing the **Cardiac Patient Monitoring Project**, which was developed based on the requirements and machine learning concepts covered during the **first four weeks of the internship**.

---

## Dataset

- **Dataset:** Cleveland Heart Disease
- **Number of patients:** 303
- **Original predictors:** 13 clinical features
- **Target column:** `num`
- **Missing-value handling:** Median imputation
- **Scaling:** Standardization using `StandardScaler` when required by distance- or variance-based methods

---

## Weekly Work

### Day 1 — K-Means Clustering

The first day introduced unsupervised learning by changing the task from predicting heart disease to discovering natural patient profiles without using diagnosis labels.

#### Main Work

- Selected six clinically relevant numerical features for distance-based clustering.
- Handled missing values using median imputation.
- Standardized the features before applying K-Means.
- Tested different values of `k` using the Elbow Method.
- Validated the candidate values using the Silhouette Score.
- Selected `k = 2` as the final configuration.
- Profiled and visualized the discovered patient clusters using their original clinical units.

---

### Day 2 — DBSCAN and Hierarchical Clustering

The second day compared alternative clustering methods using the same six standardized features from Day 1.

#### Main Work

- Applied DBSCAN and studied the effects of `eps` and `min_samples`.
- Used the k-nearest-neighbor distance plot to guide the selection of `eps`.
- Distinguished between core, border, and noise points.
- Selected `eps = 1.8` and `min_samples = 5` for the final DBSCAN experiment.
- Applied agglomerative hierarchical clustering using Ward linkage.
- Used a dendrogram and merge distances to choose an appropriate cut height.
- Profiled the resulting hierarchical clusters.
- Compared K-Means, DBSCAN, and hierarchical clustering using their structure, interpretability, and Silhouette Scores.

K-Means was retained as the most suitable method for producing complete and interpretable patient segmentation. DBSCAN mainly identified one connected patient population with a small group of noise observations.

---

### Day 3 — Principal Component Analysis

The third day focused on dimensionality reduction using Principal Component Analysis (PCA) with all 13 predictor features.

#### Main Work

- Demonstrated why PCA must be applied after feature scaling.
- Compared unscaled and standardized PCA results.
- Calculated the explained variance of every principal component.
- Selected the minimum number of components required to preserve at least 95% of the variance.
- Retained 12 components, preserving approximately 97.28% of the standardized variance.
- Created a separate two-component PCA representation for visualization.
- Analyzed the feature loadings to interpret the first two principal components.

The first two components preserved approximately 35.99% of the total standardized variance. Therefore, they were useful for visualization but could not replace the 12-component representation.

---

### Day 4 — t-SNE and Anomaly Detection

The fourth day extended the previous analysis using nonlinear visualization and anomaly detection.

#### Main Work

- Recreated the main K-Means and DBSCAN results from the previous days.
- Applied t-SNE to visualize local patient neighborhoods in two dimensions.
- Compared the global linear view produced by PCA with the local nonlinear view produced by t-SNE.
- Used the diagnosis only as an external interpretation reference after fitting the unsupervised transformations.
- Applied Isolation Forest for anomaly detection.
- Set the contamination rate using the proportion of noise observations detected by DBSCAN.
- Compared the patients flagged by DBSCAN and Isolation Forest.
- Inspected the strongest anomalous patient records using their original clinical measurements.

Both anomaly-detection methods flagged 18 patients, but they agreed on only 12 observations. This demonstrated that density-based noise and isolation-based anomalies represent related but different concepts.

---

### Day 5 — Cardiac Project Discussion

Day 5 was dedicated to discussing and presenting the **Cardiac Patient Monitoring Project**.

This project was developed to apply the requirements and machine learning concepts covered during the **first four weeks of the internship**.

#### Topics Discussed

- Data loading, inspection, and cleaning
- Exploratory data analysis and visualization
- Feature preparation and preprocessing
- Supervised machine learning model development
- Model evaluation and comparison
- Project organization and documentation
- Technical decisions and model-selection reasoning
- Project results and limitations
- Possible future improvements

The discussion demonstrated the ability to explain the complete machine learning workflow rather than only execute the code.

---

## Repository Structure

```text
week-5/
├── day1.ipynb   # K-Means clustering
├── day2.ipynb   # DBSCAN and hierarchical clustering
├── day3.ipynb   # PCA dimensionality reduction
├── day4.ipynb   # t-SNE and anomaly detection
└── README.md    # Weekly documentation