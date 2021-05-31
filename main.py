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
drawColor = (255, 0, 255)

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
    lmList = detector.findPosition(img, draw=False)

    # print(lmList)
    if len(lmList) != 0:
        # print(lmList)

        # get tip of fingers
        x1, y1 = lmList[8][1:]  # index
        x2, y2 = lmList[12][1:]  # middle

        # (3) identify upright phalanges
        #     only draw when index finger is up
        fingers = detector.fingersUp()
        # print(fingers)

        # (4) SELECTION MODE
        if fingers[1] and fingers[2]:
            print("Selection Mode")

            # if within 100px header region
            if y1 < 100:
                # RED
                if 100 < x1 < 400:
                    header = overlayList[1]
                    drawColor = (0, 0, 255)
                # GREEN
                elif 450 < x1 < 740:
                    header = overlayList[3]
                    drawColor = (0, 255, 0)
                # BLUE
                elif 765 < x1 < 1035:
                    header = overlayList[2]
                    drawColor = (255, 0, 0)
                # ERASER
                elif 1047 < x1 < 1265:
                    header = overlayList[0]
                    drawColor = (0, 0, 0)
        cv2.rectangle(img, (x1, y1-25), (x2, y2+25), drawColor, cv2.FILLED)

        # (5) DRAWING MODE
        if fingers[1] and fingers[2] == False:
            cv2.circle(img, (x1, y1), 15, drawColor, cv2.FILLED)
            print("Drawing Mode")

    # render header
    img[0:100, 0:1280] = header
    cv2.imshow("Image", img)
    cv2.waitKey(1)
