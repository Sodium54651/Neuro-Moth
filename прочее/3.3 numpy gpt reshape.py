import numpy as np
# Создай одномерный массив из чисел от 1 до 12.
# Сделай из него 3 строки по 4 элемента.


losos = np.arange(1, 13)
print(losos.reshape(3, 4))

print(losos.reshape(4, -1))


losos = np.arange(1, 17)
losos = losos.reshape(4, 4)
print(losos)
losos = losos.reshape(1, -1)
print(losos)


losos = np.arange(6)
print(losos.reshape(2, -1))



losos = np.arange(12).reshape(3, 4)
print(losos)
print(losos.reshape(-1))


a = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

print(a.reshape(2, 3))



# в последнем вывеит ошибку потому что если мы попробуем поделить 10 на 3 строки он поделится не нацело
# и у нас будет остаток 1 число, и поэтому подсиськовать мы его не сможем, поэтому ошибка потому что пустого места 
# в массиве быть не может может null nill или как он здесь принято но не сегодня






