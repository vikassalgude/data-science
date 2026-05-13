import pandas as pd
import numpy as np

# --- STEP 1: Create Dataset ---
data = {
    'Name': ['Vikas', 'Amit', 'Sita', 'John', 'Ryan'],
    'Score': [85, 92, np.nan, 78, 500], # nan is missing, 500 is an outlier
    'Study_Hours': [1, 2, 5, 10, 100]    # Highly skewed data
}
df = pd.DataFrame(data)
print("Original Data:\n", df)

# --- STEP 2: Handle Missing Values ---
# We fill the missing score with the Mean
df['Score'] = df['Score'].fillna(df['Score'].mean())

# --- STEP 3: Handle Outliers (IQR Method) ---
Q1 = df['Score'].quantile(0.25)
Q3 = df['Score'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

# Clip the outliers to the upper/lower bounds
df['Score'] = np.where(df['Score'] > upper, upper, 
              np.where(df['Score'] < lower, lower, df['Score']))

# --- STEP 4: Data Transformation ---
# Apply Log Transform to 'Study_Hours' to reduce skewness
df['Log_Study'] = np.log1p(df['Study_Hours']) 

print("\nCleaned & Transformed Data:")
print(df)
