from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.handlers.sequences import send_string, simple_key_sequence
import board
import digitalio

# local_increment = None
# local_decrement = None

keyboard = KMKKeyboard()

# custom keys used for encoder actions
Zoom_in = KC.LCTL(KC.EQUAL)
Zoom_out = KC.LCTL(KC.MINUS)

# standard filler keys
_______ = KC.TRNS
XXXXXXX = KC.NO

# for use in the encoder extension
encoder_map = [
    [# LAYER 1
        (Zoom_in,Zoom_out,2), (Zoom_in,Zoom_out,2), (Zoom_in,Zoom_out,2)
    ]
]

layers_ext = Layers()

encoder_ext = EncoderHandler([board.GP10, board.GP12, board.GP21],[board.GP11, board.GP13, board.GP20], encoder_map)
encoder_ext.encoders[0].is_inverted = False
encoder_ext.encoders[1].is_inverted = False
encoder_ext.encoders[2].is_inverted = False

keyboard.modules = [layers_ext, encoder_ext]

keyboard.tap_time = 250
keyboard.debug_enabled = False

# make keymap
keyboard.keymap = [
    [# LAYER 1
        KC.ESC, KC.N1,  KC.N2,  KC.N3,  KC.N4,
        KC.N5,  KC.N6,  KC.N7,  KC.N8,  KC.N9,
        KC.Q,   KC.W,   KC.E,   KC.R,   KC.T,
    ],
]

# TURN ON LED
led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT
led.value = True

if __name__ == "__main__":
    keyboard.go()