# Import essential libraries
from tkinter import VERTICAL
import requests
import cv2
import numpy as np
import imutils
import sys

if len(sys.argv) != 2:
    print("[Error] Incorrect number of arguments. You must give the adress of your cam")
    exit(1)
arg = sys.argv[1]
url = "http://" + arg + "/shot.jpg"
rotCode = 0
  
# While loop to continuously fetching data from the Url
while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    img = imutils.resize(img, width=1000, height=1800)
    if rotCode != None:
        img = cv2.rotate(img, rotCode)
    cv2.imshow(sys.argv[1], img)
  
    # Press Esc key to exit
    key = cv2.waitKey(1)
    if key == 27:
        print("Killing it")
        break
    elif key == 97:
        rotCode = None
        print("[Info] Flipping to :{}".format(rotCode))
    elif key == 122:
        rotCode = cv2.ROTATE_90_CLOCKWISE
        print("[Info] Flipping to :{}".format(rotCode))
    elif key == 101:
        rotCode = cv2.ROTATE_90_COUNTERCLOCKWISE
        print("[Info] Flipping to :{}".format(rotCode))
    elif key == 114:
        rotCode = cv2.ROTATE_180
        print("[Info] Flipping to :{}".format(rotCode))
                     
cv2.destroyAllWindows()