# Airpaint
This is a simple python script designed to grab webcam input and pipe it through mediapipe / opencv2.
It then lets you select & draw colors (r/g/b) on screen using your phalanges (fingers).

## Installation
```
git clone https://github.com/diamondbond/airpaint ~/airpaint
cd ~/airpaint
pip3 install -r requirements.txt
# place your hand within the webcams POV
python3 main.py
```

## Features
- Use two fingers together to select a color: hover over a color to select it
- Use one finger to draw
- R/G/B only palette
- Eraser
- 20~30fps @ 720p
- Adjustable brush & eraser thickness (from within the "Vars" section of the script at the top of main.py: line 10-11)

## Bugs/FAQ
- If no webcam input is found (may vary depending on OS and/or amount of video devices plugged in) please try changing line 29 in main.py from the default:
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
To avoid this please place one of your hands within the webcams POV prior to hitting enter to run the script (also: wiggling your fingers slowly upon starting the script sometimes help the detection of fingers).
- Its very sensitive and is prone to crashing easily - there is not much I can do about this as of right now, sorry.

## Have Fun! :)