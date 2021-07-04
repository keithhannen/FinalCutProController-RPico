from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.handlers.sequences import send_string, simple_key_sequence
import board
import digitalio

keyboard = KMKKeyboard()

# CUSTOM KEY DEFINITIONS
#   these are separated into "SWITCHES" and "ROTARIES" for organization only. Functionally, they are
#   identical in that any key function can be placed on either a switch or rotary increment/decrement.
#   EX: VolumeUp could be assinged to a switch and/or rotary direction.
#
#   Key codes can be found at https://raw.githubusercontent.com/KMKfw/kmk_firmware/master/docs/keycodes.md
#
#   MAC OS:
#           Control key = LCTL
#           Option key = LALT or RALT
#           Command key = LGUI or RGUI
#-----------------------------------------------------------------------------------------------------
## SWITCHES
_______ = KC.TRNS                       # transparent space in layer map (uses function on lower map)
XXXXXXX = KC.NO                         # no key info, no response to activation of switch
AudioFX = KC.LALT(KC.LGUI(KC.E))        # apply default audio effect
_Blade_ = KC.LGUI(KC.B)                 # cut clip
_Copy__ = KC.LGUI(KC.C)                 # copy selection
DefTrns = KC.LGUI(KC.T)                 # apply default transition
Delete_ = KC.DEL                        # delete selection
Exp_Aud = KC.LCTL(KC.LALT(KC.S))        # expand/contract audio components
KeyFram = KC.LALT(KC.K)                 # mark keyframe
Marker_ = KC.M                          # place a marker
_Paste_ = KC.LGUI(KC.V)                 # paste contents of clipboard
Rng_In_ = KC.I                          # mark range start
Rng_Out = KC.O                          # mark range end
## ROTARIES
CoarseSF = KC.LSFT(KC.RGHT)             # coarse scrub forward
CoarseSR = KC.LSFT(KC.LEFT)             # coarse scrub reverse
FineSFwd = KC.RGHT                      # fine scrub forward
FineSRev = KC.LEFT                      # fine scrub reverse
VolumeUp = KC.LCTL(KC.EQUAL)            # raise volume of selection +1dB
VolumeDn = KC.LCTL(KC.MINUS)            # lower volume of selection -1dB
_ZoomIn_ = KC.LCTL(KC.EQUAL)
_ZoomOut = KC.LCTL(KC.MINUS)

# Encoder map
encoder_map = [
    [# LAYER 1
        (CoarseSF,CoarseSR,2), (FineSFwd,FineSRev,2), (VolumeUp,VolumeDn,2)
    ],
    [# LAYER 2
        (CoarseSF,CoarseSR,2), (FineSFwd,FineSRev,2), (_ZoomIn_,_ZoomOut,2)
    ],
]

layers_ext = Layers()

encoder_ext = EncoderHandler([board.GP10, board.GP12, board.GP21],[board.GP11, board.GP13, board.GP20], encoder_map)
encoder_ext.encoders[0].is_inverted = False
encoder_ext.encoders[1].is_inverted = False
encoder_ext.encoders[2].is_inverted = False

keyboard.modules = [layers_ext, encoder_ext]

keyboard.tap_time = 250
keyboard.debug_enabled = False

# KEYMAP
keyboard.keymap = [
    [# LAYER 0 The default layer
        _Copy__,    Rng_In_,    AudioFX,    XXXXXXX,    Delete_,
        _Paste_,    Rng_Out,    DefTrns,    XXXXXXX,    XXXXXXX,
        KC.MO(1),   KC.SPACE,   Marker_,    KeyFram,    XXXXXXX,
    ],
    [# LAYER 1 The first alternative layer
        _Copy__,    Rng_In_,    AudioFX,    XXXXXXX,    Delete_,
        _Paste_,    Rng_Out,    DefTrns,    XXXXXXX,    XXXXXXX,
        _______,    _Blade_,    Marker_,    KeyFram,    XXXXXXX,
    ],
]

# TURN ON LED
led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT
led.value = True

if __name__ == "__main__":
    keyboard.go()