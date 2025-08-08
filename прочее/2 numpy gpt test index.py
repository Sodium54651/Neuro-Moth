import numpy as np
# типо 1 задание
losos = np.array([1, 2, 3, 4, 5]) * 100

# штука 2
print(losos[0], losos[-1], losos[1:4])

# штука 3
arr2 = np.random.rand(2, 3).round(3)
print(arr2)

# штука 4 не выполняемо там нет таких циферок или значений.
# losos = 
print(arr2[arr2 <= 0.2])


