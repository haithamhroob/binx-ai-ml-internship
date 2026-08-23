# Week 6 — Deep Learning Introduction

## Project: ECG-Based Cardiac Diagnosis Using PTB-XL

Week 6 begins Sprint 1 of the deep learning phase. The project uses clinical 12-lead ECG signals from the PTB-XL dataset to perform multi-label cardiac diagnosis.

The selected diagnostic classes are:

- `NORM`: Normal ECG
- `MI`: Myocardial Infarction
- `STTC`: ST/T Change
- `CD`: Conduction Disturbance
- `HYP`: Hypertrophy

A single ECG may contain more than one diagnosis, so the project is treated as a multi-label classification problem.

## Week 6 Objectives

- Understand neurons, weights, biases, and neural network layers.
- Study activation functions and forward propagation.
- Understand loss, backpropagation, and gradient descent.
- Build and train a neural network using TensorFlow/Keras.
- Apply dropout, batch normalization, and callbacks.
- Tune and compare the neural network with a classical baseline.
- Complete the Sprint Review and Retrospective.

## Dataset

The project uses the open-access PTB-XL dataset.

The complete dataset contains:

- 21,799 clinical ECG recordings.
- 18,869 patients.
- 12 ECG leads.
- 10 seconds per recording.
- 100 Hz and 500 Hz signal versions.
- Standardized SCP-ECG diagnostic annotations.

This project currently uses the 100 Hz recordings from `records100`.

Dataset source:

[PTB-XL on PhysioNet](https://physionet.org/content/ptb-xl/1.0.3/)

## Local Dataset Structure

```text
cardiac-patient-monitoring/
└── data/
    └── raw/
        └── ptb-xl/
            ├── ptbxl_database.csv
            ├── scp_statements.csv
            └── records100/
```

The raw ECG waveform files are not uploaded to GitHub because of their number and size.

## Day 1 — Sprint Planning, Baseline, and Neural Network Architecture

Notebook:

```text
day1.ipynb
```

### Work Completed

- Inspected the PTB-XL metadata and waveform structure.
- Verified the existence of both `.dat` and `.hea` files.
- Matched the locally available ECG signals with their metadata.
- Loaded and visualized a complete 12-lead ECG.
- Converted SCP-ECG codes into five diagnostic superclasses.
- Prepared multi-label binary targets.
- Examined the class distribution.
- Extracted statistical features from all 12 ECG leads.
- Built a Logistic Regression baseline using One-vs-Rest classification.
- Used the official patient-safe PTB-XL folds.
- Explained neurons, weights, biases, activations, and neural network layers.
- Prepared the Sprint 1 goal, backlog, blockers, and acceptance criteria.

### Available Data

The metadata contains 21,799 ECG records, but 2,012 complete waveform records were available locally during the initial experiment.

Twenty-two recordings without any of the five selected diagnostic targets were removed.

The provisional modeling dataset contained:

```text
1,990 ECG recordings
```

The official folds produced:

```text
Training:   1,505 ECGs
Validation:   232 ECGs
Test:         253 ECGs
```

The test fold was kept untouched.

## Baseline Model

Six statistical features were extracted from each of the 12 leads:

- Mean
- Standard deviation
- Minimum
- Maximum
- Range
- Root Mean Square

This produced:

```text
12 leads × 6 statistics = 72 features
```

The baseline pipeline contained:

- StandardScaler
- OneVsRestClassifier
- Logistic Regression
- Balanced class weights

## Provisional Baseline Results

The model was evaluated on the validation fold.

| Metric | Score |
|---|---:|
| Macro Precision | 0.50 |
| Macro Recall | 0.72 |
| Macro F1-score | 0.59 |
| Micro F1-score | 0.60 |
| Weighted F1-score | 0.61 |

### Per-Class Results

| Class | Precision | Recall | F1-score |
|---|---:|---:|---:|
| NORM | 0.68 | 0.81 | 0.74 |
| MI | 0.48 | 0.76 | 0.59 |
| STTC | 0.39 | 0.54 | 0.45 |
| CD | 0.45 | 0.77 | 0.57 |
| HYP | 0.49 | 0.73 | 0.59 |

The provisional baseline to beat is:

```text
Macro F1-score = 0.59
```

## Main Day 1 Insight

The statistical baseline summarizes the amplitude and variability of each ECG lead, but it does not preserve the temporal morphology of the signal.

A neural network may improve performance by learning more complex relationships from the ECG data.

A neuron performs:

```text
Weighted Sum + Bias → Activation
```

Hidden layers combine multiple learned patterns, while non-linear activation functions prevent the network from behaving like one linear model.

## Current Limitation

The baseline was trained using only the ECG signals currently available locally.

The result is provisional and must be repeated after downloading the complete `records100` dataset.

## Week Structure

```text
week6/
└── day1/
    └── files/
        ├── day1.ipynb
        └── README.md

The remaining notebooks will be added as the week progresses:

- Day 2: Activations, forward propagation, and loss.
- Day 3: Backpropagation, gradient descent, and optimizers.
- Day 4: Building and training a Keras neural network.
- Day 5: Tuning, evaluation, Sprint Review, and Retrospective.

## Requirements

```bash
pip install numpy pandas matplotlib scikit-learn wfdb jupyter
```

## Run the Notebook

From the repository root:

```bash
jupyter notebook week6/day1/files/day1.ipynb
```