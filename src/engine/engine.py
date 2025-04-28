import time
from core.axis import Axis
from core.figura import Figura
from core.point3d import Point3D
from engine.interface import Interface


class Engine:
    def __init__(self, 
                symbol: str="#", 
                frame_rate: int=30,
                width: int=80,
                height: int=30,
                interface: Interface=Interface(),
                angles: dict[Axis, float]={Axis.X: 2, Axis.Y: 2, Axis.Z: 2}) -> None:
        self._angles = angles
        self._tick: float = 1 / frame_rate
        self.width = width
        self.height = height
        self._interface = interface
        self._symbol = symbol

        self._clear_buffer = [[' ' for _ in range(self.width)] for _ in range(self.height)]

    #simplified coordinate system
    def _PointLocation(self, point: Point3D, scale: int=10) -> list[int]:
        return [
            int(point.x * scale + self.width // 2),
            int(point.y * scale / 2 + self.height // 2)
        ]

    #Bresenham's line algorithm
    def _DrawLine(self, buffer: list[list[str]], start: list[int], end: list[int]) -> None:

        x1, y1 = start
        x2, y2 = end

        x1 = max(0, min(x1, self.width - 1))
        y1 = max(0, min(y1, self.height - 1))
        x2 = max(0, min(x2, self.width - 1))
        y2 = max(0, min(y2, self.height - 1))

        delta_x = abs(x2 - x1)
        delta_y = abs(y2 - y1)

        step_x = 1 if x2 > x1 else -1
        step_y = 1 if y2 > y1 else -1

        error = delta_x - delta_y

        while True:
            if 0 <= x1 < self.width and 0 <= y1 < self.height:
                buffer[y1][x1] = self._symbol
            
            if x1 == x2 and y1 == y2:
                break

            error2 = error * 2

            if error2 > -delta_y:
                error -= delta_y
                x1 += step_x
            
            if error2 < delta_x:
                error += delta_x
                y1 += step_y

    def render_frame(self, figura: Figura) -> None:

            Buffer = [row.copy() for row in self._clear_buffer]

            # rotation of each point (I'll change it later)
            figura.rotate(self._angles)

            # drawing lines between connected points
            for edge in figura.edges:
            
                start = self._PointLocation(figura.vertexes[edge[0]])
                end = self._PointLocation(figura.vertexes[edge[1]])

                self._DrawLine(Buffer, start, end)
        
            #os.system('cls' if os.name == 'nt' else 'clear')
            self._interface.clear()
        
            self._interface.write('\n'.join(''.join(row) for row in Buffer))
    
            time.sleep(self._tick)

    def run(self, figura: Figura) -> None:
        while True:
            self.render_frame(figura)