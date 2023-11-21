import microcontroller
import asyncio

async def get_debugger(keystrokes):
    print("-> debugger started")
    print("\nWelcome to the Type-OS Debugger")
    print("CPU Temp: {}".format(microcontroller.cpu.temperature))
    print("CPU Frequency: {}".format(microcontroller.cpu.frequency))

    print("\n--- input from keyboard ---")
    while True:
        print(keystrokes.debug_char, end="")
        keystrokes.debug_char = ""

        await asyncio.sleep(0)
