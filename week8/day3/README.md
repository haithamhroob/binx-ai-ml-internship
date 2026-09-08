# Week 8 - Day 3: Computer Vision Preprocessing with OpenCV

## Overview

This notebook builds a complete image-preprocessing workflow using OpenCV and connects it to a pretrained MobileNetV2 model.

The goal is to standardize raw images, create realistic augmented training examples, and ensure that the final inputs match the expectations of a transfer-learning model.

## Dataset

The notebook uses the Oxford-IIIT Pet image dataset:

- Image files found: 7,390
- Classes: 37 cat and dog breeds
- Images have different sizes, poses, lighting conditions, and backgrounds
- Target image size: `224 x 224`

The image archive is downloaded automatically during the first notebook run.

## Topics Covered

- Why image standardization is necessary
- Reading images with OpenCV
- Image arrays and `(height, width, channels)`
- The BGR versus RGB color-order pitfall
- Direct resizing and aspect-ratio distortion
- Resizing with padding
- Pixel normalization from `[0, 255]` to `[0, 1]`
- Building a reusable OpenCV preprocessing function
- Image augmentation
- MobileNetV2-specific preprocessing
- Using a pretrained model as a feature extractor
- Running pretrained ImageNet inference

## OpenCV Preprocessing Pipeline

The general preprocessing function performs:

```text
Read image
-> Convert BGR to RGB
-> Resize while preserving aspect ratio
-> Add padding to reach 224 x 224
-> Convert to float32
-> Normalize pixels to [0, 1]
```

Six images with different original dimensions were processed successfully into one batch with:

```text
Shape: (6, 224, 224, 3)
Data type: float32
Pixel range: [0, 1]
```

## Image Augmentation

The training augmentation pipeline applies controlled random transformations:

- Rotation
- Width and height shifts
- Zoom
- Horizontal flipping
- Brightness variation

These transformations generate varied training examples while preserving the original breed label. Augmentation is intended only for training data, not validation, testing, or inference.

## MobileNetV2 Preprocessing

MobileNetV2 does not use the general `[0, 1]` normalization. Its `preprocess_input` function converts raw floating-point pixels to approximately `[-1, 1]`:

```text
Read image
-> Convert BGR to RGB
-> Resize with padding
-> Convert to float32
-> Apply MobileNetV2 preprocess_input
```

The two normalization methods must not be applied together.

## Transfer-Learning Connection

A frozen MobileNetV2 convolutional base pretrained on ImageNet was used as a feature extractor.

| Item | Result |
|---|---:|
| Input shape | `(1, 224, 224, 3)` |
| Feature-map shape | `(1, 7, 7, 1280)` |
| Base-model parameters | 2,257,984 |
| Base model trainable | False |

The output feature map contains learned visual features such as edges, textures, shapes, and object parts. It is not yet a custom 37-breed classifier.

## Pretrained Inference Check

The complete ImageNet MobileNetV2 classifier successfully produced 1,000-class probability distributions for the processed images. Example results included:

| Dataset breed | Relevant ImageNet prediction | Confidence |
|---|---|---:|
| Persian | Persian Cat | 95.93% |
| Basset Hound | Basset | 94.26% |
| Pug | Pug | 91.20% |
| Yorkshire Terrier | Yorkshire Terrier, rank 2 | 34.21% |

These predictions verify pipeline compatibility. They are not an accuracy evaluation of an Oxford-IIIT Pet classifier because the Oxford labels and the 1,000 ImageNet classes are not identical.

## Saved Outputs

The notebook saves the following files under:

```text
outputs/week8_day3
```

- `raw_image_dimension_sample.csv`
- `preprocessing_summary.csv`
- `pretrained_imagenet_predictions.csv`

## Running the Notebook

Place the notebook inside `week8/day3` and run all cells in order.

The first run downloads:

- The Oxford-IIIT Pet image archive
- MobileNetV2 ImageNet weights
- ImageNet class labels

The CUDA messages can be ignored when no supported GPU is available; TensorFlow completes the notebook using the CPU.

## Conclusion

Day 3 implemented the complete preprocessing sequence required for image models: reading, resizing, color conversion, normalization, augmentation, and model-specific preparation.

The final OpenCV pipeline produces consistent model-ready images, while the MobileNetV2 experiment confirms that preprocessing must match the configuration used during pretraining.
