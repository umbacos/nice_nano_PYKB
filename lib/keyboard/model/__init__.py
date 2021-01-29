from .ut47 import Matrix, COORDS, battery_level

# fmt: off
KEY_NAME =  (
    'ESC', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'BACKSPACE',
    'TAB', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', 'ENTER',
    'LSHIFT', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', 'UP', 'RSHIFT',
    'LCTRL', 'LGUI', 'LALT', 'FN', 'FN', 'SPACE', 'FN', 'FN', 'LEFT', 'DOWN', 'RIGHT'
)
# fmt: on


def key_name(key):
    return KEY_NAME[COORDS[key]]
