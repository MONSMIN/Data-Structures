import numpy as np
import scipy.integrate as spi

from tabulate import tabulate

# Визначте функцію, яку потрібно інтегрувати, наприклад, f(x) = x^2
def f(x):
    return x ** 2

# Визначте межі інтегрування, наприклад, від 0 до 1
a = 0  # Нижня межа
b = 2  # Верхня межа

# Обчислення інтеграла методом Монте-Карло
num_points = 10000
random_x = np.random.uniform(a, b, num_points)
random_y = np.random.uniform(0, max(f(random_x)), num_points)
points_under_curve = sum(random_y <= f(random_x))
area_ratio = points_under_curve / num_points
monte_carlo_integral = (b - a) * max(f(random_x)) * area_ratio

# Обчислення інтеграла за допомогою функції quad
quad_integral, quad_error = spi.quad(f, a, b)


results = [
    ["Метод", "Значення інтеграла"],
    ["Монте-Карло", monte_carlo_integral],
    ["quad", quad_integral]
]

# Виведення результатів
print(tabulate(results, headers="firstrow", tablefmt="fancy_grid"))
print(f"Оцінка абсолютної помилки {quad_error}")
