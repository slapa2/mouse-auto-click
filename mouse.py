"""
mouse auto click
"""
from enum import Enum, auto
from time import sleep
from typing import Dict
from pynput.mouse import Controller, Button


class MouseAction(Enum):
    """ mouse actions """
    SET_POSITION = auto()
    CLICK = auto()
    MOVE = auto()


class Mouse:
    """
    mous controler class
    """
    def __init__(self) -> None:
        self._controller = Controller()
        self._actions = {
            MouseAction.SET_POSITION: self._set_position,
            MouseAction.CLICK: self._click,
            MouseAction.MOVE: self._move,
        }

    def action(self, action: str, params: Dict = None, sleep_time: int = 0.5) -> None:
        """ this metod executs action with given parameters

        Args:
            action (MouseAction): action to execute
            params (Dict, optional): action params
            sleep_time (int, optional): time to sleep after mouse action. Defaults to 0.5.
        """
        if params is None:
            params = {}
        self._actions[MouseAction[action]](**params)
        sleep(sleep_time)

    def _set_position(self, *, x_position, y_position) -> None:
        self._controller.position = (x_position, y_position)

    def _click(self, *, button: str, click_number: int = 1) -> None:
        self._controller.click(Button[button], click_number)

    def _move(self, *, x_move: int, y_move: int) -> None:
        self._controller.move(x_move, y_move)
