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