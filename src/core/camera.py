import math


class Camera:
    def __init__(
            self,
            fov: float = 90,
            aspect_ratio: float = 16/9,
            near: float = 0.1,
            far: float = 1000
    ) -> None:
        
        self._fov = math.radians(fov)
        self._aspect = aspect_ratio
        self._near = near
        self._far = far

        self.projection_matrix = self._create_projection_matrix()

    def _create_projection_matrix(self) -> list[list[float]]:

        tan_half_fov = math.tan(self._fov / 2)

        return [
            [1 / (self._aspect * tan_half_fov), 0, 0, 0],
            [0, 1 / tan_half_fov, 0, 0],
            [0, 0, -(self._far + self._near) / (self._far - self._near), -1],
            [0, 0, -2 * self._far * self._near / (self._far - self._near), 0]
        ]