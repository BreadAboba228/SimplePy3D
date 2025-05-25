import math
from typing import Self
from core.axis import Axis

class Point3D:
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0):
        self._x: float = x
        self._y: float = y
        self._z: float = z

    #functions to find the new geometry of points
    def rotate(self, axis: Axis, angle: float, center: Self) -> None:
        rad = angle * math.pi / 180
        match axis:
            case Axis.X:
                return self._rotate_x(rad, center)
            case Axis.Y:
                return self._rotate_y(rad, center)
            case Axis.Z:
                return self._rotate_z(rad, center)
            
    def _rotate_x(self, rad: float, center: Self) -> None:
        y: float = self._y - center.y
        z: float = self._z - center.z
        self._y = y * math.cos(rad) - z * math.sin(rad) + center.y
        self._z = y * math.sin(rad) + z * math.cos(rad) + center.z
    
    def _rotate_y(self, rad: float, center: Self) -> None:
        x: float = self._x - center.x
        z: float = self._z - center.z
        self._x = x * math.cos(rad) + z * math.sin(rad) + center.x
        self._z = z * math.cos(rad) - x * math.sin(rad) + center.z

    def _rotate_z(self, rad: float, center: Self) -> None:
        x: float = self._x - center.x
        y: float = self._y - center.y
        self._x = x * math.cos(rad) - y * math.sin(rad) + center.x
        self._y = y * math.cos(rad) + x * math.sin(rad) + center.y
    
    @property
    def x(self) -> float:
        return self._x
    
    @property
    def y(self) -> float:
        return self._y
    
    @property
    def z(self) -> float:
        return self._z