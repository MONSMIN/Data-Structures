import timeit
import random

from prettytable import PrettyTable

from insertion_sort import insertion_sort
from merge_sort import merge_sort

table = PrettyTable(["\033[91mАлгоритм\033[0m",
                     "\033[92mЧас обробки малих даних\033[0m",
                     "\033[94mЧас обробки середніх даних\033[0m",
                     "\033[95mЧас обробки чималих даних\033[0m"])

if __name__ == '__main__':
    data_small = [random.randint(0, 1_000) for _ in range(1_000)]
    data_medium = [random.randint(0, 10_000) for _ in range(10_000)]
    data_large = [random.randint(0, 100_000) for _ in range(100_000)]

    time_small_insertion = timeit.timeit(lambda: insertion_sort(data_small[:]), number=5)
    time_small_merge = timeit.timeit(lambda: merge_sort(data_small[:]), number=5)
    time_small_timsort = timeit.timeit(lambda: sorted(data_small[:]), number=5)

    time_medium_insertion = timeit.timeit(lambda: insertion_sort(data_medium[:]), number=5)
    time_medium_merge = timeit.timeit(lambda: merge_sort(data_medium[:]), number=5)
    time_medium_timsort = timeit.timeit(lambda: sorted(data_medium[:]), number=5)

    time_large_insertion = timeit.timeit(lambda: insertion_sort(data_large[:]), number=5)
    time_large_merge = timeit.timeit(lambda: merge_sort(data_large[:]), number=5)
    time_large_timsort = timeit.timeit(lambda: sorted(data_large[:]), number=5)

    table.add_row(
        ["Сортування вставками (Insertion sort)", time_small_insertion, time_medium_insertion, time_large_insertion])
    table.add_row(["Сортування злиттям (Merge sort)", time_small_merge, time_medium_merge, time_large_merge])
    table.add_row(["Timsort — гібридний алгоритм", time_small_timsort, time_medium_timsort, time_large_timsort])
    print(table)
