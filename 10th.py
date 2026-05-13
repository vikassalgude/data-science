
exp-10
Data Visualization III
Download the Iris flower dataset or any other dataset into a DataFrame. (e.g.,
https://archive.ics.uci.edu/ml/datasets/Iris ). Scan the dataset and give the inference as:
1. List down the features and their types (e.g., numeric, nominal) available in the dataset.
2. Create a histogram for each feature in the dataset to illustrate the feature distributions.
3. Create a boxplot for each feature in the dataset.
4. Compare distributions and identify outliers.


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 1. Load Iris Dataset
iris = sns.load_dataset('iris')

# List features and their types
print("Features and Types:")
print(iris.dtypes)
# Inference: sepal_length, sepal_width, petal_length, petal_width are Numeric (float).
# 'species' is Nominal (Categorical).

# 2. Histogram for each feature
iris.hist(figsize=(10, 8), bins=20, color='teal', edgecolor='black')
plt.suptitle("Feature Distributions (Histograms)")
plt.show()

# 3. Boxplot for each feature
plt.figure(figsize=(10, 6))
sns.boxplot(data=iris)
plt.title("Boxplot for each Numerical Feature")
plt.show()

# 4. Identifying Outliers
# Inference: By looking at the boxplots, 'sepal_width' is the only feature 
# that shows visible outliers (points above and below the whiskers). 
# 'petal_length' and 'petal_width' show a bimodal distribution (two peaks) 
# because of the distinct differences between species.
