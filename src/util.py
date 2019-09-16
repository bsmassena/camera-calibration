import cv2
import numpy as np
from src.point import Point

def mouse_handler(event, x, y, flags, data) :
  if event == cv2.EVENT_LBUTTONDOWN :
    cv2.circle(data['im'], (x,y),3, (0,0,255), 5, 16)
    cv2.imshow("Image", data['im'])
    if len(data['point']) == 0 :
      data['point'] = [x, y]

def get_user_input_point_from_img(im):
  # Set up data to send to mouse handler
  data = {}
  data['im'] = im.copy()
  data['point'] = []
  
  #Set the callback function for any mouse event
  cv2.imshow("Image",im)
  cv2.setMouseCallback("Image", mouse_handler, data)
  cv2.waitKey(0)

  return Point(data['point'])

def calculate_transformation_matrix(pts_src, pts_dst):
  matrix, _ = cv2.findHomography(pts_src, pts_dst)
  return matrix
