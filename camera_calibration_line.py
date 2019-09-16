import cv2
import numpy as np
from src.dlt import calculate_transformation_matrix
from src.util import *

# Questao 2
if __name__ == '__main__' :
  # Read source image.
  im_src = cv2.imread('images/maracana2.jpg')

  # Corresponding points
  pts_src = np.array([[269, 23], [264, 344], [439, 23], [585, 346]])
  pts_dst = np.array([[0, 0], [0, 68], [11, 0], [11, 68]])

  # Calculate transformation matrix
  matrix = calculate_transformation_matrix(pts_src, pts_dst)

  # Draw line
  draw_line_on_hover(im_src, matrix)
