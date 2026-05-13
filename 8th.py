exp-8
Data Visualization I
1. Use the inbuilt dataset 'titanic'. The dataset contains 891 rows and contains information
about the passengers who boarded the unfortunate Titanic ship. Use the Seaborn library to
see if we can find any patterns in the data.
2. Write a code to check how the price of the ticket (column name: 'fare') for each passenger
is distributed by plotting a histogram.


import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load the inbuilt Titanic dataset
df = sns.load_dataset('titanic')

# Check the first few rows
print(df.head())

# 2. Plotting the Histogram for 'fare'
plt.figure(figsize=(10, 6))
sns.histplot(df['fare'], bins=30, kde=True, color='blue')
plt.title('Distribution of Ticket Fare')
plt.xlabel('Fare')
plt.ylabel('Frequency')
plt.show()

# Pattern Check: Let's see the count of survivors based on Class
sns.countplot(x='pclass', hue='survived', data=df)
plt.title('Survival Count by Ticket Class')
plt.show()
