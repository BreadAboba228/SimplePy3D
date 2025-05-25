from core.figura import Figura
from core.point3d import Point3D


class Cube(Figura):
    def __init__(self, center: Point3D = Point3D(), edge_length: float = 4):
        
        half_edge = edge_length / 2
        vertexes: dict[str | int, Point3D] = dict()

        x_range = [center.x - half_edge, center.x + half_edge]
        y_range = [center.y - half_edge, center.y + half_edge]
        z_range = [center.z - half_edge, center.z + half_edge]

        i = 0
        for x in x_range:
            for y in y_range:
                for z in z_range:
                    vertexes[i] = Point3D(x, y, z)
                    i += 1
  
        edges: list[tuple[str | int, str | int]] = [
            (0, 1), (0, 2), (0, 4), (1, 3),
            (1, 5), (2, 3), (2, 6), (3, 7),
            (4, 5), (4, 6), (5, 7), (6, 7)
        ]

        super().__init__(vertexes, edges, center)