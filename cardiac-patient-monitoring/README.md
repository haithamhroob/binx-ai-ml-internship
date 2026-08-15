# Cardiac Patient Monitoring — Heart Disease Classification Module

A supervised machine-learning project that classifies the presence of heart disease from clinical and test-related patient features using the processed Cleveland Heart Disease dataset.

## Project question

Can patient clinical measurements and test-related features classify heart-disease presence while maintaining a reliable, leakage-controlled machine-learning workflow?

## Dataset

- 303 patient records
- 13 input features
- Original target `num` with values 0–4
- Binary target: `0` = no heart disease, `1` = heart disease (`num` 1–4)
- Six non-standard missing markers: four in `ca`, two in `thal`

See `data/data_dictionary.md` for feature definitions.

## Workflow

1. Raw data audit and target validation
2. Development/final-test split before target-driven EDA
3. Univariate, bivariate, and correlation analysis
4. Semantic preprocessing with Scikit-learn Pipelines
5. Logistic Regression baseline vs. Random Forest
6. Train/validation comparison and 5-fold stratified cross-validation
7. Error analysis and ROC-AUC comparison
8. Controlled feature-engineering experiment
9. Final refit on all development data
10. One-time evaluation on the untouched final test set

## Key decisions

- **Primary model-selection metric:** F1-score, supported by recall, confusion matrices, and ROC-AUC.
- **Selected model:** Logistic Regression.
- Random Forest performed better on one validation split but showed stronger overfitting and lower mean cross-validated F1.
- Two engineered interactions were tested but rejected because they did not provide meaningful, consistent improvement.
- Imputation, scaling, and encoding are fitted inside Scikit-learn Pipelines.

## Final test results

| Metric | Score |
|---|---:|
| Accuracy | 0.869 |
| Precision | 0.812 |
| Recall | 0.929 |
| F1 | 0.867 |
| ROC-AUC | 0.958 |

Final confusion matrix: **TN = 27, FP = 6, FN = 2, TP = 26**.

## Project structure

```text
cardiac-patient-monitoring-ml/
├── data/
│   ├── processed.cleveland.data
│   ├── heart-disease.names
│   └── data_dictionary.md
├── notebooks/
│   └── cardiac_patient_monitoring.ipynb
├── src/
│   └── train_model.py
├── models/
│   ├── final_logistic_pipeline.joblib
│   └── README.md
├── outputs/
│   ├── categorical_features_vs_target.png
│   ├── correlation_analysis.png
│   ├── feature_engineering_comparison.csv
│   ├── final_confusion_matrix.csv
│   ├── final_test_confusion_matrix.png
│   ├── final_test_metrics.csv
│   ├── model_comparison.csv
│   ├── numerical_features_vs_target.png
│   ├── result_summary.md
│   ├── validation_confusion_matrix_logistic_regression.png
│   └── validation_confusion_matrix_random_forest.png
├── README.md
├── requirements.txt
└── .gitignore
```

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate      # Linux/macOS
# .venv\Scripts\activate     # Windows

pip install -r requirements.txt
jupyter notebook
```

Open `notebooks/cardiac_patient_monitoring.ipynb` and run the notebook from top to bottom.

### Reproduce the saved model

From the project root, run:

```bash
python src/train_model.py
```

This command reproduces the notebook's final 80/20 stratified split, trains the
selected Logistic Regression Pipeline on the development set, evaluates it on
the untouched final test set, and saves:

- `models/final_logistic_pipeline.joblib`

### Load the saved Pipeline

```python
import joblib

pipeline = joblib.load("models/final_logistic_pipeline.joblib")
predictions = pipeline.predict(patient_dataframe)
probabilities = pipeline.predict_proba(patient_dataframe)[:, 1]
```

`patient_dataframe` must contain the 13 input columns documented in
`data/data_dictionary.md`. The saved artifact contains preprocessing and the
classifier together, so imputation, scaling, and encoding are applied inside
the Pipeline.

## Limitations

- The dataset contains only 303 observations.
- The Cleveland data are fixed clinical observations, not continuous time-series monitoring.
- Disease severity values 1–4 are combined into one positive class.
- The workflow is an educational ML classifier and is not intended for clinical diagnosis, treatment, or emergency decisions.

## Dataset attribution

Janosi, A., Steinbrunn, W., Pfisterer, M., & Detrano, R. Heart Disease. UCI Machine Learning Repository. DOI: `10.24432/C52P4X`.
