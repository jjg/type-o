# TODO: scan keyboard pins for input
# TODO: write buffered input to LCD
# TODO: write buffered input to file
import board
import busio
import adafruit_character_lcd.character_lcd_i2c as character_lcd
#i2c = busio.I2C(board.SCL, board.SDA)
i2c = busio.I2C(3, 2)
cols = 40 
rows = 4
lcd = character_lcd.Character_LCD_I2C(i2c, cols, rows)

lcd.message = "Hello\nType-O!"
