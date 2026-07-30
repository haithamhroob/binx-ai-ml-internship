# Day 5 — EDA Part 2: Correlation & Data Storytelling

## Summary
This notebook completes the Day 5 EDA workflow for the OBD-II dataset. It uses data cleaning, numeric feature selection, bivariate charts, and correlation analysis to reveal relationships between vehicle sensor measurements.

Key steps:
- Load the dataset and inspect structure
- Remove fully empty rows and columns
- Select numeric features for analysis
- Create scatter plots and box plots for bivariate relationships
- Compute and visualize a correlation matrix
- Use a pairplot to scan several numeric relationships together

## Notes
- The notebook focuses on EDA storytelling rather than modeling.
- Correlation shows association, not causation.
- `filtered_df` contains only numeric columns and is used for the correlation and pairplot analysis.
- `ENGINE_RPM` and `SPEED` are the strongest visual relationship in this dataset.
- The notebook is structured to support a clear narrative: data inspection, cleanup, relationship exploration, and conclusion.
