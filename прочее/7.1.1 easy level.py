import numpy as np

def Relu(z):
    return np.maximum(z, 0)

def DRelu(z):
    return (z > 0).astype(float)


Data = np.array([
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 5],
    [5, 6]
])

Answers = np.array([
    [5],
    [8],
    [11],
    [14],
    [17]
])


w1 = np.random.rand(3, 2)
b1 = np.array([[0.1, 0.1, 0.1]])

w2 = np.random.rand(4, 3)
b2 = np.array([[0.1, 0.1, 0.1, 0.1]])

w3 = np.random.rand(1, 4)
b3 = np.array([[0.1]])

n1 = Relu(Data @ w1.T + b1)
n2 = Relu(n1 @ w2.T + b2)
n3 = n2 @ w3.T + b3
print(n3, "\n")

LR = 0.001
for rh in range(10000):
    loss = n3 - Answers

    w3G = loss.T @ n2
    b3G = np.sum(loss, axis=0, keepdims=True)

    ww2G = loss @ w3 * DRelu(n2)
    w2G = n1.T @ ww2G
    b2G = np.sum(ww2G, keepdims=True, axis=0)

    ww1G = ww2G @ w2 * DRelu(n1)
    w1G = Data.T @ ww1G
    b1G = np.sum(ww1G, keepdims=True, axis=0)


    w3 -= w3G * LR
    b3 -= b3G * LR

    w2 -= w2G.T * LR
    b2 -= b2G * LR

    w1 -= w1G.T * LR
    b1 -= b1G * LR


    n1 = Relu(Data @ w1.T + b1)
    n2 = Relu(n1 @ w2.T + b2)
    n3 = n2 @ w3.T + b3
print(n3)


