import student_code as sc
import timeit
from memory_profiler import profile


@profile
def main():
    execution_time = timeit.timeit(lambda: sc.function(), number=1)
    print(execution_time)


if __name__ == "__main__":
    main()