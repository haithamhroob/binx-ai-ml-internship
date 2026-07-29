# BinX Tech AI & ML Internship

## Week 2 - Day 4: Exploratory Data Analysis

### Summary

Performed exploratory data analysis on a music dataset using Pandas, Matplotlib, and Seaborn. Inspected the dataset structure, checked missing values and duplicates, analyzed feature distributions, detected tempo outliers using the IQR method, and explored relationships between numerical features using scatter plots and a correlation heatmap.

### Notes

- Inspected the dataset shape, columns, data types, and descriptive statistics.
- Checked missing values and duplicated rows (5 duplicate rows found).
- Target class distribution: {1: 1020, 0: 997} (nearly balanced).
- Removed the unnecessary index column (`Unnamed: 0`) from the dataset.
- Visualized numerical feature distributions using histograms and a box plot.
- Detected tempo outliers using the Interquartile Range method (15 outliers detected).
- Examined the relationship between `energy` and `loudness` (strong positive correlation ≈ 0.76).
- Used a correlation heatmap to identify relationships between numerical features.
- Summarized the main findings and prepared the dataset for the next analysis stage.