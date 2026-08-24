# Week 6 — Day 2

## Activation Functions, Forward Propagation, and Loss

This day continues the ECG-based cardiac diagnosis project using the PTB-XL dataset.

The project is treated as a multi-label classification task because one ECG may contain more than one disease. The current target order is:

```text
[MI, STTC, CD, HYP]
```

## The Problem

A neural network must do more than combine inputs linearly. It must learn complex relationships, convert its internal values into meaningful disease probabilities, and measure how different those probabilities are from the true labels.

The main questions addressed during Day 2 were:

- Why are activation functions necessary?
- Which activation should be used in hidden and output layers?
- How does information move forward through a neural network?
- Which loss function is appropriate for multi-label classification?

## The Solution

Three activation functions were implemented and compared:

- ReLU
- Sigmoid
- Tanh

ReLU was selected for the hidden layers because it introduces non-linearity while preserving positive activations.

Four independent sigmoid units were selected for the output layer. Softmax was rejected because it forces all class probabilities to compete and sum to one, while an ECG may contain several diseases simultaneously.

Binary Cross-Entropy was selected as the loss function because every disease output is an independent binary decision.

## Forward Propagation

A small NumPy network was created with:

- One input sample
- Two input features
- Two hidden neurons
- Four output neurons

The forward pass followed these equations:

```text
Z1 = XW1 + b1
A1 = ReLU(Z1)
Z2 = A1W2 + b2
Y_hat = Sigmoid(Z2)
```

The example produced:

```text
Z1 = [2.0, -0.5]
A1 = [2.0, 0.0]
Z2 = [1.0, 1.0, -1.0, -0.5]
Predicted probabilities = [0.731, 0.731, 0.269, 0.378]
```

These probabilities were produced using manually selected weights and are only intended to demonstrate the calculation.

## Loss Experiment

Binary Cross-Entropy was implemented manually with NumPy. Three types of predictions were compared against the same true label vector:

- Good prediction
- Uncertain prediction
- Confidently incorrect prediction

The experiment showed that:

- Good predictions produce a small loss.
- Uncertain predictions produce an intermediate loss.
- Confidently incorrect predictions receive the largest penalty.

## Final Project Decisions

| Component | Decision |
|---|---|
| Hidden activation | ReLU |
| Output neurons | 4 |
| Output activation | Independent sigmoid |
| Loss function | Binary Cross-Entropy |
| Target order | MI, STTC, CD, HYP |
| Evaluation priority | Recall, with Macro F1 and per-class metrics |

The `0.5` threshold used during this notebook is provisional. The final thresholds should be tuned using validation data, with special attention to Recall.

## What Was Learned

- Why non-linear activations are necessary.
- How ReLU, sigmoid, and tanh transform values.
- How matrix dimensions represent network connections.
- How forward propagation produces multi-label predictions.
- Why sigmoid is appropriate for independent disease probabilities.
- Why Binary Cross-Entropy is the appropriate loss function.
- Why confident incorrect predictions receive a large penalty.

## Files

```text
day2/
├── day2.ipynb
└── README.md
```

## Next Step

Day 3 will cover gradients, backpropagation, learning rates, and optimization using Adam and SGD.
