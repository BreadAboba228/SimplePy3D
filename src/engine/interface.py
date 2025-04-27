import os
from typing import Any, Callable

class Interface:
    def __init__(self, input_method: Callable[[str], None] = print, 
        clear_method: Callable[[], Any] = lambda: os.system("cls" if os.name == "nt" else "clear")) -> None:
        self._input_method = input_method
        self._clear_method = clear_method

    def write(self, text: str) -> None:
        self._input_method(text)

    def clear(self) -> None:
        self._clear_method()

class Engine:
    def __init__(self, symbol: str="#", frame_rate: int=30, width: int=80, height: int=30, interface: Interface=Interface(),
                 angle: float=2) -> None:
        self._angle = angle
        self._tick: float = 1 / frame_rate
        self.width = width
        self.height = height
        self._interface = interface
        self._symbol = symbol

        self._clear_buffer = [[' ' for _ in range(self.width)] for _ in range(self.height)]