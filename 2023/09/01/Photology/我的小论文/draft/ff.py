import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np
img=cv.imread("text2.jpg",0)
A=img
fft_v = np.fft.fft2(img)
fft_v = np.fft.fftshift(fft_v)
fft_v=20*np.log(np.abs(fft_v))
plt.subplot(0),plt.imshow(img,"gray"),plt.title("Original")
plt.subplot(1),plt.imshow(fft_v,cmap='gray'),plt.title("Magnitude Spectrum")
plt.show()