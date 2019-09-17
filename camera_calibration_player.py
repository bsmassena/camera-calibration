import cv2
import numpy as np
from src.dlt import calculate_transformation_matrix
from src.util import *

# Questao 1
if __name__ == '__main__' :
  # Read source image.
  im_src = cv2.imread('images/maracana1.jpg')

  # Calibration points
  image_points = np.array([
    # Linha de fundo
    [275, 84],
    [227, 107],
    [159, 141],
    [125, 158],
    [31, 205],
    # Canto inferior direito da grande area
    [250, 222],
    # Cantos superiores da goleira
    [158, 112],
    [124, 128],
    # Cantos da direita da pequena area
    [241, 132],
    [160, 177]
  ])

  world_points = np.array([
    # Linha de fundo
    [0, 0, 0],
    [0, 13.84, 0],
    [0, 30.34, 0],
    [0, 37.66, 0],
    [0, 54.16, 0],
    # Canto inferior direito da grande area
    [16.5, 54.16, 0],
    # Cantos superiores da goleira
    [0, 30.34, 2.44],
    [0, 37.66, 2.44],
    # Cantos da direita da pequena area
    [5.5 ,24.84 , 0],
    [5.5 ,43.16 , 0]
  ])

  # Calculate transformation matrix
  matrix = calculate_transformation_matrix(image_points, world_points)

  # Draw player
  draw_player_on_hover(im_src, matrix)
