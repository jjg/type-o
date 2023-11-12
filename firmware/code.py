# TODO: scan keyboard pins for input
# TODO: write buffered input to LCD
# TODO: write buffered input to file
import time
import board
import microcontroller
from digitalio import DigitalInOut, Direction, Pull

# init keyboard
row_1 = DigitalInOut(microcontroller.pin.GPIO18)
row_1.direction = Direction.OUTPUT
col_1 = DigitalInOut(microcontroller.pin.GPIO12)
col_1.direction = Direction.INPUT

# main event loop
while True: 

    # TODO: Read keypress from keyboard
    print("Entering keyboard scan")
    row_1.value = True

    if col_1.value == True:
        print("key pressed")

    # TODO: Initialize display
    #import busio
    #import adafruit_character_lcd.character_lcd_i2c as character_lcd
    #i2c = busio.I2C(board.SCL, board.SDA)
    #cols = 40 
    #rows = 4 
    #lcd = character_lcd.Character_LCD_I2C(i2c, cols, rows)

    #lcd.message = "Hell\n"

    time.sleep(1)
