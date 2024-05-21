"""
Интерполяция функции y = |x| с использованием полинома Лагранжа на равномерной и сетке Чебышева.

Переменные:
x_min, x_max: минимальное и максимальное значения для интерполяции
num_points: количество точек для интерполяции
x_uniform: массив X-координат с равномерной сеткой
x_chebyshev: массив X-координат с сеткой Чебышева
y: массив Y-координат для равномерной сетки
y_chebyshev: массив Y-координат для сетки Чебышева
x_interp: массив X-координат для интерполяции
y_interp_uniform: интерполированные значения для равномерной сетки
y_interp_chebyshev: интерполированные значения для сетки Чебышева

Функции:
lagrange_interpolation(x, y, x_interp): интерполяция с использованием полинома Лагранжа
absolute_function(x): определение функции y = |x|

Библиотеки:
numpy as np: библиотека для работы с массивами
matplotlib.pyplot as plt: библиотека для построения графиков
"""

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

# Функция для интерполяции полиномом Лагранжа
def lagrange_interpolation(x, y, x_interp):
    """
    Интерполяция с использованием полинома Лагранжа.

    Параметры:
        x (массив): X-координаты известных точек.
        y (массив): Y-координаты известных точек.
        x_interp (массив): X-координаты, в которых требуется интерполяция.

    Возвращает:
        массив: Интерполированные значения, соответствующие x_interp.
    """
    n = len(x)  # Количество известных точек
    m = len(x_interp)  # Количество точек для интерполяции
    interpolated_values = np.zeros(m)  # Массив для хранения интерполированных значений

    # Вычисление интерполированных значений для каждой точки x_interp
    for i in range(m):
        sum = 0.0
        for j in range(n):
            product = y[j]
            for k in range(n):
                if k != j:
                    product *= (x_interp[i] - x[k]) / (x[j] - x[k])
            sum += product
        interpolated_values[i] = sum

    return interpolated_values

# Определение функции y = |x|
def absolute_function(x):
    return abs(x)

# Задание границ интервала и количества точек для интерполяции
x_min, x_max = -1, 1
num_points = 11

# Генерация точек для равномерной сетки
x_uniform = np.linspace(x_min, x_max, num_points)

# Генерация точек для сетки Чебышева
x_chebyshev = ((x_max + x_min) / 2) + ((x_max - x_min) / 2) * np.cos(
    ((2 * np.arange(0, num_points) + 1) * np.pi) / (2 * (num_points)))

# Вычисление значений y для каждой сетки
y = absolute_function(x_uniform)
y_chebyshev = absolute_function(x_chebyshev)

# Генерация точек для интерполяции
x_interp = np.linspace(x_min, x_max, 1000)

# Интерполяция с использованием полинома Лагранжа на равномерной сетке
y_interp_uniform = lagrange_interpolation(x_uniform, y, x_interp)

# Интерполяция с использованием полинома Лагранжа на сетке Чебышева
y_interp_chebyshev = lagrange_interpolation(x_chebyshev, y_chebyshev, x_interp)

# Построение графиков
plt.figure(figsize=(12, 6))

# Первый график с равномерной сеткой
plt.subplot(1, 2, 1)
plt.plot(x_interp, absolute_function(x_interp), label='Исходная Функция', color='black')
plt.plot(x_interp, y_interp_uniform, label='Равномерная Интерполяция', linestyle='--', color='blue')
plt.scatter(x_uniform, y, label='Точки Интерполяции (Равномерные)', color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Равномерная Интерполяция y = |x|')
plt.legend()
plt.grid(True)

# Второй график с сеткой Чебышева
plt.subplot(1, 2, 2)
plt.plot(x_interp, absolute_function(x_interp), label='Исходная Функция', color='black')
plt.plot(x_interp, y_interp_chebyshev, label='Интерполяция на сетке Чебышева', linestyle='--', color='red')
plt.scatter(x_chebyshev, y_chebyshev, label='Точки Интерполяции (Чебышев)', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Интерполяция на сетке Чебышева y = |x|')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
