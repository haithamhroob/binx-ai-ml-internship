# BinX Tech AI & ML Internship

## Week 2 - Day 4: Exploratory Data Analysis

### Summary

Performed exploratory data analysis on a music dataset using Pandas, Matplotlib, and Seaborn.

The dataset was inspected and cleaned before analyzing feature distributions, target classes, tempo outliers, relationships between variables, and correlations.

### Notes

- Inspected the dataset shape, columns, data types, and descriptive statistics.
- Checked missing values and duplicated rows.
- Removed five duplicated rows before continuing the analysis.
- Removed the unnecessary index column from the dataset.
- Examined the target-class distribution after cleaning.
- The target classes were nearly balanced, with 1015 songs in class 1 and 997 songs in class 0.
- Visualized numerical feature distributions using histograms and box plots.
- Detected tempo outliers using the Interquartile Range method.
- Found sixteen potential tempo outliers, representing about 0.8% of the cleaned dataset.
- Retained the tempo outliers because they may represent valid songs rather than data-entry errors.
- Examined the relationship between energy and loudness using a scatter plot.
- Compared energy distributions between the target classes using a grouped box plot.
- Examined the relationship between danceability and valence.
- Created a correlation matrix and heatmap.
- Identified the strongest relationships between numerical features.
- Found a strong positive correlation of about 0.76 between energy and loudness.
- Summarized the main findings and prepared the dataset for the next analysis stage.

### Tools Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook