# Week 4 - Day 1: Train, Validation and Test Sets

## Overview

Today I reused the **Breast Cancer Wisconsin dataset** from Week 3 to practice a proper three-way split:

- 60% Training
- 20% Validation
- 20% Test

The main goal was to use the validation set for model selection while keeping the test set untouched until the final evaluation.

## Model

I used **K-Nearest Neighbors (KNN)** with `StandardScaler`.

Several values of `k` were tested using the validation set only:

| K | Validation F1 |
|---:|---:|
| 1 | 0.9333 |
| 3 | 0.9524 |
| 5 | 0.9639 |
| 7 | 0.9639 |
| 11 | 0.9639 |
| 21 | 0.9512 |

I selected **k = 7** as a middle value among the tied best candidates.

## Final Result

- Validation F1: **0.964**
- Final Test F1: **0.925**

The test set was used only once after all model-selection decisions were completed.

## Key Lesson

- Training set → trains the model
- Validation set → guides model decisions
- Test set → final independent evaluation

Using test results repeatedly for tuning would make the final evaluation less reliable.

## Tools

Python, Pandas, Scikit-learn, Jupyter Notebook