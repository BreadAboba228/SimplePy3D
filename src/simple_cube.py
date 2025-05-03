from core.camera import Camera
from geometry.cube import Cube
from engine.engine import Engine

if __name__ == "__main__":
    app = Engine(camera=Camera(fov=120))
    cube = Cube()
    app.run(cube)