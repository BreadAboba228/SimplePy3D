import os
from typing import Any, Callable

class Interface:
    def __init__(
            self, 
            input_method: Callable[[str], None] = print, 
            clear_method: Callable[[], Any] = lambda: os.system("cls" if os.name == "nt" else "clear")
        ) -> None:
        
        self._input_method = input_method
        self._clear_method = clear_method

    def write(self, text: str) -> None:
        self._input_method(text)

    def clear(self) -> None:
        self._clear_method()
