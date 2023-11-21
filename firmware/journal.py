import storage
import asyncio

async def get_journal(keystrokes):
    print("-> journal started")
    try:
        with open("/journal.md", "a") as fp:
            while True:
                fp.write(keystrokes.storage_char)
                fp.flush()
                await asyncio.sleep(0)
    except OSError as e:
        print("-X {}".format(e))
        print("-> journal stopped")
