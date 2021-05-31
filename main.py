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