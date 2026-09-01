# Week 7 — Day 2: Building CNNs & Transfer Learning

### Melanoma Skin Cancer Classification (Benign vs. Malignant)

This notebook moves from convolution fundamentals to complete image-classification pipelines. It compares a CNN from scratch, the same CNN with data augmentation, frozen MobileNetV2 transfer learning, and limited MobileNetV2 fine-tuning.

## Learning Objectives

- Explain and apply Max Pooling.
- Build a complete CNN using convolution, pooling, flattening, and dense layers.
- Apply data augmentation to reduce overfitting.
- Use a frozen pre-trained model as a feature extractor.
- Fine-tune a limited set of pre-trained layers using a small learning rate.
- Compare models using accuracy, malignant recall, F1, F2, validation loss, and training time.
- Evaluate the selected model once on the untouched test set.

## Dataset

- Source: [Melanoma Skin Cancer Dataset](https://www.kaggle.com/datasets/ailearner-researchlab/melanoma-skin-cancer-dataset-benign-vs-malignant)
- Total images detected in the original run: 13,879
- Classes: `benign` and `malignant`
- The original training set is divided using a stratified 80/20 training-validation split.
- The original test set remains untouched until final evaluation.

## Experimental Sequence

1. Demonstrate Max Pooling numerically and on a real image.
2. Train a three-block CNN from scratch.
3. train the same CNN with `RandomFlip`, `RandomRotation`, and `RandomZoom`.
4. Train a frozen MobileNetV2 feature extractor.
5. Fine-tune the final 30 MobileNetV2 layers while keeping Batch Normalization frozen.
6. Compare all experiments on validation data.
7. Select by F2, with malignant recall as the tie-breaker.
8. Evaluate the winner once on the test set.

## Models Compared

| Model | Architecture |
|---|---|
| CNN from Scratch | 3× (`Conv2D → MaxPooling2D`) → `Flatten` → `Dense(128)` → `Dense(1, sigmoid)` |
| Augmented CNN | Same CNN preceded by mild image augmentation |
| Frozen MobileNetV2 | Frozen MobileNetV2 → `GlobalAveragePooling2D` → `Dense(1, sigmoid)` |
| Fine-tuned MobileNetV2 | Same transfer model with the final 30 layers opened at learning rate `1e-5` |

## Medical Evaluation Decision

The positive class is malignant. Accuracy alone can hide dangerous false negatives, so the primary metrics are malignant recall and F2. The final confusion matrix reports the number of malignant lesions predicted as benign.

## Best-Weight Protection

Every experiment uses Early Stopping with `restore_best_weights=True`, monitored by validation loss. Therefore final metrics correspond to the strongest retained weights rather than simply the last epoch.

## Results

Exact corrected results are produced when the notebook is run. They are intentionally not hard-coded here because early stopping and fine-tuning change the original ten-epoch benchmark. Copy the generated validation comparison and final test table here only after completing the run.

## Tools

- Python 3
- TensorFlow / Keras
- KaggleHub
- NumPy, pandas, Matplotlib
- scikit-learn
- Pillow

## Usage

1. Open `day2_corrected.ipynb` in Jupyter or Colab with GPU enabled.
2. Run all cells from top to bottom.
3. Use the generated validation table to explain why the model was selected.
4. Report the final test metrics and the false-negative count from the confusion matrix.
