# Week 7 — Day 3

## RNNs and LSTMs for Sequential ECG Data

This notebook studies sequential deep-learning architectures by classifying ECG heartbeats from the MIT-BIH Arrhythmia Dataset.

Unlike images, where spatial relationships are important, an ECG signal is a time sequence. Each measurement occurs at a particular time, and its meaning depends on the measurements that came before and after it.

The experiment compares three approaches:

1. A non-recurrent Dense baseline.
2. A Simple Recurrent Neural Network.
3. A Long Short-Term Memory network.

The objective is to determine whether recurrent memory and temporal order improve heartbeat classification.

---

## Learning Objectives

By completing this notebook, we learned how to:

* Explain why order matters in sequential ECG data.
* Understand how an RNN processes a sequence one time step at a time.
* Explain how the hidden state carries information across a sequence.
* Understand the vanishing-gradient problem.
* Explain how LSTM gates control memory.
* Prepare ECG signals for recurrent neural networks.
* Build and train Dense, Simple RNN, and LSTM models.
* Address severe class imbalance using class weights.
* Compare models using medical classification metrics.
* Test whether changing the ECG time order affects model performance.
* Select a model using validation data before evaluating the test set.

---

## Dataset

The experiment uses the ECG Heartbeat Categorization Dataset:

https://www.kaggle.com/datasets/shayanfazeli/heartbeat

The complete Kaggle dataset contains two ECG collections:

* MIT-BIH Arrhythmia Dataset.
* PTB Diagnostic ECG Database.

For this experiment, we used the MIT-BIH files:

* `mitbih_train.csv`
* `mitbih_test.csv`

Each row represents one segmented heartbeat:

* The first `187` columns contain ordered ECG measurements.
* The final column contains the heartbeat class.
* The sampling frequency is `125 Hz`.
* Signal values are normalized between `0` and `1`.
* Sequences are padded with zeros when necessary.

Each input heartbeat therefore has the following structure:

$$
(187\ \text{time steps},\ 1\ \text{feature})
$$

---

## Heartbeat Classes

| Label | Symbol | Class                              |
| ----: | :----: | ---------------------------------- |
|     0 |    N   | Normal heartbeat                   |
|     1 |    S   | Supraventricular ectopic heartbeat |
|     2 |    V   | Ventricular ectopic heartbeat      |
|     3 |    F   | Fusion heartbeat                   |
|     4 |    Q   | Unknown or unclassified heartbeat  |

---

## Dataset Shape

| Split                  | Samples |
| ---------------------- | ------: |
| Original Training File |  87,554 |
| Training Subset        |  70,043 |
| Validation Subset      |  17,511 |
| Test Set               |  21,892 |

A stratified split was applied to the original training file:

* `80%` for training.
* `20%` for validation.
* The provided test set remained untouched until final evaluation.

---

## Training Class Distribution

| Class                |  Count | Percentage |
| -------------------- | -----: | ---------: |
| N — Normal           | 72,471 |     82.77% |
| S — Supraventricular |  2,223 |      2.54% |
| V — Ventricular      |  5,788 |      6.61% |
| F — Fusion           |    641 |      0.73% |
| Q — Unclassified     |  6,431 |      7.35% |

The dataset is highly imbalanced. The Normal class represents more than `82%` of the training data, while the Fusion class represents less than `1%`.

For this reason, accuracy alone was not considered sufficient.

---

## Why Order Matters

An ECG heartbeat is an ordered sequence:

$$
x_1 \rightarrow x_2 \rightarrow x_3
\rightarrow \cdots \rightarrow x_{187}
$$

If the measurements are randomly shuffled, the values remain the same, but the original waveform is destroyed.

Important ECG information depends on:

* When a rise begins.
* Where a peak occurs.
* How quickly the signal falls.
* What pattern follows the peak.
* How earlier and later measurements relate to each other.

A sequential model can process these relationships in their original temporal order.

---

## Simple RNN

A Simple RNN processes one ECG measurement at a time.

Its hidden state is updated using:

$$
h_t =
\tanh
\left(
W_xx_t + W_hh_{t-1} + b
\right)
$$

Where:

* $x_t$ is the current ECG measurement.
* $h_{t-1}$ is the previous hidden state.
* $h_t$ is the updated hidden state.
* $W_x$ and $W_h$ are learned weights.
* $b$ is the bias.

The hidden state acts as a memory that carries information from earlier measurements to later time steps.

---

## Vanishing-Gradient Problem

During training, gradients must propagate backward through all recurrent time steps.

Conceptually:

$$
\frac{\partial L}{\partial h_{t-k}}
=
\frac{\partial L}{\partial h_t}
\prod_{j=t-k+1}^{t}
\frac{\partial h_j}{\partial h_{j-1}}
$$

If the repeated gradient terms are smaller than `1`, their product becomes extremely small.

For example:

$$
0.5^{10} \approx 0.00098
$$

When this happens, early time steps receive very small parameter updates. The RNN may therefore struggle to learn relationships between distant parts of the sequence.

---

## LSTM

An LSTM addresses the memory limitations of a Simple RNN using:

* A cell state.
* A forget gate.
* An input gate.
* An output gate.

The cell-state update is:

$$
c_t =
f_t \odot c_{t-1}
+
i_t \odot \tilde{c}_t
$$

The forget gate controls how much previous information is preserved, while the input gate controls how much new information enters the memory.

The hidden state is calculated using:

$$
h_t =
o_t \odot \tanh(c_t)
$$

These gates allow the LSTM to learn what should be retained, updated, forgotten, and passed forward.

A GRU uses a similar gated-memory concept with fewer gates and no separate cell state. The practical experiment focused on LSTM.

---

## Why Embedding Was Not Used

Embedding layers are commonly used with text.

They convert discrete word indices into learned vectors. The ECG inputs in this experiment are already continuous numerical measurements.

Therefore, the ECG values can enter the recurrent layers directly without an Embedding layer.

---

## Class Weights

Balanced class weights were used to reduce the effect of class imbalance.

The weight for class $c$ is:

$$
w_c =
\frac{N}
{K \times n_c}
$$

Where:

* $N$ is the total number of training samples.
* $K$ is the number of classes.
* $n_c$ is the number of samples belonging to class $c$.

The calculated weights were:

| Class                |  Weight |
| -------------------- | ------: |
| N — Normal           |  0.2416 |
| S — Supraventricular |  7.8789 |
| V — Ventricular      |  3.0256 |
| F — Fusion           | 27.3072 |
| Q — Unclassified     |  2.7228 |

The rare Fusion class received the highest weight.

---

## Model Architectures

### Dense Baseline

```text
Input (187)
↓
Dense (64, ReLU)
↓
Dense (32, ReLU)
↓
Dense (5, Softmax)
```

Trainable parameters: `14,277`

### Simple RNN

```text
Input (187, 1)
↓
SimpleRNN (32)
↓
Dense (32, ReLU)
↓
Dense (5, Softmax)
```

Trainable parameters: `2,309`

### LSTM

```text
Input (187, 1)
↓
LSTM (32)
↓
Dense (32, ReLU)
↓
Dense (5, Softmax)
```

Trainable parameters: `5,573`

All three models used:

* Adam optimizer.
* Sparse categorical cross-entropy.
* Maximum of `12` epochs.
* Batch size of `256`.
* Early stopping with patience of `3`.
* Restoration of the best validation-loss weights.

---

## Evaluation Metrics

Because the dataset is imbalanced, the models were evaluated using:

* Accuracy.
* Balanced Accuracy.
* Macro Recall.
* Macro F1.
* Macro F2.
* Per-class precision and recall.
* Confusion matrices.
* Training time.

Macro Recall gives every class equal importance:

$$
\text{Macro Recall}
=
\frac{1}{K}
\sum_{c=1}^{K}
\text{Recall}_c
$$

Macro F2 gives recall more importance than precision:

$$
F_2
=
\frac{
5 \times \text{Precision} \times \text{Recall}
}{
4 \times \text{Precision} + \text{Recall}
}
$$

The final model was selected using validation Macro F2, with Macro Recall as the tie-breaker.

---

## Validation Results

| Model          | Accuracy | Balanced Accuracy | Macro Recall | Macro F1 | Macro F2 | Training Time |
| -------------- | -------: | ----------------: | -----------: | -------: | -------: | ------------: |
| Dense Baseline |   0.7659 |            0.8054 |       0.8054 |   0.5482 |   0.6230 |      0.14 min |
| LSTM           |   0.3543 |            0.5897 |       0.5897 |   0.2564 |   0.3311 |      6.54 min |
| Simple RNN     |   0.3501 |            0.5397 |       0.5397 |   0.2151 |   0.2671 |      1.06 min |

The Dense baseline achieved the strongest validation result and required the shortest training time.

---

## Why Did the Dense Model Win?

The result shows that a more complex sequential architecture does not automatically produce better performance.

The heartbeat signals were already:

* Segmented.
* Normalized.
* Aligned.
* Cropped to a fixed region.
* Padded to the same length.

Because the measurements appeared at consistent positions, the Dense model could learn strong patterns directly from the fixed input locations.

The recurrent models also had to carry information across `187` steps. The Simple RNN was affected by limited long-term memory, while the small LSTM architecture did not learn representations as effectively as the Dense baseline under the current settings.

The large class weights also encouraged the models to predict rare classes more frequently, increasing recall but producing many false-positive predictions.

---

## Temporal-Order Experiment

The trained LSTM was evaluated using:

1. The original ECG order.
2. The same values after randomly permuting the time steps.

| Input               | Accuracy | Balanced Accuracy | Macro Recall | Macro F1 |
| ------------------- | -------: | ----------------: | -----------: | -------: |
| Original ECG Order  |   0.3543 |            0.5897 |       0.5897 |   0.2564 |
| Permuted Time Steps |   0.0596 |            0.1993 |       0.1993 |   0.0387 |

The large performance decrease shows that the LSTM depended on the temporal arrangement of the ECG measurements.

Therefore, temporal order contained useful information, even though the LSTM did not outperform the Dense baseline.

---

## Selected Model

The Dense baseline was selected because it achieved:

* The highest validation Macro F2.
* The highest validation Macro Recall.
* The highest validation accuracy.
* The shortest training time.

The test set was not used during model selection.

---

## Final Test Results

| Metric                 | Result |
| ---------------------- | -----: |
| Test Loss              | 0.6796 |
| Test Accuracy          | 0.7632 |
| Test Balanced Accuracy | 0.7985 |
| Test Macro Recall      | 0.7985 |
| Test Macro F1          | 0.5448 |
| Test Macro F2          | 0.6182 |

The validation and test results were similar, indicating consistent generalization to the provided test data.

---

## Test Performance by Class

| Class                | Precision | Recall |     F1 |
| -------------------- | --------: | -----: | -----: |
| N — Normal           |    0.9763 | 0.7516 | 0.8494 |
| S — Supraventricular |    0.1928 | 0.6888 | 0.3012 |
| V — Ventricular      |    0.5380 | 0.7569 | 0.6290 |
| F — Fusion           |    0.0760 | 0.8827 | 0.1399 |
| Q — Unclassified     |    0.7198 | 0.9123 | 0.8047 |

The model achieved high recall for the rare Fusion class, but its precision was only `0.0760`.

This means that class weighting helped detect most real Fusion heartbeats, but many heartbeats from other classes were incorrectly predicted as Fusion.

This demonstrates the trade-off between recall and precision when large weights are assigned to rare classes.

---

## Main Findings

* ECG measurements must remain in their original temporal order.
* Simple RNNs carry memory through a hidden state but may suffer from vanishing gradients.
* LSTMs use gates to control what information should be retained or forgotten.
* The LSTM was strongly affected when the ECG order was shuffled.
* Temporal order was useful, but recurrent processing did not produce the best classification result.
* The Dense baseline achieved the strongest validation and test performance.
* Accuracy alone was insufficient because the dataset was severely imbalanced.
* Class weighting increased rare-class recall but also produced false-positive predictions.
* A more complex model should not be selected unless the measured results justify its complexity.

---

## Generated Model

The selected model was saved as:

```text
day3_best_ecg_model.keras
```

---

## Final Conclusion

This experiment demonstrated the difference between fixed-vector processing, recurrent hidden-state memory, and gated LSTM memory.

The Simple RNN and LSTM processed the ECG as an ordered sequence, while the Dense baseline processed the heartbeat as a fixed vector.

Although the LSTM depended strongly on temporal order, the Dense baseline achieved the best overall result on this preprocessed dataset.

The final decision was therefore based on validation metrics and class-level performance rather than assuming that the most complex architecture would automatically be the strongest.
