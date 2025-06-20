import pandas as pd
import numpy as np

# Opening the file
df = pd.read_excel("INDIAN_EMPLOYEE.xlsx")
print(df)

# Reading first 5 rows
print("SHOWING FIRST 5 COLUMNS AND ROWS")
print(df.head())

# Identifying NaN and Inf values and their count
print("Missing values in each column:")
print(df.isnull().sum())

# Filling missing values
df["Performance rating"].fillna(df['Performance rating'].mean(), inplace=True)
df["Salary"].fillna(df['Salary'].median(), inplace=True)

# Replacing infinite values with NaN and filling them
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.fillna(df.mean(numeric_only=True), inplace=True)
# Handling negative salary values
df["Salary"] = np.where(df["Salary"] < 0, df["Salary"].mean(), df["Salary"])

# Removing salary outliers (3 standard deviations rule)
salary_mean = df['Salary'].mean()
salary_std = df["Salary"].std()
lower_bound = salary_mean - (3 * salary_std)
upper_bound = salary_mean + (3 * salary_std)
df = df[(df["Salary"] >= lower_bound) & (df["Salary"] <= upper_bound)]

# Saving cleaned data to new Excel file
df.to_excel('cleaned_indian_employee.xlsx', index=False)
print(df)