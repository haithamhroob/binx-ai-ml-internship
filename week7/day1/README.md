# Week 7 — Day 1: Sprint 2 Planning and Convolutional Neural Networks

## Project: Melanoma Skin Cancer Classification

### Overview

Week 7 starts the second project sprint and introduces Convolutional Neural Networks (CNNs) for medical-image classification.

During Week 6, a fully connected neural network learned from manually extracted ECG features. In this project, the input consists of dermoscopic images, so the model must preserve spatial relationships between neighboring pixels and learn visual features directly from the images.

The dataset contains two classes:

- **Benign:** non-cancerous skin lesions.
- **Malignant:** cancerous melanoma lesions.

The purpose of Day 1 was not to train the final classifier. It was to understand convolution, filters, feature maps, stride, padding, and parameter sharing, and then select the appropriate core architecture for the project.

## Day 1 Objectives

- Define the Sprint 2 goal and core-model backlog.
- Inspect the dataset and verify its class structure.
- Explain why dense-only networks are inefficient for image data.
- Implement a manual two-dimensional convolution operation.
- Apply vertical and horizontal edge-detection filters.
- Examine the effects of stride and padding.
- Compare the parameter counts of dense and convolutional layers.
- Select the core architecture for melanoma classification.

## Dataset

**Source:** [Melanoma Skin Cancer Dataset — Benign vs Malignant](https://www.kaggle.com/datasets/ailearner-researchlab/melanoma-skin-cancer-dataset-benign-vs-malignant)

The notebook detected **13,879 dermoscopic images**.

| Split | Benign | Malignant | Total |
|---|---:|---:|---:|
| Training | 6,289 | 5,590 | 11,879 |
| Test | 1,000 | 1,000 | 2,000 |
| **Total** | **7,289** | **6,590** | **13,879** |

The training set is reasonably balanced, and the test set is perfectly balanced. No missing image paths or duplicate paths were detected.

The dataset does not include a separate validation set. A stratified validation subset must therefore be created later from the training set, while the test set remains untouched until final evaluation.

## Medical Evaluation Priority

Predicting a malignant lesion as benign is more dangerous than producing a false-positive warning. Therefore, the main evaluation focus for the project will be:

- Malignant-class Recall
- F2-score
- Confusion Matrix

Accuracy and F1-score will also be reported, but they will not be interpreted alone.

## Manual Two-Dimensional Convolution

A convolutional filter is a small matrix of weights that moves across an image. At each location, the image region and filter are multiplied element by element, and the results are summed:

$$
Y(i,j)=\sum_{m=0}^{k_h-1}\sum_{n=0}^{k_w-1}X(i+m,j+n)K(m,n)
$$

Repeating this operation across the image produces a **feature map** that shows where the filter detected its target visual pattern.

Two manually defined $3\times3$ filters were applied to a grayscale malignant-lesion image:

- A vertical-edge filter that responds to left-to-right intensity changes.
- A horizontal-edge filter that responds to top-to-bottom intensity changes.

The resulting feature maps emphasized lesion boundaries, internal texture changes, and other strong visual transitions. These hand-defined filters do not diagnose melanoma; they may also respond to hair, lighting, image borders, and unrelated skin texture. A trained CNN learns many useful filters automatically from the training data.

Grayscale was used only to simplify the manual demonstration. The final classifier should preserve all three RGB channels because lesion color may contain useful diagnostic information.

## Stride and Padding Experiment

The convolution output size is calculated using:

$$
H_{out}=\left\lfloor\frac{H+2P-K}{S}\right\rfloor+1
$$

$$
W_{out}=\left\lfloor\frac{W+2P-K}{S}\right\rfloor+1
$$

where $P$ is padding, $K$ is kernel size, and $S$ is stride.

| Configuration | Output Shape |
|---|---:|
| Padding 0, Stride 1 | `(222, 222)` |
| Padding 1, Stride 1 | `(224, 224)` |
| Padding 1, Stride 2 | `(112, 112)` |

Padding preserves border information and can maintain the spatial dimensions. A larger stride reduces computation and memory use, but it examines fewer image positions and may discard small lesion details.

## Parameter Sharing

Flattening an RGB image of shape `(224, 224, 3)` produces:

$$
224\times224\times3=150,528
$$

Connecting these inputs to a dense layer with 32 neurons requires:

$$
(150,528\times32)+32=4,816,928
$$

trainable parameters.

A convolutional layer with 32 RGB filters of size $3\times3$ requires only:

$$
(3\times3\times3\times32)+32=896
$$

trainable parameters.

The dense layer therefore uses approximately **5,376 times more parameters**. The convolutional layer is much more efficient because each small filter reuses the same weights at every spatial location. This mechanism is called **parameter sharing**.

## Core Architecture Decision

The selected core architecture is a **two-dimensional Convolutional Neural Network** because it:

- Preserves the two-dimensional spatial structure of images.
- Processes small local regions.
- Shares filters across the complete image.
- Learns visual features directly from training images.
- Builds a hierarchy from simple edges and textures to more complex lesion representations.
- Uses dramatically fewer parameters than a dense-only image model.

The planned binary output configuration is:

```python
Dense(1, activation="sigmoid")
```

with:

```python
loss="binary_crossentropy"
```

The output represents the predicted probability of the malignant class.

## Sprint 2 Experimental Principle

Only one major experimental factor should be changed at a time. Each configuration and its validation metrics should be recorded, while the test set should be preserved for one final evaluation.

This makes it possible to determine which modification caused an improvement instead of combining several changes and guessing which one helped.

## Day 1 Conclusion

Day 1 established the architectural foundation for the melanoma image-classification project. Dataset inspection confirmed that the images were available, reasonably balanced, and free of missing or duplicate paths.

Manual edge filters demonstrated how convolution extracts local image patterns. The stride and padding experiments showed how convolution settings control feature-map dimensions, while the parameter comparison demonstrated the efficiency of shared convolutional filters.

The final decision was to use a **2D CNN** as the core model because it preserves spatial information, learns useful visual patterns, and requires far fewer parameters than a dense-only approach.

## Requirements

```bash
pip install kagglehub matplotlib numpy pandas pillow
```

## Notebook

- `day1.ipynb` — Sprint 2 planning, dataset inspection, manual convolution, edge detection, stride and padding experiments, parameter comparison, and architecture selection.
