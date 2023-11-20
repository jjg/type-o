import usb_hid
import usb_midi
import board
import digitalio
import storage

usb_hid.enable((usb_hid.Device.KEYBOARD,))  # Disable all HID but keyboard.
usb_midi.disable()                          # We also don't use midi, so disable it.

# TODO: enable this code once we have a read-only switch wired-up
#switch = digitalio.DigitalInOut(board.D2)
#switch.direction = digitalio.Direction.INPUT
#switch.pull = digitalio.Pull.UP
#storage.remount("/", switch.value)
