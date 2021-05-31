#!/usr/bin/env python3

import cv2
import numpy as np
import time
import os
import HandTrackingModule as htm

# Vars #
brushThickness = 15
eraserThickness = 100
########

# import assets
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

# grab video device
cap = cv2.VideoCapture(-1)  # linux -1, win 0/1
cap.set(3, 1280)
cap.set(4, 720)

# high detection confidence for painting; lower if errors occur
detector = htm.handDetector(detectionCon=0.85)

# xprev & yprev init
xp, yp = 0, 0

# init canvas (1280x720 with 3 channel colors as 8bit unsigned int)
imgCanvas = np.zeros((720, 1280, 3), np.uint8)

while True:
    # (1) import image
    success, img = cap.read()
    # flip image (mirror real life)
    img = cv2.flip(img, 1)

    # (2) find hand landmarks
    img = detector.findHands(img, draw=False)
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

        # (4) SELECTION MODE (index & middle finger)
        if fingers[1] and fingers[2]:
            xp, yp = 0, 0  # reset
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

        # (5) DRAWING MODE (index only)
        if fingers[1] and fingers[2] == False:
            cv2.circle(img, (x1, y1), 15, drawColor, cv2.FILLED)
            print("Drawing Mode")

            # first frame condition
            if xp == 0 and yp == 0:
                xp, yp = x1, y1

            if drawColor == (0, 0, 0):
                cv2.line(img, (xp, yp), (x1, y1), drawColor, eraserThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1),
                         drawColor, eraserThickness)
            else:
                cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1),
                         drawColor, brushThickness)

            # update
            xp, yp = x1, y1

    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, imgInv)  # add images
    img = cv2.bitwise_or(img, imgCanvas)

    # render header
    img[0:100, 0:1280] = header
    #img = cv2.addWeighted(img, 0.5, imgCanvas, 0.5, 0)
    cv2.imshow("AirPaint", img)
    #cv2.imshow("Canvas", imgCanvas)
    #cv2.imshow("Inverse", imgInv)
    cv2.waitKey(1)
