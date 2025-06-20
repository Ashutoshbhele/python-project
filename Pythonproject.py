import pandas as pd
import numpy as np

# Opening the file
df = pd.read_excel("PYTHON_EMP_PROJECT.xlsx",header=0)
print(df)

# Reading first 5 rows
print("SHOWING FIRST 5 COLUMNS AND ROWS")
print(df.head())

# Identifying NaN and Inf values and their count
print("Missing values in each column:")
print(df.isnull().sum())

# Filling missing values
df["PERFORMANCE SCORE"].fillna(df['PERFORMANCE SCORE'].mean(), inplace=True)
df["SALARY"].fillna(df['SALARY'].median(), inplace=True)

# Replacing infinite values with NaN and filling them
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.fillna(df.mean(numeric_only=True), inplace=True)


# Handling negative salary values
df['SALARY'] = np.where(df['SALARY'] < 0, df['SALARY'].mean(), df['SALARY'])

# Removing salary outliers (3 standard deviations rule)
salary_mean = df['SALARY'].mean()
salary_std = df['SALARY'].std()
lower_bound = salary_mean - (3 * salary_std)
upper_bound = salary_mean + (3 * salary_std)
df = df[(df['SALARY'] >= lower_bound) & (df['SALARY'] <= upper_bound)]

# Saving cleaned data to new Excel file
df.to_excel('cleaned_indian_employee.xlsx', index=False)
print(df)