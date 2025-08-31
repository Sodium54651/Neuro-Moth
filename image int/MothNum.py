import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import os

from PIL import Image
import numpy as np

# 1. Загружаем данные MNIST
transform = transforms.ToTensor()
train_data = datasets.MNIST(root="data", train=True, download=True, transform=transform)
test_data = datasets.MNIST(root="data", train=False, download=True, transform=transform)

train_loader = DataLoader(train_data, batch_size=64, shuffle=True)
test_loader = DataLoader(test_data, batch_size=64)

# 2. Определяем простую нейросетку
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.flatten = nn.Flatten()
        self.fc = nn.Linear(28*28, 10)  # вход = картинка 28x28, выход = 10 цифр

    def forward(self, x):
        x = self.flatten(x)
        x = self.fc(x)
        return x

model = SimpleNet()


if ("y" in str(input("Загружаем / обучаем y/n: "))):
    model.load_state_dict(torch.load("C:/Users/vzdis/OneDrive/Рабочий стол/MothStuff/image int/mnist_net.pth"))
    model.eval()
else: 
# ===========================================================

    


    # 3. Функция ошибки и оптимизатор
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=0.01)

    # 4. Обучение (всего 1 эпоха для теста)
    for epoch in range(1):
        for images, labels in train_loader:
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
        print(f"Эпоха {epoch+1}, ошибка = {loss.item():.4f}")

# 5. Проверка на тестовых данных
correct = 0
total = 0
with torch.no_grad():
    for images, labels in test_loader:
        outputs = model(images)
        _, predicted = torch.max(outputs, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print(f"Точность на тесте: {100 * correct / total:.2f}%")




torch.save(model.state_dict(), "C:/Users/vzdis/OneDrive/Рабочий стол/MothStuff/image int/mnist_net.pth")
print("сохранили")
