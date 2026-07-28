import numpy as np

reshaping_array = np.array([[1, 2, 3], [4, 5, 6]])
print("Original Array:")
print(reshaping_array)

print("\nReshaping:")

# Reshape to a 1D array
print("Reshaped to 1D:")
print(reshaping_array.reshape(-1))

# Reshape to a 2D array with different dimensions
print("Reshaped to 3x2:")
print(reshaping_array.reshape(3, 2))