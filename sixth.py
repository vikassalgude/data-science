exp-6
Data Analytics III
1. Implement Simple Naïve Bayes classification algorithm using Python/R on iris.csv dataset.
2. Compute Confusion matrix to find TP, FP, TN, FN, Accuracy, Error rate, Precision, Recall
on the given dataset.


import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

# 1. Load Dataset
iris = sns.load_dataset('iris')

# 2. Features and Target
# X contains measurements, y contains the species names
X = iris.drop('species', axis=1)
y = iris['species']

# 3. Split data (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train Naïve Bayes Model
# We use GaussianNB because our features are continuous numbers
model = GaussianNB()
model.fit(X_train, y_train)

# 5. Prediction
y_pred = model.predict(X_test)

# 6. Compute Confusion Matrix and Metrics
cm = confusion_matrix(y_test, y_pred)

# Note: Since Iris has 3 classes, CM is 3x3. 
# For multi-class, we calculate macro-averaged precision/recall.
accuracy = accuracy_score(y_test, y_pred)
error_rate = 1 - accuracy
precision = precision_score(y_test, y_pred, average='macro')
recall = recall_score(y_test, y_pred, average='macro')

print("--- Confusion Matrix (3x3 for 3 species) ---")
print(cm)

print(f"\n--- Performance Metrics ---")
print(f"Accuracy: {accuracy:.2f}")
print(f"Error Rate: {error_rate:.2f}")
print(f"Precision (Macro): {precision:.2f}")
print(f"Recall (Macro): {recall:.2f}")

# To show individual TP, FP, TN, FN for a specific class (e.g., Setosa)
# We can explain this logic to the examiner
