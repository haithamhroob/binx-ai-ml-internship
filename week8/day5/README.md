# Week 8 — Day 5: Full Evaluation, Explainability and Sprint Review

## Project Overview

This notebook completes the evaluation and explainability stage of the Oxford-IIIT Pet classification project.

The integrated MobileNetV2 model from Day 4 was loaded without retraining and evaluated on unseen images. Its performance was compared with a valid baseline, weak breeds were analyzed, and SHAP was used to explain individual and global predictions.

---

## Learning Objectives

* Evaluate the classifier using task-appropriate metrics.
* Compare the trained model with a valid baseline.
* Study class balance and decide whether SMOTE is required.
* Analyze the precision-recall trade-off for individual breeds.
* Explain correct and incorrect predictions using SHAP.
* Generate a representative Global SHAP explanation.
* Communicate results to non-technical stakeholders.
* Complete the Sprint Review and Retrospective.

---

## Dataset

**Dataset:** Oxford-IIIT Pet Dataset

The dataset contains 7,390 images across 37 cat and dog breeds.

| Split      | Images |
| ---------- | -----: |
| Training   |  5,173 |
| Validation |  1,108 |
| Test       |  1,109 |
| Total      |  7,390 |

The exact class ordering, random state, and stratified split from Day 4 were reused to guarantee consistent evaluation.

---

## Loaded Artifacts

The following Day 4 artifacts were loaded:

* `pet_breed_classifier.keras`
* `class_names.json`
* `preprocessing_config.json`

These files preserve the trained model, the order of the 37 output classes, and the expected preprocessing operations.

---

## Preprocessing Consistency

The test pipeline applies the same operations used during training:

1. Read the image using OpenCV.
2. Convert BGR into RGB.
3. Resize while preserving the aspect ratio.
4. Add padding to produce a `224 × 224` image.
5. Convert pixels to `float32`.
6. Apply MobileNetV2 normalization.

The pixel range is transformed from:

$$
[0,255] \rightarrow [-1,1]
$$

Using the same preprocessing function prevents training/serving skew.

---

## Class Balance and SMOTE Decision

The smallest training class contained 134 images, while the largest contained 140 images.

The imbalance ratio was:

$$
\text{Imbalance Ratio}
=
\frac{140}{134}
=
1.0448
$$

This ratio is close to 1, showing that the dataset is balanced.

SMOTE was not applied because:

* The classes were already balanced.
* SMOTE is mainly designed for tabular feature vectors.
* Interpolating raw image pixels may generate unrealistic images.
* Image augmentation is more appropriate for computer-vision tasks.

---

## Evaluation Baseline

The Week 6 ECG model could not be used as a direct numerical baseline because it solved a different task using different inputs and labels.

Instead, a class-prior baseline was created using the training class frequencies. This baseline does not inspect image pixels and represents a valid minimum reference for the same 37-class problem.

---

## Complete Evaluation Results

| Metric          | Class-Prior Baseline | MobileNetV2 |
| --------------- | -------------------: | ----------: |
| Accuracy        |                2.71% |      89.00% |
| Macro Precision |                0.07% |      89.76% |
| Macro Recall    |                2.70% |      88.98% |
| Macro F1-score  |                0.14% |      88.96% |
| Top-3 Accuracy  |                8.12% |      98.38% |
| Macro ROC-AUC   |               50.00% |      99.78% |
| Macro PR-AUC    |                2.70% |      95.33% |

The classifier correctly predicted 987 of the 1,109 test images and misclassified 122 images.

The model substantially outperformed the baseline across every evaluation metric.

---

## Per-Breed Analysis

Precision, recall, F1-score, and Average Precision were calculated independently for all 37 breeds.

### Weakest Breeds

| Breed                      | Precision | Recall | F1-score | Average Precision |
| -------------------------- | --------: | -----: | -------: | ----------------: |
| Staffordshire Bull Terrier |    57.58% | 65.52% |   61.29% |            70.45% |
| American Pit Bull Terrier  |    72.73% | 53.33% |   61.54% |            77.43% |
| Ragdoll                    |    67.65% | 76.67% |   71.88% |            81.49% |
| Bengal                     |   100.00% | 56.67% |   72.34% |            95.08% |
| Russian Blue               |    73.53% | 83.33% |   78.12% |            87.99% |

The greatest weakness occurred between visually similar breeds, especially American Pit Bull Terrier and Staffordshire Bull Terrier.

### Strongest Breeds

* Scottish Terrier: 100% F1-score.
* Wheaten Terrier: 98.31% F1-score.
* Newfoundland: 96.77% F1-score.
* Yorkshire Terrier: 96.67% F1-score.
* Pug: 96.67% F1-score.

Precision-Recall curves were generated for the five weakest breeds to show how precision and recall change at different probability thresholds.

---

## SHAP Explainability

SHAP was used to measure how different image regions influenced model predictions.

The Shapley value for a feature is:

$$
\phi_i =
\sum_{S \subseteq F \setminus \{i\}}
\frac{|S|!(|F|-|S|-1)!}{|F|!}
\left[
f(S \cup \{i\})-f(S)
\right]
$$

For image classification:

* Positive SHAP regions support the selected breed.
* Negative SHAP regions oppose the selected breed.
* Regions near zero have little influence.

A blurred image masker and Partition SHAP were used to hide image regions and measure changes in model output.

---

## Correct Prediction Explanation

A Sphynx image was classified correctly with 97.95% confidence.

The strongest positive SHAP regions appeared around:

* The large ears.
* The wrinkled face.
* The exposed skin.
* The front limbs.

These regions represent meaningful characteristics of the Sphynx breed.

Background and padded regions provided little or negative support, indicating that the model focused mainly on the animal.

---

## Incorrect Prediction Explanation

A Havanese image was incorrectly classified as Newfoundland with 99.05% confidence.

The positive SHAP regions concentrated around the dark coat and body.

Because Havanese and Newfoundland dogs may share long, dark fur, the model relied heavily on coat appearance. It could not directly understand the real-world difference in body size.

The image was clear, so the error was categorized as a model weakness caused by visual similarity rather than a data-quality issue.

Some important regions extended into the grass, suggesting that background context may also have slightly influenced the prediction.

---

## Global SHAP Results

Global SHAP was calculated using five correctly classified, high-confidence images from different breeds.

| Image Region  | Importance |
| ------------- | ---------: |
| Top Left      |      7.61% |
| Top Center    |     11.44% |
| Top Right     |      3.19% |
| Middle Left   |     28.08% |
| Middle Center |     32.27% |
| Middle Right  |      7.41% |
| Bottom Left   |      3.92% |
| Bottom Center |      4.34% |
| Bottom Right  |      1.75% |

The middle row contained 67.76% of the total spatial importance.

The middle-left and middle-center regions alone contained 60.35%, indicating that the model generally focused on the central animal regions.

The Global SHAP result is representative rather than exact because only five images were used to keep CPU execution practical.

---

## Stakeholder Summary

The system distinguishes between 37 cat and dog breeds.

On unseen images:

* The correct breed was selected approximately 89 times out of 100.
* The correct breed appeared among the three strongest predictions approximately 98 times out of 100.
* The model strongly outperformed the 2.71% baseline.
* SHAP showed that meaningful animal regions generally supported predictions.
* Visually similar breeds can still be confused with high confidence.

For deployment, the interface should display the three strongest predictions, their probabilities, and a visual explanation instead of showing only one breed name.

---

## Sprint Review

The completed sprint delivered:

* A consistent OpenCV preprocessing pipeline.
* A 37-class MobileNetV2 classifier.
* An end-to-end raw-image prediction function.
* Full evaluation against a valid baseline.
* Accuracy, precision, recall, F1, Top-3 accuracy, ROC-AUC, and PR-AUC.
* A documented SMOTE decision.
* Per-breed Precision-Recall analysis.
* Confusion-matrix and misclassification analysis.
* Local SHAP explanations for correct and incorrect predictions.
* A representative Global SHAP explanation.
* Exported model and deployment configuration files.

All Day 5 quality checks passed successfully.

---

## Sprint Retrospective

### What Went Well

* Transfer learning achieved strong results without training a large CNN from scratch.
* Validation and test performance remained close.
* Top-3 accuracy reached 98.38%.
* SHAP connected model predictions with visible image regions.
* The exported artifacts support reproducible deployment.

### Challenges

* Visually similar breeds were difficult to separate.
* The model sometimes produced high confidence for incorrect predictions.
* SHAP required more computation than normal inference.
* Global SHAP required a limited representative sample because the environment used CPU.

### Concrete Change for Sprint 4

Sprint 4 will implement a confidence-aware web interface that displays:

* The uploaded image.
* The three strongest breed predictions.
* Prediction probabilities.
* Influential image regions.
* A warning for uncertain predictions.

---

## Generated Outputs

The notebook generates:

* `baseline_comparison.csv`
* `baseline_comparison.png`
* `per_breed_metrics.csv`
* `weakest_breeds_precision_recall.png`
* `local_shap_explanation.png`
* `wrong_prediction_shap.png`
* `global_shap_importance.png`
* `global_shap_regions.csv`
* `stakeholder_summary.png`
* `day5_result_summary.json`

---

## Tools Used

* Python
* TensorFlow / Keras
* MobileNetV2
* OpenCV
* SHAP
* NumPy
* Pandas
* Scikit-learn
* Matplotlib
* Seaborn
* Jupyter Notebook

---

## Conclusion

The final classifier achieved 89.00% test accuracy and 98.38% Top-3 accuracy across 37 pet breeds.

The model substantially outperformed the baseline, while per-class evaluation identified specific weaknesses between visually similar breeds.

SHAP explanations connected mathematical feature contributions with visible image regions and explained both successful and incorrect predictions.

The sprint closes with a trained, integrated, evaluated, explainable, and exported image-classification system ready for web deployment.
