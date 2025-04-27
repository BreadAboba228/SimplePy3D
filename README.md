# SimplePy3D 
![Exam custom figura](https://github.com/BreadAboba228/SimplePy3D/blob/master/docs/exam_custom_figura.png)
![example_cube](https://github.com/BreadAboba228/SimplePy3D/blob/master/docs/example_cube.gif)

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
from core.point3d import Point3D
from geometry.cube import Cube
from engine.engine import Engine

if __name__ == "__main__":
    app = Engine()
    cube = Cube(center=Point3D(0, 0, 0), edge_length=3)
    app.run(figure=cube)
```
### Advanced Custom Figure
```python
from core.point3d import Point3D
from core.figura import Figura
from engine.engine import Engine

if __name__ == "__main__":

    custom_figura = Figura(
        [
            Point3D(-3, -2, -1), #0
            Point3D(-3, 0, -1),  #1
            Point3D(-3, 0, 1),   #2
            Point3D(-3, -2, 1),  #3
            Point3D(0, 0, -1),   #4
            Point3D(0, 0, 1),    #5
            Point3D(0, 3, 1),    #6
            Point3D(2, 3, 1),    #7
            Point3D(2, -2, 1),   #8
            Point3D(2, -2, -1),  #9
            Point3D(0 , 3, -1),  #10
            Point3D(2, 3, -1)    #11
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
```

---

## 🔧 API Reference

### Engine Configuration
**`from engine.engine import Engine`**
#### Paremeters

| Parameter  | Default     | Description                            |
| ---------- | ----------- | -------------------------------------- |
| symbol     | "#"         | ASCII character for rendering          |
| frame_rate | 30          | Target FPS (console limitations apply) |
| width      | 80          | Terminal width in characters           |
| height     | 30          | Terminal height in characters          |
| angle      | 2           | Angle of rotation of the figure        |
| interface  | Interface() | Integration class                      |
#### Methods

| Method         | Paremeter | Return        | Description                                                                 |
| -------------- | --------- | ------------- | --------------------------------------------------------------------------- |
| render_frame() | Figura()  | list(Point3D) | Rotates and draws the figure and returns the rotated vertices of the figure |
| run()          | Figura()  | None          | Starts animation of the figure                                              |


---

### Interface Configuration
**`from engine.interface import Interface`**
#### Parameters

| Parameter    | Default                                     | Description          |
| ------------ | ------------------------------------------- | -------------------- |
| input_method | print                                       | Text output function |
| clear_method | os.system("cls" if os == "nt" else "clear") | Text clear function  |
#### Methods

| Method  | Paremeter | Return | Description                              |
| ------- | --------- | ------ | ---------------------------------------- |
| write() | str       | None   | Writes to the console using input_method |
| clear() | None      | None   | Clear the console using clear_method     |

### Figura Configuration
**`from core.figura import Figura`**
#### Paremeters

| Parameter | Type                  | Description                   |
| --------- | --------------------- | ----------------------------- |
| vertexes  | list(Point3D)         | Figura vertices               |
| edges     | list(tuple(int, int)) | Figura edges between vertexes |
| center    | Point3D               | Center of rotation            |
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
