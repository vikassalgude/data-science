import pandas as pd

# Load dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# 1. Provide summary statistics for 'Age' grouped by 'Survived'
grouped_stats = df.groupby('Survived')['Age'].agg(['mean', 'median', 'min', 'max', 'std'])

print("--- Summary Statistics of Age Grouped by Survival ---")
print(grouped_stats)

# 2. Create a list that contains a numeric value for each response to the categorical variable
# This shows the unique categories present in the 'Survived' column
category_list = df['Survived'].unique().tolist()
print("\nList of responses in the categorical variable:", category_list)


###################
import seaborn as sns

# Load the iris dataset from seaborn library
iris = sns.load_dataset('iris')

# The problem asks for specific species: setosa, versicolor, and virginica
species_to_check = ['setosa', 'versicolor', 'virginica']

print("--- Statistical Details per Species ---")

for species in species_to_check:
    print(f"\nDetails for Species: {species}")
    # Filter the dataframe for the specific species
    specific_data = iris[iris['species'] == species]
    
    # describe() provides mean, std, min, max, and percentiles (25%, 50%, 75%)
    print(specific_data.describe())
