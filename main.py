# version 2.0

import cv2
import numpy as np

cap = cv2.VideoCapture(0)


while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # red color
    low_color = np.array([170,120,70])
    high_color = np.array([180,255,255])

    # blue color
    #low_color = np.array([110,50,50])
    #high_color = np.array([130,255,255])

    # green color
    # low_color = np.array([25, 52, 72])
    # high_color = np.array([130,255,255])



    color_mask = cv2.inRange(hsv_frame, low_color, high_color)
    res = cv2.bitwise_and(frame, frame, mask=color_mask)


    kernel = np.ones((5,5), np.uint8)
    erosion = cv2.erode(color_mask, kernel, iterations=1)
    dilation = cv2.dilate(color_mask, kernel, iterations=1)

    opening = cv2.morphologyEx(dilation, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

    x_medium = 0
    y_medium = 0
    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        x_medium = int((x + x + w) / 2)  # finding center
        y_medium = int((y + y + h) / 2)

        break

    cv2.line(frame, (x_medium, 0), (x_medium, 480), (0, 255, 255), 1)  # drawing a line in the middle
    cv2.line(frame, (0, y_medium), (640, y_medium), (0, 255, 255), 1)


    cv2.imshow("###frame###", frame)
    cv2.imshow('mask',color_mask)
    cv2.imshow('res', res)
    cv2.imshow('erosion', erosion)
    cv2.imshow('dilation', dilation)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)

    key = cv2.waitKey(1)

    if key == 27:
        break


cap.release()
cv2.destroyAllWindows()