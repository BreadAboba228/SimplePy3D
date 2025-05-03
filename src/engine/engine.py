import time
from core.axis import Axis
from core.camera import Camera
from core.figura import Figura
from engine.interface import Interface
from render.wireframe import render_frame

class Engine:
    def __init__(
            self, 
            symbol: str="#", 
            frame_rate: int = 30,
            width: int = 80,
            height: int = 30,
            interface: Interface = Interface(),
            angles: dict[Axis, float] = {Axis.X: 2, Axis.Y: 2, Axis.Z: 2},
            camera: Camera = Camera()
    ) -> None:
        
        self._angles = angles
        self._tick: float = 1 / frame_rate
        self._width = width
        self._height = height
        self._interface = interface
        self._symbol = symbol
        self._camera = camera

        self._clear_buffer = [[' ' for _ in range(self._width)] for _ in range(self._height)]

    def run(self, figura: Figura) -> None:
        
        while True:

            buffer = [row.copy() for row in self._clear_buffer]

            render_frame(
                figura,
                buffer,
                self._angles,
                self._height,
                self._width,
                self._symbol,
                self._camera
            )
            
            self._interface.clear()
        
            self._interface.write('\n'.join(''.join(row) for row in buffer))
    
            time.sleep(self._tick)