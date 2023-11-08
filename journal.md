# Type-O Project Journal

## 11072023

Ooohh where to start...

I did a lot of datasheet reading last night and figured out some good things and some bad things.  The good is that it looks like I *don't* need the boost converter for the 5v LCD.  Turns out the i2c backback does this (I thought it only did level matching on the logic side).  This also means that I might be able to use the connector Adafruit calls "STEMMA QT" to connect the Feather to the backpack.

The bad news is that I mapped the pins between the backpack and the LCD and I don't think it's going to work unmodified.  The LCD has two controller enable pins (I assume it needs to controllers for 40 character lines vs. the 20 character lines this backpack was designed for) and I assume that the second enable pin needs to be "enabled" at the right time in order to run the display correctly.  I have a few theories about how this works and how I might address it, but I'll need to read some code and more datasheets to know for sure.  For the moment I'm just going to hook everything up as if it had a single controller and see how far I get.

### Pin mapping between i2c backpack and 4x40 LCD

| Backpack | LCD | Description/notes |
|:---------|-----|-------------------|
| 1        | 13  | GND |
| 2        | 14  | VCC |
| 3        | 12  | VEE (Backlight brightness?) |
| 4        | 11  | RS |
| 5        | 10  | RW |
| 6        | 9   | Enable 1 |
| 7        | 8   | DB0 |
| 8        | 7   | DB1 |
| 9        | 6   | DB2 |
| 10       | 5   | DB3 |
| 11       | 4   | DB4 |
| 12       | 3   | DB5 |
| 13       | 2   | DB6 |
| 14       | 1   | DB7 |
| 15       | 17  | LED + (on the opposite end of the LCD board from the rest of the pins) |
| 16       | 18  | LED - (on the opposite end of the LCD board from the rest of the pins) |



## 11042023

Spent some time early this morning on the first draft of a case design.  It's very primative at this point but I think it's enough of a start to hold the key components in place and see how well the virtual parts match-up with the real ones.

I'll try running a set later today and see how things fit.

Started piecing-together the fimrware as well.  So far mostly just grabbing dependencies and references.



## 11032023

Not exactly the start of this project, but the start of anything meaningful in this repository at least.

Pretty much set on the hardware for the prototype and it's mostly off-the-shelf parts.  The brains will be an RP2040 chip in the form of an Adafruit Feather board, as this is cheap, convenient and solves the battery problem.  It also works out-of-the-box with Circuit Python which is going to be the simplest way to provide both access to the typing (in the form of a flash drive) and the HID aspects that will let Type-O be used as a regular mechanical keyboard.

Speaking of keyboard, for the prototype I'll be reusing the PLANCK mechanical keyboard I made for RAIN-PSP.  This is a hand-wired affair which will consume 16 pins of the RP2040 feature which means we won't have enough left to drive the HD44780 for the LCD directly.  This is why the I2C/SPI "backpack" is needed, which hopefully will work with the selected display (a ~$20 Ebay special).

Other than that the only other hardware is whatever Li-poly battery I have lying around and maybe some toggle switches to switch between typing/keyboard mode (unless we do that in software...).  It will depend on whether or not there are any pins left on the Feather after the keyboard and LCD are attached.

OK, let's try mapping this thing out:

### Pin mapping between Feather and  periphereal devices

| Feather Pin | Device       | Device Pin | Description/Notes |
|:------------|--------------|------------|-------------------|
| RESET       |              |            | external reset button |
| 3v3         |              |            | open |
| GND         |              |            | common ground |
| VBAT        | Lipo         | Positive   | battery connector |
| GND         | Lipo         | Negative   | battery connector |
| VBAT        |              |            | open (maybe 5vdc boost? |
| EN          |              |            | enable pin, maybe connect to "sleep" switch? |
| VBUS        |              |            | power from USB? |
| GPIO3       | I2C Backpack | CLK        | I2C clock pin (SCL)     |
| GPIO2       | I2C Backpack | DAT        | I2C data pin (SDA)      |
| 3v3         | I2C Backpack | VIN        | 3.3v supply |
| GND         | I2C Backpack | GND        | shared ground     |
| GPIO13      | Keyboard     | COL1       | first keyboard column (this is also the built-in LED, hopefully that won't cause problems or we'll have to move this) |
| GPIO12      | Keyboard     | COL2       | second keyboard column | 
| GPIO11      | Keyboard     | COL3       | third keyboard column |
| GPIO10      | Keyboard     | COL4       | fourth keyboard column | 
| GPIO9       | Keyboard     | COL5       | fifth keyboard column |
| GPIO8       | Keyboard     | COL6       | sixth keyboard column |
| GPIO7       | Keyboard     | COL7       | seventh keyboard column |
| GPIO6       | Keyboard     | COL8       | eighth keyboard column |
| GPIO0       | Keyboard     | COL9       | ninth keyboard column |
| GPIO1       | Keyboard     | COL10      | tenth keyboard column |
| GPIO20      | Keyboard     | COL11      | eleventh keyboard column |
| GPIO19      | Keyboard     | COL12      | twelfth keyboard column |
| GPIO18      | Keyboard     | ROW1       | first keyboard row |
| GPIO25      | Keyboard     | ROW2       | second keyboard row |
| GPIO24      | Keyboard     | ROW3       | third keyboard row |
| GPIO29      | Keyboard     | ROW4       | forth keyboard row |
| GPIO26      |              |            | open |
| GPIO27      |              |            | open |
| GPIO26      | Feather      | GPIO26     | analog input for battery level |
| GPIO16      | Neopixel     | DATA       | Feather's built-in Neopixel (maybe shine-through case for status/debgging?) |

A few things come to mind after this exercise:

* We might still have two pins left to play with (and they are analog inputs as well!)
* There's no obvious 5v supply for the 5v LCD

Maybe I can coax the LCD into working with 4.2v from the lipo.  If not, I'll have to add a boost converter to the prototype BOM and buy a 3v3 LCD next time.


