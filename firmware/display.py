import asyncio
import board
import busio
import adafruit_character_lcd.character_lcd_i2c as character_lcd

async def get_display(keystrokes):
    print("-> display started")

    # TODO: Initialize display
    #import busio
    #import adafruit_character_lcd.character_lcd_i2c as character_lcd
    i2c = busio.I2C(board.SCL, board.SDA)
    cols = 16 
    rows = 2
    lcd = character_lcd.Character_LCD_I2C(i2c, cols, rows)

    while True:
        # TODO: Actually write the character to the LCD one-at-a-time
        lcd.message = "Hell\n"
        keystrokes.display_char = ""
        await asyncio.sleep(0)
