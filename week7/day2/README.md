# Week 7 — Day 2: Building CNNs & Transfer Learning
### Melanoma Skin Cancer Classification (Benign vs. Malignant)

This notebook builds on Day 1 (convolution fundamentals) and moves from individual convolution operations to complete, trainable image-classification pipelines. It compares three approaches for classifying dermoscopic skin-lesion images as **benign** or **malignant**: a CNN built from scratch, the same CNN with data augmentation, and transfer learning with a pre-trained MobileNetV2.

---

## Learning Objectives

By the end of this notebook, you will be able to:

- Explain how pooling reduces the spatial size of feature maps.
- Build a complete CNN using convolution, pooling, flattening, and dense layers.
- Train a CNN from scratch on the melanoma image dataset.
- Apply data augmentation to improve generalization and reduce overfitting.
- Use transfer learning with a pre-trained image-classification model.
- Compare validation performance and training time across different approaches.
- Identify which approach provides the strongest practical result for the image-classification project.

---

## Dataset

- **Source:** [Melanoma Skin Cancer Dataset (Benign vs Malignant)](https://www.kaggle.com/datasets/ailearner-researchlab/melanoma-skin-cancer-dataset-benign-vs-malignant) via `kagglehub`
- **Total images detected:** 13,879
- **Classes:** `benign`, `malignant`
- **Splits:** The raw dataset ships with `train` and `test` only. A stratified **20% validation split** is carved out of the training data (preserving the benign/malignant ratio), while the **test set stays completely untouched** until final model evaluation.

---

## Experimental Plan

**Problem:** A CNN trained from scratch can learn useful image features, but a limited dataset may cause overfitting and require significant training time.

**Goal:** Build a full CNN, improve its generalization with data augmentation, and compare it against a pre-trained transfer-learning model.

**Sequence:**
1. Create a stratified validation split from the training data.
2. Examine how pooling changes feature-map dimensions.
3. Build and train a CNN from scratch.
4. Add data augmentation and compare validation behavior.
5. Apply transfer learning using a pre-trained MobileNetV2 model.
6. Compare accuracy, validation performance, and training time.
7. Select the best-performing model and evaluate it once on the held-out test set.

---

## Notebook Contents

| Section | Description |
|---|---|
| **2.1 Pooling** | Explains max pooling — shrinking feature maps by keeping the strongest signal in each region — and why it reduces computation, controls overfitting, and adds robustness to small shifts. |
| **2.2 Full CNN Architecture** | Builds a 3-block `Conv2D → MaxPooling2D` stack, flattened into dense layers, for binary classification (`Dense(1, activation="sigmoid")`). Input images are resized to 128×128×3. |
| **2.3 Data Augmentation** | Applies `RandomFlip`, `RandomRotation`, and `RandomZoom` to artificially expand the training set and reduce overfitting — the standard first line of defense in computer vision. |
| **2.4 Transfer Learning** | Loads `MobileNetV2` pre-trained on ImageNet, freezes its feature-extractor layers (`base.trainable = False`), and attaches a new classification head. |
| **Hands-On Lab** | Trains all three models, records validation accuracy/loss and training time for each, and documents which approach performs best and why. |
| **2.7 Final Test Evaluation** | Evaluates only the selected best model once, on the untouched test set. |

---

## Models Compared

| Model | Approach |
|---|---|
| CNN from Scratch | 3× (Conv2D + MaxPooling2D) → Flatten → Dense(128) → Dense(1, sigmoid) |
| CNN + Data Augmentation | Same architecture, with `RandomFlip` / `RandomRotation` / `RandomZoom` preprocessing |
| MobileNetV2 Transfer Learning | Frozen pre-trained MobileNetV2 base (ImageNet weights) + Flatten → Dense(1, sigmoid) |

---

## Results

| Model | Best Validation Accuracy | Training Time (minutes) |
|---|---|---|
| CNN from Scratch | ~87.37% | ~11.19 |
| CNN + Data Augmentation | ~86.57% | ~11.95 |
| **MobileNetV2 Transfer Learning** | **~88.09%** | ~13.75 |

**Final test evaluation (selected model — MobileNetV2 Transfer Learning):**
- Test Loss: **0.2682**
- Test Accuracy: **88.45%**

---

## Conclusion

- The **CNN from scratch** achieved strong validation performance, showing that convolutional layers can learn useful visual features directly from melanoma images.
- **Data augmentation** added training variation but did not improve the best validation accuracy over the plain CNN in this run.
- **MobileNetV2 transfer learning** achieved both the highest validation accuracy and the lowest validation loss, and was therefore selected for final test evaluation.
- This experiment demonstrates the practical value of comparing multiple modeling approaches rather than relying on a single architecture.

---

## Tools & Requirements

- Python 3.12
- TensorFlow / Keras (`tensorflow==2.21.0`)
- `kagglehub` (dataset download)
- `pandas`, `numpy`, `matplotlib`
- `scikit-learn` (`train_test_split` for stratified validation split)
- `Pillow` (PIL)
- Jupyter Notebook / JupyterLab (GPU recommended for training speed)

Install core dependencies:
```bash
pip install tensorflow kagglehub pandas numpy matplotlib scikit-learn pillow
```

## Usage

1. Ensure a Kaggle API token is configured (`kagglehub` will prompt / cache credentials on first run).
2. Open `day2.ipynb` in Jupyter.
3. Run all cells top to bottom — the notebook downloads the dataset, builds the stratified validation split, trains all three models in sequence, and produces the comparison table/charts and final test evaluation automatically.

> **Note:** Random seeds (`SEED = 42`) are fixed for `random`, `numpy`, and `tensorflow` to keep results reproducible, though exact accuracy may vary slightly by hardware/TF version.
