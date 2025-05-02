from geometry.cube import Cube
from engine.engine import Engine

if __name__ == "__main__":
    app = Engine()
    cube = Cube()
    app.run(cube)