# Async in Python
## Overview
Asynchronous programming allows for the execution of tasks without waiting for each to complete before starting the next. This can greatly improve the efficiency and performance of programs that involve I/O-bound operations, such as network requests or file I/O. Python's asyncio library provides the foundation for writing asynchronous code using async and await.

## Prerequisites
Python 3.7 or higher installed on your machine.
Basic understanding of Python programming.
Installation
No additional installation is required as asyncio is included in the Python standard library. Simply ensure you have Python 3.7+ installed:

`` python --version``
## Key Concepts
async: Defines an asynchronous function that can use await within its body.
await: Pauses the execution of an async function until the awaited task completes.
asyncio: The core library for asynchronous programming in Python, providing event loops, coroutines, and tasks.
Example Code
Below is an example script demonstrating asynchronous programming with asyncio:

python
``#!/usr/bin/env python3
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
    print(f"{__file__} executed in {elapsed:0.2f} seconds.") ``

## How It Works
### Defining Asynchronous Functions:

async def count(): The count function is defined as asynchronous, allowing the use of await within its body.
await asyncio.sleep(1): This pauses the function for 1 second without blocking the event loop, allowing other tasks to run.
### Running Multiple Coroutines Concurrently:

await asyncio.gather(count(), count(), count()): The gather function runs the count function three times concurrently. Each count function instance will wait for 1 second simultaneously.
### Measuring Execution Time:

The script measures and prints the total execution time, demonstrating the efficiency of asynchronous execution.
### Running the Script
To run the script, execute it from the command line:

``python countasync.py``
You should see the following output:

``One
One
One
Two
Two
Two
countasync.py executed in 1.00 seconds``


This output demonstrates that the three count function calls run concurrently, each waiting for 1 second before printing "Two", resulting in a total execution time of approximately 1 second.

Further Reading
Official Python asyncio Documentation
Real Python's Guide to asyncio
PEP 492 – Coroutines with async and await syntax
## License
This project is licensed under the MIT License.