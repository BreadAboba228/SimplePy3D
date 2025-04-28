import math
from typing import Self
from core.axis import Axis

class Point3D:
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0):
        self._x, self._y, self._z = x, y, z

    #functions to find the new geometry of points
    def rotate(self, axis: Axis, angle: float, center: Self) -> Self:
        rad = angle * math.pi / 180
        match axis:
            case Axis.X:
                return self._rotate_x(rad, center)
            case Axis.Y:
                return self._rotate_y(rad, center)
            case Axis.Z:
                return self._rotate_z(rad, center)
            
    def _rotate_x(self, rad: float, center: Self) -> Self:
        y = self._y - center.y
        z = self._z - center.z
        new_y: float = y * math.cos(rad) - z * math.sin(rad) + center.y
        new_z: float = y * math.sin(rad) + z * math.cos(rad) + center.z
        return self.__class__(self._x, new_y, new_z)
    
    def _rotate_y(self, rad: float, center: Self) -> Self:
        x = self._x - center.x
        z = self._z - center.z
        new_x = x * math.cos(rad) + z * math.sin(rad) + center.x
        new_z = z * math.cos(rad) - x * math.sin(rad) + center.z
        return self.__class__(new_x, self._y, new_z)

    def _rotate_z(self, rad: float, center: Self) -> Self:
        x = self._x - center.x
        y = self._y - center.y
        new_x = x * math.cos(rad) - y * math.sin(rad) + center.x
        new_y = y * math.cos(rad) + x * math.sin(rad) + center.y
        return self.__class__(new_x, new_y, self._z)
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @property
    def z(self):
        return self._z