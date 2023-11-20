# Type-O Project Journal

## 2023-11-20

Switching to ISO-8601 dates.

Spent some time today refactoring the code to use coroutines so I can scan the keyboard, update the display and run the debugger in a "multitasking" way.  So far it seems to be working and I think it's going to make it a lot easier to improve each individual component of the system.

It does seem to break the REPL a bit because I don't seem to be able to feed it control signals via the serial console when the coroutines are running.  Maybe there's a trick to fixing that but for now I'm just operating under the assumption that if I need the REPL, I have to disable running the "OS" tasks.

I've given the firmware the name `Type-OS`, it's probably overkill to refer to this as an operating system, but what the heck, right?

I also started fleshing-out experimental support for storing text, but this won't get enabled until I can add another switch to enable/disable read-only mode (can't write to storage from CircuitPython when a computer can write to storage via USB).

## 11192023

Going to try to wire-up the rest of the keyboard and see how much we an get working.

Wires are connected, now to do the software side of things...

First row working!
All rows working!

OK, so now we have a complete (lower-case) keymap and we can read every key on the keyboard sucessfully.  There's a few places we can go from here:

* Properly handle modifier keys (shift, control, etc.) & improve keymap
* Implement async functions to read & display keyboard values correctly
* Forward keystrokes on to UID so the keyboard can work like a USB keyboard
* Write the keystrokes to disk in a file that can be read on the attached computer.

All of these are a bit of work so for now I'm just going to tweak the display code a bit to see if I can get the keyboard to type "normally".  

Ok, now we can type a line of text and even hit return!  Here's the first lines of text written with the prototype:

```
ok, this is pretty o???? cool

you coul ?d almost wrie ??te somethinig with this...
```

Obviously there are some important keys missing (like Backspace), but certainly enough to demonstrate that the electrical side of things is sound, and it's *almost* useable to write something!

So after thinking about it for awhile I think the right thing to do next is to implement concurrency so we can separate scanning the keyboard from writing to the display and storing data.  Since everything else will be built on this, it's probably a good time to start doing things this way.

This will be a pretty big refactor so the code might be a mess for awhile.





## 11182023

Tweaked the bottom case design to add clearance under the keyboard and elsewhere to accomodate the wiring between modules (the Dupont connectors add a lot of height).  This might be reducable in the future with more customized components.


## 11122023

Since the display is giving me trouble I'm going to play with the keyboard for awhile.

I think a reasonable first goal is to get to a point where pressing a single key results in printing the key's character to the serial console.  That should prove the basic electrical and software designs without a lot of extra wiring and such.

So the theory behind the keyboard code is that there are 4 rows and 12 columns in a matrix.  I'll connect a line from each row and column to a GPIO, assert a signal to each row in turn and while that row is turned "on", read through each column GPIO to look for the signal.  If a signal is found on a column, we can say that the key at the row+col position is pressed.

My initial thought on how to do this is to take each row GPIO and configure it for output, and configure each column GPIO for input, and assert a 1 or `true` to each row as I cycle through them.  But I'm not sure this actually makes sense wrt how the board works electrically so I need to do a little digging there.

row 1 GPIO: 18
col 1 GPIO: 12

> tips: use `dir(microcontroller.pin)` (`import` `board`, `microcontroller` first) to get a list GPIO names available for the board.
> `help(modules)` will show all the built-in  modules available for the current board.

OK, this seems to work.  If I configure `GPIO18` for `OUTPUT` and `GPIO12` for `INPUT`, I'm able to set `GPIO18` to `True` and get the keypressed state as a `True`/`False` by reading the `value` of the pin object.

Now let's try scanning more than one row.

This didn't work.  I'm not sure if it doesn't work because I did something wrong (miswiring, etc.) or if maybe the last experiment didn't work how I thought it did.  I'm going to dig a little deeper into how the pins are working to make sure it's doing what I expect at an electrical level.

After doing a little reading I think I want to alter things a bit.  I think what I want to do is setup the rows as [open collectors]() and then read the columns in a way that it can tell if the column pin is grounded.  I think this means I want the input pulled-up (defaulting to `True`), so when the row is selected (open-collector closed) and a key is pressed the input gets pulled to ground and reads `False`.

This seems to work!  Now let's try it with a second row...

Second row works as well!  Now the question is, do we re-work this to use a more dynamic setup (instead of a line of code for each row and column) or test a second column first?

Yeah let's test a second column first.  If that works we should know all we need to know to scan the entire keyboard.

Second column works!  Now it's time to refactor this into a more reasonable means of looping over all these bits.



## 11082023

Today we debug the display.

First I want to make sure the "objects" used to initialize i2c match the pins I actually used for the display.  This appears to be the case, so moving-on.

With `cols` set to `40` and `rows` set to `4`, the message `Hello\nType-O` results in solid boxes filling the first and third rows of the display.  I tried changing the message to see what happens on the display and it stays the same until I remove the `\n`, at which point the display is blank.

I also tried tweaking the `rows`/`cols` settings to see what impact that has and it doesn't appear to have any.  I'll double-check the wiring and then dive into the library code a bit.

Spent what feels like an hour double-checking the connections and I can't find any errors there.

After digging around a bit I'm starting to wonder if there is something more fundamentally wrong with using the backpack this way.  Even basic stuff like turning the backlight off isn't working, so maybe I need to consider other options.

While reading about the internals of the backpack I noticed that the heavy lifting is done by a MCP23008 which if I remember right is the same chip I used to make a custom board for the front panel of RAIN-PSC.  So if I can't get the backpack to work, maybe I can just make my own i2c adapter for the display using a MCP23008 and write a custom driver/library for it?

I posted a question to the [Adafruit message board](https://forums.adafruit.com/viewtopic.php?t=205816) to see if anyone else has any ideas, but in the meantime I think I'll switch to working on the keyboard side of things.


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
| GPIO12      | Keyboard     | COL1       | first keyboard column  |
| GPIO13      | Keyboard     | COL2       | second keyboard column (this is also the built-in LED, hopefully that won't cause problems or we'll have to move this)| 
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


