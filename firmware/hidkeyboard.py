import asyncio

async def get_hidkeyboard(keystrokes):
    print("-> hidkeyboard started")
    
    while True:
        # TODO: write char to HID keyboard device
        keystrokes.hid_char = ""
        await asyncio.sleep(0)
