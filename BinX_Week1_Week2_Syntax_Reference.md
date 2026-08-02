# BinX AI/ML Internship — Week 1 & Week 2 Syntax Reference

> Quick reference only: **syntax + simple English meaning**.  
> Repeated commands are merged so the file stays useful while working.

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

**Purpose:** Keep this file open beside your Week 3 notebooks and use `Ctrl + F` to find syntax quickly.
