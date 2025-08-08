import numpy as np
arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(arr[1])
print(arr[:, 1])
print(arr[2, 2])
print(arr[:2, :3])
print(arr[1:3, :3])
print(arr[0::2, 0::2])
print(arr[1, 1])
print(arr[::2, ::2])
print(arr[arr > 50])
print(25 in arr)