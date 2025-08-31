import numpy as np
import torch as th
# ns = NeuroStuff
class NeuroStuff:

    def __init__(self):
        self.wias = []
        self.bias = []
        self.LR = 0.001


# число входный и выходных нейронов
# делает веса для нужно слоя на колличество
# оно должно быть равно числу выходный нейрончиков
    def nlay(self, inn, out):
        # w1, w2, w3...
        self.wias.append(np.random.rand(out, inn)) 

        # b1, b2, b3...
        self.bias.append(np.full((1, out), 0.1))


    def Relu(self, z):
        return np.maximum(z, 0)
    
    def DRelu(self, z):
        return (z > 0).astype(float)
    
# делаем проходку прямой ход 
    def Start(self, Data):

        # это ответы от слоя, 0 => 1
        self.layers = [Data]
        for rh in range(len(self.wias) -1):
            Data = self.Relu(Data @ self.wias[rh].T + self.bias[rh])
            self.layers.append(Data)
        self.layers.append(Data @ self.wias[-1].T + self.bias[-1])
        return self.layers[-1]


# тренер будет обучать, ТРЕНЕЕЕЕЕР!!!!!
    def trener(self, Data, Answers, cicle):

        for rh in range(cicle):
            loss = self.Start(Data) - Answers
            # промежуточный подвесовые ошибки
            self.wg = loss.T @ self.layers[-2]
            self.wias[-1] -= self.wg * self.LR

            self.bias[-1] -= np.sum(loss, axis=0, keepdims=True) * self.LR
# тут катыль в виде loss его надо как то убрать пока так
            for rhh in range(len(self.wias) - 2, -1, -1):

                loss = loss @ self.wias[rhh+1] * self.DRelu(self.layers[rhh+1])
                self.wg = self.layers[rhh].T @ loss
                
                self.wias[rhh] -= self.wg.T * self.LR
                self.bias[rhh] -= np.sum(loss, keepdims=True, axis=0) * self.LR


# y = x1^2 * x2
# запись данных
Data = np.array([
    [1, 1],
    [2, 1],
    [1, 2],
    [2, 2],
    [3, 3]
])

Answers = np.array([
    [2],
    [5],
    [5],
    [10],
    [27]
])




# ======================================================================= #
# NeuroStuff(Data, Answers)
ns = NeuroStuff()
# добавляем слои c весами(вход, выход) и платы за воздух(выход, оно само)
ns.nlay(2, 6)
ns.nlay(6, 2)
ns.nlay(2, 1)

# запуск нейросети с входными данными 
print(ns.Start(Data))
print()
# её обучение, с входными данными, и ответами, и циклом обучения
ns.trener(Data, Answers, 7500)
print(ns.Start(Data))
print()



# проверка 
print("====================")
print("  Тестовые данные   ")
print("====================")

Data = np.array([
    [2, 5]
])

Answers = np.array([
    [2]
])
print(ns.Start(Data))

print("\n====================")
print("       Ответы       ")
print("====================")
print(Answers)

