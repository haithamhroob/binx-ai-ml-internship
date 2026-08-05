# BinX tech AI & ML Internship

## Week 3 - Day 4: Trees, Forests, SVM & k-NN

### Summary

Trained and compared four classification algorithms on the Breast Cancer Wisconsin dataset using the same train/test split and F1-score metric. The work focused on understanding how Decision Trees, Random Forests, Support Vector Machines, and k-Nearest Neighbors make predictions, how preprocessing affects their performance, and how to compare models fairly.

### Models

- Decision Tree
- Random Forest
- Support Vector Machine (SVM)
- k-Nearest Neighbors (k-NN)

### Work Completed

- Reused the Breast Cancer Wisconsin dataset with:
  - `0` → Benign
  - `1` → Malignant
- Used the same stratified train/test split for all models.
- Trained and evaluated a Decision Tree.
- Visualized the first levels of the Decision Tree and interpreted its nodes.
- Compared Decision Tree training and testing F1-scores to observe overfitting.
- Trained a Random Forest with 100 trees.
- Compared Random Forest training and testing performance.
- Extracted and visualized the top Random Forest feature importances.
- Applied `StandardScaler` before training SVM and k-NN.
- Compared Linear and RBF SVM kernels.
- Tested multiple values of `k` for k-NN.
- Compared all four classifiers using the same F1-score metric.

### Main Results

| Model | F1-score |
|---|---:|
| Random Forest | 0.963 |
| RBF SVM | 0.963 |
| k-NN (`k=5`) | 0.938 |
| Decision Tree | 0.886 |

### Decision Tree Observation

- Train F1 ≈ `0.982`
- Test F1 ≈ `0.886`

The noticeable train-test gap shows that a single Decision Tree can become sensitive to the training data and overfit.

### Random Forest Observation

- Train F1 = `1.000`
- Test F1 ≈ `0.963`

Random Forest achieved stronger test performance and a smaller train-test gap than the single Decision Tree.

### Random Forest Feature Importance

The highest-ranked features included:

- `worst area`
- `worst concave points`
- `worst radius`
- `worst perimeter`
- `mean concave points`

Feature importance indicates how useful a feature was for the model's predictions. It does not imply that the feature causes the medical condition.

### SVM Observation

Feature scaling had a major effect on SVM performance:

- Without scaling: F1 ≈ `0.849`
- With scaling: F1 ≈ `0.963`

Kernel comparison:

- Linear SVM: F1 = `0.950`
- RBF SVM: F1 ≈ `0.963`

The RBF kernel performed slightly better on this dataset.

### k-NN Observation

| k | F1-score |
|---:|---:|
| 1 | 0.902 |
| 3 | 0.911 |
| 5 | 0.938 |
| 7 | 0.938 |
| 11 | 0.925 |
| 21 | 0.911 |

The experiment showed that a very small `k` can make predictions too sensitive to individual samples, while a very large `k` can smooth the decision too much.

### Key Takeaways

- Decision Trees are easy to interpret but can overfit.
- Random Forests improve stability by combining many diverse trees.
- SVM depends strongly on feature scaling and can model non-linear boundaries using kernels.
- k-NN classifies samples according to nearby training examples and also depends strongly on feature scaling.
- Tree-based models normally do not require feature scaling.
- No single classifier is best for every problem; models should be compared under the same evaluation conditions.
