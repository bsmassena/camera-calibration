import cv2
import numpy as np
from src.util import *

if __name__ == '__main__' :
  # Read source image.
  im_src = cv2.imread('images/maracana2.jpg')

  # Corresponding points
  pts_src = np.array([[268, 61], [266, 237], [458, 62], [509, 239]])
  pts_dst = np.array([[0, 0], [0, 40.32], [11, 0], [11, 40.32]])

  # Calculate transformation matrix
  matrix = calculate_transformation_matrix(pts_src, pts_dst)

  pixel_point = get_user_input_point_from_img(im_src)
  world_point = pixel_point.to_world(matrix)

  print(pixel_point)
  print(world_point)
  print(world_point.to_pixel(matrix))