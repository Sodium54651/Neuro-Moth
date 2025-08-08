import numpy as np
# Создай массив arr из чисел от 1 до 5. Умножь все элементы на 10, затем прибавь к каждому по 3. Выведи результат.

arr = np.array([1, 2, 3, 4, 5]) * 10 + 3
print(arr)

# np.sum(), np.mean(), np.max(), np.min()
arr2 = np.array([4, 8, 15, 16, 23, 42])
print("сумма всего говнище", arr2.sum())
print("sr", np.mean(arr2))
print(arr2.max())
print(arr2.min())

arr3 = np.array([5, 10, 15, 20, 25])
print(arr3[arr3 > 15])
print(20 in arr3)

# Создай двумерный массив 2 x 3 из чисел от 1 до 6.
arr4 = np.array([[1, 2, 3], [4, 5, 5]])
print(arr4)
print(arr4[0])
print(arr4[1])

print(arr4.sum(axis=0))
print(arr4.sum(axis=1))




















