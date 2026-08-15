# Saved Model

`final_logistic_pipeline.joblib` is the final trained Logistic Regression
Pipeline. It contains missing-value handling, feature scaling, categorical
encoding, and the classifier together.

The `.joblib` file is binary, so it should not be opened or edited as a text
file. The unusual symbols shown by a text editor are normal.

## Recreate the model

Run this command from the project folder:

```bash
python src/train_model.py
```

## Load the model

```python
import joblib

model = joblib.load("models/final_logistic_pipeline.joblib")
predictions = model.predict(patient_data)
probabilities = model.predict_proba(patient_data)[:, 1]
```

`patient_data` must be a Pandas DataFrame containing the 13 feature columns
listed in `data/data_dictionary.md`.

This model is an educational project and is not a clinical diagnosis tool.
