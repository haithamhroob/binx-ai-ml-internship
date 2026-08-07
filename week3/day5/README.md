# Week 3 - Day 5
## Supervised Learning Mini-Project

### Summary
Completed an end-to-end binary classification project using the IBM Telco Customer Churn dataset. The project predicts whether a telecom customer will churn and connects data cleaning, EDA, leakage-safe preprocessing, supervised-learning models, evaluation metrics, and model interpretation in one workflow.

### Work Completed
- Inspected the raw dataset, class distribution, missing values, duplicates, and data types.
- Converted `TotalCharges` to numeric, removed 11 rows with blank values, and removed `customerID` from the predictive features.
- Explored churn relationships with tenure, monthly charges, total charges, contract type, internet service, and tech support.
- Used an 80/20 stratified train/test split with `random_state=42`.
- Used `ColumnTransformer` and `Pipeline` so scaling and one-hot encoding are learned only from the training data.
- Compared a `DummyClassifier` baseline with Logistic Regression, Decision Tree, Random Forest, SVM, and k-NN.
- Evaluated all models using Accuracy, Precision, Recall, F1-score, ROC-AUC, confusion matrix, and classification report.
- Used Random Forest feature importance to inspect features that helped the model make predictions.

### Key Result
The baseline achieved **0.7342 Accuracy** but **0.0000 Recall and F1-score** for churn. The selected model was the **Decision Tree**, with:

- Accuracy: **0.7896**
- Precision: **0.6021**
- Recall: **0.6150**
- F1-score: **0.6085**
- ROC-AUC: **0.8296**

The Decision Tree was selected because it produced the highest F1-score and stronger churn Recall. Logistic Regression was extremely close in F1 and achieved higher Accuracy and ROC-AUC, so the final choice was based on the churn-focused Recall/F1 trade-off rather than Accuracy alone.

### Main Learning Outcomes
- Built a complete supervised-learning classification pipeline on a real dataset.
- Prevented data leakage by fitting preprocessing only through the training pipeline.
- Understood why class imbalance makes Accuracy insufficient by itself.
- Compared different classifier behaviors using the same test set.
- Connected False Negatives and Recall to the real customer-retention problem.
- Interpreted feature importance as model evidence, not proof of causation.
