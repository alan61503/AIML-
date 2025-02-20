import pandas as pd
import numpy as np

# Task 1: Read a CSV file and print the first and last five lines
df = pd.read_csv('sample.csv')  # Replace 'sample.csv' with your actual file
print("First five rows:\n", df.head())
print("Last five rows:\n", df.tail())

# Task 2: Create and display a one-dimensional Pandas Series
series = pd.Series([10, 20, 30, 40, 50])
print("Pandas Series:\n", series)

# Task 3: Compare elements of two Pandas Series
series1 = pd.Series([2, 4, 6, 8, 10])
series2 = pd.Series([1, 3, 5, 7, 10])
print("Equal:\n", series1 == series2)
print("Greater than:\n", series1 > series2)
print("Less than:\n", series1 < series2)

# Task 4: Select 'name' and 'score' columns from a DataFrame
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)
df_selected = df[['name', 'score']]
print("Selected Columns:\n", df_selected)

# Task 5: Count the number of rows and columns in a DataFrame
rows = df.shape[0]
columns = df.shape[1]
print(f"Number of rows: {rows}")
print(f"Number of columns: {columns}")

# Task 6: Join two DataFrames along columns
df1 = df[['name', 'score']]
df2 = df[['attempts', 'qualify']]
result = pd.concat([df1, df2], axis=1)
print("Joined DataFrame:\n", result)
