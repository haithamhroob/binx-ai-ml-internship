# Week 9 — Day 1

## Sprint 4 Planning, Reproducibility & Serialization

This notebook starts the final BinX Tech project: an educational platform that classifies educational posts, analyzes teaching feedback, and recommends posts and people.

Day 1 converts the research proposal into a clear Sprint 4 plan and verifies the complete serialization path:

```text
train → preprocess → predict → save → load → reproduce prediction
```

## Project Scope

The MVP contains three separate AI systems:

1. **Post Topic Classification**
   Classifies English post text and optional images into one or more educational topics.

2. **Teaching-Feedback Analysis**
   Detects teaching-related aspects and sentiment in written feedback. The text signal remains separate from the user's 1–5 star rating.

3. **Post and People Recommendation**
   Ranks eligible posts or public profiles using user interests, content similarity, and transparent reason codes.

The current scope contains no payment, paid content, discounts, or financial rewards. Recommendation does not grant access to restricted content; authorization remains a backend responsibility.

## MVP Topic Taxonomy

Post classification is **multi-label**, because one post may belong to several topics.

* Programming/Web
* AI/Data
* Electronics/Embedded
* Robotics
* Cybersecurity
* Design
* Mathematics
* Natural Sciences

Health, Business, Languages, Humanities, Education, and General Engineering remain possible future additions. They are not added until the team confirms the product scope and suitable data.

## Day 1 Work

The notebook includes:

* Sprint 4 goal and five-day backlog.
* Boundaries between the three AI systems.
* Multi-label taxonomy configuration.
* Candidate dataset and baseline-model mapping.
* Proposed input and output contracts.
* Fixed random seed and environment-version capture.
* A small topic-classification serialization smoke test.
* Model and preprocessing bundling with `joblib`.
* Reloading the saved bundle and reproducing a known prediction.
* An honest status checklist for completed and pending work.

## Candidate Data and Baselines

| System                     | Candidate data                                                         | First baseline                                       |
| -------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------- |
| Text topic classification  | EngineeringConcepts and audited Wikibooks labels                       | TF-IDF + One-vs-Rest Logistic Regression             |
| Image topic classification | MMMU/ScienceQA exploration and a project-style test set                | OCR → text classifier; CLIP evaluated separately     |
| Teaching feedback          | EduRABSA and an optional independent feedback dataset                  | Teaching-aspect sentiment classifier                 |
| Recommendations            | Explicit interests and eligible content; MIND-small for rehearsal only | TF-IDF vs sentence embeddings with cosine similarity |

These sources are **candidates, not adopted training datasets**. Licence, label mapping, class balance, duplicates, and split leakage must be audited before training or reporting results.

## Serialization Smoke Test

The notebook trains a tiny illustrative multi-label topic pipeline to verify the engineering workflow. It saves the following objects together:

* Fitted TF-IDF vectorizer.
* One-vs-Rest classifier.
* Ordered label encoder.
* Decision threshold.
* Topic taxonomy.
* Random seed.
* Model version and status.

The bundle is loaded again, and an assertion confirms that the prediction before saving and after loading is identical.

> The 16-row corpus is a teaching-only smoke test. It is too small for evaluation, deployment, or accuracy/F1 claims.

## Run the Notebook

Create and activate a Python environment, then install the required packages:

```bash
python -m pip install jupyter pandas numpy scikit-learn joblib
jupyter notebook week9_day1.ipynb
```

Run all cells from top to bottom. The final checks should report that the pipeline was fitted and the serialization round trip passed.

## Current Status

| Item                                 | Status                            |
| ------------------------------------ | --------------------------------- |
| Sprint goal and system boundaries    | Complete                          |
| Eight-topic taxonomy                 | Draft; team confirmation required |
| Dataset/model mapping                | Candidate plan; audit required    |
| Seed and environment capture         | Complete                          |
| Save/load smoke test                 | Passed                            |
| Real project training and evaluation | Not started                       |

## Day 2 Handoff

The next step is to audit and adopt permitted real data, replace the smoke-test pipeline with an evaluated baseline, and expose versioned project outputs through FastAPI with validated request and response schemas.

## Tools Used

Python • Jupyter • Scikit-learn • Joblib • Pandas • NumPy
