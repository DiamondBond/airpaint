#!/usr/bin/env python3

import cv2
import numpy as np
import time
import os
import HandTrackingModule as htm

folderPath = "assets"
myList = os.listdir(folderPath)
print(myList)
overlayList = []

for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)
print(len(overlayList))

header = overlayList[0]

cap = cv2.VideoCapture(-1)  # linux -1, win 0/1
cap.set(3, 1280)
cap.set(4, 720)

# high detection confidence for painting; lower if errors occur
detector = htm.handDetector(detectionCon=0.85)

while True:
    # (1) import image
    success, img = cap.read()
    # flip image (mirror real life)
    img = cv2.flip(img, 1)

    # (2) find hand landmarks
    img = detector.findHands(img)

    # (3) identify upright phalanges
    #     only draw when index finger is up

    # (4) identify selection mode
    #     only when two fingers are up

    # (5) if drawing mode
    #     only when index finger is up

    # render header
    img[0:100, 0:1280] = header
    cv2.imshow("Image", img)
    cv2.waitKey(1)
