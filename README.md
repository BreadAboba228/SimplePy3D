# SimplePy3D 
![example_cube](https://github.com/BreadAboba228/SimplePy3D/blob/master/docs/example_cube.gif)
![Exam custom figura](https://github.com/BreadAboba228/SimplePy3D/blob/master/docs/exam_custom_figura.png)


---

A simple Python library for rendering 3D wireframe models in the console using ASCII art. Perfect for nostalgic developers and terminal enthusiasts.

---

## 📦 Installation

```bash
git clone https://github.com/BreadAboba228/SimplePy3D.git
cd SimplePy3D
```
## 🚀 Quick Start
### Basic Cube Example
```python
from geometry.cube import Cube
from engine.engine import Engine

  

if __name__ == "__main__":
    app = Engine()
    сube = Cube()
    app.run(сube)
```
### Advanced Custom Figure
```python
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
```

---

## 🔧 API Reference
### Point3D Configuration
**`from core.point3d import Point3D`**
#### Parameters

| Parameter | Description  |
| --------- | ------------ |
| x         | x coordinate |
| y         | y coordinate |
| z         | z coordinate |
#### Methods

| Method | Parameters                                | Description                                        |
| ------ | ----------------------------------------- | -------------------------------------------------- |
| rotate | axis: Axis, angle: float, center: Point3D | rotates a point by an angle relative to the center |

### Engine Configuration
**`from engine.engine import Engine`**
#### Paremeters

| Parameter  | Default                           | Description                            |
| ---------- | --------------------------------- | -------------------------------------- |
| symbol     | "#"                               | ASCII character for rendering          |
| frame_rate | 30                                | Target FPS (console limitations apply) |
| width      | 80                                | Terminal width in characters           |
| height     | 30                                | Terminal height in characters          |
| angle      | {Axis.X: 2, Axis.Y: 2, Axis.Z: 2} | Angle of rotation of the figure        |
| interface  | Interface()                       | Integration class                      |
#### Methods

| Method         | Paremeter      | Description                    |
| -------------- | -------------- | ------------------------------ |
| render_frame() | figura: Figura | Rotates and draws the figure   |
| run()          | figura: Figura | Starts animation of the figure |


---

### Interface Configuration
**`from engine.interface import Interface`**
#### Parameters

| Parameter    | Default                                          | Description          |
| ------------ | ------------------------------------------------ | -------------------- |
| input_method | print                                            | Text output function |
| clear_method | os.system("cls" if os.name == "nt" else "clear") | Text clear function  |
#### Methods

| Method  | Paremeter | Return | Description                              |
| ------- | --------- | ------ | ---------------------------------------- |
| write() | str       | None   | Writes to the console using input_method |
| clear() | None      | None   | Clear the console using clear_method     |

### Figura Configuration
**`from core.figura import Figura`**
#### Paremeters

| Parameter | Type                                 | Description                                     |
| --------- | ------------------------------------ | ----------------------------------------------- |
| vertexes  | dict(str \| int,Point3D)             | name and location of the vertices of the figure |
| edges     | list(tuple((str \| int, str \| int)) | connecting vertices using their names           |
| center    | Point3D                              | Center of rotation                              |
### Cube Configuration 
**`from geometry.cube import Cube`**
#### Parameters

| Parameter   | Type    | Description        |
| ----------- | ------- | ------------------ |
| edge_length | float   | Edge length        |
| center      | Point3D | Center of rotation |


---

## ⚠️ Known Issues
- Terminal flickering on Windows 
- Z-fighting artifacts at certain angles

---

License: MIT. Rotate responsibly! 🌀
