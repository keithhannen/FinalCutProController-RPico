# IMPORTS
import board


from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.matrix import DiodeOrientation
# from kmk.matrix import intify_coordinate as ic

# DEFINE ROW & COLUMN PINS, DEFINE DIODE ORIENTATION
class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        board.GP5,
        board.GP6,
        board.GP7,
        board.GP8,
        board.GP9,
    )

    row_pins = (board.GP2, board.GP3, board.GP4)

    diode_orientation = DiodeOrientation.COLUMNS