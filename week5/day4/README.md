# Week 5 — Day 4: t-SNE & Anomaly Detection

This notebook continues the Cleveland Heart Disease unsupervised-learning workflow developed during Days 1–3.

## Main Questions

- Can t-SNE reveal local patient neighborhoods that were less visible in the linear PCA projection?
- Does Isolation Forest identify unusual patients similar to the noise observations found by DBSCAN?

## Dataset

The notebook uses the same processed Cleveland Heart Disease dataset used during the previous days:

- 303 patient records
- 13 predictor variables
- 1 diagnosis variable (`num`)

The diagnosis was excluded from all unsupervised fitting. It was used only after fitting as an interpretation reference.

## Continuity with Previous Days

- **Day 1 — K-Means:** `k=2`, cluster sizes 131 and 172, Silhouette Score = 0.232.
- **Day 2 — DBSCAN:** `eps=1.8`, `min_samples=5`, one connected cluster and 18 noise patients.
- **Day 2 — Hierarchical Clustering:** two clusters of 143 and 160 patients, Silhouette Score = 0.192.
- **Day 3 — PCA:** PC1 and PC2 retained 35.99% of standardized variance; 12 components retained 97.28%.

## What Was Applied

### t-SNE Visualization

- Recreated the same 13-feature standardized representation used for PCA.
- Applied t-SNE with `perplexity=30` and a fixed random state.
- Compared the local t-SNE view with the global linear PCA view.
- Colored the completed visualizations by the Day 1 K-Means clusters.
- Used diagnosis labels only afterward for cautious interpretation.

### Isolation Forest

- Recreated the same six-feature representation used during Days 1–2.
- Set contamination to the DBSCAN noise proportion: `18 / 303 = 5.94%`.
- Compared Isolation Forest anomalies directly with DBSCAN noise.
- Inspected the two patients with the strongest Isolation Forest anomaly evidence.

## Key Results

- t-SNE revealed clearer local organization in parts of the patient data, but the two broad profiles still overlapped.
- Isolation Forest flagged 18 patients.
- DBSCAN and Isolation Forest agreed on 12 patients.
- Six patients were flagged only by DBSCAN, and six only by Isolation Forest.
- The Jaccard similarity between the two flagged sets was 0.500.
- Patients 91 and 121 showed several strongly unusual measurements, especially involving `oldpeak`, `ca`, and cholesterol.

## Key Lesson

PCA and t-SNE preserve different aspects of high-dimensional structure. PCA provides a transparent global linear view, while t-SNE emphasizes local neighborhoods.

DBSCAN and Isolation Forest also define unusualness differently. DBSCAN focuses on local density, while Isolation Forest focuses on how easily an observation can be isolated through random feature splits.

Clusters, t-SNE regions, DBSCAN noise, and Isolation Forest anomalies are statistical findings. They are not diagnoses and require external clinical validation before any medical interpretation.

## Run the Notebook

Place the notebook beside the previous Week 5 notebooks while keeping the Cleveland data file at the same relative path used during Days 1–3:

```text
../../processed.cleveland.data
```

Then open:

```text
day4_cleveland_tsne_anomaly_detection.ipynb
```

and run all cells from top to bottom.

## Requirements

- Python 3
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- Jupyter Notebook or JupyterLab
