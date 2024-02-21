# def prime(data):
#     if data == 2:
#         return("its a prime & even Number ")
        
#     for i in range(2, data):
#     # for i in range(2, int(data**0.5)+1):
#         print(f"{i} this much of time executed")
#         if data % i == 0:
#             return "its a not a prime Number"
        
        
#     return "this is a prime Number"

# print(prime(1450))

import timeit
from memory_profiler import profile

@profile
def simple_loop():
    for _ in range(1000000):
        pass

@profile
def main():
    # Measure execution time using timeit
    execution_time = timeit.timeit(lambda: simple_loop(), number=1)
    print(f"Execution time: {execution_time} seconds")

if __name__ == "__main__":
    main()
