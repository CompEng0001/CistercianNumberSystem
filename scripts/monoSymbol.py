import cv2
import numpy as np

imageToCheck = cv2.imread('./symbols/UpperRightQuadrant-Ones/1.PNG') #mainimage
groundTruthImage = cv2.imread('./symbols/Cisterican_Digits_grouped/Cistercian_digits.PNG')  #coin?
w, h = imageToCheck.shape[:-1]

res = cv2.matchTemplate(groundTruthImage,imageToCheck,cv2.TM_CCOEFF_NORMED)
threshold = 1
location = np.where(res >= threshold)

for pt in zip(*location[::-1]):  # Switch collumns and rows
    cv2.rectangle(groundTruthImage, pt, (pt[1]+h, pt[0]+w), (0, 0, 255), 2)

cv2.imwrite('result.png', groundTruthImage)