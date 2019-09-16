import cv2
import numpy as np
from src.dlt import calculate_transformation_matrix
from src.util import *

# Questao 1
if __name__ == '__main__' :
  # Read source image.
  im_src = cv2.imread('images/maracana1.jpg')

  # TODO: Find corresponding points
  pts_src = np.array([])
  pts_dst = np.array([])

  # Calculate transformation matrix
  matrix = calculate_transformation_matrix(pts_src, pts_dst)

  # Draw player
  draw_player_on_hover(im_src, matrix)
