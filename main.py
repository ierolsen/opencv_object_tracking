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
    # low_color = np.array([110,50,50])
    # high_color = np.array([130,255,255])

    # green color
    # low_color = np.array([25, 52, 72])
    # high_color = np.array([130,255,255])



    color_mask = cv2.inRange(hsv_frame, low_color, high_color)

    res = cv2.bitwise_and(hsv_frame, hsv_frame, mask=color_mask)


    contours, hierarchy  = cv2.findContours(color_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

    x_medium=0
    y_medium=0
    for cnt in contours:

        (x, y, w, h) = cv2.boundingRect(cnt)

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        x_medium = int((x + x + w) / 2) #finding center
        y_medium = int((y + y+h)/2)

        break


    cv2.line(frame, (x_medium, 0), (x_medium, 480), (0, 255, 255), 1) #drawing a line in the middle
    cv2.line(frame, (0, y_medium), (640, y_medium), (0, 255, 255), 1)
    cv2.imshow("###frame###", frame)
    cv2.imshow('mask',color_mask)
    cv2.imshow('res', res)

    key = cv2.waitKey(1)

    if key == 27:
        break


cap.release()
cv2.destroyAllWindows()