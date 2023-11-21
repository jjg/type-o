import asyncio

# project imports
import keyboard 
import display
import journal
import hidkeyboard
import debugger

class Keystrokes:
    def __init__(self):
        self.value = ""
        self.display_char = ""
        self.storage_char = ""
        self.hid_char = ""
        self.debug_char = ""
    def insert(self, char):
        self.value = char
        self.display_char = char
        self.storage_char = char
        self.hid_char = char
        self.debug_char = char

# main event loop
async def main():

    print("\nBooting Type-OS v0.0.0a")

    print("-> init keystrokes object")
    keystrokes = Keystrokes()

    print("-> init keyboard") 
    keyboard_task = asyncio.create_task(keyboard.get_keyboard(keystrokes))

    print("-> init display")
    display_task = asyncio.create_task(display.get_display(keystrokes))

    print("-> init journal")
    journal_task = asyncio.create_task(journal.get_journal(keystrokes))

    print("-> init hidkeyboard")
    hidkeyboard_task = asyncio.create_task(hidkeyboard.get_hidkeyboard(keystrokes))

    print("-> init debugger")
    debugger_task = asyncio.create_task(debugger.get_debugger(keystrokes))

    print("Starting tasks")
    await asyncio.gather(keyboard_task, display_task, journal_task, hidkeyboard_task, debugger_task)

asyncio.run(main())
