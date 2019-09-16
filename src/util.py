import cv2
import numpy as np
from src.point import Point

def mouse_handler(event, x, y, flags, data) :
  matrix = data['matrix']
  img = data['img'].copy()

  world_coords = Point([x, y]).to_world(matrix)
  x = world_coords.x

  p1 = Point([x, 0]).to_pixel(matrix)
  p2 = Point([x, 68]).to_pixel(matrix)

  cv2.line(img, (p1.x, p1.y), (p2.x, p2.y), (65,195,195), 2)
  cv2.imshow("Image", img)

def draw_line_on_hover(img, matrix):
  data = {}
  data['img'] = img.copy()
  data['matrix'] = matrix

  # First draw and set callback
  cv2.imshow("Image",img)
  cv2.setMouseCallback("Image", mouse_handler, data)
  cv2.waitKey(0)

def calculate_transformation_matrix(pts_src, pts_dst):
  matrix, _ = cv2.findHomography(pts_src, pts_dst)
  return matrix
