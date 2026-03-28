import pandas as pd

data = {
    "ID": [1, 2, 3, 4, 5],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, 28, 35, 29],
    "Salary": [45000, 55000, 60000, 52000, 58000]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("\nSorting by Age (ascending):")
print(df.sort_values(by="Age"))

print("\nSorting by Salary (descending):")
print(df.sort_values(by="Salary", ascending=False))

print("\nFirst 3 rows (slicing):")
print(df[:3])

print("\nRows 2 to 4 (slicing):")
print(df[1:4])

print("\nSlicing 'Name' and 'Salary' columns:")
print(df[["Name", "Salary"]])