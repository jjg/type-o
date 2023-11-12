# TODO: scan keyboard pins for input
# TODO: write buffered input to LCD
# TODO: write buffered input to file
import time
import board
import microcontroller
from digitalio import DigitalInOut, Direction, DriveMode, Pull

# init keyboard

# map keys to characters ([row][column])
r = 4 
c = 12
keymap = [[0 for x in range(r)] for y in range(c)]
keymap[0][0] = "c"
keymap[1][0] = "?"
keymap[0][1] = "q"
keymap[1][1] = "a"

# row GPIOs
row_gpios = [
        microcontroller.pin.GPIO18,
        microcontroller.pin.GPIO25
        ]

# init rows
kbd_rows = []
for gpio in row_gpios:
    row = DigitalInOut(gpio)
    row.direction = Direction.OUTPUT
    row.drive_mode = DriveMode.OPEN_DRAIN
    row.value = False
    kbd_rows.append(row)

# TODO: Add remaining rows
#row_3 = DigitalInOut(microcontroller.pin.GPIO24)
#row_4 = DigitalInOut(microcontroller.pin.GPIO29)

# col GPIOs
col_gpios = [
        microcontroller.pin.GPIO12,
        microcontroller.pin.GPIO13
        ]
# init cols
kbd_cols = []
for gpio in col_gpios:
    col = DigitalInOut(gpio)
    col.direction = Direction.INPUT
    col.pull = Pull.UP
    kbd_cols.append(col)

# keyboard input buffers
kbd_char = ""
kbd_last_char = ""

# main event loop
while True: 

    # TODO: Read keypress from keyboard
    #print("Entering keyboard scan")

    keymap_x = 0
    keymap_y = 0
    for kbd_row in kbd_rows:
        kbd_row.value = False   # connect the row
        for kbd_col in kbd_cols:
            if kbd_col.value == False:
                kbd_char = keymap[keymap_x][keymap_y]
            keymap_y = keymap_y + 1
        kbd_row.value = True    # disconnect the row
        keymap_y = 0
        keymap_x = keymap_x + 1

    print(kbd_char)

    #if kbd_char != kbd_last_char:
    #    print(kbd_char)
    #    kbd_last_char = kbd_char

    #row_1.value = False # Connect drain to ground to scan the row
    #print(col_1.value)  # False if pressed (pulled to ground)
    #if col_1.value == False:
    #    print("crop key pressed")
    #if col_2.value == False:
    #    print("q key pressed")
    #row_1.value = True  # Disconnect drain from ground to stop scanning row

    #row_2.value = False # Connect drain to ground to scan the row
    #print(col_1.value)  # False if pressed (pulled to ground)
    #if col_1.value == False:
    #    print("weird key pressed")
    #if col_2.value == False:
    #    print("a key pressed")
    #row_2.value = True  # Disconnect drain from ground to stop scanning row

    # TODO: Initialize display
    #import busio
    #import adafruit_character_lcd.character_lcd_i2c as character_lcd
    #i2c = busio.I2C(board.SCL, board.SDA)
    #cols = 40 
    #rows = 4 
    #lcd = character_lcd.Character_LCD_I2C(i2c, cols, rows)

    #lcd.message = "Hell\n"

    time.sleep(1)
