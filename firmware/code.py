# TODO: scan keyboard pins for input
# TODO: write buffered input to LCD
# TODO: write buffered input to file
import time
import board
import microcontroller
from digitalio import DigitalInOut, Direction, DriveMode, Pull

# init keyboard
row_1 = DigitalInOut(microcontroller.pin.GPIO18)
row_1.direction = Direction.OUTPUT
row_1.drive_mode = DriveMode.OPEN_DRAIN
row_1.value = False

row_2 = DigitalInOut(microcontroller.pin.GPIO25)
row_2.direction = Direction.OUTPUT
row_2.drive_mode = DriveMode.OPEN_DRAIN
row_2.value = False

#row_2 = DigitalInOut(microcontroller.pin.GPIO25)
#row_3 = DigitalInOut(microcontroller.pin.GPIO24)
#row_4 = DigitalInOut(microcontroller.pin.GPIO29)

col_1 = DigitalInOut(microcontroller.pin.GPIO12)
col_1.direction = Direction.INPUT
col_1.pull = Pull.UP

col_2 = DigitalInOut(microcontroller.pin.GPIO13)
col_2.direction = Direction.INPUT
col_2.pull = Pull.UP

# main event loop
while True: 

    # TODO: Read keypress from keyboard
    #print("Entering keyboard scan")

    row_1.value = False # Connect drain to ground to scan the row
    #print(col_1.value)  # False if pressed (pulled to ground)
    if col_1.value == False:
        print("crop key pressed")
    if col_2.value == False:
        print("q key pressed")
    row_1.value = True  # Disconnect drain from ground to stop scanning row

    row_2.value = False # Connect drain to ground to scan the row
    #print(col_1.value)  # False if pressed (pulled to ground)
    if col_1.value == False:
        print("weird key pressed")
    if col_2.value == False:
        print("a key pressed")
    row_2.value = True  # Disconnect drain from ground to stop scanning row

    # TODO: Initialize display
    #import busio
    #import adafruit_character_lcd.character_lcd_i2c as character_lcd
    #i2c = busio.I2C(board.SCL, board.SDA)
    #cols = 40 
    #rows = 4 
    #lcd = character_lcd.Character_LCD_I2C(i2c, cols, rows)

    #lcd.message = "Hell\n"

    time.sleep(1)
