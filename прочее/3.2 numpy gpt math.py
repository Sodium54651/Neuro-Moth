import numpy as np
# 1. Создай два массива:
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

# 2. Выполни и выведи:
# a) Сумму a + b
# b) Разность a - b
# c) Произведение a * b
# d) Деление a / b
print(a + b)
print(a - b)
print(a * b)
print(a / b)

# 3. Возьми массив c и:
c = np.array([5, 10, 15, 20, 25])
print(c ** 2)
print(c ** 0.5)
print(c * np.pi)
# a) Возведи все элементы в квадрат
# b) Вычисли корень квадратный из всех элементов
# c) Умножь все элементы на π (используй np.pi)



a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print(a + b)
print(a - b)
print(a * b)
print()
print(a @ b)
print(a.T)
print(np.linalg.det(a))
# a) Сумму матриц a + b
# b) Разность a - b
# c) Поэлементное произведение a * b
# d) Матричное умножение (np.dot(a, b) или a @ b)
# e) Транспонированную матрицу a.T
# f) Определитель np.linalg.det(a)

