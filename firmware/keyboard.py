import microcontroller
import asyncio
from digitalio import DigitalInOut, Direction, DriveMode, Pull

import keymapper

async def get_keyboard(keystrokes):
    print("-> keyboard started")

    keymap = keymapper.get_map()

    # row GPIOs
    row_gpios = [
            microcontroller.pin.GPIO18,
            microcontroller.pin.GPIO25,
            microcontroller.pin.GPIO24,
            microcontroller.pin.GPIO29
            ]

    # init rows
    kbd_rows = []
    for gpio in row_gpios:
        row = DigitalInOut(gpio)
        row.direction = Direction.OUTPUT
        row.drive_mode = DriveMode.OPEN_DRAIN
        row.value = False
        kbd_rows.append(row)

    # col GPIOs
    col_gpios = [
            microcontroller.pin.GPIO12,
            microcontroller.pin.GPIO13,
            microcontroller.pin.GPIO11,
            microcontroller.pin.GPIO10,
            microcontroller.pin.GPIO9,
            microcontroller.pin.GPIO8,
            microcontroller.pin.GPIO7,
            microcontroller.pin.GPIO6,
            microcontroller.pin.GPIO0,
            microcontroller.pin.GPIO1,
            microcontroller.pin.GPIO20,
            microcontroller.pin.GPIO19
            ]

    # init cols
    kbd_cols = []
    for gpio in col_gpios:
        col = DigitalInOut(gpio)
        col.direction = Direction.INPUT
        col.pull = Pull.UP
        kbd_cols.append(col)

    # keyboard scan loop
    debounce_timeout = 5    # milliseconds
    this_char = ""
    last_char = this_char
    while True: 

        # read keypress from keyboard
        keymap_x = 0
        keymap_y = 0
        for kbd_row in kbd_rows:
            kbd_row.value = False   # connect the row
            for kbd_col in kbd_cols:
                if kbd_col.value == False:
                    this_char = keymap[keymap_x][keymap_y]

                    # debounce by ignoring repeated characters for 0.5 seconds
                    # NOTE: this is only accurate while asyncio.sleep() is set to 0.01!!!
                    if this_char == last_char:
                        debounce_countdown = debounce_countdown -1
                        if debounce_countdown == 0:
                            debounce_countdown = debounce_timeout
                            last_char = ""
                    else:
                        keystrokes.insert(this_char)
                        last_char = this_char

                keymap_y = keymap_y + 1
            kbd_row.value = True    # disconnect the row
            keymap_y = 0
            keymap_x = keymap_x + 1

        # yield control to the scheduler
        await asyncio.sleep(0.1)
