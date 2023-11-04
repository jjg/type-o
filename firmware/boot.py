import usb_hid
import usb_midi

usb_hid.enable((usb_hid.Device.KEYBOARD,))  # Disable all HID but keyboard.
usb_midi.disable()                          # We also don't use midi, so disable it.
