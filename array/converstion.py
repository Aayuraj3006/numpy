import numpy as np

arr_warehouse = np.array([[1, 2, 3], [4, 5, 6]])
print("Array works:", arr_warehouse.shape)
print("Array works:", arr_warehouse.dtype)
int_arr = arr_warehouse.astype(float)
print("Array warehouse:", int_arr)
print("Array works:", int_arr.dtype)
