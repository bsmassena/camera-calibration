import cv2
import numpy as np

'''
  Here using:
  x, y and z referring to the world coordinates of the point and
  u, v are referring to the pixel coordinates of the point
'''

def calculate_transformation_matrix(pts_src, pts_dst):
  # TODO: implement DLT

  homo = np.array([])

  if len(pts_dst[0]) == 2:
    x = pts_dst[:, 0]
    y = pts_dst[:, 1]
    u = pts_src[:, 0]
    v = pts_src[:, 1]
    homo = homography_2d(x, y, u, v)
    return homo

  matrix, _ = cv2.findHomography(pts_src, pts_dst)
  return matrix

'''
  Instead of defining the linear system as:
  [x1 y1 z1 1 0 0 0 0 -u1x1 -u1y1 -u1z1 -u1]   [m11]    [0]
  [0 0 0 0 x1 y1 z1 1 -v1x1 -v1y1 -v1z1 -v1] * [m12] =  [0]
  [...                                     ]   [...]    [0]
  [...                                     ]   [m34]    [0]
  
  this system will be defined here as:
  
  [x1 y1 z1 1 0 0 0 0 -u1x1 -u1y1 -u1z1]   [m11]    [u1]
  [0 0 0 0 x1 y1 z1 1 -v1x1 -v1y1 -v1z1] * [m12] =  [v1]
  [...                                 ]   [...]    [...]
  [...                                 ]   [ 1 ]    [...]
  
  this automatically avoids the trivial solution and the fixation
  of the term m34 will permits only one correct result, since
  now there is only 11 variables instead of 12 and this matches
  the 11 degrees of freedom of the problem.
  
  This new formulation is based on: http://www.kwon3d.com/theory/dlt/dlt.html
  
'''
def homography_2d(x, y, u, v):


  h = np.array([
    [x[0], y[0], 1, 0, 0, 0, -u[0] * x[0], - u[0] * y[0]],
    [0, 0, 0, x[0], y[0], 1, -v[0] * x[0], - v[0] * y[0]],
    [x[1], y[1], 1, 0, 0, 0, -u[1] * x[1], - u[1] * y[1]],
    [0, 0, 0, x[1], y[1], 1, -v[1] * x[1], - v[1] * y[1]],
    [x[2], y[2], 1, 0, 0, 0, -u[2] * x[2], - u[2] * y[2]],
    [0, 0, 0, x[2], y[2], 1, -v[2] * x[2], - v[2] * y[2]],
    [x[3], y[3], 1, 0, 0, 0, -u[3] * x[3], - u[3] * y[3]],
    [0, 0, 0, x[3], y[3], 1, -v[3] * x[3], - v[3] * y[3]],
  ])
  b = np.array([u[0], v[0], u[1], v[1], u[2], v[2], u[3], v[3]])

  m = np.linalg.solve(h, b)
  p = np.array([[m[0], m[1], m[2]], [m[3], m[4], m[5]], [m[6], m[7], 1]])
  # following the definition this inverse function would not be needed however, the function findHomography seems to
  # return the inverse of the matrix p found above, so to keep consistency with the already implemented code it was also
  # inverted here
  return np.linalg.inv(p)