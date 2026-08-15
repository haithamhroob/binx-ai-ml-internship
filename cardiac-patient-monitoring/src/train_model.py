"""Train, evaluate, and save the final Logistic Regression Pipeline."""

from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "processed.cleveland.data"
MODEL_PATH = PROJECT_ROOT / "models" / "final_logistic_pipeline.joblib"

# Column names from the processed Cleveland Heart Disease dataset.
column_names = [
    "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
    "thalach", "exang", "oldpeak", "slope", "ca", "thal", "num",
]

# 1. Load and clean the data.
data = pd.read_csv(DATA_PATH, header=None, names=column_names)
data = data.replace("?", np.nan)
data["ca"] = pd.to_numeric(data["ca"], errors="coerce")
data["thal"] = pd.to_numeric(data["thal"], errors="coerce")

# 2. Separate inputs and target.
X = data.drop(columns="num")
y = (data["num"] > 0).astype(int)

# 3. Keep 20% as an untouched final test set.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

# 4. Group columns by how they should be prepared.
numeric_features = ["age", "trestbps", "chol", "thalach", "oldpeak", "ca"]
binary_features = ["sex", "fbs", "exang"]
categorical_features = ["cp", "restecg", "slope", "thal"]

numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler()),
])

categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore")),
])

preprocessor = ColumnTransformer([
    ("numeric", numeric_pipeline, numeric_features),
    ("binary", "passthrough", binary_features),
    ("categorical", categorical_pipeline, categorical_features),
])

# 5. Put preprocessing and the model in one leakage-safe Pipeline.
model_pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", LogisticRegression(max_iter=1000)),
])

# 6. Train and predict.
model_pipeline.fit(X_train, y_train)
predictions = model_pipeline.predict(X_test)
probabilities = model_pipeline.predict_proba(X_test)[:, 1]

# 7. Calculate and print the final results.
accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions)
recall = recall_score(y_test, predictions)
f1 = f1_score(y_test, predictions)
roc_auc = roc_auc_score(y_test, probabilities)
tn, fp, fn, tp = confusion_matrix(y_test, predictions).ravel()

print("Final test results")
print("------------------")
print(f"Accuracy:  {accuracy:.3f}")
print(f"Precision: {precision:.3f}")
print(f"Recall:    {recall:.3f}")
print(f"F1-score:  {f1:.3f}")
print(f"ROC-AUC:   {roc_auc:.3f}")
print(f"Confusion matrix: TN={tn}, FP={fp}, FN={fn}, TP={tp}")

# 8. Save preprocessing and the trained model together.
MODEL_PATH.parent.mkdir(exist_ok=True)
joblib.dump(model_pipeline, MODEL_PATH)
print(f"Saved model: {MODEL_PATH}")
