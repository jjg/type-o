# Type-O Project Journal

## 11032023

Not exactly the start of this project, but the start of anything meaningful in this repository at least.

Pretty much set on the hardware for the prototype and it's mostly off-the-shelf parts.  The brains will be an RP2040 chip in the form of an Adafruit Feather board, as this is cheap, convenient and solves the battery problem.  It also works out-of-the-box with Circuit Python which is going to be the simplest way to provide both access to the typing (in the form of a flash drive) and the HID aspects that will let Type-O be used as a regular mechanical keyboard.

Speaking of keyboard, for the prototype I'll be reusing the PLANCK mechanical keyboard I made for RAIN-PSP.  This is a hand-wired affair which will consume 16 pins of the RP2040 feature which means we won't have enough left to drive the HD44780 for the LCD directly.  This is why the I2C/SPI "backpack" is needed, which hopefully will work with the selected display (a ~$20 Ebay special).

Other than that the only other hardware is whatever Li-poly battery I have lying around and maybe some toggle switches to switch between typing/keyboard mode (unless we do that in software...).  It will depend on whether or not there are any pins left on the Feather after the keyboard and LCD are attached.


