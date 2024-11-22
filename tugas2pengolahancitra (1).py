# -*- coding: utf-8 -*-
"""tugas2pengolahancitra.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XYqbcSI7r7U6MrNXqWvtw2-qS4TRwe0J
"""

import imageio
import numpy as np
import matplotlib.pyplot as plt

# 1. Membaca gambar berwarna (RGB) dan mengubahnya menjadi grayscale
image_path = '/content/1e0964ae-0888-4e26-a46f-9c2c33eb20b0.jpeg'
image_rgb = imageio.imread(image_path)
image_gray = np.dot(image_rgb[...,:3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)

# 2. Menghitung histogram intensitas piksel grayscale
histogram, bins = np.histogram(image_gray.flatten(), bins=256, range=[0, 255])

# Tampilkan gambar grayscale
plt.figure(figsize=(6, 6))
plt.imshow(image_gray, cmap='gray')  # cmap='gray' untuk menampilkan dalam format grayscale
plt.title('Grayscale Image')
plt.axis('off')  # Hilangkan sumbu agar lebih bersih
plt.show()

# 3. Menampilkan histogram menggunakan Matplotlib
plt.figure(figsize=(10, 6))
plt.bar(range(256), histogram, color='gray', width=1.0)
plt.title('Histogram Intensitas Gambar Grayscale')
plt.xlabel('Intensitas Piksel')
plt.ylabel('Jumlah Piksel')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Import library yang diperlukan
import imageio.v2 as imageio  # Pastikan menggunakan imageio.v2 untuk kompatibilitas
import numpy as np
import matplotlib.pyplot as plt

# Baca gambar berwarna (RGB)
image_path = "/content/1e0964ae-0888-4e26-a46f-9c2c33eb20b0.jpeg"  # Ganti dengan nama file gambar yang sudah diunggah
image_rgb = imageio.imread(image_path)

# Ubah gambar menjadi grayscale
image_gray = np.dot(image_rgb[...,:3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)

# Tampilkan gambar grayscale
plt.figure(figsize=(6, 6))
plt.imshow(image_gray, cmap='gray')  # cmap='gray' untuk menampilkan dalam format grayscale
plt.title('Grayscale Image')
plt.axis('off')  # Hilangkan sumbu agar lebih bersih
plt.show()

# Hitung histogram intensitas grayscale
histogram, bins = np.histogram(image_gray.flatten(), bins=256, range=[0, 256])

# Tampilkan histogram menggunakan Matplotlib
plt.figure(figsize=(10, 6))
plt.bar(range(256), histogram, color='gray', edgecolor='black')
plt.title('Histogram of Grayscale Image')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)
plt.show()

# Jumlah total piksel untuk setiap intensitas
print("Jumlah total piksel untuk setiap intensitas (0-255):")
for intensity, count in enumerate(histogram):
    print(f"Intensitas {intensity}: {count} piksel")

# Identifikasi intensitas dominan
dominant_intensity = np.argmax(histogram)
dominant_count = histogram[dominant_intensity]

print("\n**Analisis Histogram**")
print(f"Intensitas dominan adalah {dominant_intensity} dengan jumlah {dominant_count} piksel.")