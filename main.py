"""
Run this script to start mouse actoons from mouse.json file.
"""
import json
from mouse import Mouse


def main() -> None:
    mouse = Mouse()
    json_file = 'mouse.json'
    with open(json_file, 'r', encoding='UTF-8') as file:
        mouse_script = json.load(file)

    for event in mouse_script:
        mouse.action(
            event.get('action'),
            event.get('params'),
            event.get('sleep_time', 0.5)
        )


if __name__ == '__main__':
    main()
