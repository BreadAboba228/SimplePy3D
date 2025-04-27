from core.point3d import Point3D
from core.figura import Figura
from engine.engine import Engine

if __name__ == "__main__":
    custom_figura = Figura(
        [
            Point3D(-3, -2, -1), #0
            Point3D(-3, 0, -1),  #1
            Point3D(-3, 0, 1),   #2
            Point3D(-3, -2, 1),  #3
            Point3D(0, 0, -1),   #4
            Point3D(0, 0, 1),    #5
            Point3D(0, 3, 1),    #6
            Point3D(2, 3, 1),    #7
            Point3D(2, -2, 1),   #8
            Point3D(2, -2, -1),  #9
            Point3D(0 , 3, -1),  #10
            Point3D(2, 3, -1)    #11
        ],
        [
            (0, 1), (0, 3), (0, 9), (1, 2),
            (1, 4), (2, 3), (2, 5), (3, 8),
            (4, 5), (4, 10), (5, 6), (6, 10),
            (6, 7), (7, 8), (7, 11), (8, 9),
            (9, 11), (10, 11)
        ],
        Point3D(0, 0, 0)
    )

    app = Engine(
        symbol="+",
        frame_rate=25,
        width=100,
        height=35,
        angle=1.5
    )

    app.run(custom_figura)