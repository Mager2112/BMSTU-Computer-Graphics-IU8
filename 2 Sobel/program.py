# Программа сделана в CoLab
import requests
from PIL import Image
import io
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

image_url = "https://mykaleidoscope.ru/x/uploads/posts/2022-10/1666364386_1-mykaleidoscope-ru-p-natsionalnii-park-lenskie-stolbi-vkontakte-1.jpg"

response = requests.get(image_url)
image = Image.open(io.BytesIO(response.content)).convert('L')  # Конвертируем в черно-белое

image_np = np.array(image).astype('int32')

sobel_h = ndimage.sobel(image_np, 0)  # горизонтальный градиент
sobel_v = ndimage.sobel(image_np, 1)  # вертикальный градиент

magnitude = np.sqrt(sobel_h**2 + sobel_v**2)
magnitude *= 255.0 / np.max(magnitude) 

fig, axs = plt.subplots(2, 2, figsize=(8, 8))

plt.gray()

axs[0, 0].imshow(image_np)
axs[0, 1].imshow(sobel_h)
axs[1, 0].imshow(sobel_v)
axs[1, 1].imshow(magnitude)

titles = ["Оригинал", "Горизонтальный", "Вертикальный", " "]

for i, ax in enumerate(axs.ravel()):
    ax.set_title(titles[i])
    ax.axis("off")

plt.show()
