# mouse-auto-click
json based mouse control

this program allows yuou sto save mouse control macro in json file 

save write your macro in `mouse.json` file and run with `python3 main.py` command

## mouse.json file structure:

this file should contains list of objects (actions)

### action object structure:
```
{
    "action": "SET_POSITION",
    "params": {
        "x_position": 123,
        "y_position": 456
    },
    "sleep_time": 3
}
```
### possible actions:
SET_POSITION - set absolut cursor position

MOVE - move relative from current cursor position

CLICK - click mouse button in current possition

### action params:
SET_POSITION:
    x_position: integer, y_position: integer

MOVE:
    x_move: integer, y_move: integer

CLICK: button: ["left"/"right"], click_number: integer

### sleep_time: integer or number
time to vait after action it is optional parameter defalut value = 0.5s


project inspired by [pycamp.pl](https://www.pycamp.pl/)
