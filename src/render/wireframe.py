from core.axis import Axis
from core.camera import Camera
from core.figura import Figura
from core.point3d import Point3D
from render.LineAlgorithm import draw_line


def render_frame(
        figura: Figura, 
        buffer: list[list[str]], 
        angles: dict[Axis, float],
        height: int,
        width: int,
        symbol: str,
        camera: Camera
    ) -> None:

    figura.rotate(angles)

    for edge in figura.edges:
    
        start = point_location(figura.vertexes[edge[0]], camera, height, width)
        end = point_location(figura.vertexes[edge[1]], camera, height, width)

        draw_line(buffer, start, end, width, height, symbol)



def point_location(
        point: Point3D,
        camera: Camera,
        height: int,
        width: int,
        scale: int=10
    ) -> tuple[int, int]:
        
        x, y, z = point.x, point.y, point.z
        homogenerous: list[float] = [x, y, z, 1]

        projected: list[float] = [
            sum(homogenerous[i] * camera.projection_matrix[0][i]  for i in range(4)),
            sum(homogenerous[i] * camera.projection_matrix[1][i] for i in range(4)),
            sum(homogenerous[i] * camera.projection_matrix[2][i] for i in range(4)),
            sum(homogenerous[i] * camera.projection_matrix[3][i] for i in range(4))
        ]

        if projected[3] != 0:
            x_proj = projected[0] / projected[3]
            y_proj = projected[1] / projected[3]
        else:
            return (0, 0)
        
        screen_x = int((x_proj + 1) * 0.5 * width)
        screen_y = int((1 - y_proj) * 0.5 * height)

        return (screen_x, screen_y)