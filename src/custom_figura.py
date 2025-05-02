from core.axis import Axis
from core.point3d import Point3D
from core.figura import Figura
from engine.engine import Engine

if __name__ == "__main__":
    custom_figura = Figura(
        vertexes={
            1: Point3D(-3, 2, -1),
            2: Point3D(-3, 2, 1),
            3: Point3D(2, 2, -1),
            4: Point3D(2, 2, 1),
            5: Point3D(-3, 0, -1),
            6: Point3D(-3, 0, 1),
            7: Point3D(0, 0, -1),
            8: Point3D(0, 0, 1),
            9: Point3D(0, -3, -1),
            10: Point3D(0, -3, 1),
            11: Point3D(2, -3, -1),
            12: Point3D(2, -3, 1)
        },
        edges=[
            (1, 2), (1, 3), (1, 5), (2, 4),
            (2, 6), (3, 4), (3, 11), (4, 12),
            (5, 6), (5, 7), (6, 8), (7, 8),
            (7, 9), (8, 10), (9, 10), (9, 11), 
            (10, 12), (11, 12)
        ],
        center=Point3D(0, 0, 0)
    )

    app = Engine(
        symbol="+",
        frame_rate=25,
        width=100,
        height=35,
        angles={
            Axis.X: 1.5,
            Axis.Y: 1.5,
            Axis.Z: 1.5
        }
    )

    app.run(custom_figura)