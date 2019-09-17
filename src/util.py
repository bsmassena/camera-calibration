import cv2
import numpy as np
from src.point import Point

# First question
def mouse_handler_player(event, x, y, flags, data) :
  matrix = data['matrix']
  img = data['img'].copy()

  p1 = Point([x, y]).to_world(matrix)
  p2 = Point([p1.x, p1.y, 1.8])

  p1 = p1.to_pixel(matrix)
  p2 = p2.to_pixel(matrix)

  cv2.line(img, (p1.x, p1.y), (p2.x, p2.y), (50,50,220), 2)
  cv2.imshow("Image", img)

def draw_player_on_hover(img, matrix):
  data = {}
  data['img'] = img.copy()
  data['matrix'] = matrix

  # First draw and set callback
  cv2.imshow("Image", img)
  cv2.setMouseCallback("Image", mouse_handler_player, data)
  cv2.waitKey(0)

# Second question
def mouse_handler_line(event, x, y, flags, data) :
  matrix = data['matrix']
  img = data['img'].copy()

  world_coords = Point([x, y]).to_world(matrix)
  x = world_coords.x

  p1 = Point([x, 0]).to_pixel(matrix)
  p2 = Point([x, 68]).to_pixel(matrix)

  cv2.line(img, (p1.x, p1.y), (p2.x, p2.y), (50,50,220), 2)
  cv2.imshow("Image", img)

def draw_line_on_hover(img, matrix):
  data = {}
  data['img'] = img.copy()
  data['matrix'] = matrix

  # First draw and set callback
  cv2.imshow("Image", img)
  cv2.setMouseCallback("Image", mouse_handler_line, data)
  cv2.waitKey(0)
