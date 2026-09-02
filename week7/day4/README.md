# Week 7 — Day 4: Attention and Transformers

## Overview

Day 4 studies how Transformers process sequential data using the Attention mechanism instead of the step-by-step recurrent memory used by RNN and LSTM models.

The practical task is binary sentiment classification using the IMDb Movie Reviews dataset:

* `0` — Negative review
* `1` — Positive review

Two approaches were evaluated on the same test samples:

1. A text-based LSTM trained locally on IMDb reviews.
2. A pre-trained DistilBERT Transformer from Hugging Face.

---

## Learning Objectives

The main objectives of this day were to:

* Explain the limitations of step-by-step RNN processing.
* Understand Attention and Self-Attention.
* Understand Query, Key, and Value representations.
* Explain why Transformers support parallel processing.
* Understand the purpose of Positional Encoding.
* Use a pre-trained Transformer from Hugging Face.
* Build a text-based LSTM baseline.
* Compare LSTM and DistilBERT on the same text-classification task.
* Select a core architecture using Accuracy, Precision, Recall, and F1-score.

---

## Dataset

The experiment used the IMDb Movie Reviews dataset.

The complete labeled dataset contains:

* `25,000` training reviews.
* `25,000` test reviews.
* Two balanced sentiment classes.

The original training split contains:

| Sentiment | Samples | Percentage |
| --------- | ------: | ---------: |
| Negative  |  12,500 |        50% |
| Positive  |  12,500 |        50% |

Because the environment did not have a compatible GPU, a balanced experimental subset was selected:

| Split      | Samples | Negative | Positive |
| ---------- | ------: | -------: | -------: |
| Training   |   4,000 |    1,997 |    2,003 |
| Validation |   1,000 |      499 |      501 |
| Test       |   1,000 |      498 |      502 |

Duplicate reviews were removed before sampling, and stratified splitting was used to preserve class balance.

---

## Text Preparation

The text-preparation process included:

* Removing HTML line-break tags such as `<br />`.
* Collapsing repeated spaces.
* Converting text to lowercase.
* Creating the vocabulary using training data only.
* Mapping unseen words to an `<OOV>` token.
* Padding and truncating every review to `128` tokens.
* Limiting the LSTM vocabulary to the most frequent `20,000` tokens.

Fitting the tokenizer only on the training split prevents information leakage from validation or test data.

---

## Limitation of RNNs and LSTMs

An RNN updates its hidden state sequentially:

$$
h_t=\tanh(W_xx_t+W_hh_{t-1}+b)
$$

The calculation at time step $t$ depends on the result from time step $t-1$.

This creates several limitations:

* Sequence positions cannot all be processed simultaneously.
* Information from distant words must pass through many recurrent steps.
* Long sequences may cause useful information to be weakened or compressed.
* LSTM gates improve memory but do not remove sequential processing.

---

## Attention Mechanism

Attention allows every token to directly examine the relevance of every other token.

Each input representation is projected into three learned representations:

$$
Q=XW_Q
$$

$$
K=XW_K
$$

$$
V=XW_V
$$

Where:

* **Query:** what the current token is looking for.
* **Key:** what each token provides for comparison.
* **Value:** the information transferred through attention.

Scaled dot-product attention is calculated using:

$$
\operatorname{Attention}(Q,K,V)
=
\operatorname{softmax}
\left(
\frac{QK^T}{\sqrt{d_k}}
\right)V
$$

The $QK^T$ operation measures relevance between sequence positions. Softmax converts these scores into weights, and the weighted Values produce context-aware representations.

---

## Why Transformers Are Parallelizable

RNN and LSTM models process sequence positions one after another. Self-Attention instead uses matrix operations across all positions.

| Property              | RNN/LSTM               | Self-Attention           |
| --------------------- | ---------------------- | ------------------------ |
| Processing            | Step by step           | All positions together   |
| Parallelism           | Limited                | Strong                   |
| Distant relationships | Many recurrent steps   | Direct access            |
| Sequence order        | Inherent               | Added explicitly         |
| Memory                | Hidden and cell states | Attention over positions |

This parallel structure makes Transformer training more efficient on modern GPUs.

---

## Positional Encoding

Self-Attention does not inherently understand token order. Position information must therefore be added to token embeddings.

The original Transformer used sinusoidal positional encoding:

$$
PE(pos,2i)
=
\sin
\left(
\frac{pos}{10000^{2i/d_{model}}}
\right)
$$

$$
PE(pos,2i+1)
=
\cos
\left(
\frac{pos}{10000^{2i/d_{model}}}
\right)
$$

Different dimensions use different frequencies, producing a structured representation for every sequence position.

---

## Text LSTM Baseline

The LSTM architecture contained:

* An Embedding layer with `128` dimensions.
* One LSTM layer with `64` units.
* Dropout regularization.
* A Dense layer with ReLU activation.
* One Sigmoid output neuron.

The model contained:

```text
2,611,521 trainable parameters
```

Binary Cross-Entropy was used as the loss function:

$$
\mathcal{L}
=
-\frac{1}{N}
\sum_{i=1}^{N}
\left[
y_i\log(p_i)
+
(1-y_i)\log(1-p_i)
\right]
$$

Early stopping monitored validation loss and restored the best model weights.

---

## LSTM Training Behavior

The best validation result occurred at epoch 3:

* Validation Accuracy: `0.8020`
* Validation Loss: `0.6372`

After epoch 3:

* Training Accuracy continued increasing.
* Training Loss continued decreasing.
* Validation Loss started increasing.

This divergence indicated overfitting. Early stopping restored the epoch-3 weights instead of keeping the final epoch.

The total LSTM training time was approximately:

```text
0.694 minutes
```

---

## LSTM Test Results

| Metric              |         Score |
| ------------------- | ------------: |
| Accuracy            |        0.7880 |
| Precision           |        0.7726 |
| Recall              |        0.8187 |
| F1-score            |        0.7950 |
| Test Inference Time | 0.684 seconds |

The LSTM confusion matrix was:

```text
[[377, 121],
 [ 91, 411]]
```

This means:

* `377` negative reviews were classified correctly.
* `411` positive reviews were classified correctly.
* `121` negative reviews were incorrectly classified as positive.
* `91` positive reviews were incorrectly classified as negative.

The LSTM achieved relatively strong positive Recall, meaning it detected most positive reviews.

---

## Pre-trained DistilBERT

The Transformer experiment used:

```text
distilbert-base-uncased-finetuned-sst-2-english
```

This model was:

* Pre-trained on large English text collections.
* Fine-tuned previously on the SST-2 sentiment dataset.
* Loaded using the Hugging Face `pipeline`.
* Executed using PyTorch on the CPU.

The model was not trained locally from scratch. Instead, previously learned language and sentiment knowledge was transferred to the IMDb task.

---

## DistilBERT Test Results

| Metric              |           Score |
| ------------------- | --------------: |
| Accuracy            |          0.8200 |
| Precision           |          0.8411 |
| Recall              |          0.7908 |
| F1-score            |          0.8152 |
| Test Inference Time | 72.7132 seconds |

The DistilBERT confusion matrix was:

```text
[[423, 75],
 [105, 397]]
```

This means:

* `423` negative reviews were classified correctly.
* `397` positive reviews were classified correctly.
* `75` negative reviews were incorrectly classified as positive.
* `105` positive reviews were incorrectly classified as negative.

DistilBERT produced fewer false-positive positive predictions than the LSTM and achieved substantially higher positive Precision.

---

## Final Model Comparison

| Model                  |   Accuracy |  Precision |     Recall |   F1-score |
| ---------------------- | ---------: | ---------: | ---------: | ---------: |
| Text LSTM              |     0.7880 |     0.7726 | **0.8187** |     0.7950 |
| Pre-trained DistilBERT | **0.8200** | **0.8411** |     0.7908 | **0.8152** |

DistilBERT improved:

* Accuracy from `0.7880` to `0.8200`.
* Precision from `0.7726` to `0.8411`.
* F1-score from `0.7950` to `0.8152`.

The LSTM achieved higher positive Recall:

```text
LSTM Recall:        0.8187
DistilBERT Recall:  0.7908
```

Therefore:

* DistilBERT is preferable for stronger balanced classification and more reliable positive predictions.
* LSTM may be considered when detecting as many positive reviews as possible is the highest priority.
* LSTM is much faster during CPU inference.

For this general sentiment-classification task, F1-score was selected as the primary metric. Therefore, the selected model was:

```text
Pre-trained DistilBERT
```

---

## Attention Versus Recurrent Memory

An RNN or LSTM carries information through a hidden state that moves sequentially from one token to the next. A distant relationship must therefore survive several recurrent updates before influencing the final prediction. Self-Attention allows each token to compare its Query directly with the Keys of every other token and construct a weighted combination of their Values. This reduces the path between distant words and enables parallel sequence processing, while Positional Encoding provides the order information that attention does not inherently contain.

---

## Experiment Limitations

The comparison has several important limitations:

* The LSTM was trained locally on only `4,000` IMDb reviews.
* DistilBERT had already learned from large external text collections.
* DistilBERT was previously fine-tuned on SST-2.
* The comparison represents practical transfer learning, not equal training from scratch.
* Reviews were truncated to `128` tokens because execution was CPU-only.
* Fine-tuning DistilBERT directly on IMDb may improve its performance.
* The reported time values are not directly equivalent:

  * LSTM time includes local training.
  * DistilBERT reports inference without local training.

---

## Key Conclusions

* LSTM improves recurrent memory but remains sequential.
* Self-Attention provides direct access between all sequence positions.
* Query, Key, and Value determine how information moves through attention.
* Positional information is necessary because attention does not inherently preserve order.
* Pre-trained Transformers can transfer previously learned language knowledge to new tasks.
* Early stopping protected the LSTM from retaining overfitted weights.
* DistilBERT achieved the strongest overall test result.
* LSTM remained faster and achieved higher positive Recall.
* Model selection must consider both predictive metrics and computational cost.

---

## Files

```text
week7_day4_attention_transformers.ipynb
README.md
```

The notebook contains the theoretical explanation, mathematical equations, data preparation, LSTM baseline, Hugging Face Transformer inference, model evaluation, visual comparisons, and final architecture decision.
