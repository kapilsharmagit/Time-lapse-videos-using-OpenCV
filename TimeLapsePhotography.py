import numpy as np
import cv2
import time
import os
from os import listdir
from os.path import isfile, join

cap = cv2.VideoCapture(0)
image_number = 1
start_time = time.time()
frame_array = []

# Assumes that images folder already exists
pathOut = './images/video.avi'
fps = 10
timelapse = 30
image_counter = 0
capture_images = True

# If the program should start after some specified interval (in seconds)
# For example, if you want to capture the time-lapse lateter (say, in the morning),
# you may set the sleep interval to start after n hours by specifying a delay of
# n x 3600 seconds. The default is 30 seconds for you to get out of the way
time.sleep(30)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here.
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):	# If 'q' pressed, break out of the loop
        break

    # Check if the time has elapsed to capture a new frame
    time_lapse = time.time() - start_time
    if time_lapse >= timelapse:
        print ("Capturing image")
        frame_array.append(frame)			# Append to the frame array
        if capture_images == True:
            image_location = "images\image_" + str(image_counter) + ".jpg"
            cv2.imwrite( image_location, frame )
            image_counter = image_counter + 1
        height, width, layers = frame.shape
        size = (width,height)
        start_time = time.time()

out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
for i in range(len(frame_array)):
     # writing to the video file
    out.write(frame_array[i])
out.release()

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
