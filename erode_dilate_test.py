from __future__ import print_function
import cv2 as cv
import numpy as np
import argparse
erosion_size = 0
max_elem = 2
max_kernel_size = 21
title_trackbar_element_type = 'Element:\n 0: Rect \n 1: Cross \n 2: Ellipse'
title_trackbar_kernel_size = 'Kernel size:\n 2n +1'
title_erosion_window = 'Erosion Demo'
title_dilatation_window = 'Dilation Demo'
def erosion(val):
    erosion_size = cv.getTrackbarPos(title_trackbar_kernel_size, title_erosion_window)
    erosion_type = 0
    val_type = cv.getTrackbarPos(title_trackbar_element_type, title_erosion_window)
    if val_type == 0:
        erosion_type = cv.MORPH_RECT
    elif val_type == 1:
        erosion_type = cv.MORPH_CROSS
    elif val_type == 2:
        erosion_type = cv.MORPH_ELLIPSE
    element = cv.getStructuringElement(erosion_type, (2*erosion_size + 1, 2*erosion_size+1), (erosion_size, erosion_size))
    erosion_dst = cv.erode(src, element)
    cv.imshow(title_erosion_window, erosion_dst)
def dilatation(val):
    dilatation_size = cv.getTrackbarPos(title_trackbar_kernel_size, title_dilatation_window)
    dilatation_type = 0
    val_type = cv.getTrackbarPos(title_trackbar_element_type, title_dilatation_window)
    if val_type == 0:
        dilatation_type = cv.MORPH_RECT
    elif val_type == 1:
        dilatation_type = cv.MORPH_CROSS
    elif val_type == 2:
        dilatation_type = cv.MORPH_ELLIPSE
    element = cv.getStructuringElement(dilatation_type, (2*dilatation_size + 1, 2*dilatation_size+1), (dilatation_size, dilatation_size))
    dilatation_dst = cv.dilate(src, element)
    cv.imshow(title_dilatation_window, dilatation_dst)



parser = argparse.ArgumentParser(description='Code for Thresholding Operations using inRange tutorial.')
parser.add_argument('--camera', help='Camera divide number.', default=0, type=int)
args = parser.parse_args()
cap = cv.VideoCapture(args.camera)


cv.namedWindow(title_erosion_window)
cv.createTrackbar(title_trackbar_element_type, title_erosion_window , 0, max_elem, erosion)
cv.createTrackbar(title_trackbar_kernel_size, title_erosion_window , 0, max_kernel_size, erosion)
cv.namedWindow(title_dilatation_window)
cv.createTrackbar(title_trackbar_element_type, title_dilatation_window , 0, max_elem, dilatation)
cv.createTrackbar(title_trackbar_kernel_size, title_dilatation_window , 0, max_kernel_size, dilatation)

src = None


low_H = 0
low_S = 0
low_V = 126

high_H = 180
high_S = 71
high_V = 255

while True:

    ret, frame = cap.read()
    if frame is None:
        break

    src = cv.inRange(cv.cvtColor(frame, cv.COLOR_BGR2HSV), (low_H, low_S, low_V), (high_H, high_S, high_V))

    #src = cv.inRange(frame_HSV, (low_H, low_S, low_V), (high_H, high_S, high_V))
    #frame_HSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    #frame_threshold = cv.inRange(frame_HSV, (low_H, low_S, low_V), (high_H, high_S, high_V))

    erosion(0)
    dilatation(0)

    cv.imshow('k', src)
    #cv.imshow('window_detection_name', frame_threshold)

    key = cv.waitKey(30)
    if key == ord('q') or key == 27:
        break
