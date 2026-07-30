# BinX Tech AI & ML Internship

## Week 2 - Day 4: Exploratory Data Analysis

### Summary

Performed exploratory data analysis on a music dataset using Pandas, Matplotlib, and Seaborn. The notebook inspected the dataset structure, checked missing values and duplicates, analyzed feature distributions, detected tempo outliers using the IQR method, and explored relationships between numerical features using scatter plots and a correlation heatmap.

### Notes

- Inspected the dataset shape, columns, data types, and descriptive statistics.
- Checked missing values and duplicated rows. Five duplicate rows were removed.
- Target class distribution was nearly balanced at 1020 songs in class 1 and 997 songs in class 0.
- Removed the unnecessary index column from the dataset.
- Visualized numerical feature distributions using histograms and a box plot.
- Detected tempo outliers using the Interquartile Range method. Fifteen outliers were found, which represented about 0.74% of the dataset.
- Examined the relationship between energy and loudness. The correlation was about 0.76.
- Used a correlation heatmap to identify relationships between numerical features.
- Summarized the main findings and prepared the dataset for the next analysis stage.