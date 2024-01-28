import timeit
from  typing import Callable
from collections import defaultdict

from bm import boyer_moore_search
from kmp import kmp_search
from rabina import rabin_karp_search


def read_file(filename):
    with open(f'data/{filename}', 'r', encoding='utf-8') as f:
        return f.read()


def benchmark(func: Callable, text_: str, pattern_: str):
    setup_code = f"from __main__ import {func.__name__}"
    stmt = f"{func.__name__}(text, pattern)"
    return timeit.timeit(stmt=stmt, setup=setup_code, globals={'text': text_, 'pattern': pattern_}, number=10)


if __name__ == '__main__':
    
    real_pattern = "хеш-таблиці"
    fake_pattern = "пунта хейла"

    results = []
    
    for file in ['article_1.txt', 'article_2.txt']:
        text = read_file(file)
        for pattern in (real_pattern, fake_pattern):
            time = benchmark(boyer_moore_search, text, pattern)
            results.append((file, pattern, boyer_moore_search.__name__, time))
            time = benchmark(kmp_search, text, pattern)
            results.append((file, pattern, kmp_search.__name__, time))
            time = benchmark(rabin_karp_search, text, pattern)
            results.append((file, pattern, rabin_karp_search.__name__, time))

    print('\n')
    print('Результати:')
    print(f"| {'Файл':<30} | {'Підрядок':<30} | {'Алгоритм':<30} | {'Час виконання, сек':<30} |")
    print(f"| :{'-'*29} | :{'-'*29} | :{'-'*29} | :{'-'*29} |")
    for result in results:
        print(f"| {result[0]:<30} | {result[1]:<30} | {result[2]:<30} | {result[3]:<30} |")
        
best_results = defaultdict(lambda: ('', float('inf')))

for file, pattern, algorithm, time in results:
    key = (file, pattern)
    if time < best_results[key][1]:
        best_results[key] = (algorithm, time)

print(f'\nОпитальний алгоритм для пошуку:\n')
print("| {:<30} | {:<30} | {:<30} | {:<30} |".format('Файл', 'Підрядок', 'Алгоритм', 'Час виконання, сек'))
print("| :----------------------------- | :----------------------------- | :----------------------------- | :----------------------------- |")

for (file, pattern), (algorithm, time) in best_results.items():
    print("| {:<30} | {:<30} | {:<30} | {:<30} |".format(file, pattern, algorithm, time))