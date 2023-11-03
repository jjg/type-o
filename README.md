# Type-O

*"That's not writing, it's typing"*

Type-O is a simple portable writing device consisting of a *nice* keyboard and a 4x40 character LCD screen.  What you type shows-up on the screen and goes into a file.

When you connect Type-O to a computer via USB, it shows-up as a flash drive containing a file that contains your writing.

It can also be used as a nice USB keyboard!

This repository contains source code for Type-O's [firmware](./firmware), [model files](./models) for the printable parts as well as related [documentation](.docs).

Details and progress can be found in the [journal](./journal.md) or in more human-readable form in the following posts on [jasongullickson.com](https://jasongullickson.com): 

* [Type-O](https://jasongullickson.com/type-o.html)

You can also follow the hashtag #typeo in the fediverse for ad-hoc updates and discussion.


# Reference

* [Adafruit Feather RP2040](https://learn.adafruit.com/adafruit-feather-rp2040-pico)
* [Adafruit I2C/SPI LCD Backpack](https://learn.adafruit.com/i2c-spi-lcd-backpack)
* [5V 40x4 4004 LCM Monochrome Character LCD Display Module HD44780](https://www.ebay.com/itm/291024701200)
* [Cooperative Multitasking in CircuitPython](https://learn.adafruit.com/cooperative-multitasking-in-circuitpython-with-asyncio/overview)
* https://learn.adafruit.com/adafruit-gemma-m0/circuitpython-hid-keyboard-and-mouse
* https://learn.adafruit.com/circuitpython-essentials/circuitpython-storage
* https://learn.adafruit.com/diy-pico-mechanical-keyboard-with-fritzing-circuitpython/overview
* https://github.com/modulaire/RPi-Pico-HID-Keyboard
* https://docs.circuitpython.org/en/latest/docs/library/io.html
