import cv2
import numpy as np
from src.dlt import calculate_transformation_matrix
from src.util import *

# Questao 1
if __name__ == '__main__' :
  # Read source image.
  im_src = cv2.imread('images/maracana1.jpg')

  # Corresponding points
  pts_src = np.array([[275, 84], [227, 107], [159, 141], [125, 158], [31, 205], [250, 222], [158, 112], [124, 128]])
  pts_dst = np.array([[0, 0, 0], [0, 13.84, 0], [0, 30.34, 0], [0, 37.66, 0], [0, 54.16, 0], [16.5, 54.16, 0], [0, 30.34, 2.44], [0, 37.66, 2.44]])

  # Calculate transformation matrix
  matrix = calculate_transformation_matrix(pts_src, pts_dst)

  # Draw player
  draw_player_on_hover(im_src, matrix)
