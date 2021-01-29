import analogio
import microcontroller

try:
    # usebuilt-in matrix if it is available
    from matrix import Matrix
except ImportError:
    from ..matrix import Matrix
    from board import *

    Matrix.ROWS = (P0_17, P0_20, P0_22, P0_24)
    Matrix.COLS = (P1_00, P0_11, P1_04, P1_06, P0_09, P0_10, P1_01, P1_13, P1_15, P0_02, P0_29, P0_31)
    Matrix.ROW2COL = False

# fmt: off
# ESC   Q   W   E   R   T   Y   U   I   O   P   BACKSPACE
# TAB   A   S   D   F   G   H   J   K   L   ;   ENTER
#LSHIFT Z   X   C   V   B   N   M   ,   .   UP  RSHIFT
# LCTRL LGUI LALT  NAV NUM_SYM  SPACE  empty NUM_SYM NAV  LEFT DOWN RIGHT
COORDS = (
    0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11,
   12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
   24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
   36, 37, 38, 39, 40, 41, -1, 42, 43, 44, 45, 46
)


BATTERY_LIMIT = 3100  # Cutoff voltage [mV].
BATTERY_FULLLIMIT = 4190  # Full charge definition [mV].
BATTERY_DELTA = 10  # mV between each element in the SoC vector.

BATTERY_VOLTAGE = (
    0,  0,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  2,
    2,  2,  2,  2,  2,  2,  2,  2,  3,  3,  3,  3,  3,  3,  3,  4,  4,  4,  4,  4,
    4,  5,  5,  5,  6,  6,  7,  7,  8,  8,  9,  9, 10, 11, 12, 13, 13, 14, 15, 16,
    18, 19, 22, 25, 28, 32, 36, 40, 44, 47, 51, 53, 56, 58, 60, 62, 64, 66, 67, 69,
    71, 72, 74, 76, 77, 79, 81, 82, 84, 85, 85, 86, 86, 86, 87, 88, 88, 89, 90, 91,
    91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 100
)

battery_in = analogio.AnalogIn(microcontroller.pin.P0_04)


def battery_level():
    # (3300 * 2 * battery.value) >> 16
#    voltage = (3300 * battery_in.value) >> 15
    voltage = ((len(BATTERY_VOLTAGE) * 3300 * battery_in.value) //100) >> 15
    i = (voltage - BATTERY_LIMIT) // BATTERY_DELTA
    if i >= len(BATTERY_VOLTAGE):
        i = len(BATTERY_VOLTAGE) - 1
    elif i < 0:
        i = 0
    return BATTERY_VOLTAGE[i]
