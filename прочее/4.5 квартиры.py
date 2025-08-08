import numpy as np

# площадь | растояние до метро мин | этаж | состояние 1 \ 10 | цена 
Data = np.array([
    [15, 10, 5, 6, 300],
    [20, 20, 10, 7, 350],
    [5, 2, 5, 8, 400],
    [30, 45, 2, 10, 200],
    [10, 5, 25, 9, 320]
])

Coast = np.array(Data[0:, 4:])
Data = Data[0:, 0:4]

maxData = np.max(Data, axis=0)
Data = Data / maxData

Data = np.hstack([np.ones((Data.shape[0], 1)), Data])
print(Data)

w = np.linalg.inv(Data.T @ Data) @ Data.T @ Coast

print(w)
print("тестовики")

u = np.array([15, 10, 5, 6]) / maxData
u = np.insert(u, 0, 1)
print((u @ w).item())

u = np.array([40, 2, 2, 5]) / maxData
u = np.insert(u, 0, 1)
print(u @ w)