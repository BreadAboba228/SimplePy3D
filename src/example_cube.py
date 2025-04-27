from core.point3d import Point3D
from geometry.cube import Cube
from engine.engine import Engine

if __name__ == "__main__":
    app = Engine()
    cube = Cube(center=Point3D(0, 0, 0), edge_lenth=3)
    app.run(figura=cube)