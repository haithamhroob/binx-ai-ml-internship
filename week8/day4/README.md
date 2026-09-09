# Week 8 — Day 4: Model Integration and Error Analysis

## Project Overview

This notebook builds a complete image-classification pipeline for the Oxford-IIIT Pet Dataset.

The Day 3 preprocessing operations were integrated with a MobileNetV2 transfer-learning model to classify raw pet images into 37 different cat and dog breeds.

The notebook also evaluates the trained model, analyzes its errors, and exports the required files for future web deployment.

---

## Learning Objectives

* Integrate preprocessing and classification into one end-to-end pipeline.
* Ensure consistency between training-time and prediction-time preprocessing.
* Train a transfer-learning classifier for 37 pet breeds.
* Evaluate the model using Top-1 and Top-3 accuracy.
* Analyze errors using a confusion matrix.
* Inspect and categorize misclassified images.
* Export the model and preprocessing configuration.

---

## Dataset

**Dataset:** Oxford-IIIT Pet Dataset

The dataset contains 37 cat and dog breeds with approximately 200 images per class.

| Split      | Number of Images |
| ---------- | ---------------: |
| Training   |            5,173 |
| Validation |            1,108 |
| Test       |            1,109 |
| Total      |            7,390 |

A stratified 70%/15%/15% split was used to preserve the breed distribution.

The image paths were checked to guarantee that no image appeared in more than one split.

---

## Image Preprocessing

The same preprocessing function is used during both training and prediction:

1. Read the image using OpenCV.
2. Convert the image from BGR to RGB.
3. Resize while preserving the original aspect ratio.
4. Add padding to create a `224 × 224` image.
5. Convert pixel values to `float32`.
6. Apply MobileNetV2 normalization.

The original pixel range is transformed from:

$$
[0,255] \rightarrow [-1,1]
$$

Reusing the same function prevents **training/serving skew**, where deployment images are processed differently from training images.

---

## Data Augmentation

The training pipeline applies:

* Random horizontal flipping.
* Small random rotations.
* Random zooming.

Augmentation creates realistic variations of the training images and helps the model generalize to unseen images.

Augmentation is automatically disabled during validation and prediction.

---

## Model Architecture

The classifier uses a MobileNetV2 convolutional base pretrained on ImageNet.

The convolutional base was frozen during training, while a new classification head learned the 37 pet breeds.

The architecture consists of:

* MobileNetV2 feature extractor.
* Global Average Pooling.
* Dropout with a rate of `0.30`.
* Dense Softmax output layer with 37 units.

| Parameter Type           |     Count |
| ------------------------ | --------: |
| Total parameters         | 2,305,381 |
| Trainable parameters     |    47,397 |
| Non-trainable parameters | 2,257,984 |

For each image, Softmax produces 37 class probabilities:

$$
P(y=k \mid x)=
\frac{e^{z_k}}
{\sum_{j=1}^{37}e^{z_j}}
$$

---

## Training Configuration

* Optimizer: Adam
* Initial learning rate: `0.001`
* Loss: Sparse Categorical Cross-Entropy
* Maximum epochs: 8
* Batch size: 32

The following callbacks were used:

* `ModelCheckpoint`
* `EarlyStopping`
* `ReduceLROnPlateau`

The lowest validation loss occurred at epoch 6, so the model restored the weights from that epoch.

---

## Final Results

| Split      | Accuracy | Top-3 Accuracy |   Loss |
| ---------- | -------: | -------------: | -----: |
| Validation |   90.07% |         98.38% | 0.2980 |
| Test       |   89.00% |         98.38% | 0.3283 |

Additional test results:

* Correct predictions: **987**
* Misclassified images: **122**
* Test error rate: **11.00%**
* Macro F1-score: **88.96%**
* Weighted F1-score: **88.99%**

The small difference between validation and test accuracy indicates good generalization.

The high Top-3 accuracy shows that the correct breed was usually among the model’s strongest three candidates.

---

## Error Analysis

A normalized confusion matrix was created to identify which breeds were commonly confused.

The most frequent confusion patterns included:

| True Breed                | Predicted Breed            | Errors |
| ------------------------- | -------------------------- | -----: |
| Bengal                    | Egyptian Mau               |     10 |
| American Pit Bull Terrier | Staffordshire Bull Terrier |     10 |
| Ragdoll                   | Birman                     |      4 |
| American Pit Bull Terrier | American Bulldog           |      4 |
| Russian Blue              | British Shorthair          |      4 |

These errors mainly occurred between breeds with similar visual characteristics, such as coat color, face shape, body structure, and fur patterns.

The weakest recall appeared in classes such as:

* Bengal
* American Pit Bull Terrier
* Staffordshire Bull Terrier

Three high-confidence errors were inspected using image sharpness, brightness, prediction confidence, and visual similarity.

They were categorized primarily as model weaknesses caused by confident confusion between visually similar breeds.

---

## End-to-End Prediction

The final function:

`predict_pet_breed(raw_image_path)`

accepts a raw image path and automatically:

* Reads and preprocesses the image.
* Applies the trained classifier.
* Displays the uploaded image.
* Returns the three most probable breeds.
* Reports the probability of each prediction.

This creates one consistent path from raw user input to the final classification result.

---

## Exported Files

The notebook exports:

* `pet_breed_classifier.keras`
* `best_pet_breed_model.keras`
* `class_names.json`
* `preprocessing_config.json`
* `training_history.csv`
* `final_evaluation.csv`
* `classification_report.csv`
* `top_confusion_pairs.csv`
* `misclassified_examples.csv`
* `three_error_case_review.csv`
* `training_curves.png`
* `normalized_confusion_matrix.png`
* `misclassified_examples.png`

The model, class ordering, and preprocessing configuration can later be connected to a web interface without changing the prediction behavior.

---

## Tools Used

* Python
* TensorFlow / Keras
* MobileNetV2
* OpenCV
* NumPy
* Pandas
* Scikit-learn
* Matplotlib
* Seaborn
* Jupyter Notebook

---

## Conclusion

Day 4 transformed the separate preprocessing and model components into a complete and reproducible classification system.

The final pipeline can classify raw pet images across 37 breeds, return ranked probabilities, evaluate performance, identify systematic confusion patterns, and inspect individual errors.

The exported model and preprocessing contract provide a reliable foundation for future web integration.
