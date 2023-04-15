import cv2
import numpy as np
import serial
import time

arduino = serial.Serial(port='COM6', baudrate=115200, timeout=.1)


def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data


def getContours(img, imgSegmented, areaThres, drawContour = True, drawBoundingBox = True):
    area=0
    peri =0
    peribox = 0
    contours, hierachy = cv2.findContours(imgSegmented,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        check_area = cv2.contourArea(cnt)
        if check_area > areaThres:
            area = check_area
            cv2.drawContours(img, cnt, -1, (255,0,0),3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            x,y,w,h = cv2.boundingRect(approx)
            peribox = (2*w)+(2*h)

            if drawContour == True:
                cv2.drawContours(img, cnt, -1, (255, 0, 0), 3)

            if drawBoundingBox == True:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

        else:
            area = 0
            peri = 0
            peribox = 0
            pass

    return area, peri, peribox


############################################################################
#red
hsv_lowerbound = [0,70,50]
hsv_upperbound = [14,255,255]

kernel = np.ones((3,3),np.uint8)

vcap = cv2.VideoCapture(1)  # 0 built-in webcamera

if vcap.isOpened():
    width = vcap.get(3)
    height = vcap.get(4)
    fps = vcap.get(5)

    while True:
        success, img = vcap.read()

        imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        lower_bound = np.array(hsv_lowerbound)
        upper_bound = np.array(hsv_upperbound)
        mask = cv2.inRange(imgHsv, lower_bound, upper_bound)
        
        area, peri, peribox = getContours(img,mask,3000)

        if (area == 0):
            pass

        else:
            time.sleep(0.5)
            num = str(area)
            value = write_read(num)
            print(num)
        
        cv2.imshow("Output",img)
        #cv2.imshow("Output2",mask)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
