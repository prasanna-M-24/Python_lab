import pandas as pd
import numpy as np

data = {
    "ID": [1, 2, 3, 4, 5],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, np.nan, 28, 35, 29],
    "Salary": [45000, 55000, np.nan, 52000, 58000],
    "Department": ["HR", "Finance", "IT", None, "Finance"]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("\nFill missing Age with mean:")
df["Age"].fillna(df["Age"].mean(), inplace=True)
print(df)

print("\nDrop rows with missing Salary:")
df_cleaned = df.dropna(subset=["Salary"])
print(df_cleaned)

print("\nFill missing Department with 'Unknown':")
df["Department"].fillna("Unknown", inplace=True)
print(df)

print("\nAdd new column 'Bonus' (10% of Salary):")
df["Bonus"] = df["Salary"] * 0.10
print(df)

print("\nUpdate Salary of ID=2 to 60000:")
df.loc[df["ID"] == 2, "Salary"] = 60000
print(df)

print("\nDelete column 'Bonus':")
df.drop(columns=["Bonus"], inplace=True)
print(df)