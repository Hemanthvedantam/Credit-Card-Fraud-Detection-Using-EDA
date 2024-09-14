# -*- coding: utf-8 -*-
"""Credit_Card.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1v0Qv8Ra7hij1gg2wYGsB2aMQxq4q9np6
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt


df=pd.read_csv('Credit_Card.csv')
print(df.head())
print('\n')
print(df.info())
print('\n')
print(df.tail())
print('\n')

print(df.isnull())

print(df.isnull().sum())
print('\n')


df['Class'].value_counts()
print('\n')

legal=df[df.Class==0]
fraud=df[df.Class==1]

print(legal.shape)
print(fraud.shape)
print('\n')

legal.Amount.describe()
fraud.Amount.describe()

df.groupby('Class').mean()
print('\n')

legal_sample=legal.sample(n=492)

new_df=pd.concat([legal_sample,fraud],axis=0)
print(new_df.head())
print('\n')
print(new_df.tail())

new_df['Class'].value_counts()
print('\n')
new_df.groupby('Class').mean()
print('\n')


X=new_df.drop(columns='Class',axis=1)
y=new_df['Class']
print(X)
print('\n')
print(y)
print('\n')

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=2)

print(X.shape,X_train.shape,X_test.shape)
print('\n')

model=LogisticRegression()
model.fit(X_train,y_train)

prediction=model.predict(X_train)
training_accuracy=accuracy_score(prediction,y_train)
print(training_accuracy)
print('\n')
mse=mean_squared_error(prediction,y_train)
print(mse)
print('\n')

prediction=model.predict(X_test)
testing_accuracy=accuracy_score(prediction,y_test)
mse1=mean_squared_error(prediction,y_test)
print(testing_accuracy)
print('\n')
print(mse1)
print('\n')

plt.figure(figsize=(10, 5))
sns.histplot(legal['Amount'], bins=50, color='blue', kde=True, label='Legal', stat='density')
sns.histplot(fraud['Amount'], bins=50, color='red', kde=True, label='Fraud', stat='density')
plt.legend()
plt.title('Distribution of Transaction Amounts')
plt.xlabel('Transaction Amount')
plt.ylabel('Density')
plt.show()

plt.figure(figsize=(15, 10))
correlation_matrix = new_df.corr()
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

sns.countplot(data=new_df, x='Class')
plt.title('Class Distribution')
plt.show()

plt.figure(figsize=(10, 5))
sns.boxplot(x='Class', y='Amount', data=new_df)
plt.title('Boxplot of Amount by Class')
plt.show()

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, accuracy_score

# Load the dataset
df = pd.read_csv('Credit_Card.csv')

# Initial Exploration
print("Head of the DataFrame:")
print(df.head(), '\n')

print("Info of the DataFrame:")
print(df.info(), '\n')

print("Tail of the DataFrame:")
print(df.tail(), '\n')

# Check for missing values
print("Missing values in the DataFrame:")
print(df.isnull().sum(), '\n')

# Distribution of Classes (Legal vs Fraud)
print("Class Distribution:")
print(df['Class'].value_counts(), '\n')

# Descriptive Statistics
print("Descriptive statistics for 'Legal' transactions:")
print(df[df.Class == 0]['Amount'].describe(), '\n')

print("Descriptive statistics for 'Fraud' transactions:")
print(df[df.Class == 1]['Amount'].describe(), '\n')

# Grouping by Class to compare feature means
print("Mean values grouped by Class:")
print(df.groupby('Class').mean(), '\n')

# Balancing the Dataset: Sampling from the majority class (Legal)
legal = df[df.Class == 0]
fraud = df[df.Class == 1]

legal_sample = legal.sample(n=len(fraud), random_state=42)
balanced_df = pd.concat([legal_sample, fraud])

# Shuffle the dataset
balanced_df = balanced_df.sample(frac=1, random_state=42).reset_index(drop=True)

# Checking new class distribution after balancing
print("New Class Distribution:")
print(balanced_df['Class'].value_counts(), '\n')

# Correlation Matrix (EDA)
plt.figure(figsize=(15, 10))
correlation_matrix = balanced_df.corr()
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Distribution of Transaction Amounts (EDA)
plt.figure(figsize=(10, 5))
sns.histplot(legal['Amount'], bins=50, color='blue', kde=True, label='Legal', stat='density')
sns.histplot(fraud['Amount'], bins=50, color='red', kde=True, label='Fraud', stat='density')
plt.legend()
plt.title('Distribution of Transaction Amounts')
plt.xlabel('Transaction Amount')
plt.ylabel('Density')
plt.show()

# Boxplot of Amount by Class (EDA)
plt.figure(figsize=(10, 5))
sns.boxplot(x='Class', y='Amount', data=balanced_df)
plt.title('Boxplot of Transaction Amount by Class')
plt.show()

# Class Distribution (EDA)
sns.countplot(data=balanced_df, x='Class')
plt.title('Class Distribution')
plt.show()

# Pairplot for understanding pairwise relationships between features (optional)
# sns.pairplot(balanced_df, hue='Class')
# plt.show()

# Prepare Data for Model
X = balanced_df.drop(columns='Class', axis=1)
y = balanced_df['Class']

# Splitting the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Training set shape: {X_train.shape}, Testing set shape: {X_test.shape}", '\n')

# Logistic Regression Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Model Performance on Training Set
y_train_pred = model.predict(X_train)
train_accuracy = accuracy_score(y_train, y_train_pred)
train_mse = mean_squared_error(y_train, y_train_pred)

print(f"Training Accuracy: {train_accuracy}")
print(f"Training Mean Squared Error: {train_mse}", '\n')

# Model Performance on Test Set
y_test_pred = model.predict(X_test)
test_accuracy = accuracy_score(y_test, y_test_pred)
test_mse = mean_squared_error(y_test, y_test_pred)

print(f"Testing Accuracy: {test_accuracy}")
print(f"Testing Mean Squared Error: {test_mse}", '\n')

# Confusion Matrix (Optional)
from sklearn.metrics import confusion_matrix, classification_report

conf_matrix = confusion_matrix(y_test, y_test_pred)
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap='Blues')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("True")
plt.show()

# Classification Report (Optional)
print("Classification Report:")
print(classification_report(y_test, y_test_pred))