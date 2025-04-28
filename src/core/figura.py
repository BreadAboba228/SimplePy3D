from core.axis import Axis
from core.point3d import Point3D

#shape class
class Figura:
    def __init__(self, vertexes: dict[str | int, Point3D], 
                 edges: list[tuple[str | int, str | int]], 
                 center: Point3D):
        
        self._vertexes: dict[str | int, Point3D] = vertexes
        self._edges: list[tuple[str | int, str | int]] = edges
        self._center: Point3D = center

    def rotate(self, angles: dict[Axis, float]):
        for axis, angle in angles.items():
            self._vertexes = {
                name: vertex.rotate(axis, angle, self._center)
                for name, vertex in self._vertexes.items()
            }

    @property
    def vertexes(self):
        return self._vertexes
    
    @property
    def edges(self):
        return self._edges
    
    @property
    def center(self):
        return self._center