# import asyncio

# async def produce_output():
#     await asyncio.sleep(2)  # Simulate some asynchronous operation
#     return "Async output!"

# async def main():
#     # Wait for the output from the asynchronous function
#     result = await produce_output()

#     # Print the output
#     print(result)

# # Run the main function
# asyncio.run(main())

import time

def produce_output():
    time.sleep(2)  # Simulate some synchronous operation
    return "Sync output!"

def main():
    # Wait for the output from the synchronous function
    result = produce_output()

    # Print the output
    print(result)

# Run the main function
main()
