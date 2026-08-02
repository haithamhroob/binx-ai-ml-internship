# BinX Tech AI & ML Internship

## Week 3 - Day 1: Supervised Learning & Train/Test Split

### Summary

Applied the core supervised learning workflow to the Breast Cancer Wisconsin dataset.

The dataset was inspected, framed as a binary classification problem, and separated into features and target. The target distribution was analyzed to justify a stratified train/test split, which was then validated with sanity checks to confirm the split preserved all samples and class proportions.

### Notes

- Framed the task as supervised binary classification, distinguishing it from regression.
- Loaded the Breast Cancer Wisconsin dataset using Scikit-learn.
- Inspected the dataset shape, column types, and missing values.
- Separated the dataset into features (X) and target (y).
- Analyzed the target distribution and found the classes were not perfectly balanced.
- Performed an 80/20 train/test split using `stratify=y` and a fixed `random_state`.
- Validated the split shapes and confirmed no samples were lost or duplicated.
- Verified class proportions were preserved in both the training and test sets.
- Explained why the test set must remain unseen during training to avoid data leakage.

### Tools Used

- Python
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- Jupyter Notebook