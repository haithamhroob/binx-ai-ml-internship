# Week 6 — Day 3: Backpropagation, Gradient Descent, and Optimizers

## Project Context

This day continued the ECG-based multi-label cardiac diagnosis project using the PTB-XL dataset.

During Day 2, forward propagation converted the ECG features into four independent disease probabilities, while Binary Cross-Entropy measured the prediction error. Day 3 completed the training process by explaining how the error moves backward through the network and how the trainable parameters are updated.

The four target diagnostic classes were:

- `MI`: Myocardial Infarction
- `STTC`: ST/T Change
- `CD`: Conduction Disturbance
- `HYP`: Hypertrophy

## The Problem

Forward propagation and the loss function can produce predictions and measure their error, but they do not complete the learning process.

The network still needs to determine:

- Which weights contributed to the error?
- How strongly did each weight affect the loss?
- Should each weight increase or decrease?
- How large should each update be?

## The Training Loop

Neural-network training repeats four connected steps:

```text
Forward Pass → Loss → Backpropagation → Weight Update
```

1. **Forward Pass:** The ECG features move through the network to produce four disease probabilities.
2. **Loss:** Binary Cross-Entropy measures the difference between the predicted probabilities and the true labels.
3. **Backpropagation:** The chain rule calculates how each trainable weight and bias contributed to the loss.
4. **Weight Update:** The optimizer changes the parameters in the direction that should reduce future loss.

## Backpropagation and the Chain Rule

An early weight affects the final loss through multiple intermediate operations. Therefore, Backpropagation uses the chain rule to connect these effects:

$$
\frac{\partial L}{\partial W_3}
=
\frac{\partial L}{\partial \hat{Y}}
\cdot
\frac{\partial \hat{Y}}{\partial Z_3}
\cdot
\frac{\partial Z_3}{\partial W_3}
$$

The result is the gradient:

$$
Gradient=\frac{\partial L}{\partial W}
$$

The gradient measures how changing a parameter would affect the loss. In simple terms, Backpropagation assigns a share of the prediction error to every trainable parameter.

## Gradient Descent and Learning Rate

Gradient Descent updates a weight using:

$$
W_{new}
=
W_{old}
-
\eta\frac{\partial L}{\partial W}
$$

The gradient determines the update direction, while the learning rate $\eta$ controls the step size.

- A very low learning rate produces slow training.
- A suitable learning rate produces stable and efficient improvement.
- A very high learning rate may overshoot useful values, become unstable, or stagnate at a poor solution.

## Epochs, Batches, and Optimizers

- **Batch:** A subset of training records processed before one weight update.
- **Epoch:** One complete pass through the entire training dataset.
- **Optimizer:** The algorithm that uses the gradients to update the parameters.
- **SGD:** Applies the basic Gradient Descent update.
- **Adam:** Uses previous gradient information and adapts the effective update for each parameter.

The experiment used:

```python
batch_size = 32
epochs = 40
optimizer = "Adam"
loss = "Binary Cross-Entropy"
```

With 17,084 training records and a batch size of 32, the model performed approximately 534 updates per epoch and 21,360 updates during each 40-epoch experiment.

## Data Preparation

All 21,799 PTB-XL ECG recordings were available locally. After selecting recordings belonging to the five relevant diagnostic superclasses, 21,388 recordings remained.

Each ECG was represented by 72 statistical features:

```text
12 ECG leads × 6 statistical features = 72 features
```

The official PTB-XL folds produced:

| Dataset | Samples | Features | Outputs |
|---|---:|---:|---:|
| Training | 17,084 | 72 | 4 |
| Validation | 2,146 | 72 | 4 |
| Test | 2,158 | 72 | 4 |

No missing or infinite input values were found.

## Neural-Network Architecture

The experiment used the following network:

```text
72 ECG Features
        ↓
Dense(32) + ReLU
        ↓
Dense(16) + ReLU
        ↓
Dense(4) + Sigmoid
```

The four sigmoid outputs produced independent probabilities for `MI`, `STTC`, `CD`, and `HYP`.

## Learning-Rate Experiment

The same architecture, data, random seed, batch size, epochs, loss function, and Adam optimizer were used in all three experiments. Only the learning rate changed.

| Experiment | Initial Train Loss | Final Train Loss | Best Validation Loss | Best Epoch | Final Validation Loss |
|---|---:|---:|---:|---:|---:|
| Too Low: `1e-6` | 0.7724 | 0.6699 | 0.6628 | 40 | 0.6628 |
| Suitable: `1e-3` | 0.4656 | 0.3539 | **0.3946** | 29 | 0.4021 |
| Too High: `1.0` | 0.9453 | 0.5230 | 0.5120 | 1 | 0.5125 |

## Results Interpretation

### Learning Rate `1e-6`

The training and validation losses decreased smoothly, proving that the model was learning. However, the updates were too small, and the model remained slow and inefficient even after 40 epochs.

### Learning Rate `1e-3`

This value produced the best result. The model learned rapidly at the beginning and then improved more gradually. The best validation loss was `0.3946` at epoch 29.

After epoch 29, training loss continued decreasing while validation loss stopped improving consistently. This indicates the beginning of overfitting and supports saving the model from the best validation epoch instead of automatically using the final epoch.

### Learning Rate `1.0`

The loss dropped rapidly at the beginning but then stagnated near a weaker solution. The best validation result occurred at epoch 1, and later epochs did not provide meaningful improvement.

The high learning rate did not produce `NaN`, but its updates were still too aggressive to make useful fine adjustments.

## Final Decisions

Based on the experiment, the selected initial training configuration is:

```python
optimizer = Adam(learning_rate=0.001)
batch_size = 32
hidden_activation = "relu"
output_activation = "sigmoid"
loss = "binary_crossentropy"
```

The best validation checkpoint should be retained during future training.

## What Was Learned

- A neural network learns through a repeated four-step training loop.
- Backpropagation calculates gradients; it does not directly update the weights.
- The optimizer uses the gradients to perform the actual parameter updates.
- The chain rule connects early network parameters to the final loss.
- The learning rate strongly affects training speed, stability, and solution quality.
- A decreasing training loss alone is not enough; validation loss must also be monitored.
- The final epoch is not always the best epoch.
- Adam with a learning rate of `0.001` was the strongest tested configuration.

## Day 3 Requirements Status

- [x] Describe the four-step neural-network training loop.
- [x] Explain Gradient Descent and the loss surface concept.
- [x] Explain the learning rate and its effect.
- [x] Explain Backpropagation conceptually using the chain rule.
- [x] Explain optimizers, epochs, batches, SGD, and Adam.
- [x] Write the four-step training loop in the project notebook.
- [x] Train the same small network at three learning rates.
- [x] Plot and interpret the training and validation loss curves.
- [x] Explain Backpropagation in original words.
- [ ] Open the mid-sprint Pull Request and address mentor feedback.

All theoretical and notebook-based technical requirements for Day 3 were completed. The only remaining workflow requirement is opening the Pull Request and responding to the mentor's review after it is received.
