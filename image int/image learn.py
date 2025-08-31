from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import torch

from torchvision.datasets import MNIST
lime = Image.open("C:/Users/vzdis/OneDrive/Рабочий стол/MothStuff/img/lime.jpeg").convert("L")


arr = np.array(lime)
print("lime:", arr.shape, arr.dtype, arr.min(), arr.max(), arr.mean(), arr.std())
plt.imshow(lime, cmap="gray"); plt.show()

g = np.array(lime).astype(np.float32) / 255.0
print("gray 0..1:", g.shape, g.dtype, g.min(), g.max())

small = lime.resize((28, 28), Image.BILINEAR)
plt.imshow(small, cmap="gray"); plt.show()

s = np.array(small)
print("small:", s.shape, s.dtype, s.min(), s.max())


mnist = MNIST("data", download=True)
image, label = mnist[0]
arr_m = np.array(image)
print("mnist0:", arr_m.shape, arr_m.dtype, arr_m.min(), arr_m.max(), arr_m.mean(), arr_m.std())
print("label:", label)





from torchvision.datasets import MNIST
import matplotlib.pyplot as plt 
from PIL import Image
import numpy as np

mnist = MNIST("data", download=True)

ima = Image.open("C:/Users/vzdis/OneDrive/Рабочий стол/MothStuff/img/lime.jpeg")

ima = np.array(ima)
print(ima)
plt.imshow(ima)
plt.show()

image, text = mnist[0]

# Переводим PIL.Image в numpy-массив
image_array = np.array(image)
# print(image_array)
# Рисуем
print()

plt.imshow(image_array, cmap="gray")
plt.show()

print("Done")