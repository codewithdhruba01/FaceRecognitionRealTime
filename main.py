import os

import cv2


cap = cv2.VideoCapture(1)
cap.set(3,640)
cap.set(4,480)

imgBackground = cv2.imread('src/background.png')

#import images list
folderModePath = 'src/Modes'
modePathList = os.listdir(folderModePath)
imgModeList=[]
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath,path)))
# print(len(imgModeList))


while True:
    success, img = cap.read()

    imgBackground[162:162 + 480, 55:55 + 640] = img #Set_imges_backgraund+My image capture
    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[1]

    # cv2.imshow("Webcam", img)

    cv2.imshow("Face Attendance", imgBackground)
    cv2.waitKey(1)

