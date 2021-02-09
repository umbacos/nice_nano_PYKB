from keyboard import *

# Utilities
___ = TRANSPARENT
XXX = NO
BOOT = BOOTLOADER
_S = lambda a: MODS_KEY(MODS(RSHIFT), a) # hold SHIFT  + tap character
_A = lambda a: MODS_KEY(MODS(RALT), a)   # hold ALT    + tap character
_C = lambda a: MODS_KEY(MODS(RCTRL), a)  # hold CONTROL+ tap character
LT = lambda a,b=None: LAYER_TAP(a,b)     # layer "a" if held, "b" if tapped (b is optional)
MT = lambda a,b: MODS_TAP(MODS(a),b)     # modifier "a" if held, "b" if tapped

# ITALIAN CHARMAP FOR ANSI LAYOUT
# Set the computer in the Italian keyboard input mode
IT_EGRV='['
IT_AGRV='\''
IT_UGRV='\\'
IT_IGRV='='
IT_OGRV=';'
IT_EURO=_A(E)
IT_EXCL=_S(1)
IT_AT  =_A(';')
IT_SHRP=_A('\'')
IT_DOLL=_S(4)
IT_PERC=_S(5)
IT_POWE=_S('=')
IT_ECOM=_S(6)
IT_STAR=_S(']')
IT_LPAR=_S(8)
IT_RPAR=_S(9)
IT_EQAL=_S(0)
IT_MINU='/'
IT_PLUS=']'
IT_UNDS=_S('/')
IT_LSQR=_A('[')
IT_RSQR=_A(']')
IT_LBRK=_A(_S('['))
IT_RBRK=_A(_S(']'))
IT_SCLN=_S(',')
IT_COLN=_S('.')
IT_QUOT='-'
IT_DQUO=_S(2)
IT_COMM=','
IT_FULL='.'
IT_SLSH=_S(7)
IT_QSTN=_S('-')
IT_MINO='`'
IT_MAJO=_S('`')
IT_BSLS=0x64     # Non US backslash \
IT_PIPE=_S(0x64) # Non US pipe |

# layer definitions
QWERT=0
SHIFT=1
NUMBE=2
SYMBO=3
FUNCT=4
BLUET=5
ACCEN=6
MOUSE=7
NAVIG=8

keyboard = Keyboard()
keyboard.keymap = (
    # layer 0 QWERT: remapped to match the ANSI layout with the Italian keyboard on the computer
    (
        ESC,   Q,   W,   E,   R,   T,   Y,   U,   I,   O,   P, BACKSPACE,
        MT(LSHIFT, TAB),  A,   S, LT(NAVIG,D), F,   G,   H,   J,   K,   L, IT_SCLN, MT(RSHIFT, ENTER),
        LT(SHIFT, DEL),  Z,   X,   C,   V, LT(BLUET, B),   N,   M, IT_COMM, IT_FULL, UP, LT(SHIFT, IT_SLSH),
        LCTRL, LALT, LT(FUNCT), LGUI, LT(NUMBE),      LT(ACCEN, SPACE),   LT(SYMBO), LT(NAVIG, IT_QUOT),  LEFT, DOWN, RIGHT
    ),

    # layer 1 SHIFT: remapped to match the ANSI layout with the Italian keyboard on the computer
    (
        ESC, _S(Q), _S(W),   _S(E),   _S(R),   _S(T),   _S(Y),   _S(U),   _S(I),   _S(O),   _S(P), BACKSPACE,
        TAB, _S(A), _S(S),   _S(D),   _S(F),   _S(G),   _S(H),   _S(J),   _S(K),   _S(L), IT_COLN,    _S(ENTER),
        LSHIFT,  _S(Z), _S(X),   _S(C),   _S(V),   _S(B),   _S(N),   _S(M), IT_MINO, IT_MAJO, _S(UP), IT_QSTN,
        _S(LCTRL), _S(LALT), _S(LGUI), _S(LGUI), LT(SYMBO),  LT(ACCEN, SPACE),  LT(SYMBO), LT(NAVIG, IT_DQUO), _S(LEFT),  _S(DOWN), _S(RIGHT)
    ),

    # layer 0 NUMBE: remapped to match the ANSI layout with the Italian keyboard on the computer
    (
        ESC,   1,   2,   3,   4,   5,   6,   7,   8,   9,   0, BACKSPACE,
        MT(LSHIFT, TAB),  IT_PLUS,  IT_MINU, IT_SLSH, IT_STAR,   IT_EQAL,  XXX,  XXX,   IT_LSQR, IT_RSQR, IT_BSLS, ENTER,
        LT(SHIFT, DEL),   XXX,      XXX,     XXX,     XXX,       XXX,      XXX,  XXX,   XXX,     XXX,     XXX,     XXX,
        LCTRL,  LALT,     LGUI,    LGUI,    LT(NUMBE), LT(ACCEN, SPACE),   LT(SYMBO), LT(NAVIG, LGUI),  LEFT, DOWN, RIGHT
    ),

    # layer 1 SYMBO: remapped to match the ANSI layout with the Italian keyboard on the computer
    (
        ESC, IT_EXCL, IT_AT, IT_SHRP, IT_DOLL, IT_PERC, IT_POWE, IT_ECOM, IT_STAR, IT_LPAR, IT_RPAR, BACKSPACE,
        MT(LSHIFT, TAB),  IT_EQAL,  IT_UNDS, IT_QSTN, IT_STAR,   IT_EQAL,  XXX,  XXX, IT_LBRK, IT_RBRK, IT_PIPE, ENTER,
        LT(SHIFT, DEL),  XXX,   XXX,   XXX,   XXX, XXX,   XXX,   XXX,   XXX,   XXX,   XXX, XXX,
        LCTRL, LALT, LGUI, LGUI, LT(NUMBE),      LT(ACCEN, SPACE),   LT(SYMBO), LT(NAVIG, LGUI),  LEFT, DOWN, RIGHT
    ),

    # layer 2 FUNCT: MACRO(0) to read the battery level (requires a 3 wires JST connector from the battery)
    (
        ESC,  F1,  F2,  F3,  F4,  F5,  F6,  F7,  F8,  F9, F10, DEL,
        XXX, XXX, XXX, XXX, SHUTDOWN, XXX, XXX, XXX,SUSPEND,AUDIO_VOL_DOWN,AUDIO_VOL_UP,AUDIO_MUTE,
        LSHIFT, XXX, XXX, XXX, XXX,BOOT, XXX,MACRO(0), XXX, XXX, UP, RSHIFT,
        LCTRL, LALT, LGUI, LGUI, LT(NUMBE),      LT(ACCEN, SPACE),   LT(SYMBO), LT(NAVIG, LGUI),  LEFT, DOWN, RIGHT
    ),

    # layer 3 BLUET: default bluetooth functionality plus the RGB effects
    (
        BT_TOGGLE,BT1,BT2, BT3,BT4,BT5,BT6,BT7, BT8, BT9, BT0, BOOTLOADER,
        XXX, XXX, XXX, XXX, XXX, XXX, XXX, XXX, XXX, XXX, XXX, XXX,
        XXX, XXX, XXX, XXX, XXX, XXX, XXX, XXX, XXX, XXX, XXX, XXX,
        XXX, XXX, XXX, XXX, XXX, XXX, XXX, XXX, XXX, XXX, XXX,
    ),

    # layer 4 ACCEN: hit space and the corresponding letter to get the accent letter and the euro sign
    (
        '`', IT_EURO,XXX, IT_EGRV, XXX, XXX, XXX, IT_UGRV,IT_IGRV,IT_OGRV, XXX, MODS_KEY(MODS(LGUI,LSHIFT), 3),
        XXX, IT_AGRV,XXX, XXX, XXX, XXX, XXX, XXX, XXX, XXX, XXX, XXX,
        LSHIFT, XXX,    XXX, XXX, XXX,   XXX, XXX, XXX, XXX, XXX, XXX,   RSHIFT,
        XXX, XXX, XXX, XXX, XXX, XXX, XXX, XXX, XXX, XXX, XXX,
    ),

    # layer 5 MOUSE: mouse movements
    (
        ___, ___, ___, ___, ___, ___,MS_W_UP,MS_UL,MS_UP,MS_UR, ___, ___,
        ___, ___, ___, ___, ___, ___,MS_BTN1,MS_LT,MS_DN,MS_RT,MS_BTN2, ___,
        LSHIFT, ___, ___, ___, ___, ___,MS_W_DN,MS_DL,MS_DN,MS_DR, ___, RSHIFT,
        ___, ___, ___, ___, ___, ___, ___,  ___, ___, ___, ___,  ___
    ),

    # layer 6 NAVIG: navigation movements using j, k, l, i
    (
        ___, ___, ___, ___, ___, ___, ___, HOME,    UP, PGUP, ___, ___,
        ___, ___, ___, ___, RSHIFT, ___, ___, LEFT, DOWN,RIGHT,___, ___,
        LSHIFT, ___, ___, ___, ___, ___, ___, END,  DOWN, PGDN, ___,      UP,
        ___, ___, ___, ___, ___, ___, ___,  ___, ___, LEFT, DOWN, RIGHT
    ),
)

def macro_handler(dev, n, is_down):
    if is_down:
        pass
    else:
        dev.send_text('battery level is {}%'.format(battery_level()))

keyboard.macro_handler = macro_handler

keyboard.verbose = False
keyboard.fast_type_thresh = 60 # lower value to avoid navigation issue when hitting right shift too fast. Default is 200

keyboard.run()
