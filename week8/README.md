# Week 8 — NLP & Computer Vision

## Sprint 3: Preprocessing, Representation, Integration and Explainability

This week developed two machine-learning tracks designed for future web deployment:

1. **Text sentiment analysis** using the IMDB dataset.
2. **Image classification** using the Oxford-IIIT Pet Dataset.

The work progressed from raw-input preprocessing to numeric representation, transfer learning, end-to-end integration, complete evaluation, error analysis, and SHAP explainability.

---

## Weekly Objectives

* Build reusable preprocessing pipelines for text and images.
* Match preprocessing decisions to each model architecture.
* Convert text into TF-IDF and embedding representations.
* Process images using OpenCV and MobileNetV2 requirements.
* Integrate preprocessing and prediction into one consistent pipeline.
* Evaluate models using task-appropriate metrics.
* Analyze systematic and individual prediction errors.
* Explain image predictions using local and global SHAP.
* Export reusable artifacts for future web deployment.

---

# Day 1 — Sprint Planning and NLP Preprocessing

## Dataset

**IMDB Movie Reviews**

The same experiment split from Week 7 was reused:

| Split      | Reviews |
| ---------- | ------: |
| Training   |   4,000 |
| Validation |   1,000 |
| Test       |   1,000 |
| Total      |   6,000 |

Reusing the same split allowed fair comparison with the previous LSTM, DistilBERT, TF-IDF, and ensemble experiments.

## Previous Week 7 Results

| Model                        | Test F1 |
| ---------------------------- | ------: |
| Text LSTM                    |  0.7950 |
| Pretrained DistilBERT        |  0.8152 |
| TF-IDF + Logistic Regression |  0.8617 |
| Weighted Ensemble            |  0.8939 |

## Text Preprocessing

Two text representations were created instead of applying one cleaning strategy to every model.

### Minimal Text

Designed for LSTM and transformer models:

$$
Raw
\rightarrow
HTML\ Removal
\rightarrow
Lowercase
\rightarrow
Whitespace\ Normalization
$$

This version preserves most punctuation, word order, and natural sentence structure.

### Classical Text

Designed for TF-IDF and traditional machine-learning models:

$$
Minimal
\rightarrow
Negation\ Expansion
\rightarrow
Punctuation\ Removal
\rightarrow
Tokenization
\rightarrow
Task\text{-}Aware\ Stop\ Words
\rightarrow
Lemmatization
$$

Important sentiment words such as `not`, `never`, `hardly`, and `without` were protected from stop-word removal.

## Quality Checks

* Exact duplicates were removed before sampling.
* Training, validation, and test splits remained separate.
* No missing or empty processed reviews were found.
* Negation-preservation tests passed.
* All blocking quality checks passed.

## Saved Outputs

* `imdb_train_preprocessed.csv`
* `imdb_validation_preprocessed.csv`
* `imdb_test_preprocessed.csv`

---

# Day 2 — TF-IDF and Word Embeddings

Day 2 converted the processed IMDB reviews into numerical representations.

## Bag of Words and TF-IDF

TF-IDF weights terms according to their importance inside a document and their rarity across the training collection:

$$
TF\text{-}IDF(t,d)
=
TF(t,d)
\times
IDF(t)
$$

$$
IDF(t)
=
\ln
\left(
\frac{N+1}{DF(t)+1}
\right)
+1
$$

The vectorizer was fitted on training data only to prevent data leakage.

## TF-IDF Experiments

The experiments compared:

* Minimal text versus classical text.
* Unigrams versus unigrams and bigrams.
* Vocabulary size.
* Rare-term filtering.
* Common-term filtering.
* Sublinear term frequency.

The best configuration used:

* `minimal_text`
* Unigrams and bigrams
* 10,000 features
* Sublinear term frequency
* Logistic Regression classifier

## TF-IDF Results

| Metric         | Result |
| -------------- | -----: |
| Validation F1  | 0.8808 |
| Test Accuracy  | 0.8590 |
| Test Precision | 0.8519 |
| Test Recall    | 0.8705 |
| Test F1        | 0.8611 |
| Test ROC-AUC   | 0.9441 |

Logistic Regression coefficients were inspected to identify the words and bigrams that pushed predictions toward positive or negative sentiment.

## GloVe Embeddings

Pretrained 100-dimensional GloVe vectors were used to represent words.

Each review was converted into one vector by averaging the vectors of its known words. Out-of-vocabulary words were skipped.

Cosine similarity was used to measure relationships between word vectors:

$$
\cos(\theta)
=
\frac{A \cdot B}
{\lVert A \rVert \lVert B \rVert}
$$

## Representation Comparison

| Representation | Validation F1 | Test F1 |
| -------------- | ------------: | ------: |
| Tuned TF-IDF   |        0.8808 |  0.8611 |
| Averaged GloVe |        0.7972 |  0.7830 |

TF-IDF performed better because it learned task-specific word and bigram importance directly from the sentiment data.

Averaging GloVe vectors captured general semantic relationships but lost word order and diluted important sentiment signals.

The Week 7 weighted ensemble remained the strongest text model with a Test F1 of 0.8939.

## Saved Outputs

* `tfidf_validation_experiments.csv`
* `representation_test_metrics.csv`
* `representation_f1_comparison.csv`
* `strongest_negative_terms.csv`
* `strongest_positive_terms.csv`

---

# Day 3 — Computer Vision Preprocessing with OpenCV

## Dataset

**Oxford-IIIT Pet Dataset**

| Property           |     Value |
| ------------------ | --------: |
| Images             |     7,390 |
| Cat and dog breeds |        37 |
| Model input size   | 224 × 224 |
| Color channels     |         3 |

## OpenCV Preprocessing

The image-processing pipeline performs:

1. Read the image using OpenCV.
2. Convert BGR into RGB.
3. Resize while preserving the aspect ratio.
4. Add padding to create a `224 × 224` image.
5. Convert the pixel data type to `float32`.
6. Apply the normalization required by the selected model.

Aspect-ratio-preserving resizing prevented animals from being stretched or compressed.

## Normalization

General normalization transforms pixels into:

$$
[0,255] \rightarrow [0,1]
$$

MobileNetV2 preprocessing transforms pixels into:

$$
[0,255] \rightarrow [-1,1]
$$

The two methods are both valid, but they must not be applied together.

## Data Augmentation

The augmentation pipeline included:

* Rotation
* Width and height shifting
* Zoom
* Horizontal flipping
* Brightness variation

These transformations generate realistic variations and reduce memorization of the training images.

## MobileNetV2 Compatibility

A frozen MobileNetV2 convolutional base converted each input image into a feature map with shape:

```text
(7, 7, 1280)
```

A complete pretrained ImageNet model also produced valid probability outputs.

These predictions verified pipeline compatibility but were not treated as an evaluation of a custom 37-breed classifier.

## Saved Outputs

* `preprocessing_summary.csv`
* `pretrained_imagenet_predictions.csv`
* `raw_image_dimension_sample.csv`

---

# Day 4 — Model Integration and Error Analysis

Day 4 connected the OpenCV preprocessing pipeline with a custom 37-class transfer-learning model.

## Dataset Splits

| Split      | Images |
| ---------- | -----: |
| Training   |  5,173 |
| Validation |  1,108 |
| Test       |  1,109 |

The split was stratified, and no image appeared in more than one subset.

## Model Architecture

The model consisted of:

* Frozen MobileNetV2 convolutional base.
* Global Average Pooling.
* Dropout with a rate of 0.30.
* Dense Softmax output layer with 37 units.

| Parameter Type           |     Count |
| ------------------------ | --------: |
| Total parameters         | 2,305,381 |
| Trainable parameters     |    47,397 |
| Non-trainable parameters | 2,257,984 |

Softmax produces one probability for every breed:

$$
P(y=k \mid x)
=
\frac{e^{z_k}}
{\sum_{j=1}^{37}e^{z_j}}
$$

The model was trained using Adam and Sparse Categorical Cross-Entropy.

ModelCheckpoint, ReduceLROnPlateau, and EarlyStopping were used to control training. The lowest validation loss occurred at epoch 6.

## Final Results

| Split      | Accuracy | Top-3 Accuracy |   Loss |
| ---------- | -------: | -------------: | -----: |
| Validation |   90.07% |         98.38% | 0.2980 |
| Test       |   89.00% |         98.38% | 0.3283 |

Additional results:

* Correct test predictions: 987
* Misclassified images: 122
* Test error rate: 11.00%
* Macro F1-score: 88.96%
* Weighted F1-score: 88.99%

## Error Analysis

A normalized confusion matrix and individual misclassified examples were inspected.

The most frequent confusion patterns included:

| True Breed                | Predicted Breed            | Errors |
| ------------------------- | -------------------------- | -----: |
| Bengal                    | Egyptian Mau               |     10 |
| American Pit Bull Terrier | Staffordshire Bull Terrier |     10 |
| Ragdoll                   | Birman                     |      4 |
| American Pit Bull Terrier | American Bulldog           |      4 |
| Russian Blue              | British Shorthair          |      4 |

Most errors occurred between breeds with similar fur, face shapes, colors, or body structures.

## End-to-End Prediction

The final `predict_pet_breed()` function:

* Accepts a raw image path.
* Applies the complete OpenCV preprocessing contract.
* Runs the trained classifier.
* Returns the three strongest breed predictions and their probabilities.

## Exported Artifacts

* `pet_breed_classifier.keras`
* `best_pet_breed_model.keras`
* `class_names.json`
* `preprocessing_config.json`
* Evaluation and error-analysis CSV files
* Training and confusion-matrix figures

---

# Day 5 — Full Evaluation, Explainability and Sprint Review

Day 5 completed the evaluation and explainability cycle without retraining the Day 4 model.

## Class Balance and SMOTE Decision

The smallest training class contained 134 images, while the largest contained 140.

$$
Imbalance\ Ratio
=
\frac{140}{134}
=
1.0448
$$

The dataset was already balanced, so SMOTE was not required.

SMOTE was also unsuitable because interpolation between raw image pixels may create unrealistic samples. Image augmentation was the task-appropriate alternative.

## Baseline Comparison

A class-prior baseline was used because the Week 6 ECG model solved a different task and could not provide a valid numerical comparison.

| Metric         | Class-Prior Baseline | MobileNetV2 |
| -------------- | -------------------: | ----------: |
| Accuracy       |                2.71% |      89.00% |
| Macro F1       |                0.14% |      88.96% |
| Top-3 Accuracy |                8.12% |      98.38% |
| Macro ROC-AUC  |               50.00% |      99.78% |
| Macro PR-AUC   |                2.70% |      95.33% |

The trained classifier substantially outperformed the baseline across every metric.

## Per-Breed Evaluation

The weakest classes by F1-score were:

| Breed                      | Precision | Recall |     F1 |
| -------------------------- | --------: | -----: | -----: |
| Staffordshire Bull Terrier |    57.58% | 65.52% | 61.29% |
| American Pit Bull Terrier  |    72.73% | 53.33% | 61.54% |
| Ragdoll                    |    67.65% | 76.67% | 71.88% |
| Bengal                     |   100.00% | 56.67% | 72.34% |
| Russian Blue               |    73.53% | 83.33% | 78.12% |

Precision-Recall curves were generated for these five breeds.

## SHAP Explainability

SHAP measured how image regions pushed predictions toward or away from a selected class.

### Correct Prediction

A Sphynx image was classified correctly with 97.95% confidence.

The strongest positive regions appeared around:

* Large ears
* Wrinkled face
* Exposed skin
* Front limbs

These are meaningful visual characteristics of the breed.

### Incorrect Prediction

A Havanese image was classified as Newfoundland with 99.05% confidence.

The strongest support appeared around the dark coat and body. The image was clear, so the error was categorized as a model weakness caused by visual similarity rather than poor data quality.

The model relied on coat appearance but could not directly understand the real-world difference in animal size.

### Global SHAP

Global SHAP used five correctly classified images from different breeds.

| Region                        | Importance |
| ----------------------------- | ---------: |
| Top row                       |     22.24% |
| Middle row                    |     67.76% |
| Bottom row                    |     10.01% |
| Middle-left and middle-center |     60.35% |

The model generally focused on the central animal regions and assigned less importance to padding and outer background areas.

Because five images were used to keep CPU execution practical, this result is representative rather than an exact summary of every test image.

## Saved Outputs

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

All Day 5 quality checks passed.

---

# Weekly Results Summary

## Text Track

* Created separate preprocessing pipelines for classical and deep-learning models.
* Preserved sentiment-changing negation.
* Tuned TF-IDF achieved Test F1 `0.8611`.
* GloVe achieved Test F1 `0.7830`.
* The previous weighted TF-IDF and DistilBERT ensemble remained strongest with Test F1 `0.8939`.

## Image Track

* Built a reusable OpenCV preprocessing pipeline.
* Trained a classifier for 37 pet breeds.
* Achieved 89.00% Test Accuracy.
* Achieved 98.38% Top-3 Accuracy.
* Reached 99.78% Macro ROC-AUC.
* Identified systematic confusion between visually similar breeds.
* Generated local and global SHAP explanations.
* Exported the model and preprocessing contract for deployment.

The text and image metrics should not be directly compared because they measure different tasks.

---

# Main Technical Lessons

1. Preprocessing must match the model architecture.
2. Stronger cleaning is not always better for natural-language models.
3. TF-IDF can outperform averaged embeddings on limited task-specific data.
4. Word order and context remain limitations of simple lexical representations.
5. OpenCV loads images as BGR rather than RGB.
6. Image resizing should preserve the original aspect ratio.
7. Pretrained models require their original normalization contract.
8. Transfer learning can produce strong results with relatively few trainable parameters.
9. Accuracy must be supported by per-class and ranking metrics.
10. High confidence does not guarantee that a prediction is correct.
11. Error analysis reveals weaknesses hidden by one overall score.
12. SHAP connects mathematical feature contributions with visible image regions.
13. Training and deployment must use identical preprocessing.

---

# Sprint Review

Sprint 3 delivered:

* Reproducible text and image preprocessing pipelines.
* TF-IDF and GloVe representation experiments.
* An integrated 37-class image-classification model.
* Full baseline and per-class evaluation.
* Confusion-matrix and misclassification analysis.
* Local and global SHAP explanations.
* Exported model and configuration artifacts.
* Deployment-ready prediction functions.

The completed notebooks and generated outputs are ready to be committed and pushed to the Week 8 repository directories.

---

# Sprint Retrospective

## What Went Well

* Fixed splits allowed fair comparisons.
* Task-specific preprocessing prevented unnecessary information loss.
* Transfer learning achieved strong image-classification performance.
* The final test set remained untouched until model decisions were complete.
* SHAP made correct and incorrect predictions visually understandable.
* All final quality checks passed.

## Main Challenges

* Negation and word order remained important challenges for classical NLP.
* Averaged GloVe vectors lost sequence information.
* Visually similar animal breeds caused systematic classification errors.
* Some incorrect image predictions had very high confidence.
* SHAP image explanations required more computation on CPU.

## Concrete Change for Sprint 4

Sprint 4 will create a confidence-aware web interface that supports both project tracks.

The interface will allow users to:

* Enter text and receive a sentiment prediction.
* View the words or phrases that influenced the sentiment decision.
* Upload an animal image.
* Receive the three strongest breed predictions and their probabilities.
* View the image regions that supported the classification.
* Receive a warning when a prediction is uncertain.

---

# Tools Used

* Python
* Jupyter Notebook
* TensorFlow / Keras
* MobileNetV2
* OpenCV
* SHAP
* Scikit-learn
* NLTK
* Hugging Face Datasets and Transformers
* GloVe
* NumPy
* Pandas
* Matplotlib
* Seaborn

---

# Conclusion

Week 8 transformed separate NLP and computer-vision experiments into reproducible, evaluated, and explainable machine-learning pipelines.

The IMDB track demonstrated how preprocessing and representation choices affect sentiment classification. TF-IDF remained highly competitive, while GloVe illustrated the strengths and limitations of fixed word embeddings.

The Oxford-IIIT Pet track progressed from raw OpenCV preprocessing to a custom 37-breed MobileNetV2 classifier with 89.00% Test Accuracy and 98.38% Top-3 Accuracy.

Complete evaluation and SHAP explanations showed both what the models achieved and where they still failed.

The resulting text and image artifacts now provide the technical foundation for an interactive web application in the next sprint.
