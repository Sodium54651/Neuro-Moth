import numpy as np

# def finall(losos):
#     los = [1]
#     # los = ((losos[rh] / maxData[rh]) for rh in range())
#     for rh in range(len(losos)):
#         los.append(losos[rh] / maxData[rh + 1])
#     return np.sum(w * los)



# def writeData(w, maxData):
#     GradsText = np.array(["двоешник", "троешник", "четвёрошник", "пятёрошник", "неизвестная ошибка"])
#     UData = np.array([int(input("Оценки за домашку: ")), 
#                      int(input("Активность: ")), 
#                      int(input("Пропуски: "))
#                      ])
#     UData = np.array([90, 5, 2])
#     UData = UData / maxData
#     UData = np.insert(UData, 0, 1)
#     print(w)
#     UData = w.flatten() @ UData

#     UData = round(UData.item(), 3)
#     if UData < 3.0 and UData > 1.9: print(GradsText[0])
#     elif UData < 3.5: print(GradsText[1])
#     elif UData < 4.5: print(GradsText[2])
#     elif UData < 5.1: print(GradsText[3])
#     else: print(GradsText[4])

#     return UData


# Домашка | Активность | Пропуски | Оценка (с шумами)
Data = np.array([
    [90, 9, 1, 5],
    [30, 1, 10, 2],
    [75, 6, 3, 4],
    [100, 8, 0, 5],
    [55, 4, 7, 3],
    [40, 2, 8, 5],     # ← Шум? Хм...
    [80, 5, 2, 4],
    [95, 9, 0, 5],
    [20, 0, 9, 4],     # ← Ну такое...
    [65, 5, 4, 3],
    [85, 7, 2, 2],     # ← А вот тут что-то подозрительное...
    [100, 10, 0, 1],   # ← Хах, модель в шоке
    [35, 2, 9, 3],     # ← А ведь может и не шум
    [70, 5, 4, 5],     # ← Или слишком щедро
    [60, 4, 6, 2],     # ← На грани
])

# высиськовываем данные.

Grads = np.array(Data[0:, 3:4])
Data = np.array(Data[0:, 0:3])
# xData = np.copy(Data)

# нормализация данных - вычисляем максимальный в каждой столбце
maxData = np.max(Data, axis=0)
Data = Data / maxData




# z scores
# print()
# # проверка на шум до создания модели
# av = np.average(xData)
# var = np.var(xData)


# av = np.mean(xData, axis=0)
# var = np.std(xData, axis=0)

# print("муссор")
# z = np.abs((xData - av) / var)
# q = (var / len(xData)) ** 0.5
# for rh in range(len(xData)):
#     if np.any(z[rh] > 3): print(rh, ". ", xData[rh, :6])
# print("закончили зарядку")



# очистка данных
# maxData = np.ones((Data.shape[1], ))
# for rh in range(Data.shape[1]):
#     # maxData[rh] = np.max(Data[rh:, rh:rh + 1])
#     # Data[rh:, rh:rh + 1] = (Data[rh:, rh:rh + 1] / maxData[rh])
#     maxData[rh] = np.max(Data[:, rh])
#     Data[:, rh] = Data[:, rh] / maxData[rh]
    # Data[:, rh] = Data[:, rh] / np.max(Data[:, rh]) 
    # X[:, i] = X[:, i] / np.max(X[:, i])
    # print()
    # break
# print(Data)



# добавляем единички 
Data = np.hstack([np.ones(((Data.shape[0]), 1)), Data])
print(Data)

w = np.linalg.inv(Data.T @ Data) @ Data.T @ Grads



# ввод данных
print(w)
u = np.array([90, 9, 1])
u = u / maxData
u = np.insert(u, 0, 1)
print(u)
print(round((u @ w).item(), 3))
# print(writeData(w, maxData))


# # проверка на шум через проверну
# Noise = Data @ w
# print(Noise)

# print("все мусорные данные")
# mass = np.array([])
# for rh in range(Noise.shape[0]):
#     # print(Noise[rh])
#     if abs(Grads[rh] - Noise[rh]) > 1: print(rh, ". ", Data[rh, :5], Grads[rh])
    





