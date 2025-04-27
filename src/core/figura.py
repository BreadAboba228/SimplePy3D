from core.point3d import Point3D

#shape class
class Figura:
    def __init__(self, vertexes: list[Point3D], edges: list[tuple[int, int]], center: Point3D):
        self._vertexes = vertexes
        self._edges = edges
        self._center = center

    @property
    def vertexes(self):
        return self._vertexes
    
    @property
    def edges(self):
        return self._edges
    
    @property
    def center(self):
        return self._center