#!/usr/bin/env python3
# countasync.py

import asyncio

# Define an asynchronous function 'count' that prints "One", waits for 1 second, and then prints "Two"
async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

# Define the main asynchronous function 'main' that runs the 'count' function three times concurrently using asyncio.gather
async def main():
    await asyncio.gather(count(), count(), count())

# The entry point of the script
if __name__ == "__main__":
    # Import the time module to measure execution time
    import time
    # Record the start time
    s = time.perf_counter()
    # Run the main function using asyncio.run to execute the event loop
    asyncio.run(main())
    # Calculate the elapsed time
    elapsed = time.perf_counter() - s
    # Print the execution time
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
