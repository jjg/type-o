import time
import board
import microcontroller
import asyncio
import storage
from digitalio import DigitalInOut, Direction, DriveMode, Pull

class Keystrokes:
    def __init__(self):
        self.value = ""
        self.display_char = ""
        self.storage_char = ""
        self.hid_char = ""
        self.debug_char = ""
    def insert(self, char):
        self.value = char
        self.display_char = char
        self.storage_char = char
        self.hid_char = char
        self.debug_char = char

async def keyboard(keystrokes):
    print("-> keyboard started")

    # init keymap
    row_count = 4
    col_count = 12
    keymap = [[0 for x in range(col_count)] for y in range(row_count)]

    # map keys to characters ([row][column])
    # TODO: this can probaby be done with a literal, and
    # ideally would use some standard config file format
    # TODO: If the value were a tuple, we could define 
    # the modified values (uppercase, etc.) as well

    # row 1
    keymap[0][0] = "?"
    keymap[0][1] = "q"
    keymap[0][2] = "w"
    keymap[0][3] = "e"
    keymap[0][4] = "r"
    keymap[0][5] = "t"
    keymap[0][6] = "y"
    keymap[0][7] = "u"
    keymap[0][8] = "i"
    keymap[0][9] = "o"
    keymap[0][10] = "p"
    keymap[0][11] = "?"

    # row 2
    keymap[1][0] = "?"
    keymap[1][1] = "a"
    keymap[1][2] = "s"
    keymap[1][3] = "d"
    keymap[1][4] = "f"
    keymap[1][5] = "g"
    keymap[1][6] = "h"
    keymap[1][7] = "j"
    keymap[1][8] = "k"
    keymap[1][9] = "l"
    keymap[1][10] = ";"
    keymap[1][11] = "'"

    # row 3
    keymap[2][0] = "S"
    keymap[2][1] = "z"
    keymap[2][2] = "x"
    keymap[2][3] = "c"
    keymap[2][4] = "v"
    keymap[2][5] = "b"
    keymap[2][6] = "n"
    keymap[2][7] = "m"
    keymap[2][8] = ","
    keymap[2][9] = "."
    keymap[2][10] = "/"
    keymap[2][11] = "\n"

    # row 4
    keymap[3][0] = "F"
    keymap[3][1] = "C"
    keymap[3][2] = "U"
    keymap[3][3] = "A"
    keymap[3][4] = "L"
    keymap[3][5] = ""   # NC, space takes two columns
    keymap[3][6] = " "
    keymap[3][7] = "R"
    keymap[3][8] = "L"
    keymap[3][9] = "D"
    keymap[3][10] = "U"
    keymap[3][11] = "R"

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
    while True: 

        # read keypress from keyboard
        kbd_char = ""
        keymap_x = 0
        keymap_y = 0
        for kbd_row in kbd_rows:
            kbd_row.value = False   # connect the row
            for kbd_col in kbd_cols:
                if kbd_col.value == False:
                    #kbd_char = keymap[keymap_x][keymap_y]
                    #keystrokes.value = keymap[keymap_x][keymap_y]
                    keystrokes.insert(keymap[keymap_x][keymap_y])
                keymap_y = keymap_y + 1
            kbd_row.value = True    # disconnect the row
            keymap_y = 0
            keymap_x = keymap_x + 1

        # yeild control to the scheduler
        await asyncio.sleep(0)

async def display(keystrokes):
    print("-> display started")

    # TODO: Initialize display
    #import busio
    #import adafruit_character_lcd.character_lcd_i2c as character_lcd
    #i2c = busio.I2C(board.SCL, board.SDA)
    #cols = 40 
    #rows = 4 
    #lcd = character_lcd.Character_LCD_I2C(i2c, cols, rows)

    while True:
        # TODO: Actually write the character to the LCD one-at-a-time
        #lcd.message = "Hell\n"
        keystrokes.display_char = ""
        await asyncio.sleep(0)

async def storage(keystrokes):
    print("-> storage started")
    try:
        with open("/journal.md", "a") as fp:
            while True:
                fp.write(keystrokes.storage_char)
                fp.flush()
                await asyncio.sleep(0)
    except OSError as e:
        print("-X {}".format(e))
        print("-> storage stopped")

async def hid(keystrokes):
    print("-> hid started")
    
    while True:
        # TODO: write char to HID device
        keystrokes.hid_char = ""
        await asyncio.sleep(0)

async def debugger(keystrokes):
    print("-> debugger started")
    print("\nWelcome to the Type-OS Debugger")
    print("CPU Temp: {}".format(microcontroller.cpu.temperature))
    print("CPU Frequency: {}".format(microcontroller.cpu.frequency))

    print("\n--- input from keyboard ---")
    while True:
        print(keystrokes.debug_char, end="")
        keystrokes.debug_char = ""

        await asyncio.sleep(0)


# main event loop
async def main():

    print("\nBooting Type-OS v0.0.0a")

    print("-> init keystrokes object")
    keystrokes = Keystrokes()

    print("-> init keyboard") 
    keyboard_task = asyncio.create_task(keyboard(keystrokes))

    print("-> init display")
    display_task = asyncio.create_task(display(keystrokes))

    print("-> init storage")
    storage_task = asyncio.create_task(storage(keystrokes))

    print("-> init hid")
    hid_task = asyncio.create_task(hid(keystrokes))

    print("-> init debugger")
    debugger_task = asyncio.create_task(debugger(keystrokes))

    print("Starting tasks")
    await asyncio.gather(keyboard_task, display_task, storage_task, hid_task, debugger_task)

asyncio.run(main())
