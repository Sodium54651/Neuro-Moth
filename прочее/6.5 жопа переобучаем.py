import numpy as np

def Relu(z):
    return np.maximum(0, z)


def  DRelu(z):
    return (z > 0).astype(float)


Answer = []
Data = []
for i in range(1, 10):
    for j in range(1, 10):
        Data += [[i, j]]
        Answer += [[i ** 0.5 * j ** 0.5]]

Data = np.array(Data)
Answer = np.array(Answer)
print(Answer)
print()
print(Data)

w = np.random.rand(2, 2)
bias = np.array([[0.0, 0.0]])

w1 = np.random.rand(2, 2)
bias1 = np.array([[0.0, 0.0]])

w2 = np.random.rand(1, 2)
bias2 = np.array([[0.0]])


z = Relu(Data @ w.T + bias)
print(z)
z1 = Relu(z @ w1.T + bias1)
NAnswer = z1 @ w2.T + bias2

LR = 0.01
for rh in range(1000):
    loss = NAnswer - Answer

    # w2G = loss.T @ z1
    w2 -= LR * loss.T @ z1
    # bias2 = LR * np.sum(loss, axis=0, keepdims=True)

    w1 -= LR * (loss @ w2).T @ z
    # bias1 = LR * np.sum(loss, axis=0, keepdims=True)

    w -= LR * (loss @ w2 @ w1).T @ Data
    # bias1 = LR * np.sum(loss, axis=0, keepdims=True)
    

    z = Relu(Data @ w.T + bias)
    # print(z)
    z1 = Relu(z @ w1.T + bias1)
    NAnswer = z1 @ w2.T + bias2
    print(NAnswer)
print(Answer)







