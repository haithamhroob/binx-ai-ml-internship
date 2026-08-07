BinX AI/ML Internship — Week 1, Week 2 & Week 3 Syntax Reference

Quick reference only: syntax + simple English meaning.Repeated commands are merged so the file stays useful while working.A Worked Examples section at the end groups related syntax and shows code with expected output.

1. Environment & Imports

Syntax

Simple English

python3 -m venv .venv

Create a Python virtual environment.

source .venv/bin/activate

Activate the virtual environment on Linux/Ubuntu.

pip install -r requirements.txt

Install packages from requirements.txt.

jupyter notebook

Start Jupyter Notebook.

import numpy as np

Import NumPy as np.

import pandas as pd

Import Pandas as pd.

import matplotlib.pyplot as plt

Import Matplotlib plotting tools.

import matplotlib

Import the Matplotlib package.

import seaborn as sns

Import Seaborn as sns.

import notebook

Import the Jupyter Notebook package.

np.__version__

Get NumPy version.

pd.__version__

Get Pandas version.

matplotlib.__version__

Get Matplotlib version.

notebook.__version__

Get Notebook version.

WEEK 1

2. Basic Python

Syntax

Simple English

print(value)

Print a value.

len(values)

Return the number of items.

sum(values)

Sum all items.

max(values)

Return the largest item.

min(values)

Return the smallest item.

range(4)

Generate numbers from 0 to 3.

def function_name(parameters):

Define a function.

return value

Return a result from a function.

x if condition else y

Short conditional expression.

{"key": value}

Create a dictionary.

dictionary["key"]

Access a dictionary value.

[x for x in values]

Create a list with list comprehension.

[x for x in values if condition]

Filter values with list comprehension.

for x in values:

Loop through values.

if condition:

Run code when a condition is true.

elif condition:

Check another condition.

else:

Run code when previous conditions are false.

try:

Try code that may raise an error.

except ValueError as error:

Catch a ValueError.

f"{value}"

Insert a value inside a string.

f"{value:.2f}"

Format a number to two decimal places.

OOP

Syntax

Simple English

class ClassName:

Define a class.

def __init__(self, ...):

Define the class constructor.

self.name = name

Save data inside an object.

def method(self):

Define a class method.

obj = ClassName(...)

Create an object.

obj.method()

Call an object method.

Files

Syntax

Simple English

with open("file.txt", "w") as file:

Open a file for writing.

file.write(text)

Write text to a file.

3. NumPy — Arrays

Syntax

Simple English

np.array([1, 2, 3])

Create a NumPy array.

np.array([[1, 2], [3, 4]])

Create a 2D array.

np.arange(1, 17)

Create values from 1 to 16.

array.reshape(4, 4)

Change array shape.

array.shape

Return array dimensions.

array.dtype

Return array data type.

array.T

Transpose rows and columns.

array.copy()

Create an independent copy.

np.set_printoptions(precision=2)

Control displayed decimal precision.

np.set_printoptions(precision=2, suppress=True)

Hide scientific notation for small values.

Indexing & Slicing

Syntax

Simple English

array[0]

Get the first item/row.

array[-1]

Get the last item/row.

array[:, 1]

Get the second column.

array[-1, :]

Get the last row.

array[1:4]

Slice part of an array.

array[i][j]

Access one value using two indexes.

array[i, j]

Access one value in a 2D array.

Boolean Masking

Syntax

Simple English

array > value

Create a Boolean condition.

array[array > value]

Keep values matching a condition.

array[array > array.mean()]

Keep values above the array mean.

(condition1) & (condition2)

AND between Boolean conditions.

(condition1) | (condition2)

OR between Boolean conditions.

~condition

Reverse a Boolean condition.

Broadcasting & Vectorized Operations

Syntax

Simple English

array + number

Add one number to every element.

matrix + vector

Add a vector to matrix rows using broadcasting.

array / 3.6

Divide every element without a loop.

array * value

Multiply every element without a loop.

4. NumPy — Statistics & Analysis

Syntax

Simple English

np.mean(array)

Calculate the mean.

np.median(array)

Calculate the median.

np.max(array)

Find the maximum.

np.min(array)

Find the minimum.

np.sum(array)

Sum values.

np.argmax(array)

Return the index of the largest value.

np.percentile(array, 25)

Calculate a percentile.

np.nanpercentile(array, [25, 75])

Calculate percentiles while ignoring NaN values.

np.unique(array)

Return unique values.

np.unique(array, return_counts=True)

Return unique values and their counts.

np.linalg.norm(vector)

Calculate vector magnitude.

5. NumPy — CSV Data

Syntax

Simple English

np.genfromtxt("file.csv", delimiter=",", skip_header=1)

Load numeric CSV data with NumPy.

np.delete(array, 0, axis=1)

Delete a column.

np.delete(array, 0, axis=0)

Delete a row.

Example used:

sensors_data = np.genfromtxt(
    "OBDii_data.csv",
    delimiter=",",
    skip_header=1
)

sensors_data = np.delete(sensors_data, 0, axis=1)

6. Pandas — Loading & Inspecting Data

Syntax

Simple English

pd.read_csv("file.csv")

Load a CSV file into a DataFrame.

df.head()

Show the first rows.

df.tail()

Show the last rows.

df.shape

Return rows and columns count.

df.columns

Return column names.

df.info()

Show columns, types, and missing values.

df.describe()

Show descriptive statistics.

df.select_dtypes(include="number")

Select numeric columns.

df.select_dtypes(include=["number"]).describe()

Describe numeric columns only.

df["column"]

Select one column.

df[["col1", "col2"]]

Select multiple columns.

df[columns].copy()

Select columns and make a copy.

df.loc[row, "column"]

Select by labels.

df.iloc[row, column]

Select by integer positions.

7. Pandas — Cleaning & Filtering

Syntax

Simple English

df.isnull()

Check missing values.

df.isnull().sum()

Count missing values per column.

df.isna().sum()

Count missing values per column.

df.duplicated()

Mark duplicate rows.

df.duplicated().sum()

Count duplicate rows.

df.drop_duplicates()

Remove duplicate rows.

df.drop(columns=["column"])

Remove a column.

df.dropna()

Remove rows containing missing values.

df["column"].dropna()

Remove missing values from one Series.

df["column"].fillna(value)

Replace missing values.

df[df["column"] > value]

Filter rows with a condition.

df[(condition1) & (condition2)]

Filter using AND.

df[(condition1) | (condition2)]

Filter using OR.

df["column"].notna()

Check values that are not missing.

8. Pandas — Statistics

Syntax

Simple English

series.mean()

Calculate mean.

series.median()

Calculate median.

series.std()

Calculate sample standard deviation.

series.var()

Calculate sample variance.

series.mode()

Return the mode.

series.max()

Return maximum.

series.min()

Return minimum.

series.quantile(0.25)

Calculate Q1.

series.quantile(0.75)

Calculate Q3.

series.value_counts()

Count each unique value.

series.tolist()

Convert a Series to a Python list.

df.corr()

Calculate correlations between numeric columns.

df["x"].corr(df["y"])

Calculate correlation between two Series.

IQR Pattern

q1 = df["column"].quantile(0.25)
q3 = df["column"].quantile(0.75)
iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

outliers = df[
    (df["column"] < lower) |
    (df["column"] > upper)
]

9. Pandas — Grouping

Syntax

Simple English

df.groupby("column")

Group rows by a column.

df.groupby("column")["value"].mean()

Mean for each group.

df.groupby("column")["value"].sum()

Sum for each group.

df.groupby("column").agg(...)

Apply several aggregations.

10. Matplotlib — Core Plot Syntax

Syntax

Simple English

plt.figure(figsize=(8, 5))

Create a figure with a custom size.

plt.plot(x, y)

Create a line plot.

plt.scatter(x, y)

Create a scatter plot.

plt.bar(x, y)

Create a bar chart.

plt.hist(values, bins=20)

Create a histogram.

plt.boxplot(values)

Create a box plot.

plt.xlabel("X")

Set x-axis label.

plt.ylabel("Y")

Set y-axis label.

plt.title("Title")

Set plot title.

plt.legend()

Show plot legend.

plt.grid()

Show grid lines.

plt.tight_layout()

Fix spacing between plot elements.

plt.show()

Display the plot.

Histogram Examples Used

plt.hist(data, bins=30)
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(normal, bins=30, edgecolor="black")
plt.title("Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

Pandas Multi-Histogram

df[
    ["danceability", "energy", "tempo", "loudness"]
].hist(figsize=(10, 8), bins=20)

plt.tight_layout()
plt.show()

WEEK 2

11. Random Numbers & Probability

Syntax

Simple English

np.random.seed(40)

Make random results reproducible.

np.random.uniform(1, 7, 10)

Generate uniform random decimal values.

np.random.choice(values, size)

Randomly select values.

np.random.choice(values, size, p=probabilities)

Randomly select using custom probabilities.

np.random.permutation(values)

Randomly shuffle values.

np.random.randint(1, 7, 20)

Generate random integers from 1 to 6.

np.random.rand()

Generate a random decimal from 0 to 1.

np.random.normal(mean, std, size)

Generate normally distributed values.

np.random.binomial(n, p, size)

Generate binomial experiment results.

np.mean(condition)

Calculate the proportion of True values.

Coin Flip

record1 = np.random.choice(["H", "T"], 10000)
record2 = np.random.choice(["H", "T"], 10000)

p_head = np.mean(record1 == "H")
p_tail = np.mean(record1 == "T")

Dice

dice = np.random.randint(1, 7, 10000)

p4 = np.mean(dice == 4)
not_p4 = np.mean(dice != 4)

Probability Events

A = dice % 2 == 0
B = dice > 4

pA = np.mean(A)
pB = np.mean(B)
pAB = np.mean(A & B)

p_union_formula = pA + pB - pAB
p_union_direct = np.mean(A | B)

Conditional Probability

male_students = data_frame[
    data_frame["Gender"] == "M"
]

p_passed_given_male = np.mean(
    male_students["Passed"] == 1
)

Bayes Calculation

p_male_given_passed = np.mean(
    data_frame[data_frame["Passed"] == 1]["Gender"] == "M"
)

p_passed = np.mean(data_frame["Passed"] == 1)
p_male = np.mean(data_frame["Gender"] == "M")

p_passed_given_male_bayes = (
    p_male_given_passed * p_passed / p_male
)

12. Probability Distributions

Normal Distribution

normal = np.random.normal(170, 10, 100000)

plt.figure(figsize=(8, 5))
plt.hist(normal, bins=30, edgecolor="black")
plt.show()

Uniform Distribution

uniform = np.random.uniform(0, 10, 100000)

plt.hist(uniform, bins=30, edgecolor="black")
plt.show()

Binomial Distribution

binomial = np.random.binomial(
    n=10,
    p=0.5,
    size=100000
)

plt.hist(binomial, bins=11, edgecolor="black")
plt.show()

13. Linear Algebra for ML

Vectors & Matrices

car1 = np.array([2200, 60, 88])
car2 = np.array([3100, 95, 93])
car3 = np.array([1800, 40, 84])

cars = np.array([car1, car2, car3])

Syntax

Simple English

vector.shape

Return vector shape.

matrix.shape

Return matrix shape.

matrix.T

Transpose a matrix.

np.dot(a, b)

Calculate a dot product.

a @ b

Perform matrix multiplication / dot product.

np.linalg.norm(vector)

Calculate vector magnitude.

np.linalg.det(matrix)

Calculate matrix determinant.

np.linalg.inv(matrix)

Calculate matrix inverse.

np.linalg.eig(matrix)

Calculate eigenvalues and eigenvectors.

Dot Product

weights = np.array([0.003, 0.5, 0.2])

prediction_car1 = np.dot(weights, car1)
prediction_car2 = np.dot(weights, car2)
prediction_car3 = np.dot(weights, car3)

Batch Prediction

predictions = cars @ weights

Pairwise Dot Products

print(cars.T)
print(cars @ cars.T)

Norm

sensor_energy = np.linalg.norm(car1)

Determinant, Inverse, Eigenvalues

A = np.array([
    [2, 5],
    [3, 7]
])

print(np.linalg.det(A))
print(np.linalg.inv(A))
print(np.linalg.eig(A))

Shape Error Handling

try:
    print(cars @ wrong_weights)
except ValueError as error:
    print(error)

14. EDA — Data Inspection

Syntax

Simple English

df.head()

Preview the first rows.

df.info()

Inspect types and missing values.

df.select_dtypes(include=["number"]).describe()

Describe numeric columns.

df.isnull().sum()

Count missing values.

df.duplicated().sum()

Count duplicate rows.

df["target"].value_counts()

Count target classes.

15. Seaborn — Plots Used

Count Plot

sns.countplot(x="target", data=df)
plt.title("Count plot - target")
plt.show()

Meaning: Compare category counts.

Box Plot

sns.boxplot(x=df["tempo"])
plt.title("Boxplot - tempo")
plt.show()

Meaning: Show spread and possible outliers.

Regression Plot

sns.regplot(
    data=df,
    x="energy",
    y="loudness",
    scatter_kws={"alpha": 0.5}
)

plt.title("Energy vs Loudness")
plt.show()

Meaning: Show a scatter plot with a fitted regression line.

Correlation Heatmap

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

Meaning: Visualize correlations between numeric features.

Pair Plot

sns.pairplot(df[numeric_columns])
plt.show()

Meaning: Compare several numeric features pair by pair.

16. Useful Plot Parameters

Syntax

Simple English

figsize=(10, 8)

Set figure width and height.

bins=20

Set histogram bin count.

edgecolor="black"

Draw borders around histogram bars.

alpha=0.5

Make points partly transparent.

annot=True

Write values inside heatmap cells.

fmt=".2f"

Display values with two decimal places.

cmap="coolwarm"

Set heatmap color map.

center=0

Center heatmap colors around zero.

scatter_kws={"alpha": 0.5}

Set scatter-point options inside Seaborn regplot.

REVIEW SYNTAX ADDED AFTER WEEK 2

These were added while reviewing the Week 1–2 concepts.

17. Z-Score

mean = df["order_value"].mean()
std = df["order_value"].std()

df["z_score"] = (
    df["order_value"] - mean
) / std

df["z_outlier"] = df["z_score"].abs() > 3

Syntax

Simple English

series.abs()

Return absolute values.

18. Pearson & Spearman Correlation

df[["x", "y"]].corr(method="pearson")
df[["x", "y"]].corr(method="spearman")

Syntax

Simple English

method="pearson"

Measure linear correlation.

method="spearman"

Measure rank-based monotonic correlation.

19. GroupBy Named Aggregation

result = df.groupby("customer_type").agg(
    orders=("order_value", "count"),
    total_sales=("order_value", "sum"),
    delivery_avg=("delivery_minutes", "mean"),
    max_order=("order_value", "max")
)

Pattern:

new_column=("source_column", "aggregation")

20. Pivot Table

pivot = pd.pivot_table(
    df,
    values="order_value",
    index="customer_type",
    columns="channel",
    aggfunc="sum"
)

Multiple calculations:

pivot = pd.pivot_table(
    df,
    values="order_value",
    index="customer_type",
    columns="channel",
    aggfunc=["count", "sum", "mean"]
)

21. Missing-Row Detection

df.isna().sum()

df.isna().sum().sum()

df[
    df.isna().any(axis=1)
]

Syntax

Simple English

any(axis=1)

Check whether any value is True in each row.

Quick Plot Decision Guide

Question

Plot

How is one numeric feature distributed?

Histogram

Are there outliers / how spread is the data?

Box plot

How do two numeric features relate?

Scatter plot

How does a value change over ordered/time data?

Line plot

Compare category values/counts?

Bar / Count plot

Compare many numeric relationships?

Pair plot

See correlations between many features?

Heatmap

Show a linear trend between two features?

Regplot

Fast Workflow Reminder

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

Purpose: Keep this file open beside your internship notebooks and use Ctrl + F to find syntax quickly.

WEEK 3

22. Scikit-learn — Main Imports

Syntax

Simple English

from sklearn.datasets import load_breast_cancer

Load the Breast Cancer Wisconsin dataset.

from sklearn.datasets import load_diabetes

Load the Diabetes regression dataset.

from sklearn.model_selection import train_test_split

Split data into training and test sets.

from sklearn.preprocessing import StandardScaler

Standardize numeric features.

from sklearn.preprocessing import OneHotEncoder

Convert categorical values into numeric indicator columns.

from sklearn.compose import ColumnTransformer

Apply different preprocessing to different column groups.

from sklearn.pipeline import Pipeline

Chain preprocessing and a model into one workflow.

from sklearn.linear_model import LinearRegression

Import Linear Regression.

from sklearn.linear_model import LogisticRegression

Import Logistic Regression.

from sklearn.tree import DecisionTreeClassifier

Import a Decision Tree classifier.

from sklearn.ensemble import RandomForestClassifier

Import a Random Forest classifier.

from sklearn.svm import SVC

Import Support Vector Classification.

from sklearn.neighbors import KNeighborsClassifier

Import k-Nearest Neighbors.

from sklearn.dummy import DummyClassifier

Import a simple baseline classifier.

23. Supervised Learning — Features & Target

Syntax

Simple English

X = df.drop(columns="target")

Use all columns except the target as features.

y = df["target"]

Select the target to predict.

X.shape

Check feature-matrix dimensions.

y.shape

Check target dimensions.

y.value_counts()

Count samples in each target class.

y.value_counts(normalize=True)

Return class proportions instead of counts.

(y.value_counts(normalize=True) * 100).round(2)

Show target percentages.

df["Churn"].map({"No": 0, "Yes": 1})

Encode a binary target as 0 and 1.

Example — Week 3 Classification Target

X = df.drop(columns="Churn")
y = df["Churn"].map({
    "No": 0,
    "Yes": 1
})

24. Train / Test Split

Syntax

Simple English

train_test_split(X, y, test_size=0.2, random_state=42)

Keep 20% of the data for testing with a reproducible split.

stratify=y

Preserve approximately the same target-class proportions in train and test.

X_train.shape

Check training-feature shape.

X_test.shape

Check test-feature shape.

y_train.value_counts(normalize=True)

Check class proportions in the training target.

y_test.value_counts(normalize=True)

Check class proportions in the test target.

Stratified Split Used

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

Meaning: train on one part of the data and evaluate on unseen data while preserving class proportions.

25. Scikit-learn — Core Model Workflow

Syntax

Simple English

model = Model(...)

Create a model and set its options.

model.fit(X_train, y_train)

Learn patterns from training data.

model.predict(X_test)

Predict labels or values for unseen test data.

model.score(X_test, y_test)

Return the model's default score.

General Pattern

model = Model(...)
model.fit(X_train, y_train)
predictions = model.predict(X_test)

26. Linear Regression

Syntax

Simple English

model = LinearRegression()

Create a Linear Regression model.

model.fit(X_train, y_train)

Learn coefficients and intercept from training data.

model.predict(X_test)

Predict continuous target values.

model.coef_

Return learned feature coefficients.

model.intercept_

Return the learned intercept / bias.

X_train[["bmi"]]

Select BMI as a one-feature DataFrame.

Basic Linear Regression

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print(model.coef_)
print(model.intercept_)

Linear Prediction Form

prediction = Xw + b

X = features

w = learned coefficients

b = intercept

27. Regression Metrics

Syntax

Simple English

mean_absolute_error(y_test, predictions)

Calculate MAE.

root_mean_squared_error(y_test, predictions)

Calculate RMSE directly.

np.sqrt(mean_squared_error(y_test, predictions))

Another way to calculate RMSE.

r2_score(y_test, predictions)

Calculate R².

Imports

from sklearn.metrics import (
    mean_absolute_error,
    root_mean_squared_error,
    r2_score
)

Example

mae = mean_absolute_error(y_test, predictions)
rmse = root_mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

Metric Meaning

Metric

Simple Meaning

MAE

Average absolute prediction error.

RMSE

Error measure that penalizes larger errors more strongly.

R²

How much target variation the model explains relative to a mean-based reference.

28. Regression Baseline

Syntax

Simple English

y_train.mean()

Calculate the training-target mean.

np.full(len(y_test), y_train.mean())

Predict the training mean for every test sample.

Mean Baseline Pattern

baseline_value = y_train.mean()

baseline_predictions = np.full(
    len(y_test),
    baseline_value
)

baseline_rmse = root_mean_squared_error(
    y_test,
    baseline_predictions
)

Meaning: compare Linear Regression against a simple model that always predicts the training mean.

29. Residual Analysis

Syntax

Simple English

residuals = y_test - predictions

Calculate actual minus predicted values.

plt.scatter(predictions, residuals)

Plot prediction errors against predictions.

plt.axhline(y=0, linestyle="--")

Draw the zero-error reference line.

Residual Plot

residuals = y_test - predictions

plt.figure(figsize=(8, 5))
plt.scatter(predictions, residuals, alpha=0.7)
plt.axhline(y=0, linestyle="--")

plt.xlabel("Predicted Values")
plt.ylabel("Residuals")
plt.title("Residuals vs Predicted Values")
plt.show()

30. StandardScaler — Leakage-Free Scaling

Syntax

Simple English

scaler = StandardScaler()

Create a standard scaler.

scaler.fit_transform(X_train)

Learn scaling from training data and transform training data.

scaler.transform(X_test)

Transform test data using training-set scaling only.

Pattern Used

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

Important: do not fit the scaler separately on the test set.

31. Logistic Regression

Syntax

Simple English

LogisticRegression(max_iter=1000)

Create a Logistic Regression classifier with a larger iteration limit.

model.fit(X_train_scaled, y_train)

Train the classifier.

model.predict(X_test_scaled)

Return predicted classes.

model.predict_proba(X_test_scaled)

Return class probabilities.

probabilities[:, 1]

Get probability of the positive class.

model.coef_

Return learned feature coefficients.

model.intercept_

Return the intercept.

Example

model = LogisticRegression(max_iter=1000)

model.fit(X_train_scaled, y_train)

predictions = model.predict(X_test_scaled)
probabilities = model.predict_proba(X_test_scaled)

positive_probabilities = probabilities[:, 1]

32. predict() vs predict_proba()

Syntax

Simple English

model.predict(X_test)

Return final predicted classes such as 0 or 1.

model.predict_proba(X_test)

Return probability for each class.

model.predict_proba(X_test)[:, 1]

Return only positive-class probabilities.

Example probability row:

[P(class 0), P(class 1)]

33. Classification Metrics

Imports

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)

Syntax

Simple English

accuracy_score(y_test, y_pred)

Fraction of all predictions that are correct.

precision_score(y_test, y_pred)

Of predicted positives, how many are actually positive.

recall_score(y_test, y_pred)

Of actual positives, how many the model found.

f1_score(y_test, y_pred)

Balance Precision and Recall in one score.

roc_auc_score(y_test, y_score)

Measure how well scores separate the two classes across thresholds.

zero_division=0

Return 0 instead of a division warning when a metric denominator is zero.

Example

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

34. Quick Classification Metric Guide

Metric

Main Question

Accuracy

How many total predictions were correct?

Precision

Of everything predicted Positive, how much was really Positive?

Recall

Of all real Positive cases, how many were found?

F1-score

Is there a good balance between Precision and Recall?

ROC-AUC

Does the model generally give Positive cases higher scores than Negative cases across thresholds?

Confusion-Matrix Terms

Term

Meaning

TP

Predicted Positive and actually Positive.

TN

Predicted Negative and actually Negative.

FP

Predicted Positive but actually Negative.

FN

Predicted Negative but actually Positive.

35. Confusion Matrix

Imports

from sklearn.metrics import (
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report
)

Syntax

Simple English

confusion_matrix(y_test, y_pred)

Return TN, FP, FN, TP counts.

cm.ravel()

Unpack a 2×2 confusion matrix into four values.

classification_report(y_test, y_pred)

Show Precision, Recall, F1, and support.

ConfusionMatrixDisplay.from_predictions(...)

Build and display a confusion matrix directly from predictions.

ConfusionMatrixDisplay(confusion_matrix=cm).plot()

Plot an already calculated confusion matrix.

Example

cm = confusion_matrix(y_test, predictions)

tn, fp, fn, tp = cm.ravel()

print("TN:", tn)
print("FP:", fp)
print("FN:", fn)
print("TP:", tp)

ConfusionMatrixDisplay.from_predictions(
    y_test,
    predictions,
    display_labels=["Benign", "Malignant"]
)

plt.show()

36. Classification Report

print(
    classification_report(
        y_test,
        predictions
    )
)

With custom class names:

print(
    classification_report(
        y_test,
        y_pred,
        target_names=["Stay", "Churn"]
    )
)

Meaning: display Precision, Recall, F1-score, and support for each class.

37. DummyClassifier — Classification Baseline

Syntax

Simple English

DummyClassifier(strategy="most_frequent")

Always predict the most common training class.

baseline.fit(X_train, y_train)

Fit the simple baseline.

baseline.predict(X_test)

Generate baseline predictions.

baseline.predict_proba(X_test)[:, 1]

Return baseline positive-class probability.

Example

baseline = DummyClassifier(
    strategy="most_frequent"
)

baseline.fit(X_train, y_train)

baseline_predictions = baseline.predict(X_test)

Meaning: check whether the real model beats a naive strategy.

38. ROC Curve & ROC-AUC

Imports

from sklearn.metrics import (
    roc_curve,
    roc_auc_score,
    RocCurveDisplay
)

Syntax

Simple English

roc_curve(y_test, positive_probabilities)

Calculate ROC points across thresholds.

roc_auc_score(y_test, positive_probabilities)

Calculate area under the ROC curve.

RocCurveDisplay.from_predictions(y_test, y_score)

Plot an ROC curve directly from actual labels and scores.

ROC Pattern

fpr, tpr, thresholds = roc_curve(
    y_test,
    positive_probabilities
)

auc = roc_auc_score(
    y_test,
    positive_probabilities
)

Plot Pattern

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

Quick meaning: AUC closer to 1 means stronger class separation; around 0.5 is close to random ranking.

39. Decision Tree

Syntax

Simple English

DecisionTreeClassifier(random_state=42)

Create a reproducible Decision Tree.

DecisionTreeClassifier(max_depth=5, random_state=42)

Limit tree depth to reduce complexity.

model.fit(X_train, y_train)

Train the tree.

model.predict(X_test)

Predict test classes.

Example

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

40. Decision Tree Visualization

from sklearn.tree import plot_tree

plt.figure(figsize=(18, 8))

plot_tree(
    tree_model,
    max_depth=2,
    filled=True,
    feature_names=feature_names,
    class_names=class_names
)

plt.show()

Parameter

Simple English

max_depth=2

Display only the first tree levels.

filled=True

Color the tree nodes.

feature_names=...

Show feature names in the nodes.

class_names=...

Show class names.

41. Train vs Test Score — Overfitting Check

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

Meaning: a large gap between training and test performance can indicate overfitting.

42. Random Forest

Syntax

Simple English

RandomForestClassifier(n_estimators=100, random_state=42)

Build a forest containing 100 trees.

model.feature_importances_

Return model-based feature importance values.

Example

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

43. Random Forest Feature Importance

feature_importance = pd.Series(
    rf_model.feature_importances_,
    index=feature_names
)

feature_importance = (
    feature_importance
    .sort_values(ascending=False)
)

top_features = (
    feature_importance
    .head(10)
)

Meaning: rank features by how useful they were to the fitted Random Forest.

44. Support Vector Machine — SVM

Syntax

Simple English

SVC(kernel="linear")

Use a linear SVM boundary.

SVC(kernel="rbf")

Use the RBF kernel for a non-linear boundary.

SVC(kernel="rbf", probability=True)

Enable probability estimates for predict_proba().

Examples

linear_svm = SVC(
    kernel="linear"
)

rbf_svm = SVC(
    kernel="rbf"
)

Week 3 mini-project pattern:

svm = SVC(
    kernel="rbf",
    probability=True,
    random_state=42
)

Important: SVM was evaluated after feature scaling.

45. k-Nearest Neighbors — k-NN

Syntax

Simple English

KNeighborsClassifier(n_neighbors=5)

Classify using the 5 nearest training samples.

n_neighbors=k

Set the value of k.

Basic Example

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

Testing Several k Values

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

46. Cleaning TotalCharges in the Telco Dataset

Syntax

Simple English

series.astype(str)

Convert values to strings.

series.str.strip()

Remove spaces around strings.

series.eq("")

Check which values are empty strings.

pd.to_numeric(series, errors="coerce")

Convert values to numeric and turn invalid values into NaN.

df.dropna(subset=["TotalCharges"])

Remove rows where TotalCharges is missing.

Blank-Value Check

blank_total_charges = (
    df["TotalCharges"]
    .astype(str)
    .str.strip()
    .eq("")
    .sum()
)

Conversion & Cleaning

df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

df = df.dropna(
    subset=["TotalCharges"]
).copy()

47. Removing an Identifier

df = df.drop(
    columns="customerID"
)

"customerID" not in df.columns

Meaning: remove a unique identifier that should not be used as a predictive feature.

48. Churn EDA Patterns

Numeric Summary

numeric_summary = df[
    [
        "SeniorCitizen",
        "tenure",
        "MonthlyCharges",
        "TotalCharges"
    ]
].describe().round(2)

Grouped Medians

df.groupby("Churn")[
    [
        "tenure",
        "MonthlyCharges",
        "TotalCharges"
    ]
].median().round(2)

Churn Rate by Category

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

Pandas Bar Plot

contract_churn.plot(
    kind="bar"
)

plt.ylabel("Churn Rate (%)")
plt.show()

49. Selecting Numeric & Categorical Features

Syntax

Simple English

X_train.select_dtypes(include=np.number)

Select numeric training columns.

X_train.select_dtypes(exclude=np.number)

Select non-numeric / categorical training columns.

.columns.tolist()

Convert column names to a Python list.

Pattern Used

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

50. One-Hot Encoding

OneHotEncoder(
    handle_unknown="ignore"
)

Meaning: convert categorical values into numeric indicator columns and safely handle categories not seen during fitting.

51. ColumnTransformer

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

Meaning:

scale numeric features,

one-hot encode categorical features,

keep both transformations in one preprocessing object.

52. Scikit-learn Pipeline

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

Syntax

Simple English

pipeline.fit(X_train, y_train)

Fit preprocessing and the model using training data.

pipeline.predict(X_test)

Apply learned preprocessing and predict test classes.

pipeline.predict_proba(X_test)[:, 1]

Return positive-class probabilities after pipeline preprocessing.

pipeline.named_steps["model"]

Access the fitted model inside the pipeline.

pipeline.named_steps["preprocessor"]

Access the fitted preprocessor inside the pipeline.

Main benefit: preprocessing is learned during training and is not fitted on the test set.

53. Dictionary of Models

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

Meaning: store several models under readable names so they can be trained with the same workflow.

54. Training Several Models with One Loop

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

Meaning: train every model using the same preprocessing and the same train/test split.

55. Saving Model Metrics in a List

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

56. Model Comparison DataFrame

results_df = (
    pd.DataFrame(results)
    .set_index("Model")
)

results_sorted = (
    results_df
    .sort_values(
        ["F1-score", "Recall"],
        ascending=False
    )
)

results_sorted.round(4)

Syntax

Simple English

pd.DataFrame(results)

Convert model-result dictionaries into a table.

.set_index("Model")

Use model names as row labels.

.sort_values(["F1-score", "Recall"], ascending=False)

Rank models by F1 first, then Recall.

.round(4)

Display four decimal places.

57. Selecting the Best Model from Results

best_model_name = (
    results_sorted.index[0]
)

best_metrics = results_df.loc[
    best_model_name
]

selected_model = trained_models[
    best_model_name
]

Meaning: use the first model in the sorted comparison table instead of manually hard-coding a winner.

58. ROC Curves for Several Models

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

59. Accessing Pipeline Steps

rf_pipeline = trained_models[
    "Random Forest"
]

rf_preprocessor = rf_pipeline.named_steps[
    "preprocessor"
]

rf_model = rf_pipeline.named_steps[
    "model"
]

Meaning: access fitted objects stored inside a trained pipeline.

60. Feature Names After One-Hot Encoding

feature_names = (
    rf_preprocessor
    .get_feature_names_out()
)

feature_names = [
    name
    .replace("num__", "")
    .replace("cat__", "")

    for name in feature_names
]

Meaning: retrieve transformed feature names and remove transformer prefixes.

61. Feature Importance After a Pipeline

feature_importance = pd.Series(
    rf_model.feature_importances_,
    index=feature_names,
    name="Importance"
)

feature_importance = (
    feature_importance
    .sort_values(
        ascending=False
    )
)

top_features = (
    feature_importance
    .head(10)
    .to_frame()
)

62. Horizontal Feature-Importance Plot

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

63. IPython Display

Syntax

Simple English

display(value)

Display an object nicely inside Jupyter.

display(df.round(4))

Display a formatted DataFrame.

Markdown(text)

Convert a string into rendered Markdown.

display(Markdown(text))

Render generated Markdown inside a notebook.

Import

from IPython.display import (
    display,
    Markdown
)

Week 3 Model Decision Guide

Situation

Useful Metric / Idea

Regression — easy average error

MAE

Regression — large errors should matter more

RMSE

Regression — explained variation

R²

Classification — overall correct predictions

Accuracy

Predicted positives must be reliable

Precision

Missing real positives is expensive

Recall

Need Precision/Recall balance

F1-score

Compare class separation across thresholds

ROC-AUC

Check whether a model adds value

Compare with a baseline

Check possible overfitting

Compare train vs test performance

SVM / k-NN use distance or geometry

Scaling is important

Tree / Random Forest

Scaling is normally not required

Mixed numeric + categorical columns

ColumnTransformer + Pipeline

Week 3 Fast Workflow Reminder

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

Week 3 focus: supervised learning, train/test discipline, regression, classification, model comparison, leakage-free preprocessing, meaningful metrics, and a complete end-to-end ML pipeline.

WORKED EXAMPLES — RELATED SYNTAX GROUPS

This section groups related syntax into short examples.Each example shows code + expected output so the syntax is easier to connect while reviewing.

Example 1 — Basic Python: List + Loop + Condition + Dictionary + f-string

scores = [78, 91, 65, 88]

result = {
    "passed": 0,
    "failed": 0
}

for score in scores:
    if score >= 70:
        result["passed"] += 1
    else:
        result["failed"] += 1

print(result)
print(f"Highest score: {max(scores)}")

Output:

{'passed': 3, 'failed': 1}
Highest score: 91

Syntax connected: list, dictionary, for, if/else, indexing, max(), f-string.

Example 2 — NumPy: Array + Shape + Reshape + Slicing + Boolean Masking + Mean

import numpy as np

values = np.array([10, 20, 30, 40, 50, 60])

matrix = values.reshape(2, 3)

print(matrix)
print("Shape:", matrix.shape)
print("Second column:", matrix[:, 1])
print("Above mean:", values[values > values.mean()])

Output:

[[10 20 30]
 [40 50 60]]
Shape: (2, 3)
Second column: [20 50]
Above mean: [40 50 60]

Syntax connected: np.array(), .reshape(), .shape, slicing, Boolean masking, .mean().

Example 3 — NumPy Statistics: Mean + Median + Percentile + Unique Counts

data = np.array([2, 2, 3, 4, 4, 4, 8])

print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Q1:", np.percentile(data, 25))

values, counts = np.unique(
    data,
    return_counts=True
)

print("Values:", values)
print("Counts:", counts)

Output:

Mean: 3.857142857142857
Median: 4.0
Q1: 2.5
Values: [2 3 4 8]
Counts: [2 1 3 1]

Syntax connected: np.mean(), np.median(), np.percentile(), np.unique(..., return_counts=True).

Example 4 — Pandas: DataFrame + Inspect + Missing Values + Duplicates + Cleaning

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "speed": [40, 50, np.nan, 50],
    "rpm": [1500, 2000, 2200, 2000]
})

print(df.shape)
print(df.isna().sum())
print("Duplicates:", df.duplicated().sum())

clean_df = df.dropna()

print(clean_df)

Output:

(4, 2)

speed    1
rpm      0
dtype: int64

Duplicates: 1

   speed   rpm
0   40.0  1500
1   50.0  2000
3   50.0  2000

Syntax connected: pd.DataFrame(), .shape, .isna().sum(), .duplicated().sum(), .dropna().

Example 5 — Pandas Statistics + Filtering + GroupBy

df = pd.DataFrame({
    "type": ["A", "A", "B", "B"],
    "value": [10, 20, 30, 40]
})

print("Mean:", df["value"].mean())

high_values = df[
    df["value"] > 20
]

print(high_values)

grouped = df.groupby("type")["value"].mean()

print(grouped)

Output:

Mean: 25.0

  type  value
2    B     30
3    B     40

type
A    15.0
B    35.0
Name: value, dtype: float64

Syntax connected: column selection, .mean(), filtering, groupby(), grouped aggregation.

Example 6 — IQR: Detecting Outliers

values = pd.Series(
    [10, 11, 12, 12, 13, 14, 50]
)

q1 = values.quantile(0.25)
q3 = values.quantile(0.75)

iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

outliers = values[
    (values < lower) |
    (values > upper)
]

print("Q1:", q1)
print("Q3:", q3)
print("Outliers:", outliers.tolist())

Output:

Q1: 11.5
Q3: 13.5
Outliers: [50]

Syntax connected: .quantile(), IQR, Boolean conditions, filtering, .tolist().

Example 7 — Plotting: Figure + Histogram + Labels + Show

import matplotlib.pyplot as plt

data = [2, 3, 3, 4, 5, 5, 5, 6]

plt.figure(
    figsize=(6, 4)
)

plt.hist(
    data,
    bins=5
)

plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Simple Distribution")

plt.show()

Output:

A histogram figure is displayed.

Syntax connected: plt.figure(), plt.hist(), labels, title, plt.show().

Example 8 — Probability Simulation: Random Choice + Seed + Proportion

np.random.seed(40)

coin = np.random.choice(
    ["H", "T"],
    size=10
)

print(coin)

p_head = np.mean(
    coin == "H"
)

print("P(H):", p_head)

Output:

['H' 'T' 'T' 'H' 'H' 'H' 'H' 'T' 'T' 'H']
P(H): 0.6

Syntax connected: np.random.seed(), np.random.choice(), Boolean comparison, np.mean() as a probability.

Example 9 — Linear Algebra: Matrix + Dot Product + Batch Prediction

cars = np.array([
    [1000, 50],
    [1500, 70],
    [2000, 90]
])

weights = np.array([
    0.01,
    0.5
])

predictions = cars @ weights

print("Shape:", cars.shape)
print("Predictions:", predictions)

Output:

Shape: (3, 2)
Predictions: [35. 50. 65.]

Syntax connected: 2D arrays, .shape, matrix multiplication @, batch predictions.

Example 10 — Train/Test Split + Stratify

from sklearn.model_selection import train_test_split

X = pd.DataFrame({
    "feature": range(10)
})

y = pd.Series(
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Train shape:", X_train.shape)
print("Test shape:", X_test.shape)

print(
    "Train class proportions:",
    y_train.value_counts(
        normalize=True
    ).sort_index().round(2).to_dict()
)

print(
    "Test class proportions:",
    y_test.value_counts(
        normalize=True
    ).sort_index().round(2).to_dict()
)

Output:

Train shape: (8, 1)
Test shape: (2, 1)
Train class proportions: {0: 0.62, 1: 0.38}
Test class proportions: {0: 0.5, 1: 0.5}

With very small datasets, exact proportions cannot always match perfectly.stratify=y keeps them as close as the split size allows.

Syntax connected: train_test_split(), test_size, random_state, stratify.

Example 11 — Linear Regression: Fit + Predict + Coefficient + Intercept

from sklearn.linear_model import LinearRegression

X = np.array([
    [1],
    [2],
    [3],
    [4]
])

y = np.array([
    3,
    5,
    7,
    9
])

model = LinearRegression()

model.fit(
    X,
    y
)

prediction = model.predict(
    [[5]]
)

print("Coefficient:", model.coef_)
print("Intercept:", model.intercept_)
print("Prediction for x=5:", prediction)

Output:

Coefficient: [2.]
Intercept: 1.0
Prediction for x=5: [11.]

Meaning: the learned relationship is approximately:

y = 2x + 1

Syntax connected: LinearRegression(), .fit(), .predict(), .coef_, .intercept_.

Example 12 — Regression Metrics: MAE + RMSE + R²

from sklearn.metrics import (
    mean_absolute_error,
    root_mean_squared_error,
    r2_score
)

actual = np.array([
    10,
    20,
    30,
    40
])

predicted = np.array([
    12,
    18,
    33,
    37
])

print(
    "MAE:",
    mean_absolute_error(
        actual,
        predicted
    )
)

print(
    "RMSE:",
    root_mean_squared_error(
        actual,
        predicted
    )
)

print(
    "R2:",
    r2_score(
        actual,
        predicted
    )
)

Output:

MAE: 2.5
RMSE: 2.5495097567963922
R2: 0.948

Syntax connected: MAE, RMSE, R².

Example 13 — Scaling: fit_transform() on Train + transform() on Test

from sklearn.preprocessing import StandardScaler

X_train = np.array([
    [10],
    [20],
    [30]
])

X_test = np.array([
    [40]
])

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(
    X_train
)

X_test_scaled = scaler.transform(
    X_test
)

print(
    np.round(
        X_train_scaled,
        2
    )
)

print(
    np.round(
        X_test_scaled,
        2
    )
)

Output:

[[-1.22]
 [ 0.  ]
 [ 1.22]]

[[2.45]]

Syntax connected: StandardScaler(), .fit_transform(), .transform(), leakage-free preprocessing.

Example 14 — Classification Metrics + Confusion Matrix

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

y_true = np.array([
    1, 1, 1, 1,
    0, 0, 0, 0,
    0, 0
])

y_pred = np.array([
    1, 1, 1, 0,
    1, 0, 0, 0,
    0, 0
])

print(
    "Accuracy:",
    accuracy_score(
        y_true,
        y_pred
    )
)

print(
    "Precision:",
    precision_score(
        y_true,
        y_pred
    )
)

print(
    "Recall:",
    recall_score(
        y_true,
        y_pred
    )
)

print(
    "F1:",
    f1_score(
        y_true,
        y_pred
    )
)

print(
    confusion_matrix(
        y_true,
        y_pred
    )
)

Output:

Accuracy: 0.8
Precision: 0.75
Recall: 0.75
F1: 0.75

[[5 1]
 [1 3]]

The matrix means:

TN = 5
FP = 1
FN = 1
TP = 3

Syntax connected: Accuracy, Precision, Recall, F1, confusion matrix.

Example 15 — predict_proba() + ROC-AUC

from sklearn.metrics import roc_auc_score

y_true = np.array([
    1,
    1,
    0,
    0
])

positive_scores = np.array([
    0.90,
    0.75,
    0.40,
    0.10
])

auc = roc_auc_score(
    y_true,
    positive_scores
)

print("ROC-AUC:", auc)

Output:

ROC-AUC: 1.0

Meaning: every Positive sample received a higher score than every Negative sample in this small example.

Syntax connected: positive-class scores and roc_auc_score().

Example 16 — Baseline: High Accuracy Can Still Be Useless

from sklearn.dummy import DummyClassifier
from sklearn.metrics import (
    accuracy_score,
    recall_score
)

X = np.arange(10).reshape(-1, 1)

y = np.array([
    0, 0, 0, 0, 0,
    0, 0, 0, 1, 1
])

baseline = DummyClassifier(
    strategy="most_frequent"
)

baseline.fit(
    X,
    y
)

predictions = baseline.predict(
    X
)

print(
    "Accuracy:",
    accuracy_score(
        y,
        predictions
    )
)

print(
    "Recall:",
    recall_score(
        y,
        predictions
    )
)

Output:

Accuracy: 0.8
Recall: 0.0

Meaning: the baseline gets 80% Accuracy by always predicting class 0, but it detects none of the actual Positive cases.

Syntax connected: DummyClassifier, Accuracy, Recall, imbalanced-data interpretation.

Example 17 — Decision Tree + Random Forest + SVM + k-NN

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

models = {
    "Tree": DecisionTreeClassifier(
        max_depth=3,
        random_state=42
    ),

    "Forest": RandomForestClassifier(
        n_estimators=50,
        random_state=42
    ),

    "SVM": SVC(
        kernel="rbf"
    ),

    "k-NN": KNeighborsClassifier(
        n_neighbors=3
    )
}

for name, model in models.items():
    print(
        name,
        "->",
        type(model).__name__
    )

Output:

Tree -> DecisionTreeClassifier
Forest -> RandomForestClassifier
SVM -> SVC
k-NN -> KNeighborsClassifier

Syntax connected: model creation and model dictionaries.

Example 18 — Telco Cleaning: Blank Strings + Numeric Conversion + Drop Missing + Remove ID

df = pd.DataFrame({
    "customerID": [
        "A1",
        "A2",
        "A3"
    ],
    "TotalCharges": [
        "100.5",
        " ",
        "250.0"
    ],
    "Churn": [
        "No",
        "Yes",
        "No"
    ]
})

print(
    "Missing before conversion:",
    df["TotalCharges"]
      .isna()
      .sum()
)

df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

print(
    "Missing after conversion:",
    df["TotalCharges"]
      .isna()
      .sum()
)

df = df.dropna(
    subset=["TotalCharges"]
).copy()

df = df.drop(
    columns="customerID"
)

print(df)

Output:

Missing before conversion: 0
Missing after conversion: 1

   TotalCharges Churn
0         100.5    No
2         250.0    No

Syntax connected: .isna(), pd.to_numeric(errors="coerce"), .dropna(), .copy(), .drop(columns=...).

Example 19 — ColumnTransformer + Pipeline

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import (
    StandardScaler,
    OneHotEncoder
)
from sklearn.linear_model import LogisticRegression

numeric_features = [
    "tenure",
    "MonthlyCharges"
]

categorical_features = [
    "Contract"
]

preprocessor = ColumnTransformer(
    transformers=[
        (
            "num",
            StandardScaler(),
            numeric_features
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

pipeline = Pipeline([
    (
        "preprocessor",
        preprocessor
    ),
    (
        "model",
        LogisticRegression(
            max_iter=1000
        )
    )
])

print(
    pipeline.steps
)

Output:

[
  ('preprocessor', ColumnTransformer(...)),
  ('model', LogisticRegression(...))
]

Meaning: numeric scaling, categorical encoding, and the classifier are connected into one workflow.

Syntax connected: ColumnTransformer, OneHotEncoder, StandardScaler, Pipeline.

Example 20 — Model Comparison Table

results = [
    {
        "Model": "Model A",
        "Accuracy": 0.82,
        "Recall": 0.60,
        "F1-score": 0.64
    },
    {
        "Model": "Model B",
        "Accuracy": 0.79,
        "Recall": 0.68,
        "F1-score": 0.67
    }
]

results_df = (
    pd.DataFrame(results)
    .set_index("Model")
)

results_sorted = results_df.sort_values(
    ["F1-score", "Recall"],
    ascending=False
)

print(results_sorted)

Output:

         Accuracy  Recall  F1-score
Model
Model B      0.79    0.68      0.67
Model A      0.82    0.60      0.64

Meaning: the model with the highest Accuracy is not automatically the model selected when F1/Recall are more important.

Syntax connected: list of dictionaries, pd.DataFrame(), .set_index(), .sort_values().

How to Use the Examples

When you forget a command:

1. Ctrl + F the syntax.
2. Read the one-line meaning in the reference table.
3. Find the related worked example.
4. Read the code.
5. Predict the output yourself.
6. Check the shown output.

This keeps the file useful as both a syntax reference and a fast revision sheet.