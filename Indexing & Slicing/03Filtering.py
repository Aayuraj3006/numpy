import numpy as np

filtering_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original Array:")
print(filtering_array)

print("\nFiltering:")

# Create a boolean mask
mask = filtering_array > 5
print("Boolean Mask:")
print(mask)

# Apply the mask
print("Filtered Array:")
print(filtering_array[mask])