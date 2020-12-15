import cv2
import matplotlib as plt
import numpy as np

img = cv2.imread('Gradient.png')

print(f"Original Dimensions: {img.shape}")

resized = cv2.resize(img, (16,16), interpolation = cv2.INTER_AREA)

print(f"Resized Dimensions: {resized.shape}")

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Resized image', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

exit()