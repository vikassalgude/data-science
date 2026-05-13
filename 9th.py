exp-9
Data Visualization II
1. Use the inbuilt dataset 'titanic' as used in the above problem. Plot a box plot for distribution
of age with respect to each gender along with the information about whether they survived
or not. (Column names : 'sex' and 'age')
2. Write observations on the inference from the above statistics.

import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset('titanic')

# 1. Box plot for Age vs Gender with Survival status
plt.figure(figsize=(12, 7))
sns.boxplot(x='sex', y='age', hue='survived', data=df)
plt.title('Distribution of Age by Gender and Survival')
plt.show()

# 2. Observations/Inference:
# - The median age of survivors and non-survivors is fairly similar across genders.
# - There are several outliers (dots) in the 'male' age category, representing very elderly passengers.
# - In the female category, the age spread for those who didn't survive is slightly tighter than those who did.
