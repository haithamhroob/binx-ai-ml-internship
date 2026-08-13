# Week 4 - Day 5

## Scikit-learn Pipelines & Tuned Mini-Project

Built a complete leak-free classification workflow using:

- `Pipeline`
- `ColumnTransformer`
- `FunctionTransformer`
- `StandardScaler`
- `OneHotEncoder`
- `GridSearchCV`
- KNN

The workflow combined feature engineering, preprocessing, and modeling into one object so every transformation was fitted correctly inside cross-validation.

GridSearchCV selected:

- `n_neighbors = 7`
- `weights = uniform`
- categorical radius representation = dropped

### Results

- Best CV F1: **0.9605 ± 0.0157**
- Final Test F1: **0.9231**
- Final malignant recall: **0.8571**

### Key Lesson

The main value of an end-to-end Pipeline is not just cleaner code. It makes preprocessing, tuning, and model evaluation reproducible and prevents information leakage during cross-validation.