import numpy as np
import cv2
import matplotlib.pyplot as plt

img_file_name = './Comp-Map-G25-550.jpg'
img = cv2.imread(img_file_name)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# edges = cv2.Canny(gray, 50, 150, apertureSize=3)

cv2.imshow('original', img)
cv2.imshow('grayscale', gray)


# fig, axs = plt.subplots(1,2)
# axs[0].imshow(img)
# axs[1].imshow(gray)
# plt.show()

# lines = cv2.HoughLines(edges, 1, np.pi/180, 200)


# for rho, theta in lines[0]:
#     a = np.cos(theta)
#     b = np.sin(theta)
#     x0 = a*rho
#     y0 = b*rho
#     x1 = int(x0 + 1000*(-b))
#     y1 = int(y0 + 1000*(a))
#     x2 = int(x0 - 1000*(-b))
#     y2 = int(y0 - 1000*(a))
#     cv2.line(img, (x1, y1), (x2, y2), (0,0,255), 2)

# cv2.imwrite('houghlines3.jpg', img)