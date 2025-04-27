from core.figura import Figura
from core.point3d import Point3D


class Cube(Figura):
    def __init__(self, center: Point3D, edge_lenth: float):
        
        self._center = center
        self._radius = edge_lenth / 2
        self._vertexes: list[Point3D] = list()

        x_range = [self._center.x - self._radius, self._center.x + self._radius]
        y_range = [self._center.y - self._radius, self._center.y + self._radius]
        z_range = [self._center.z - self._radius, self._center.z + self._radius]

        for x in x_range:
            for y in y_range:
                for z in z_range:
                    self._vertexes.append(Point3D(x, y, z))
  
        self._edges: list[tuple[int, int]] = [
            (0, 1), (0, 2), (0, 4), (1, 3),
            (1, 5), (2, 3), (2, 6), (3, 7),
            (4, 5), (4, 6), (5, 7), (6, 7)
        ]