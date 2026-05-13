# ==========================================
# 1. Import required Python Libraries
# ==========================================
import pandas as pd
import numpy as np

# ==========================================
# 2 & 3. Locate and Load Dataset
# Source: https://www.kaggle.com/c/titanic/data
# ==========================================
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)
print("--- Step 3: Dataset Loaded ---")
print(df.head())

# ==========================================
# 4. Data Preprocessing
# ==========================================
print("\n--- Step 4: Data Preprocessing ---")
print("Dimensions (Rows, Cols):", df.shape)

# Check for missing values
print("\nMissing Values per column:\n", df.isnull().sum())

# Initial statistics
print("\nSummary Statistics:\n", df.describe())

# ==========================================
# 5. Data Formatting and Normalization
# ==========================================
print("\n--- Step 5: Formatting & Normalization ---")

# Check current types
print("Initial Data Types:\n", df.dtypes)

# Type Conversion: Changing Pclass to category for better logical grouping
df['Pclass'] = df['Pclass'].astype('category')

# Normalization: Scaling the 'Fare' column (Min-Max Scaling)
# This scales values to be between 0 and 1
df['Fare'] = (df['Fare'] - df['Fare'].min()) / (df['Fare'].max() - df['Fare'].min())

print("\nUpdated Fare column (First 5 rows):\n", df['Fare'].head())

# ==========================================
# 6. Categorical to Quantitative
# ==========================================
print("\n--- Step 6: Categorical to Quantitative ---")

# Convert 'Sex' into a dummy variable (0 or 1)
# drop_first=True prevents redundant data (the dummy variable trap)
df = pd.get_dummies(df, columns=['Sex'], drop_first=True)

print("\nFinal Dataframe Sample (Note the Sex_male column):")
print(df[['Name', 'Sex_male', 'Fare', 'Pclass']].head())
