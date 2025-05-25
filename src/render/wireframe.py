from core.axis import Axis
from core.figura import Figura
from core.point3d import Point3D
from render.LineAlgorithm import draw_line


def render_frame(figura: Figura, 
                 buffer: list[list[str]], 
                 angles: dict[Axis, float],
                 height: int,
                 width: int,
                 symbol: str,
                 camera: Point3D) -> None:

    figura.rotate(angles)

    for edge in figura.edges:
    
        start = point_location(figura.vertexes[edge[0]], camera, height, width)
        end = point_location(figura.vertexes[edge[1]], camera, height, width)

        draw_line(buffer, start, end, width, height, symbol)



def point_location(point: Point3D,
                    camera: Point3D,
                    height: int,
                    width: int,
                    scale: int=10,) -> list[int]:
        min_distance = 0.1
        distance = max(camera.z - point.z, min_distance)
        z_coeff = 3 / distance
        return [
            int(point.x * scale * z_coeff + width // 2),
            int(point.y * scale * z_coeff / 2 + height // 2)
        ]