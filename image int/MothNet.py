import torch
import torch.nn as nn
from torchvision import transforms
import os
from PIL import Image
import matplotlib.pyplot as plt

# 1. Определяем простую нейросеть
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.flatten = nn.Flatten()
        self.fc = nn.Linear(28*28, 10)  # вход = картинка 28x28, выход = 10 цифр

    def forward(self, x):
        x = self.flatten(x)
        x = self.fc(x)
        return x

# 2. Загружаем обученную модель
model = SimpleNet()
model.load_state_dict(torch.load(
    "C:/Users/vzdis/OneDrive/Рабочий стол/MothStuff/image int/mnist_net.pth"
))
model.eval()  # режим предсказания

# 3. Проверяем на внешних файлах
while "y" in input("Хочешь попробовать со своими данными? y/n: "):
    print("Положи свои картинки в папку img")

    path = "C:/Users/vzdis/OneDrive/Рабочий стол/MothStuff/image int/img"
    files = os.listdir(path)

    for rh in files:
        img_path = os.path.join(path, rh)  # корректный путь
        img = Image.open(img_path).convert("L")  # ч/б
        img = img.resize((28, 28), Image.BILINEAR)  # сжать до 28x28
        plt.imshow(img); plt.show()


        transform = transforms.ToTensor()
        tensor = transform(img).unsqueeze(0)  # (1, 1, 28, 28)

        with torch.no_grad():
            output = model(tensor)
            probs = torch.softmax(output, dim=1)  # вероятности
            confidence, predicted = torch.max(probs, 1)

        print(f"{rh} → Это число {predicted.item()}, "
              f"уверенность {confidence.item()*100:.2f}%")

print("Закончили")
