from unittest.mock import patch
from pynput.mouse import Button
from mouse import Mouse


@patch('pynput.mouse.Controller.click')
def test_mouse_action_left_click(mock_controller):
    mouse = Mouse()
    mouse.action(
        'CLICK',
        {'button': 'left'}
    )
    mock_controller.assert_called_with(Button.left, 1)


@patch('pynput.mouse.Controller.click')
def test_mouse_action_left_click_twice(mock_controller):
    mouse = Mouse()
    mouse.action(
        'CLICK',
        {'button': 'left', 'click_number': 2}
    )
    mock_controller.assert_called_with(Button.left, 2)


@patch('pynput.mouse.Controller.click')
def test_mouse_action_right_click(mock_controller):
    mouse = Mouse()
    mouse.action(
        'CLICK',
        {'button': 'right'}
    )
    mock_controller.assert_called_with(Button.right, 1)


@patch('pynput.mouse.Controller._position_set')
def test_mouse_action_set_position(mock_controller):
    mouse = Mouse()
    mouse.action(
        'SET_POSITION',
        {'x_position': 100, 'y_position': 200}
    )
    mock_controller.assert_called_with((100, 200, ))

@patch('pynput.mouse.Controller.move')
def test_mouse_action_move(mock_controller):
    mouse = Mouse()
    mouse.action(
        'MOVE',
        {'x_move': 100, 'y_move': 200}
    )
    mock_controller.assert_called_with(100, 200)
