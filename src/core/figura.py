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

    def rotate(self, angles: dict[Axis, float]) -> None:
        for axis, angle in angles.items():
            for vertex in self._vertexes.values():
                vertex.rotate(axis, angle, self._center)

    @property
    def vertexes(self) -> dict[str | int, Point3D]:
        return self._vertexes
    
    @property
    def edges(self) -> list[tuple[str | int, str | int]]:
        return self._edges
    
    @property
    def center(self) -> Point3D:
        return self._center