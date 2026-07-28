import numpy as np

fancy_index = np.array([[1, 2],
                        [3, 4],
                        [5, 6]])

print("Original Array:")
print(fancy_index)

print("\nFancy Indexing:")

# Select rows 0 and 2
print("Rows 0 and 2:")
print(fancy_index[[0, 2]])

# Select specific elements
print("\nElements (0,1) and (2,0):")
print(fancy_index[[0, 2], [1, 0]])