import numpy as np

class Point:
  def __init__(self, coords):
    self.coords = coords

  def to_world(self, matrix):
    # Convert to homogeneous coords
    array = np.append(self.coords, [1])

    # Multiply by the matrix
    out = matrix.dot(array)

    coords = []
    for index in range(0, len(out)-1):
      # Convert back to normal coords;
      coords.append(out[index]/out[-1])

    return Point(coords)

  def to_pixel(self, matrix):
    # Calculate inverse matrix
    matrix = np.linalg.inv(matrix)

    # Convert to homogeneous coords
    array = np.append(self.coords, [1])

    # Multiply by the matrix
    out = matrix.dot(array)

    coords = []
    for index in range(0, len(out)-1):
      # Convert back to normal coords;
      coords.append(int(round(out[index]/out[-1])))

    return Point(coords)

  def __str__(self):
    coords = self.coords
    if len(coords) == 2:
      return '[X, Y] = [{}, {}]'.format(coords[0], coords[1])
    else:
      return '[X, Y, Z] = [{}, {}, {}]'.format(coords[0], coords[1], coords[2])

  def __repr__(self):
    coords = self.coords
    if len(coords) == 2:
      return '[X, Y] = [{}, {}]'.format(coords[0], coords[1])
    else:
      return '[X, Y, Z] = [{}, {}, {}]'.format(coords[0], coords[1], coords[2])

  @property
  def x(self):
    return self.coords[0]

  @property
  def y(self):
    return self.coords[1]

  @property
  def z(self):
    return self.coords[2]