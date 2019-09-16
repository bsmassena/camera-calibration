import cv2
import numpy as np

def calculate_transformation_matrix(pts_src, pts_dst):
  # TODO: implement DLT
  matrix, _ = cv2.findHomography(pts_src, pts_dst)
  return matrix