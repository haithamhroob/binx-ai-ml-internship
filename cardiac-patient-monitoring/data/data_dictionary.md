# Data Dictionary

The project uses the 14-column processed Cleveland Heart Disease dataset. The
first 13 columns are model inputs. The original `num` target is converted to a
binary project target named `heart_disease`.

| Feature | Type | Description / coding |
|---|---|---|
| `age` | Numeric | Age in years. |
| `sex` | Binary | `1` = male, `0` = female. |
| `cp` | Categorical | Chest-pain type: `1` typical angina, `2` atypical angina, `3` non-anginal pain, `4` asymptomatic. |
| `trestbps` | Numeric | Resting blood pressure in mm Hg on admission. |
| `chol` | Numeric | Serum cholesterol in mg/dl. |
| `fbs` | Binary | Fasting blood sugar > 120 mg/dl: `1` true, `0` false. |
| `restecg` | Categorical | Resting ECG: `0` normal, `1` ST-T abnormality, `2` probable/definite LV hypertrophy. |
| `thalach` | Numeric | Maximum heart rate achieved. |
| `exang` | Binary | Exercise-induced angina: `1` yes, `0` no. |
| `oldpeak` | Numeric | ST depression induced by exercise relative to rest. |
| `slope` | Categorical | Peak exercise ST slope: `1` upsloping, `2` flat, `3` downsloping. |
| `ca` | Discrete numeric | Number of major vessels (0-3) colored by fluoroscopy. Missing values appear as `?`. |
| `thal` | Categorical | `3` normal, `6` fixed defect, `7` reversible defect. Missing values appear as `?`. |
| `num` | Original target | `0` indicates <50% diameter narrowing; values `1-4` indicate heart-disease presence/severity in the processed dataset. |
| `heart_disease` | Derived target | Project target: `0` when `num = 0`; `1` when `num > 0`. |

Missing `?` markers are converted to `NaN`. The final Pipeline imputes numeric
features with the median and categorical features with the most frequent value.

Source: UCI Heart Disease dataset documentation (`heart-disease.names`).
