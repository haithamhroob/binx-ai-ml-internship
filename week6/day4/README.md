# Week 6 — Day 4

## Building and Training a Neural Network in Keras

### Project

ECG-Based Multi-Label Cardiac Diagnosis Using PTB-XL

---

## Overview

Day 4 implemented the complete TensorFlow/Keras workflow for the ECG-based cardiac diagnosis project.

The previous days established the neural-network architecture, activation functions, loss function, training loop, optimizer, and learning rate. Day 4 combined these decisions into a complete Keras experiment.

Two neural networks were trained and compared:

1. A basic neural network.
2. A regularized neural network using Batch Normalization and Dropout.

The models predicted four independent cardiac-disease labels:

- MI: Myocardial Infarction
- STTC: ST/T Change
- CD: Conduction Disturbance
- HYP: Hypertrophy

Because one ECG may contain multiple diagnoses, the project was treated as a multi-label classification problem.

---

## Learning Objectives

- Build a neural network using the Keras Sequential API.
- Understand the role of Input, Dense, ReLU, and Sigmoid layers.
- Compile a multi-label network using Adam and Binary Cross-Entropy.
- Train the network using training and validation data.
- Read and diagnose the Keras training history.
- Plot training and validation loss and accuracy.
- Apply Batch Normalization and Dropout.
- Compare a basic model with a regularized model.
- Evaluate the selected model on the official test set.
- Compare the neural network with the Day 1 baseline.

---

## Dataset

- Dataset: PTB-XL
- Total ECG recordings: 21,799
- ECGs used for modeling: 21,388
- Recording duration: 10 seconds
- Sampling frequency: 100 Hz
- ECG leads: 12
- Target labels: 4
- Task type: Multi-label classification

Recordings outside the five diagnostic superclasses were removed. Normal ECG recordings were retained during sample selection but represented in the four-disease target as:

    [0, 0, 0, 0]

These samples taught the network how the absence of all four target diseases appeared.

---

## Feature Representation

Each ECG was represented using six statistical features from each of the 12 leads:

- Mean
- Standard deviation
- Minimum
- Maximum
- Range
- Root Mean Square

The total number of input features was:

    12 leads × 6 features = 72 features

The final feature and target shapes were:

- Feature table: (21,388, 72)
- Target table: (21,388, 4)

---

## Data Splitting

The official PTB-XL stratified folds were used:

- Folds 1–8: Training
- Fold 9: Validation
- Fold 10: Test

The resulting shapes were:

- Training inputs: (17,084, 72)
- Training targets: (17,084, 4)
- Validation inputs: (2,146, 72)
- Validation targets: (2,146, 4)
- Test inputs: (2,158, 72)
- Test targets: (2,158, 4)

The training label counts were:

- MI: 4,379
- STTC: 4,186
- CD: 3,907
- HYP: 2,119

The training set contained 7,243 rows with four zero disease labels.

No missing or infinite input values remained.

---

## Data Standardization

StandardScaler was fitted using the training data only.

The learned training means and standard deviations were then applied to the validation and test sets.

This prevented information from the validation or test data from influencing preprocessing and avoided data leakage.

---

## Keras Workflow

The main Keras workflow used during Day 4 was:

    Build → Compile → Fit → Evaluate

- Build defined the model architecture.
- Compile selected the optimizer, loss function, and training metrics.
- Fit performed forward propagation, loss calculation, Backpropagation, and parameter updates.
- Evaluate measured performance on unseen data.

TensorFlow handled the mathematical operations and gradient calculations, while Keras provided the high-level model-building interface.

---

## Basic Neural Network

The basic network used the following architecture:

    72 Inputs
        ↓
    Dense(32) + ReLU
        ↓
    Dense(16) + ReLU
        ↓
    Dense(4) + Sigmoid

The output layer contained four independent Sigmoid neurons, one for each disease.

Softmax was not appropriate because the diseases were not mutually exclusive.

### Parameter Count

- First Dense layer: 2,336 parameters
- Second Dense layer: 528 parameters
- Output layer: 68 parameters
- Total parameters: 2,932
- Trainable parameters: 2,932
- Non-trainable parameters: 0

---

## Compilation Configuration

The basic model was compiled using:

- Optimizer: Adam
- Learning rate: 0.001
- Loss: Binary Cross-Entropy
- Training metric: Binary Accuracy
- Batch size: 32
- Epochs: 40

Binary Cross-Entropy was selected because every output represented a separate binary disease decision.

Binary Accuracy was recorded to satisfy the training-history requirement, but it was not treated as the main medical evaluation metric because the target contained many negative labels.

---

## Basic Model Training Results

The basic model produced:

- Initial training loss: 0.4656
- Final training loss: 0.3539
- Best validation loss: 0.3946
- Best validation epoch: 29
- Final validation loss: 0.4021
- Final validation Binary Accuracy: approximately 0.8343

Training loss continued decreasing throughout the 40 epochs.

Validation loss reached its minimum at epoch 29 and then increased slightly while training loss continued decreasing.

This indicated mild overfitting.

---

## Basic Model Validation Metrics

Using a fixed threshold of 0.5, the basic model achieved:

- Macro Precision: 0.6905
- Macro Recall: 0.3947
- Macro F1-score: 0.5009

Disease-specific results were:

| Disease | Precision | Recall | F1-score |
|---|---:|---:|---:|
| MI | 0.68 | 0.38 | 0.49 |
| STTC | 0.61 | 0.30 | 0.41 |
| CD | 0.78 | 0.52 | 0.63 |
| HYP | 0.68 | 0.37 | 0.48 |

The model produced relatively high Precision but low Recall.

This meant that its positive predictions were often correct, but it missed many true disease cases.

The result also demonstrated why Binary Accuracy alone was misleading. Validation Binary Accuracy was approximately 83%, while Macro Recall was only approximately 39%.

---

## Batch Normalization and Dropout

A second network was created to stabilize training and reduce overfitting.

Batch Normalization standardized intermediate layer values during training and learned suitable scale and shift parameters.

Dropout randomly disabled 30% of layer outputs during each training step. This prevented the network from depending too heavily on specific neurons.

Dropout was active only during training. It was disabled automatically during validation, evaluation, and prediction.

---

## Regularized Neural Network

The regularized architecture was:

    72 Inputs
        ↓
    Dense(32)
        ↓
    Batch Normalization
        ↓
    ReLU
        ↓
    Dropout(0.3)
        ↓
    Dense(16)
        ↓
    Batch Normalization
        ↓
    ReLU
        ↓
    Dropout(0.3)
        ↓
    Dense(4) + Sigmoid

The Dense biases were disabled before Batch Normalization because the normalization layer already learned a shift parameter.

### Parameter Count

- Total parameters: 3,076
- Trainable parameters: 2,980
- Non-trainable parameters: 96

The non-trainable parameters were the moving means and moving variances maintained by the Batch Normalization layers.

Dropout added no trainable parameters.

---

## Regularized Model Results

The regularized model produced:

- Initial training loss: 0.5122
- Final training loss: 0.4110
- Best validation loss: 0.3947
- Best validation epoch: 39
- Final validation loss: 0.3954
- Final validation Binary Accuracy: approximately 0.8221

The training and validation losses remained close.

This showed that Batch Normalization and Dropout successfully reduced the overfitting gap.

Training loss was sometimes higher than validation loss because Dropout made training more difficult by disabling neurons, while all neurons were active during validation.

---

## Regularized Model Validation Metrics

The regularized model achieved:

- Macro Precision: 0.7437
- Macro Recall: 0.2415
- Macro F1-score: 0.3511

Disease-specific results were:

| Disease | Precision | Recall | F1-score |
|---|---:|---:|---:|
| MI | 0.72 | 0.19 | 0.29 |
| STTC | 0.65 | 0.11 | 0.18 |
| CD | 0.81 | 0.45 | 0.58 |
| HYP | 0.79 | 0.22 | 0.34 |

The regularized model achieved higher Precision but substantially lower Recall and F1-score.

Applying 30% Dropout after both hidden layers was too restrictive for this small network.

Regularization reduced overfitting but also reduced the model’s ability to identify positive disease cases.

---

## Model Comparison

| Model | Best Validation Loss | Best Epoch | Final Validation Loss | Macro Precision | Macro Recall | Macro F1 |
|---|---:|---:|---:|---:|---:|---:|
| Basic Model | 0.3946 | 29 | 0.4021 | 0.6905 | 0.3947 | 0.5009 |
| BatchNorm + Dropout | 0.3947 | 39 | 0.3954 | 0.7437 | 0.2415 | 0.3511 |

The regularized network produced a more stable loss curve, but its Recall and F1-score were much lower.

Because identifying true disease cases was the main project priority, the basic model was selected for final test evaluation.

---

## Basic Model Test Results

The selected basic model achieved:

- Test Binary Cross-Entropy Loss: 0.4030
- Test Binary Accuracy: 0.8289
- Macro Precision: 0.6717
- Macro Recall: 0.3751
- Macro F1-score: 0.4803

Disease-specific test results were:

| Disease | Precision | Recall | F1-score |
|---|---:|---:|---:|
| MI | 0.67 | 0.35 | 0.46 |
| STTC | 0.57 | 0.29 | 0.38 |
| CD | 0.75 | 0.49 | 0.59 |
| HYP | 0.70 | 0.37 | 0.49 |

The validation and test results were similar, indicating consistent generalization.

However, Recall remained too low for the medical priority of detecting disease cases.

---

## Fair Baseline Comparison

The provisional Day 1 baseline had originally been trained when only 1,990 ECG recordings were available and predicted five labels, including NORM.

A direct comparison with the current four-label neural network would not have been valid.

The Day 1 One-vs-Rest Logistic Regression method was therefore retrained using:

- The complete dataset
- The same 72 features
- The same four disease targets
- The same standardized inputs
- The same official training and test folds

This created a fair comparison between the baseline and the neural network.

---

## Final Baseline Comparison

| Model | Macro Precision | Macro Recall | Macro F1 |
|---|---:|---:|---:|
| Logistic Regression Baseline | 0.4086 | 0.6642 | 0.5037 |
| Basic Neural Network | 0.6717 | 0.3751 | 0.4803 |

The neural network produced much higher Precision.

However, Logistic Regression achieved substantially higher Recall and a slightly higher Macro F1-score.

Because Recall was the main project priority, the current neural network did not yet outperform the baseline.

This was not treated as a failed experiment. It demonstrated that model complexity alone did not guarantee better performance and identified the exact limitation that needed to be addressed during tuning.

---

## Main Findings

- Keras successfully implemented the complete neural-network workflow.
- The basic network learned useful relationships from the ECG features.
- The basic model showed mild overfitting after epoch 29.
- Batch Normalization and Dropout reduced the overfitting gap.
- Applying 30% Dropout after both hidden layers over-regularized the small network.
- Binary Accuracy was not sufficient for evaluating the imbalanced multi-label task.
- Disease-specific Precision, Recall, and F1-score were required.
- The neural network was more precise than the baseline.
- Logistic Regression detected substantially more true disease cases.
- The neural network had not yet beaten the baseline according to Recall or Macro F1-score.

---

## Day 4 Requirements

- Built a Keras Sequential network: Completed
- Used Dense hidden layers: Completed
- Used the correct four-neuron Sigmoid output: Completed
- Used Binary Cross-Entropy: Completed
- Compiled the model with Adam: Completed
- Trained for at least 30 epochs: Completed with 40 epochs
- Used separate validation data: Completed
- Read the Keras training history: Completed
- Plotted training and validation loss: Completed
- Plotted training and validation accuracy: Completed
- Diagnosed overfitting: Completed
- Applied Batch Normalization: Completed
- Applied Dropout: Completed
- Compared basic and regularized networks: Completed
- Evaluated the selected model on the test set: Completed
- Compared the neural network with the baseline: Completed

---

## Conclusion

Day 4 completed all required Keras model-building, training, evaluation, and regularization tasks.

The basic network produced better Recall and F1-score than the regularized network, while the regularized network produced more stable loss curves and higher Precision.

The final comparison showed that the current neural network was more precise but less sensitive than Logistic Regression. Therefore, it did not yet justify replacing the simpler baseline.

Day 5 will focus on systematic tuning using validation data, EarlyStopping, saving the best model weights, and improving disease Recall before preparing the final Sprint 1 comparison.