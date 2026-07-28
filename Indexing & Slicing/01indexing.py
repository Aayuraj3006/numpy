import numpy as np

arr = np.array([[1, 2, 3, 4,5, 6, 7, 8, 9, 10]])

print("Original Array:")
print(arr)

# Access first row
print("\nFirst row:", arr[0])

# Access element at row 0, column 3
print("Element at index (0,3):", arr[0, 3])

print("\nSlicing")

# Columns 3 to 5
print("Columns 3:6 ->", arr[0, 3:6])

# First five columns
print("Columns :5 ->", arr[0, :5])

# Columns from index 3 onward
print("Columns 3: ->", arr[0, 3:])

# Entire row
print("Entire row ->", arr[0, :])

# Reverse the row
print("Reverse ->", arr[0, ::-1])