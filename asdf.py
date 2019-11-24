import cv2
import numpy as np
import os

for i in os.listdir("img1/"):
    mask = cv2.imread('mask.jpg', 0)
    mask.reshape(320, 240, 1)
    mask = np.expand_dims(mask, axis=2)

    print(i)
    img = cv2.imread("img1/"+i)
    img = cv2.resize(img, dsize=(320, 240), interpolation=cv2.INTER_AREA)
    dst = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)

    src = dst

    height, width, channel = src.shape
    matrix = cv2.getRotationMatrix2D((width / 2, height / 2), 180, 1)
    ak = cv2.warpAffine(src, matrix, (width, height))

    cv2.waitKey(0)

    cv2.imwrite('asdf/'+i,ak)