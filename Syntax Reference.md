# BinX AI/ML Internship — Week 1, Week 2 & Week 3 Syntax Reference

> Quick reference only: **syntax + simple English meaning**.  
> Repeated commands are merged so the file stays useful while working.  
> At the end, related syntax is grouped in **organized tables: Related Syntax | Example Code | Expected Result**.

---

## 1. Environment & Imports

| Syntax | Simple English |
|---|---|
| `python3 -m venv .venv` | Create a Python virtual environment. |
| `source .venv/bin/activate` | Activate the virtual environment on Linux/Ubuntu. |
| `pip install -r requirements.txt` | Install packages from requirements.txt. |
| `jupyter notebook` | Start Jupyter Notebook. |
| `import numpy as np` | Import NumPy as `np`. |
| `import pandas as pd` | Import Pandas as `pd`. |
| `import matplotlib.pyplot as plt` | Import Matplotlib plotting tools. |
| `import matplotlib` | Import the Matplotlib package. |
| `import seaborn as sns` | Import Seaborn as `sns`. |
| `import notebook` | Import the Jupyter Notebook package. |
| `np.__version__` | Get NumPy version. |
| `pd.__version__` | Get Pandas version. |
| `matplotlib.__version__` | Get Matplotlib version. |
| `notebook.__version__` | Get Notebook version. |

---

# WEEK 1

## 2. Basic Python

| Syntax | Simple English |
|---|---|
| `print(value)` | Print a value. |
| `len(values)` | Return the number of items. |
| `sum(values)` | Sum all items. |
| `max(values)` | Return the largest item. |
| `min(values)` | Return the smallest item. |
| `range(4)` | Generate numbers from 0 to 3. |
| `def function_name(parameters):` | Define a function. |
| `return value` | Return a result from a function. |
| `x if condition else y` | Short conditional expression. |
| `{"key": value}` | Create a dictionary. |
| `dictionary["key"]` | Access a dictionary value. |
| `[x for x in values]` | Create a list with list comprehension. |
| `[x for x in values if condition]` | Filter values with list comprehension. |
| `for x in values:` | Loop through values. |
| `if condition:` | Run code when a condition is true. |
| `elif condition:` | Check another condition. |
| `else:` | Run code when previous conditions are false. |
| `try:` | Try code that may raise an error. |
| `except ValueError as error:` | Catch a ValueError. |
| `f"{value}"` | Insert a value inside a string. |
| `f"{value:.2f}"` | Format a number to two decimal places. |

### OOP

| Syntax | Simple English |
|---|---|
| `class ClassName:` | Define a class. |
| `def __init__(self, ...):` | Define the class constructor. |
| `self.name = name` | Save data inside an object. |
| `def method(self):` | Define a class method. |
| `obj = ClassName(...)` | Create an object. |
| `obj.method()` | Call an object method. |

### Files

| Syntax | Simple English |
|---|---|
| `with open("file.txt", "w") as file:` | Open a file for writing. |
| `file.write(text)` | Write text to a file. |

---

## 3. NumPy — Arrays

| Syntax | Simple English |
|---|---|
| `np.array([1, 2, 3])` | Create a NumPy array. |
| `np.array([[1, 2], [3, 4]])` | Create a 2D array. |
| `np.arange(1, 17)` | Create values from 1 to 16. |
| `array.reshape(4, 4)` | Change array shape. |
| `array.shape` | Return array dimensions. |
| `array.dtype` | Return array data type. |
| `array.T` | Transpose rows and columns. |
| `array.copy()` | Create an independent copy. |
| `np.set_printoptions(precision=2)` | Control displayed decimal precision. |
| `np.set_printoptions(precision=2, suppress=True)` | Hide scientific notation for small values. |

### Indexing & Slicing

| Syntax | Simple English |
|---|---|
| `array[0]` | Get the first item/row. |
| `array[-1]` | Get the last item/row. |
| `array[:, 1]` | Get the second column. |
| `array[-1, :]` | Get the last row. |
| `array[1:4]` | Slice part of an array. |
| `array[i][j]` | Access one value using two indexes. |
| `array[i, j]` | Access one value in a 2D array. |

### Boolean Masking

| Syntax | Simple English |
|---|---|
| `array > value` | Create a Boolean condition. |
| `array[array > value]` | Keep values matching a condition. |
| `array[array > array.mean()]` | Keep values above the array mean. |
| `(condition1) & (condition2)` | AND between Boolean conditions. |
| `(condition1) \| (condition2)` | OR between Boolean conditions. |
| `~condition` | Reverse a Boolean condition. |

### Broadcasting & Vectorized Operations

| Syntax | Simple English |
|---|---|
| `array + number` | Add one number to every element. |
| `matrix + vector` | Add a vector to matrix rows using broadcasting. |
| `array / 3.6` | Divide every element without a loop. |
| `array * value` | Multiply every element without a loop. |

---

## 4. NumPy — Statistics & Analysis

| Syntax | Simple English |
|---|---|
| `np.mean(array)` | Calculate the mean. |
| `np.median(array)` | Calculate the median. |
| `np.max(array)` | Find the maximum. |
| `np.min(array)` | Find the minimum. |
| `np.sum(array)` | Sum values. |
| `np.argmax(array)` | Return the index of the largest value. |
| `np.percentile(array, 25)` | Calculate a percentile. |
| `np.nanpercentile(array, [25, 75])` | Calculate percentiles while ignoring NaN values. |
| `np.unique(array)` | Return unique values. |
| `np.unique(array, return_counts=True)` | Return unique values and their counts. |
| `np.linalg.norm(vector)` | Calculate vector magnitude. |

---

## 5. NumPy — CSV Data

| Syntax | Simple English |
|---|---|
| `np.genfromtxt("file.csv", delimiter=",", skip_header=1)` | Load numeric CSV data with NumPy. |
| `np.delete(array, 0, axis=1)` | Delete a column. |
| `np.delete(array, 0, axis=0)` | Delete a row. |

Example used:

```python
sensors_data = np.genfromtxt(
    "OBDii_data.csv",
    delimiter=",",
    skip_header=1
)

sensors_data = np.delete(sensors_data, 0, axis=1)
```

---

## 6. Pandas — Loading & Inspecting Data

| Syntax | Simple English |
|---|---|
| `pd.read_csv("file.csv")` | Load a CSV file into a DataFrame. |
| `df.head()` | Show the first rows. |
| `df.tail()` | Show the last rows. |
| `df.shape` | Return rows and columns count. |
| `df.columns` | Return column names. |
| `df.info()` | Show columns, types, and missing values. |
| `df.describe()` | Show descriptive statistics. |
| `df.select_dtypes(include="number")` | Select numeric columns. |
| `df.select_dtypes(include=["number"]).describe()` | Describe numeric columns only. |
| `df["column"]` | Select one column. |
| `df[["col1", "col2"]]` | Select multiple columns. |
| `df[columns].copy()` | Select columns and make a copy. |
| `df.loc[row, "column"]` | Select by labels. |
| `df.iloc[row, column]` | Select by integer positions. |

---

## 7. Pandas — Cleaning & Filtering

| Syntax | Simple English |
|---|---|
| `df.isnull()` | Check missing values. |
| `df.isnull().sum()` | Count missing values per column. |
| `df.isna().sum()` | Count missing values per column. |
| `df.duplicated()` | Mark duplicate rows. |
| `df.duplicated().sum()` | Count duplicate rows. |
| `df.drop_duplicates()` | Remove duplicate rows. |
| `df.drop(columns=["column"])` | Remove a column. |
| `df.dropna()` | Remove rows containing missing values. |
| `df["column"].dropna()` | Remove missing values from one Series. |
| `df["column"].fillna(value)` | Replace missing values. |
| `df[df["column"] > value]` | Filter rows with a condition. |
| `df[(condition1) & (condition2)]` | Filter using AND. |
| `df[(condition1) \| (condition2)]` | Filter using OR. |
| `df["column"].notna()` | Check values that are not missing. |

---

## 8. Pandas — Statistics

| Syntax | Simple English |
|---|---|
| `series.mean()` | Calculate mean. |
| `series.median()` | Calculate median. |
| `series.std()` | Calculate sample standard deviation. |
| `series.var()` | Calculate sample variance. |
| `series.mode()` | Return the mode. |
| `series.max()` | Return maximum. |
| `series.min()` | Return minimum. |
| `series.quantile(0.25)` | Calculate Q1. |
| `series.quantile(0.75)` | Calculate Q3. |
| `series.value_counts()` | Count each unique value. |
| `series.tolist()` | Convert a Series to a Python list. |
| `df.corr()` | Calculate correlations between numeric columns. |
| `df["x"].corr(df["y"])` | Calculate correlation between two Series. |

### IQR Pattern

```python
q1 = df["column"].quantile(0.25)
q3 = df["column"].quantile(0.75)
iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

outliers = df[
    (df["column"] < lower) |
    (df["column"] > upper)
]
```

---

## 9. Pandas — Grouping

| Syntax | Simple English |
|---|---|
| `df.groupby("column")` | Group rows by a column. |
| `df.groupby("column")["value"].mean()` | Mean for each group. |
| `df.groupby("column")["value"].sum()` | Sum for each group. |
| `df.groupby("column").agg(...)` | Apply several aggregations. |

---

## 10. Matplotlib — Core Plot Syntax

| Syntax | Simple English |
|---|---|
| `plt.figure(figsize=(8, 5))` | Create a figure with a custom size. |
| `plt.plot(x, y)` | Create a line plot. |
| `plt.scatter(x, y)` | Create a scatter plot. |
| `plt.bar(x, y)` | Create a bar chart. |
| `plt.hist(values, bins=20)` | Create a histogram. |
| `plt.boxplot(values)` | Create a box plot. |
| `plt.xlabel("X")` | Set x-axis label. |
| `plt.ylabel("Y")` | Set y-axis label. |
| `plt.title("Title")` | Set plot title. |
| `plt.legend()` | Show plot legend. |
| `plt.grid()` | Show grid lines. |
| `plt.tight_layout()` | Fix spacing between plot elements. |
| `plt.show()` | Display the plot. |

### Histogram Examples Used

```python
plt.hist(data, bins=30)
plt.show()
```

```python
plt.figure(figsize=(8, 5))
plt.hist(normal, bins=30, edgecolor="black")
plt.title("Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
```

### Pandas Multi-Histogram

```python
df[
    ["danceability", "energy", "tempo", "loudness"]
].hist(figsize=(10, 8), bins=20)

plt.tight_layout()
plt.show()
```

---

# WEEK 2

## 11. Random Numbers & Probability

| Syntax | Simple English |
|---|---|
| `np.random.seed(40)` | Make random results reproducible. |
| `np.random.uniform(1, 7, 10)` | Generate uniform random decimal values. |
| `np.random.choice(values, size)` | Randomly select values. |
| `np.random.choice(values, size, p=probabilities)` | Randomly select using custom probabilities. |
| `np.random.permutation(values)` | Randomly shuffle values. |
| `np.random.randint(1, 7, 20)` | Generate random integers from 1 to 6. |
| `np.random.rand()` | Generate a random decimal from 0 to 1. |
| `np.random.normal(mean, std, size)` | Generate normally distributed values. |
| `np.random.binomial(n, p, size)` | Generate binomial experiment results. |
| `np.mean(condition)` | Calculate the proportion of True values. |

### Coin Flip

```python
record1 = np.random.choice(["H", "T"], 10000)
record2 = np.random.choice(["H", "T"], 10000)

p_head = np.mean(record1 == "H")
p_tail = np.mean(record1 == "T")
```

### Dice

```python
dice = np.random.randint(1, 7, 10000)

p4 = np.mean(dice == 4)
not_p4 = np.mean(dice != 4)
```

### Probability Events

```python
A = dice % 2 == 0
B = dice > 4

pA = np.mean(A)
pB = np.mean(B)
pAB = np.mean(A & B)

p_union_formula = pA + pB - pAB
p_union_direct = np.mean(A | B)
```

### Conditional Probability

```python
male_students = data_frame[
    data_frame["Gender"] == "M"
]

p_passed_given_male = np.mean(
    male_students["Passed"] == 1
)
```

### Bayes Calculation

```python
p_male_given_passed = np.mean(
    data_frame[data_frame["Passed"] == 1]["Gender"] == "M"
)

p_passed = np.mean(data_frame["Passed"] == 1)
p_male = np.mean(data_frame["Gender"] == "M")

p_passed_given_male_bayes = (
    p_male_given_passed * p_passed / p_male
)
```

---

## 12. Probability Distributions

### Normal Distribution

```python
normal = np.random.normal(170, 10, 100000)

plt.figure(figsize=(8, 5))
plt.hist(normal, bins=30, edgecolor="black")
plt.show()
```

### Uniform Distribution

```python
uniform = np.random.uniform(0, 10, 100000)

plt.hist(uniform, bins=30, edgecolor="black")
plt.show()
```

### Binomial Distribution

```python
binomial = np.random.binomial(
    n=10,
    p=0.5,
    size=100000
)

plt.hist(binomial, bins=11, edgecolor="black")
plt.show()
```

---

## 13. Linear Algebra for ML

### Vectors & Matrices

```python
car1 = np.array([2200, 60, 88])
car2 = np.array([3100, 95, 93])
car3 = np.array([1800, 40, 84])

cars = np.array([car1, car2, car3])
```

| Syntax | Simple English |
|---|---|
| `vector.shape` | Return vector shape. |
| `matrix.shape` | Return matrix shape. |
| `matrix.T` | Transpose a matrix. |
| `np.dot(a, b)` | Calculate a dot product. |
| `a @ b` | Perform matrix multiplication / dot product. |
| `np.linalg.norm(vector)` | Calculate vector magnitude. |
| `np.linalg.det(matrix)` | Calculate matrix determinant. |
| `np.linalg.inv(matrix)` | Calculate matrix inverse. |
| `np.linalg.eig(matrix)` | Calculate eigenvalues and eigenvectors. |

### Dot Product

```python
weights = np.array([0.003, 0.5, 0.2])

prediction_car1 = np.dot(weights, car1)
prediction_car2 = np.dot(weights, car2)
prediction_car3 = np.dot(weights, car3)
```

### Batch Prediction

```python
predictions = cars @ weights
```

### Pairwise Dot Products

```python
print(cars.T)
print(cars @ cars.T)
```

### Norm

```python
sensor_energy = np.linalg.norm(car1)
```

### Determinant, Inverse, Eigenvalues

```python
A = np.array([
    [2, 5],
    [3, 7]
])

print(np.linalg.det(A))
print(np.linalg.inv(A))
print(np.linalg.eig(A))
```

### Shape Error Handling

```python
try:
    print(cars @ wrong_weights)
except ValueError as error:
    print(error)
```

---

## 14. EDA — Data Inspection

| Syntax | Simple English |
|---|---|
| `df.head()` | Preview the first rows. |
| `df.info()` | Inspect types and missing values. |
| `df.select_dtypes(include=["number"]).describe()` | Describe numeric columns. |
| `df.isnull().sum()` | Count missing values. |
| `df.duplicated().sum()` | Count duplicate rows. |
| `df["target"].value_counts()` | Count target classes. |

---

## 15. Seaborn — Plots Used

### Count Plot

```python
sns.countplot(x="target", data=df)
plt.title("Count plot - target")
plt.show()
```

**Meaning:** Compare category counts.

### Box Plot

```python
sns.boxplot(x=df["tempo"])
plt.title("Boxplot - tempo")
plt.show()
```

**Meaning:** Show spread and possible outliers.

### Regression Plot

```python
sns.regplot(
    data=df,
    x="energy",
    y="loudness",
    scatter_kws={"alpha": 0.5}
)

plt.title("Energy vs Loudness")
plt.show()
```

**Meaning:** Show a scatter plot with a fitted regression line.

### Correlation Heatmap

```python
numeric_df = df.select_dtypes(include="number")

numeric_df.corr()

plt.figure(figsize=(14, 10))

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    center=0
)

plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()
```

**Meaning:** Visualize correlations between numeric features.

### Pair Plot

```python
sns.pairplot(df[numeric_columns])
plt.show()
```

**Meaning:** Compare several numeric features pair by pair.

---

## 16. Useful Plot Parameters

| Syntax | Simple English |
|---|---|
| `figsize=(10, 8)` | Set figure width and height. |
| `bins=20` | Set histogram bin count. |
| `edgecolor="black"` | Draw borders around histogram bars. |
| `alpha=0.5` | Make points partly transparent. |
| `annot=True` | Write values inside heatmap cells. |
| `fmt=".2f"` | Display values with two decimal places. |
| `cmap="coolwarm"` | Set heatmap color map. |
| `center=0` | Center heatmap colors around zero. |
| `scatter_kws={"alpha": 0.5}` | Set scatter-point options inside Seaborn regplot. |

---

# REVIEW SYNTAX ADDED AFTER WEEK 2

These were added while reviewing the Week 1–2 concepts.

## 17. Z-Score

```python
mean = df["order_value"].mean()
std = df["order_value"].std()

df["z_score"] = (
    df["order_value"] - mean
) / std

df["z_outlier"] = df["z_score"].abs() > 3
```

| Syntax | Simple English |
|---|---|
| `series.abs()` | Return absolute values. |

---

## 18. Pearson & Spearman Correlation

```python
df[["x", "y"]].corr(method="pearson")
df[["x", "y"]].corr(method="spearman")
```

| Syntax | Simple English |
|---|---|
| `method="pearson"` | Measure linear correlation. |
| `method="spearman"` | Measure rank-based monotonic correlation. |

---

## 19. GroupBy Named Aggregation

```python
result = df.groupby("customer_type").agg(
    orders=("order_value", "count"),
    total_sales=("order_value", "sum"),
    delivery_avg=("delivery_minutes", "mean"),
    max_order=("order_value", "max")
)
```

**Pattern:**

```python
new_column=("source_column", "aggregation")
```

---

## 20. Pivot Table

```python
pivot = pd.pivot_table(
    df,
    values="order_value",
    index="customer_type",
    columns="channel",
    aggfunc="sum"
)
```

Multiple calculations:

```python
pivot = pd.pivot_table(
    df,
    values="order_value",
    index="customer_type",
    columns="channel",
    aggfunc=["count", "sum", "mean"]
)
```

---

## 21. Missing-Row Detection

```python
df.isna().sum()
```

```python
df.isna().sum().sum()
```

```python
df[
    df.isna().any(axis=1)
]
```

| Syntax | Simple English |
|---|---|
| `any(axis=1)` | Check whether any value is True in each row. |

---

# Quick Plot Decision Guide

| Question | Plot |
|---|---|
| How is one numeric feature distributed? | Histogram |
| Are there outliers / how spread is the data? | Box plot |
| How do two numeric features relate? | Scatter plot |
| How does a value change over ordered/time data? | Line plot |
| Compare category values/counts? | Bar / Count plot |
| Compare many numeric relationships? | Pair plot |
| See correlations between many features? | Heatmap |
| Show a linear trend between two features? | Regplot |

---

# Fast Workflow Reminder

```python
# 1. Load
df = pd.read_csv("data.csv")

# 2. Inspect
df.head()
df.shape
df.info()
df.describe()

# 3. Check quality
df.isna().sum()
df.duplicated().sum()

# 4. Explore distributions
df.hist()
plt.show()

# 5. Explore relationships
df.corr(numeric_only=True)

# 6. Visualize
sns.heatmap(
    df.corr(numeric_only=True),
    annot=True
)
plt.show()
```

---

**Purpose:** Keep this file open beside your internship notebooks and use `Ctrl + F` to find syntax quickly.


---

# WEEK 3

## 22. Scikit-learn — Main Imports

| Syntax | Simple English |
|---|---|
| `from sklearn.datasets import load_breast_cancer` | Load the Breast Cancer Wisconsin dataset. |
| `from sklearn.datasets import load_diabetes` | Load the Diabetes regression dataset. |
| `from sklearn.model_selection import train_test_split` | Split data into training and test sets. |
| `from sklearn.preprocessing import StandardScaler` | Standardize numeric features. |
| `from sklearn.preprocessing import OneHotEncoder` | Convert categorical values into numeric indicator columns. |
| `from sklearn.compose import ColumnTransformer` | Apply different preprocessing to different column groups. |
| `from sklearn.pipeline import Pipeline` | Chain preprocessing and a model into one workflow. |
| `from sklearn.linear_model import LinearRegression` | Import Linear Regression. |
| `from sklearn.linear_model import LogisticRegression` | Import Logistic Regression. |
| `from sklearn.tree import DecisionTreeClassifier` | Import a Decision Tree classifier. |
| `from sklearn.ensemble import RandomForestClassifier` | Import a Random Forest classifier. |
| `from sklearn.svm import SVC` | Import Support Vector Classification. |
| `from sklearn.neighbors import KNeighborsClassifier` | Import k-Nearest Neighbors. |
| `from sklearn.dummy import DummyClassifier` | Import a simple baseline classifier. |

---

## 23. Supervised Learning — Features & Target

| Syntax | Simple English |
|---|---|
| `X = df.drop(columns="target")` | Use all columns except the target as features. |
| `y = df["target"]` | Select the target to predict. |
| `X.shape` | Check feature-matrix dimensions. |
| `y.shape` | Check target dimensions. |
| `y.value_counts()` | Count samples in each target class. |
| `y.value_counts(normalize=True)` | Return class proportions instead of counts. |
| `(y.value_counts(normalize=True) * 100).round(2)` | Show target percentages. |
| `df["Churn"].map({"No": 0, "Yes": 1})` | Encode a binary target as 0 and 1. |

### Example — Week 3 Classification Target

```python
X = df.drop(columns="Churn")
y = df["Churn"].map({
    "No": 0,
    "Yes": 1
})
```

---

## 24. Train / Test Split

| Syntax | Simple English |
|---|---|
| `train_test_split(X, y, test_size=0.2, random_state=42)` | Keep 20% of the data for testing with a reproducible split. |
| `stratify=y` | Preserve approximately the same target-class proportions in train and test. |
| `X_train.shape` | Check training-feature shape. |
| `X_test.shape` | Check test-feature shape. |
| `y_train.value_counts(normalize=True)` | Check class proportions in the training target. |
| `y_test.value_counts(normalize=True)` | Check class proportions in the test target. |

### Stratified Split Used

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)
```

**Meaning:** train on one part of the data and evaluate on unseen data while preserving class proportions.

---

## 25. Scikit-learn — Core Model Workflow

| Syntax | Simple English |
|---|---|
| `model = Model(...)` | Create a model and set its options. |
| `model.fit(X_train, y_train)` | Learn patterns from training data. |
| `model.predict(X_test)` | Predict labels or values for unseen test data. |
| `model.score(X_test, y_test)` | Return the model's default score. |

### General Pattern

```python
model = Model(...)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

---

## 26. Linear Regression

| Syntax | Simple English |
|---|---|
| `model = LinearRegression()` | Create a Linear Regression model. |
| `model.fit(X_train, y_train)` | Learn coefficients and intercept from training data. |
| `model.predict(X_test)` | Predict continuous target values. |
| `model.coef_` | Return learned feature coefficients. |
| `model.intercept_` | Return the learned intercept / bias. |
| `X_train[["bmi"]]` | Select BMI as a one-feature DataFrame. |

### Basic Linear Regression

```python
model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print(model.coef_)
print(model.intercept_)
```

### Linear Prediction Form

```text
prediction = Xw + b
```

- `X` = features
- `w` = learned coefficients
- `b` = intercept

---

## 27. Regression Metrics

| Syntax | Simple English |
|---|---|
| `mean_absolute_error(y_test, predictions)` | Calculate MAE. |
| `root_mean_squared_error(y_test, predictions)` | Calculate RMSE directly. |
| `np.sqrt(mean_squared_error(y_test, predictions))` | Another way to calculate RMSE. |
| `r2_score(y_test, predictions)` | Calculate R². |

### Imports

```python
from sklearn.metrics import (
    mean_absolute_error,
    root_mean_squared_error,
    r2_score
)
```

### Example

```python
mae = mean_absolute_error(y_test, predictions)
rmse = root_mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)
```

### Metric Meaning

| Metric | Simple Meaning |
|---|---|
| MAE | Average absolute prediction error. |
| RMSE | Error measure that penalizes larger errors more strongly. |
| R² | How much target variation the model explains relative to a mean-based reference. |

---

## 28. Regression Baseline

| Syntax | Simple English |
|---|---|
| `y_train.mean()` | Calculate the training-target mean. |
| `np.full(len(y_test), y_train.mean())` | Predict the training mean for every test sample. |

### Mean Baseline Pattern

```python
baseline_value = y_train.mean()

baseline_predictions = np.full(
    len(y_test),
    baseline_value
)

baseline_rmse = root_mean_squared_error(
    y_test,
    baseline_predictions
)
```

**Meaning:** compare Linear Regression against a simple model that always predicts the training mean.

---

## 29. Residual Analysis

| Syntax | Simple English |
|---|---|
| `residuals = y_test - predictions` | Calculate actual minus predicted values. |
| `plt.scatter(predictions, residuals)` | Plot prediction errors against predictions. |
| `plt.axhline(y=0, linestyle="--")` | Draw the zero-error reference line. |

### Residual Plot

```python
residuals = y_test - predictions

plt.figure(figsize=(8, 5))
plt.scatter(predictions, residuals, alpha=0.7)
plt.axhline(y=0, linestyle="--")

plt.xlabel("Predicted Values")
plt.ylabel("Residuals")
plt.title("Residuals vs Predicted Values")
plt.show()
```

---

## 30. StandardScaler — Leakage-Free Scaling

| Syntax | Simple English |
|---|---|
| `scaler = StandardScaler()` | Create a standard scaler. |
| `scaler.fit_transform(X_train)` | Learn scaling from training data and transform training data. |
| `scaler.transform(X_test)` | Transform test data using training-set scaling only. |

### Pattern Used

```python
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

**Important:** do not fit the scaler separately on the test set.

---

## 31. Logistic Regression

| Syntax | Simple English |
|---|---|
| `LogisticRegression(max_iter=1000)` | Create a Logistic Regression classifier with a larger iteration limit. |
| `model.fit(X_train_scaled, y_train)` | Train the classifier. |
| `model.predict(X_test_scaled)` | Return predicted classes. |
| `model.predict_proba(X_test_scaled)` | Return class probabilities. |
| `probabilities[:, 1]` | Get probability of the positive class. |
| `model.coef_` | Return learned feature coefficients. |
| `model.intercept_` | Return the intercept. |

### Example

```python
model = LogisticRegression(max_iter=1000)

model.fit(X_train_scaled, y_train)

predictions = model.predict(X_test_scaled)
probabilities = model.predict_proba(X_test_scaled)

positive_probabilities = probabilities[:, 1]
```

---

## 32. `predict()` vs `predict_proba()`

| Syntax | Simple English |
|---|---|
| `model.predict(X_test)` | Return final predicted classes such as 0 or 1. |
| `model.predict_proba(X_test)` | Return probability for each class. |
| `model.predict_proba(X_test)[:, 1]` | Return only positive-class probabilities. |

Example probability row:

```text
[P(class 0), P(class 1)]
```

---

## 33. Classification Metrics

### Imports

```python
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)
```

| Syntax | Simple English |
|---|---|
| `accuracy_score(y_test, y_pred)` | Fraction of all predictions that are correct. |
| `precision_score(y_test, y_pred)` | Of predicted positives, how many are actually positive. |
| `recall_score(y_test, y_pred)` | Of actual positives, how many the model found. |
| `f1_score(y_test, y_pred)` | Balance Precision and Recall in one score. |
| `roc_auc_score(y_test, y_score)` | Measure how well scores separate the two classes across thresholds. |
| `zero_division=0` | Return 0 instead of a division warning when a metric denominator is zero. |

### Example

```python
accuracy = accuracy_score(y_test, y_pred)

precision = precision_score(
    y_test,
    y_pred,
    zero_division=0
)

recall = recall_score(
    y_test,
    y_pred,
    zero_division=0
)

f1 = f1_score(
    y_test,
    y_pred,
    zero_division=0
)

auc = roc_auc_score(
    y_test,
    y_score
)
```

---

## 34. Quick Classification Metric Guide

| Metric | Main Question |
|---|---|
| Accuracy | How many total predictions were correct? |
| Precision | Of everything predicted Positive, how much was really Positive? |
| Recall | Of all real Positive cases, how many were found? |
| F1-score | Is there a good balance between Precision and Recall? |
| ROC-AUC | Does the model generally give Positive cases higher scores than Negative cases across thresholds? |

### Confusion-Matrix Terms

| Term | Meaning |
|---|---|
| TP | Predicted Positive and actually Positive. |
| TN | Predicted Negative and actually Negative. |
| FP | Predicted Positive but actually Negative. |
| FN | Predicted Negative but actually Positive. |

---

## 35. Confusion Matrix

### Imports

```python
from sklearn.metrics import (
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report
)
```

| Syntax | Simple English |
|---|---|
| `confusion_matrix(y_test, y_pred)` | Return TN, FP, FN, TP counts. |
| `cm.ravel()` | Unpack a 2×2 confusion matrix into four values. |
| `classification_report(y_test, y_pred)` | Show Precision, Recall, F1, and support. |
| `ConfusionMatrixDisplay.from_predictions(...)` | Build and display a confusion matrix directly from predictions. |
| `ConfusionMatrixDisplay(confusion_matrix=cm).plot()` | Plot an already calculated confusion matrix. |

### Example

```python
cm = confusion_matrix(y_test, predictions)

tn, fp, fn, tp = cm.ravel()

print("TN:", tn)
print("FP:", fp)
print("FN:", fn)
print("TP:", tp)
```

```python
ConfusionMatrixDisplay.from_predictions(
    y_test,
    predictions,
    display_labels=["Benign", "Malignant"]
)

plt.show()
```

---

## 36. Classification Report

```python
print(
    classification_report(
        y_test,
        predictions
    )
)
```

With custom class names:

```python
print(
    classification_report(
        y_test,
        y_pred,
        target_names=["Stay", "Churn"]
    )
)
```

**Meaning:** display Precision, Recall, F1-score, and support for each class.

---

## 37. DummyClassifier — Classification Baseline

| Syntax | Simple English |
|---|---|
| `DummyClassifier(strategy="most_frequent")` | Always predict the most common training class. |
| `baseline.fit(X_train, y_train)` | Fit the simple baseline. |
| `baseline.predict(X_test)` | Generate baseline predictions. |
| `baseline.predict_proba(X_test)[:, 1]` | Return baseline positive-class probability. |

### Example

```python
baseline = DummyClassifier(
    strategy="most_frequent"
)

baseline.fit(X_train, y_train)

baseline_predictions = baseline.predict(X_test)
```

**Meaning:** check whether the real model beats a naive strategy.

---

## 38. ROC Curve & ROC-AUC

### Imports

```python
from sklearn.metrics import (
    roc_curve,
    roc_auc_score,
    RocCurveDisplay
)
```

| Syntax | Simple English |
|---|---|
| `roc_curve(y_test, positive_probabilities)` | Calculate ROC points across thresholds. |
| `roc_auc_score(y_test, positive_probabilities)` | Calculate area under the ROC curve. |
| `RocCurveDisplay.from_predictions(y_test, y_score)` | Plot an ROC curve directly from actual labels and scores. |

### ROC Pattern

```python
fpr, tpr, thresholds = roc_curve(
    y_test,
    positive_probabilities
)

auc = roc_auc_score(
    y_test,
    positive_probabilities
)
```

### Plot Pattern

```python
plt.plot(
    fpr,
    tpr,
    label=f"Model (AUC = {auc:.3f})"
)

plt.plot(
    [0, 1],
    [0, 1],
    "--",
    label="Random"
)

plt.legend()
plt.show()
```

**Quick meaning:** AUC closer to `1` means stronger class separation; around `0.5` is close to random ranking.

---

## 39. Decision Tree

| Syntax | Simple English |
|---|---|
| `DecisionTreeClassifier(random_state=42)` | Create a reproducible Decision Tree. |
| `DecisionTreeClassifier(max_depth=5, random_state=42)` | Limit tree depth to reduce complexity. |
| `model.fit(X_train, y_train)` | Train the tree. |
| `model.predict(X_test)` | Predict test classes. |

### Example

```python
tree_model = DecisionTreeClassifier(
    max_depth=5,
    random_state=42
)

tree_model.fit(
    X_train,
    y_train
)

tree_predictions = tree_model.predict(
    X_test
)
```

---

## 40. Decision Tree Visualization

```python
from sklearn.tree import plot_tree
```

```python
plt.figure(figsize=(18, 8))

plot_tree(
    tree_model,
    max_depth=2,
    filled=True,
    feature_names=feature_names,
    class_names=class_names
)

plt.show()
```

| Parameter | Simple English |
|---|---|
| `max_depth=2` | Display only the first tree levels. |
| `filled=True` | Color the tree nodes. |
| `feature_names=...` | Show feature names in the nodes. |
| `class_names=...` | Show class names. |

---

## 41. Train vs Test Score — Overfitting Check

```python
train_predictions = model.predict(X_train)
test_predictions = model.predict(X_test)

train_f1 = f1_score(
    y_train,
    train_predictions
)

test_f1 = f1_score(
    y_test,
    test_predictions
)
```

**Meaning:** a large gap between training and test performance can indicate overfitting.

---

## 42. Random Forest

| Syntax | Simple English |
|---|---|
| `RandomForestClassifier(n_estimators=100, random_state=42)` | Build a forest containing 100 trees. |
| `model.feature_importances_` | Return model-based feature importance values. |

### Example

```python
rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf_model.fit(
    X_train,
    y_train
)

rf_predictions = rf_model.predict(
    X_test
)
```

---

## 43. Random Forest Feature Importance

```python
feature_importance = pd.Series(
    rf_model.feature_importances_,
    index=feature_names
)
```

```python
feature_importance = (
    feature_importance
    .sort_values(ascending=False)
)
```

```python
top_features = (
    feature_importance
    .head(10)
)
```

**Meaning:** rank features by how useful they were to the fitted Random Forest.

---

## 44. Support Vector Machine — SVM

| Syntax | Simple English |
|---|---|
| `SVC(kernel="linear")` | Use a linear SVM boundary. |
| `SVC(kernel="rbf")` | Use the RBF kernel for a non-linear boundary. |
| `SVC(kernel="rbf", probability=True)` | Enable probability estimates for `predict_proba()`. |

### Examples

```python
linear_svm = SVC(
    kernel="linear"
)
```

```python
rbf_svm = SVC(
    kernel="rbf"
)
```

Week 3 mini-project pattern:

```python
svm = SVC(
    kernel="rbf",
    probability=True,
    random_state=42
)
```

**Important:** SVM was evaluated after feature scaling.

---

## 45. k-Nearest Neighbors — k-NN

| Syntax | Simple English |
|---|---|
| `KNeighborsClassifier(n_neighbors=5)` | Classify using the 5 nearest training samples. |
| `n_neighbors=k` | Set the value of `k`. |

### Basic Example

```python
knn = KNeighborsClassifier(
    n_neighbors=5
)

knn.fit(
    X_train_scaled,
    y_train
)

knn_predictions = knn.predict(
    X_test_scaled
)
```

### Testing Several `k` Values

```python
for k in [1, 3, 5, 7, 11, 21]:
    knn = KNeighborsClassifier(
        n_neighbors=k
    )

    knn.fit(
        X_train_scaled,
        y_train
    )

    predictions = knn.predict(
        X_test_scaled
    )

    print(
        k,
        f1_score(y_test, predictions)
    )
```

---

## 46. Cleaning `TotalCharges` in the Telco Dataset

| Syntax | Simple English |
|---|---|
| `series.astype(str)` | Convert values to strings. |
| `series.str.strip()` | Remove spaces around strings. |
| `series.eq("")` | Check which values are empty strings. |
| `pd.to_numeric(series, errors="coerce")` | Convert values to numeric and turn invalid values into NaN. |
| `df.dropna(subset=["TotalCharges"])` | Remove rows where `TotalCharges` is missing. |

### Blank-Value Check

```python
blank_total_charges = (
    df["TotalCharges"]
    .astype(str)
    .str.strip()
    .eq("")
    .sum()
)
```

### Conversion & Cleaning

```python
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

df = df.dropna(
    subset=["TotalCharges"]
).copy()
```

---

## 47. Removing an Identifier

```python
df = df.drop(
    columns="customerID"
)
```

```python
"customerID" not in df.columns
```

**Meaning:** remove a unique identifier that should not be used as a predictive feature.

---

## 48. Churn EDA Patterns

### Numeric Summary

```python
numeric_summary = df[
    [
        "SeniorCitizen",
        "tenure",
        "MonthlyCharges",
        "TotalCharges"
    ]
].describe().round(2)
```

### Grouped Medians

```python
df.groupby("Churn")[
    [
        "tenure",
        "MonthlyCharges",
        "TotalCharges"
    ]
].median().round(2)
```

### Churn Rate by Category

```python
contract_churn = (
    df.groupby("Contract")["Churn"]
      .apply(
          lambda values:
          (values == "Yes").mean() * 100
      )
      .sort_values(
          ascending=False
      )
      .round(2)
)
```

### Pandas Bar Plot

```python
contract_churn.plot(
    kind="bar"
)

plt.ylabel("Churn Rate (%)")
plt.show()
```

---

## 49. Selecting Numeric & Categorical Features

| Syntax | Simple English |
|---|---|
| `X_train.select_dtypes(include=np.number)` | Select numeric training columns. |
| `X_train.select_dtypes(exclude=np.number)` | Select non-numeric / categorical training columns. |
| `.columns.tolist()` | Convert column names to a Python list. |

### Pattern Used

```python
numerical_features = (
    X_train
    .select_dtypes(include=np.number)
    .columns
    .tolist()
)

categorical_features = (
    X_train
    .select_dtypes(exclude=np.number)
    .columns
    .tolist()
)
```

---

## 50. One-Hot Encoding

```python
OneHotEncoder(
    handle_unknown="ignore"
)
```

**Meaning:** convert categorical values into numeric indicator columns and safely handle categories not seen during fitting.

---

## 51. ColumnTransformer

```python
preprocessor = ColumnTransformer(
    transformers=[
        (
            "num",
            StandardScaler(),
            numerical_features
        ),
        (
            "cat",
            OneHotEncoder(
                handle_unknown="ignore"
            ),
            categorical_features
        )
    ]
)
```

**Meaning:**
- scale numeric features,
- one-hot encode categorical features,
- keep both transformations in one preprocessing object.

---

## 52. Scikit-learn Pipeline

```python
pipeline = Pipeline([
    (
        "preprocessor",
        preprocessor
    ),
    (
        "model",
        model
    )
])
```

| Syntax | Simple English |
|---|---|
| `pipeline.fit(X_train, y_train)` | Fit preprocessing and the model using training data. |
| `pipeline.predict(X_test)` | Apply learned preprocessing and predict test classes. |
| `pipeline.predict_proba(X_test)[:, 1]` | Return positive-class probabilities after pipeline preprocessing. |
| `pipeline.named_steps["model"]` | Access the fitted model inside the pipeline. |
| `pipeline.named_steps["preprocessor"]` | Access the fitted preprocessor inside the pipeline. |

**Main benefit:** preprocessing is learned during training and is not fitted on the test set.

---

## 53. Dictionary of Models

```python
models = {
    "Baseline": DummyClassifier(
        strategy="most_frequent"
    ),

    "Logistic Regression": LogisticRegression(
        max_iter=1000,
        random_state=42
    ),

    "Decision Tree": DecisionTreeClassifier(
        max_depth=5,
        random_state=42
    ),

    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        random_state=42
    ),

    "SVM": SVC(
        kernel="rbf",
        probability=True,
        random_state=42
    ),

    "k-NN": KNeighborsClassifier(
        n_neighbors=5
    )
}
```

**Meaning:** store several models under readable names so they can be trained with the same workflow.

---

## 54. Training Several Models with One Loop

```python
trained_models = {}
results = []

for model_name, model in models.items():

    pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("model", model)
    ])

    pipeline.fit(
        X_train,
        y_train
    )

    y_pred = pipeline.predict(
        X_test
    )

    y_score = pipeline.predict_proba(
        X_test
    )[:, 1]

    trained_models[model_name] = pipeline
```

**Meaning:** train every model using the same preprocessing and the same train/test split.

---

## 55. Saving Model Metrics in a List

```python
results.append({
    "Model": model_name,

    "Accuracy": accuracy_score(
        y_test,
        y_pred
    ),

    "Precision": precision_score(
        y_test,
        y_pred,
        zero_division=0
    ),

    "Recall": recall_score(
        y_test,
        y_pred,
        zero_division=0
    ),

    "F1-score": f1_score(
        y_test,
        y_pred,
        zero_division=0
    ),

    "ROC-AUC": roc_auc_score(
        y_test,
        y_score
    )
})
```

---

## 56. Model Comparison DataFrame

```python
results_df = (
    pd.DataFrame(results)
    .set_index("Model")
)
```

```python
results_sorted = (
    results_df
    .sort_values(
        ["F1-score", "Recall"],
        ascending=False
    )
)
```

```python
results_sorted.round(4)
```

| Syntax | Simple English |
|---|---|
| `pd.DataFrame(results)` | Convert model-result dictionaries into a table. |
| `.set_index("Model")` | Use model names as row labels. |
| `.sort_values(["F1-score", "Recall"], ascending=False)` | Rank models by F1 first, then Recall. |
| `.round(4)` | Display four decimal places. |

---

## 57. Selecting the Best Model from Results

```python
best_model_name = (
    results_sorted.index[0]
)

best_metrics = results_df.loc[
    best_model_name
]

selected_model = trained_models[
    best_model_name
]
```

**Meaning:** use the first model in the sorted comparison table instead of manually hard-coding a winner.

---

## 58. ROC Curves for Several Models

```python
plt.figure(figsize=(8, 6))

for model_name, pipeline in trained_models.items():

    if model_name == "Baseline":
        continue

    y_score = pipeline.predict_proba(
        X_test
    )[:, 1]

    RocCurveDisplay.from_predictions(
        y_test,
        y_score,
        name=model_name,
        ax=plt.gca()
    )

plt.plot(
    [0, 1],
    [0, 1],
    "--",
    label="Random"
)

plt.legend()
plt.show()
```

---

## 59. Accessing Pipeline Steps

```python
rf_pipeline = trained_models[
    "Random Forest"
]

rf_preprocessor = rf_pipeline.named_steps[
    "preprocessor"
]

rf_model = rf_pipeline.named_steps[
    "model"
]
```

**Meaning:** access fitted objects stored inside a trained pipeline.

---

## 60. Feature Names After One-Hot Encoding

```python
feature_names = (
    rf_preprocessor
    .get_feature_names_out()
)
```

```python
feature_names = [
    name
    .replace("num__", "")
    .replace("cat__", "")

    for name in feature_names
]
```

**Meaning:** retrieve transformed feature names and remove transformer prefixes.

---

## 61. Feature Importance After a Pipeline

```python
feature_importance = pd.Series(
    rf_model.feature_importances_,
    index=feature_names,
    name="Importance"
)
```

```python
feature_importance = (
    feature_importance
    .sort_values(
        ascending=False
    )
)
```

```python
top_features = (
    feature_importance
    .head(10)
    .to_frame()
)
```

---

## 62. Horizontal Feature-Importance Plot

```python
top_features \
    .sort_values("Importance") \
    .plot(
        kind="barh",
        legend=False
    )

plt.title(
    "Top 10 Random Forest Feature Importances"
)

plt.xlabel("Importance")
plt.ylabel("Feature")
plt.show()
```

---

## 63. IPython Display

| Syntax | Simple English |
|---|---|
| `display(value)` | Display an object nicely inside Jupyter. |
| `display(df.round(4))` | Display a formatted DataFrame. |
| `Markdown(text)` | Convert a string into rendered Markdown. |
| `display(Markdown(text))` | Render generated Markdown inside a notebook. |

### Import

```python
from IPython.display import (
    display,
    Markdown
)
```

---

# Week 3 Model Decision Guide

| Situation | Useful Metric / Idea |
|---|---|
| Regression — easy average error | MAE |
| Regression — large errors should matter more | RMSE |
| Regression — explained variation | R² |
| Classification — overall correct predictions | Accuracy |
| Predicted positives must be reliable | Precision |
| Missing real positives is expensive | Recall |
| Need Precision/Recall balance | F1-score |
| Compare class separation across thresholds | ROC-AUC |
| Check whether a model adds value | Compare with a baseline |
| Check possible overfitting | Compare train vs test performance |
| SVM / k-NN use distance or geometry | Scaling is important |
| Tree / Random Forest | Scaling is normally not required |
| Mixed numeric + categorical columns | `ColumnTransformer` + `Pipeline` |

---

# Week 3 Fast Workflow Reminder

```python
# 1. Load / inspect
df = pd.read_csv("data.csv")
df.head()
df.info()
df.isna().sum()
df.duplicated().sum()

# 2. Clean
# convert types, handle missing values,
# remove identifiers when appropriate

# 3. Define features and target
X = df.drop(columns="target")
y = df["target"]

# 4. Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# 5. Preprocess
# scale numeric features
# encode categorical features
# fit preprocessing on training data only

# 6. Create model
model = Model(...)

# 7. Fit
model.fit(
    X_train,
    y_train
)

# 8. Predict
y_pred = model.predict(
    X_test
)

# 9. Evaluate
# choose metrics that match the problem

# 10. Compare against baseline

# 11. Interpret results
# confusion matrix / residuals /
# feature importance / model comparison
```

---

**Week 3 focus:** supervised learning, train/test discipline, regression, classification, model comparison, leakage-free preprocessing, meaningful metrics, and a complete end-to-end ML pipeline.


---

# ORGANIZED CONNECTED EXAMPLES

> Each row groups related syntax together.  
> The example code and expected result are shown **side by side** for fast review.

---

## WEEK 1 — Python, NumPy, Pandas & Plotting

### Basic Python

| Related Syntax | Example Code | Expected Result |
|---|---|---|
| `len()` + `sum()` + `max()` + `min()` | `values = [4, 8, 2]`<br>`print(len(values), sum(values), max(values), min(values))` | `3 14 8 2` |
| `for` + `if/else` | `for x in [2, 7]:`<br>`    if x > 5:`<br>`        print("High")`<br>`    else:`<br>`        print("Low")` | `Low`<br>`High` |
| Dictionary + indexing | `student = {"name": "Ali", "score": 90}`<br>`print(student["score"])` | `90` |
| List comprehension | `nums = [1, 2, 3, 4]`<br>`even = [x for x in nums if x % 2 == 0]`<br>`print(even)` | `[2, 4]` |
| Function + `return` | `def square(x):`<br>`    return x * x`<br>`print(square(5))` | `25` |
| f-string formatting | `value = 3.14159`<br>`print(f"{value:.2f}")` | `3.14` |

### OOP & Files

| Related Syntax | Example Code | Expected Result |
|---|---|---|
| `class` + `__init__` + method | `class Car:`<br>`    def __init__(self, speed):`<br>`        self.speed = speed`<br>`    def show(self):`<br>`        return self.speed`<br>`car = Car(80)`<br>`print(car.show())` | `80` |
| `with open()` + `write()` | `with open("test.txt", "w") as file:`<br>`    file.write("Hello")` | Creates `test.txt` containing `Hello` |

### NumPy Arrays

| Related Syntax | Example Code | Expected Result |
|---|---|---|
| `np.array()` + `.shape` + `.dtype` | `a = np.array([10, 20, 30])`<br>`print(a.shape)`<br>`print(a.dtype)` | `(3,)`<br>Integer NumPy dtype such as `int64` |
| `np.arange()` + `.reshape()` | `a = np.arange(1, 7).reshape(2, 3)`<br>`print(a)` | `[[1 2 3]`<br>` [4 5 6]]` |
| Indexing + slicing | `a = np.array([[1,2,3],[4,5,6]])`<br>`print(a[0])`<br>`print(a[:, 1])` | `[1 2 3]`<br>`[2 5]` |
| Boolean masking | `a = np.array([2, 7, 4, 9])`<br>`print(a[a > 5])` | `[7 9]` |
| Broadcasting | `a = np.array([1, 2, 3])`<br>`print(a + 10)` | `[11 12 13]` |
| Vectorized operation | `speed = np.array([36, 72])`<br>`print(speed / 3.6)` | `[10. 20.]` |

### NumPy Statistics

| Related Syntax | Example Code | Expected Result |
|---|---|---|
| Mean + median | `a = np.array([1, 2, 9])`<br>`print(np.mean(a))`<br>`print(np.median(a))` | `4.0`<br>`2.0` |
| Min + max + sum | `a = np.array([3, 8, 4])`<br>`print(np.min(a), np.max(a), np.sum(a))` | `3 8 15` |
| Percentile | `a = np.array([10, 20, 30, 40])`<br>`print(np.percentile(a, 25))` | `17.5` |
| Unique values + counts | `a = np.array([1, 1, 2, 3, 3])`<br>`print(np.unique(a, return_counts=True))` | `(array([1, 2, 3]), array([2, 1, 2]))` |

### Pandas Loading, Cleaning & Filtering

| Related Syntax | Example Code | Expected Result |
|---|---|---|
| `pd.DataFrame()` + `.head()` + `.shape` | `df = pd.DataFrame({"speed":[40,50,60]})`<br>`print(df.shape)`<br>`print(df.head(2))` | Shape: `(3, 1)`<br>First two rows are displayed |
| Missing values | `df = pd.DataFrame({"x":[1, np.nan, 3]})`<br>`print(df.isna().sum())` | Column `x` has `1` missing value |
| `dropna()` | `clean = df.dropna()`<br>`print(len(clean))` | `2` |
| Duplicates | `df = pd.DataFrame({"x":[1,1,2]})`<br>`print(df.duplicated().sum())` | `1` |
| Filter rows | `df = pd.DataFrame({"speed":[30,70,90]})`<br>`print(df[df["speed"] > 60])` | Rows containing `70` and `90` |
| Drop column | `df = pd.DataFrame({"id":[1,2], "speed":[40,50]})`<br>`df = df.drop(columns=["id"])`<br>`print(df.columns.tolist())` | `['speed']` |

### Pandas Statistics, Grouping & IQR

| Related Syntax | Example Code | Expected Result |
|---|---|---|
| Mean + std | `s = pd.Series([10, 20, 30])`<br>`print(s.mean())`<br>`print(round(s.std(), 2))` | `20.0`<br>`10.0` |
| `value_counts()` | `s = pd.Series(["A","A","B"])`<br>`print(s.value_counts())` | `A    2`<br>`B    1` |
| Correlation | `df = pd.DataFrame({"x":[1,2,3], "y":[2,4,6]})`<br>`print(df["x"].corr(df["y"]))` | `1.0` |
| `groupby()` + mean | `df = pd.DataFrame({"type":["A","A","B"], "value":[10,20,30]})`<br>`print(df.groupby("type")["value"].mean())` | `A    15.0`<br>`B    30.0` |
| IQR outlier detection | `s = pd.Series([10,11,12,13,50])`<br>`q1=s.quantile(.25)`<br>`q3=s.quantile(.75)`<br>`iqr=q3-q1`<br>`upper=q3+1.5*iqr`<br>`print(s[s > upper].tolist())` | `[50]` |

### Matplotlib

| Related Syntax | Example Code | Expected Result |
|---|---|---|
| Histogram + labels | `plt.hist([1,1,2,3,3], bins=3)`<br>`plt.xlabel("Value")`<br>`plt.ylabel("Frequency")`<br>`plt.title("Distribution")`<br>`plt.show()` | Displays a histogram |
| Scatter plot | `plt.scatter([1,2,3], [2,4,5])`<br>`plt.show()` | Displays three points |
| Line plot | `plt.plot([1,2,3], [5,7,9])`<br>`plt.show()` | Displays a line graph |
| Bar chart | `plt.bar(["A","B"], [4,7])`<br>`plt.show()` | Displays two bars |

---

## WEEK 2 — Probability, Linear Algebra & EDA

### Random Numbers & Probability

| Related Syntax | Example Code | Expected Result |
|---|---|---|
| Seed + random choice | `np.random.seed(40)`<br>`coin = np.random.choice(["H","T"], 5)`<br>`print(coin)` | Same random sequence every time the code is rerun with the same seed |
| Probability from Boolean mean | `dice = np.array([1,4,4,6])`<br>`print(np.mean(dice == 4))` | `0.5` |
| Event intersection | `dice = np.array([1,2,4,5,6])`<br>`A = dice % 2 == 0`<br>`B = dice > 4`<br>`print(np.mean(A & B))` | `0.2` |
| Event union | `print(np.mean(A | B))` | Proportion satisfying `A` or `B` |
| Conditional filtering | `male = df[df["Gender"] == "M"]`<br>`p = np.mean(male["Passed"] == 1)` | Probability of passing among males |

### Probability Distributions

| Related Syntax | Example Code | Expected Result |
|---|---|---|
| Normal distribution | `normal = np.random.normal(170, 10, 1000)`<br>`print(round(normal.mean(), 1))` | Mean is approximately `170` |
| Uniform distribution | `uniform = np.random.uniform(0, 10, 1000)`<br>`print(uniform.min() >= 0, uniform.max() <= 10)` | `True True` |
| Binomial distribution | `x = np.random.binomial(n=10, p=0.5, size=1000)`<br>`print(round(x.mean(), 1))` | Mean is approximately `5.0` |

### Linear Algebra for ML

| Related Syntax | Example Code | Expected Result |
|---|---|---|
| Vector + dot product | `x = np.array([2,3])`<br>`w = np.array([4,5])`<br>`print(np.dot(x,w))` | `23` |
| Matrix batch prediction | `X = np.array([[1,2],[3,4]])`<br>`w = np.array([2,1])`<br>`print(X @ w)` | `[4 10]` |
| Transpose | `A = np.array([[1,2],[3,4]])`<br>`print(A.T)` | `[[1 3]`<br>` [2 4]]` |
| Norm | `v = np.array([3,4])`<br>`print(np.linalg.norm(v))` | `5.0` |
| Determinant | `A = np.array([[2,1],[1,2]])`<br>`print(round(np.linalg.det(A), 2))` | `3.0` |
| Inverse | `print(np.linalg.inv(np.array([[1.,0.],[0.,2.]])))` | `[[1.  0. ]`<br>` [0.  0.5]]` |

### EDA & Seaborn

| Related Syntax | Example Code | Expected Result |
|---|---|---|
| Quick inspection | `df.head()`<br>`df.info()`<br>`df.isna().sum()`<br>`df.duplicated().sum()` | Preview, data types, missing values, duplicate count |
| Count plot | `sns.countplot(x="target", data=df)`<br>`plt.show()` | Displays number of samples in each class |
| Box plot | `sns.boxplot(x=df["tempo"])`<br>`plt.show()` | Displays spread and possible outliers |
| Regression plot | `sns.regplot(data=df, x="energy", y="loudness")`<br>`plt.show()` | Scatter plot with fitted linear trend |
| Correlation heatmap | `sns.heatmap(df.corr(numeric_only=True), annot=True)`<br>`plt.show()` | Displays numeric correlations in a matrix |

### Review Syntax

| Related Syntax | Example Code | Expected Result |
|---|---|---|
| Z-score | `mean = s.mean()`<br>`std = s.std()`<br>`z = (s - mean) / std` | Standardized distance from the mean |
| Pearson vs Spearman | `df[["x","y"]].corr(method="pearson")`<br>`df[["x","y"]].corr(method="spearman")` | Two correlation matrices using different correlation methods |
| Named aggregation | `df.groupby("type").agg(avg=("value","mean"), total=("value","sum"))` | One summary row per group |
| Pivot table | `pd.pivot_table(df, values="value", index="type", columns="channel", aggfunc="sum")` | Matrix-style grouped summary |
| Missing rows | `df[df.isna().any(axis=1)]` | Only rows containing at least one missing value |

---

## WEEK 3 — Supervised Learning

### Features, Target & Train/Test Split

| Related Syntax | Example Code | Expected Result |
|---|---|---|
| Features + target | `X = df.drop(columns="Churn")`<br>`y = df["Churn"].map({"No":0, "Yes":1})` | `X` contains predictors; `y` contains `0/1` target values |
| Class counts | `print(y.value_counts())` | Number of samples in each class |
| Class percentages | `print((y.value_counts(normalize=True) * 100).round(2))` | Percentage of each target class |
| Reproducible split + stratify | `X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=42, stratify=y)` | 80% train, 20% test with similar class proportions |

### Core Scikit-learn Workflow

| Related Syntax | Example Code | Expected Result |
|---|---|---|
| Instantiate + fit + predict | `model = LogisticRegression(max_iter=1000)`<br>`model.fit(X_train, y_train)`<br>`pred = model.predict(X_test)` | Model learns from train data and returns test predictions |
| `.score()` | `print(model.score(X_test, y_test))` | Model's default evaluation score |

### Linear Regression

| Related Syntax | Example Code | Expected Result |
|---|---|---|
| Fit + coefficient + intercept | `X = np.array([[1],[2],[3]])`<br>`y = np.array([3,5,7])`<br>`model = LinearRegression().fit(X,y)`<br>`print(model.coef_)`<br>`print(model.intercept_)` | `[2.]`<br>`1.0` |
| Prediction | `print(model.predict([[4]]))` | `[9.]` |
| MAE | `mean_absolute_error([10,20], [12,18])` | `2.0` |
| RMSE | `root_mean_squared_error([10,20], [12,18])` | `2.0` |
| R² | `r2_score([10,20], [12,18])` | `0.84` |
| Mean baseline | `baseline = np.full(len(y_test), y_train.mean())` | Every test sample receives the same training-target mean |
| Residuals | `residuals = y_test - predictions` | Positive/negative prediction errors |

### StandardScaler & Leakage Prevention

| Related Syntax | Example Code | Expected Result |
|---|---|---|
| Fit train only | `scaler = StandardScaler()`<br>`X_train_scaled = scaler.fit_transform(X_train)` | Scaler learns mean/std from training data |
| Transform test | `X_test_scaled = scaler.transform(X_test)` | Test set uses the train-set scaling parameters |
| Wrong pattern to avoid | `scaler.fit_transform(X_test)` | **Avoid:** test data would influence preprocessing |

### Logistic Regression & Probabilities

| Related Syntax | Example Code | Expected Result |
|---|---|---|
| Logistic Regression | `model = LogisticRegression(max_iter=1000)`<br>`model.fit(X_train_scaled, y_train)` | Trained binary classifier |
| `predict()` | `model.predict(X_test_scaled)` | Final class labels such as `[0, 1, 0, ...]` |
| `predict_proba()` | `p = model.predict_proba(X_test_scaled)`<br>`print(p[0])` | Two probabilities: `[P(class 0), P(class 1)]` |
| Positive probability | `positive = p[:, 1]` | One positive-class score per sample |

### Classification Metrics

| Related Syntax | Example Code | Expected Result |
|---|---|---|
| Accuracy | `accuracy_score([1,1,0,0], [1,0,0,0])` | `0.75` |
| Precision | `precision_score([1,1,0,0], [1,0,1,0])` | `0.5` |
| Recall | `recall_score([1,1,0,0], [1,0,1,0])` | `0.5` |
| F1 | `f1_score([1,1,0,0], [1,0,1,0])` | `0.5` |
| ROC-AUC | `roc_auc_score([1,1,0,0], [0.9,0.8,0.3,0.1])` | `1.0` because positives receive higher scores than negatives |

### Confusion Matrix

| Related Syntax | Example Code | Expected Result |
|---|---|---|
| Matrix | `cm = confusion_matrix([1,1,0,0], [1,0,1,0])`<br>`print(cm)` | `[[1 1]`<br>` [1 1]]` |
| Unpack | `tn, fp, fn, tp = cm.ravel()`<br>`print(tn, fp, fn, tp)` | `1 1 1 1` |
| Classification report | `print(classification_report(y_test, y_pred))` | Precision, Recall, F1 and support for each class |
| Plot | `ConfusionMatrixDisplay.from_predictions(y_test, y_pred)`<br>`plt.show()` | Displays the confusion matrix |

### Baseline

| Related Syntax | Example Code | Expected Result |
|---|---|---|
| Most-frequent baseline | `baseline = DummyClassifier(strategy="most_frequent")`<br>`baseline.fit(X_train, y_train)`<br>`pred = baseline.predict(X_test)` | Always predicts the most common training class |
| Why Accuracy can mislead | `y=[0,0,0,0,1]`<br>`pred=[0,0,0,0,0]` | Accuracy = `80%`, but positive-class Recall = `0%` |

### ROC Curve

| Related Syntax | Example Code | Expected Result |
|---|---|---|
| ROC points | `fpr, tpr, thresholds = roc_curve(y_test, positive_probabilities)` | FPR, TPR and thresholds |
| AUC | `auc = roc_auc_score(y_test, positive_probabilities)` | Value between 0 and 1 |
| ROC display | `RocCurveDisplay.from_predictions(y_test, positive_probabilities)`<br>`plt.show()` | Displays ROC curve |

### Decision Tree, Random Forest, SVM & k-NN

| Related Syntax | Example Code | Expected Result |
|---|---|---|
| Decision Tree | `tree = DecisionTreeClassifier(max_depth=5, random_state=42)` | Tree with maximum depth 5 |
| Random Forest | `rf = RandomForestClassifier(n_estimators=100, random_state=42)` | Forest containing 100 trees |
| SVM RBF | `svm = SVC(kernel="rbf")` | SVM with non-linear RBF kernel |
| k-NN | `knn = KNeighborsClassifier(n_neighbors=5)` | Classifier using 5 nearest neighbors |
| Fit + predict | `tree.fit(X_train, y_train)`<br>`tree_pred = tree.predict(X_test)` | Decision Tree predictions |
| Compare train/test F1 | `train_f1 = f1_score(y_train, model.predict(X_train))`<br>`test_f1 = f1_score(y_test, model.predict(X_test))` | Large gap may indicate overfitting |
| Feature importance | `pd.Series(rf.feature_importances_, index=feature_names).sort_values(ascending=False)` | Features ranked by model importance |

### Telco Cleaning

| Related Syntax | Example Code | Expected Result |
|---|---|---|
| Detect blank text | `df["TotalCharges"].astype(str).str.strip().eq("").sum()` | Number of blank `TotalCharges` values |
| Convert to numeric | `df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")` | Numeric values; invalid text becomes `NaN` |
| Drop missing `TotalCharges` | `df = df.dropna(subset=["TotalCharges"]).copy()` | Rows with invalid/missing `TotalCharges` removed |
| Remove identifier | `df = df.drop(columns="customerID")` | `customerID` no longer appears in predictive features |
| Check duplicates after ID removal | `df.duplicated().sum()` | Number of identical rows across remaining columns |

### Numeric/Categorical Preprocessing

| Related Syntax | Example Code | Expected Result |
|---|---|---|
| Numeric columns | `num = X_train.select_dtypes(include=np.number).columns.tolist()` | List of numeric feature names |
| Categorical columns | `cat = X_train.select_dtypes(exclude=np.number).columns.tolist()` | List of categorical feature names |
| One-hot encoding | `OneHotEncoder(handle_unknown="ignore")` | Converts categories into indicator columns |
| ColumnTransformer | `preprocessor = ColumnTransformer([("num", StandardScaler(), num), ("cat", OneHotEncoder(handle_unknown="ignore"), cat)])` | Numeric features are scaled; categorical features are encoded |

### Pipeline

| Related Syntax | Example Code | Expected Result |
|---|---|---|
| Build pipeline | `pipeline = Pipeline([("preprocessor", preprocessor), ("model", LogisticRegression(max_iter=1000))])` | Preprocessing and model become one workflow |
| Fit pipeline | `pipeline.fit(X_train, y_train)` | Fits preprocessing on train, then trains model |
| Predict | `pipeline.predict(X_test)` | Test data is transformed and classified automatically |
| Probability | `pipeline.predict_proba(X_test)[:,1]` | Positive-class scores |
| Access model | `pipeline.named_steps["model"]` | Fitted model inside pipeline |
| Access preprocessor | `pipeline.named_steps["preprocessor"]` | Fitted preprocessing object |

### Comparing Several Models

| Related Syntax | Example Code | Expected Result |
|---|---|---|
| Model dictionary | `models = {"Tree": DecisionTreeClassifier(), "k-NN": KNeighborsClassifier(5)}` | Models stored under readable names |
| Loop over models | `for name, model in models.items():`<br>`    model.fit(X_train, y_train)` | Every model is trained with the same workflow |
| Save metrics | `results.append({"Model":name, "F1":f1_score(y_test, y_pred)})` | Adds one result row per model |
| DataFrame | `results_df = pd.DataFrame(results).set_index("Model")` | Clean model-comparison table |
| Sort models | `results_df.sort_values("F1", ascending=False)` | Highest F1 appears first |
| Select winner | `best_model_name = results_sorted.index[0]` | Name of first-ranked model |

### Pipeline Feature Importance

| Related Syntax | Example Code | Expected Result |
|---|---|---|
| Access fitted RF | `rf_model = trained_models["Random Forest"].named_steps["model"]` | Fitted Random Forest object |
| Access fitted preprocessor | `rf_pre = trained_models["Random Forest"].named_steps["preprocessor"]` | Fitted ColumnTransformer |
| Get transformed names | `feature_names = rf_pre.get_feature_names_out()` | Names of scaled/encoded features |
| Build importance Series | `importance = pd.Series(rf_model.feature_importances_, index=feature_names)` | Importance value for every transformed feature |
| Top features | `importance.sort_values(ascending=False).head(10)` | Top 10 model-important features |

---

# Fast Reading Rule

| If you need... | Use... |
|---|---|
| The command only | Search the **Syntax** column |
| What the command means | Read **Simple English** |
| How commands work together | Find the related row in **Organized Connected Examples** |
| What the code should produce | Read **Expected Result** |
