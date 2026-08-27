# Week 6 — Deep Learning Sprint 1

This week introduced neural networks and applied them to multi-label cardiac diagnosis using the PTB-XL ECG dataset.

## Daily Progress

### Day 1 — Architecture and Baseline

* Prepared PTB-XL for modeling.
* Extracted 72 statistical features from 12 ECG leads.
* Created four targets: MI, STTC, CD, and HYP.
* Established a Logistic Regression baseline.

### Day 2 — Activations and Forward Propagation

* Studied ReLU, Sigmoid, Tanh, and Softmax.
* Explained forward propagation and loss.
* Selected Sigmoid and Binary Cross-Entropy for multi-label classification.

### Day 3 — Backpropagation and Optimizers

* Explained the complete training loop.
* Studied gradient descent, Backpropagation, epochs, and batches.
* Compared different learning rates.

### Day 4 — Keras Network

* Built and trained a Keras Sequential network.
* Added Batch Normalization and Dropout.
* Diagnosed loss curves and overfitting.
* Compared the network with Logistic Regression.

### Day 5 — Tuning and Sprint Review

* Added EarlyStopping and ModelCheckpoint.
* Tuned learning rate, architecture, Dropout, and batch size.
* Selected the threshold using validation Macro F2.
* Completed final evaluation, Sprint Review, and Retrospective.

## Final Model

* Architecture: `72 → 64 → 32 → 4`
* Learning rate: `0.002`
* Batch size: `32`
* Dropout: `0.0`
* Threshold: `0.15`

## Final Result

The tuned neural network achieved:

* Macro Recall: `0.8035`
* Macro F1: `0.5166`
* Macro F2: `0.6561`

It outperformed Logistic Regression in the project’s primary disease-detection metrics.

## Next Step

The next sprint will investigate raw ECG waveform modeling, including 1D CNNs, instead of relying only on statistical features.
