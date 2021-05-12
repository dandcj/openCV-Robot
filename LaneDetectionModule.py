import cv2
import numpy as np
import utlis

def getLaneCurve(img):

    imgCopy = img.copy()
    ### STEP1
    imgThresh = utlis.thresholding(img)

    ### STEP2
    h,w,c = img.shape
    points = utlis.valTrackbars()
    imgWrap =  utlis.warpImg(imgThresh,points,w,h)
    imgWrapPoints = utlis.drawPoints(imgCopy,points)

    ### STEP 3
    basePoint,imgHist = utlis.getHistogram(imgWrap,display=True)


    cv2.imshow('Thresshold',imgThresh)
    cv2.imshow('Warp',imgWrap)
    cv2.imshow('Points',imgWrapPoints)
    cv2.imshow('Histogram',imgHist)



    return None

if __name__ == "__main__":
    cap = cv2.VideoCapture('vid1.mp4')
    initialTrackBarValues = [110,96,53,210]
    utlis.initializeTrackbars(initialTrackBarValues)
    frameCounter= 0
    while True:
        frameCounter += 1
        if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            frameCounter = 0

        success, img = cap.read()
        img = cv2.resize(img,(480,240))
        getLaneCurve(img)
        cv2.imshow('vid',img)
        cv2.waitKey(1)
