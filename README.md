# Airpaint
This is a simple python script to grab webcam input and pipe through mediapipe / opencv2 and draw colors (r/g/b only) on screen using phalanges (fingers).

## Installation
```
git clone https://github.com/diamondbond/airpaint ~/airpaint
cd ~/airpaint
pip3 install -r requirements.txt
# place your hand within webcam framing
python3 main.py
```

## Features
- R/G/B only palette
- Eraser
- ~ 20fps @ 720p
- Adjustable brush & eraser thickness (from within the "Vars" section of the script at the top of main.py)

## Bugs/FAQ
- If no webcam input is found (may vary depending on OS and/or amount of video devices plugged in) please try changing line 29 from main.py:
```
cap = cv2.VideoCapture(-1)
```
to either:
```
cap = cv2.VideoCapture(1)
```
or
```
cap = cv2.VideoCapture(0)
```
- If no hand is present when launching the script you will recieve the following error:
```
Traceback (most recent call last):
  File "/home/diamond/git/airpaint/main.py", line 53, in <module>
    if len(lmList) != 0:
TypeError: object of type 'NoneType' has no len()
```
To avoid this please place one of your hands within the webcams POV prior to hitting enter to run the script, if it does not work, wiggle your fingers and try running the script a few times.
