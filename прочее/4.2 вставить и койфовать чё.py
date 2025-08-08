import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

# 1. Данные: площадь от 40 до 100, плюс шум
X_area = np.linspace(40, 100, 20)
noise = np.random.normal(0, 10, X_area.shape)  # шумы с нулевым средним и отклонением 10

# 2. Истинная зависимость: цена = 50 + 0.8 * площадь
y_true = 50 + 0.8 * X_area
y = y_true + noise  # добавляем шум

# 3. Подготавливаем X (с единичкой)
X = np.vstack([np.ones_like(X_area), X_area]).T

# 4. Вычисляем веса
w = np.linalg.inv(X.T @ X) @ X.T @ y
print("Коэффициенты:", w)

# 5. Предсказание
y_pred = X @ w

# 6. График
plt.scatter(X_area, y, label='С шумом', color='red')
plt.plot(X_area, y_true, label='Истинная зависимость', color='green')
plt.plot(X_area, y_pred, label='Модель', color='blue')
plt.legend()
plt.xlabel('Площадь')
plt.ylabel('Цена')
plt.title('Полоса шумов вокруг истины')
plt.grid(True)
plt.show()
