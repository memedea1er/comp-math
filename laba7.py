"""
Функции сортировки массива: пузырьковая сортировка, сортировка подсчетом, рекурсивная сортировка.

Переменные:
- start: время начала выполнения сортировки
- count: количество итераций
- duration: время выполнения
- arr: массив для сортировки
- n: длина массива
- max_val: максимальное значение в массиве
- min_val: минимальное значение в массиве
- count_arr: массив для подсчета частоты каждого элемента при сортировке подсчетом
- sorted_arr: отсортированный массив при сортировке подсчетом
- num: текущее число при подсчете частоты в сортировке подсчетом
- iterations: общее количество итераций сортировки
- result: результирующий отсортированный массив при рекурсивной сортировке
- left, right: отсортированные части массива при рекурсивной сортировке
- left_index, right_index, res_index: индексы для слияния массивов при рекурсивной сортировке
"""

import time
from random import randint


def bubble_sort(arr):
    """
    Пузырьковая сортировка массива.

    Параметры:
    - arr: list[int] - массив для сортировки

    Возвращает:
    - tuple: (отсортированный массив, количество итераций, время выполнения)
    """
    start = time.time()
    count = 0
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            count += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    duration = time.time() - start
    return arr, count, duration


def counting_sort(arr):
    """
    Сортировка подсчетом (суммированием) массива.

    Параметры:
    - arr: list[int] - массив для сортировки

    Возвращает:
    - tuple: (отсортированный массив, количество итераций, время выполнения)
    """
    start = time.time()
    max_val, min_val = max(arr), min(arr)
    count_arr = [0] * (max_val - min_val + 1)
    iterations = 0
    for num in arr:
        count_arr[num - min_val] += 1
        iterations += 1
    sorted_arr = [i + min_val for i, count in enumerate(count_arr) for _ in range(count)]
    duration = time.time() - start
    return sorted_arr, iterations, duration


def quick_sort(arr):
    """
    Рекурсивная сортировка массива.

    Параметры:
    - arr: list[int] - массив для сортировки

    Возвращает:
    - tuple: (отсортированный массив, количество итераций, время выполнения)
    """
    start = time.time()
    if len(arr) <= 1:
        duration = time.time() - start
        return arr, 0, duration

    mid = len(arr) // 2  # Опорный элемент
    left, left_iterations, _ = quick_sort(arr[:mid])
    right, right_iterations, _ = quick_sort(arr[mid:])

    result, res_in, left_in, right_in = [0] * (len(left) + len(right)), 0, 0, 0
    iterations = left_iterations + right_iterations

    while left_in < len(left) and right_in < len(right):
        iterations += 1
        if left[left_in] < right[right_in]:
            result[res_in] = left[left_in]
            left_in += 1
        else:
            result[res_in] = right[right_in]
            right_in += 1
        res_in += 1

    result[res_in:] = left[left_in:] if left_in < len(left) else right[right_in:]
    iterations += len(left) - left_in + len(right) - right_in

    duration = time.time() - start
    return result, iterations, duration


my_list = [randint(-10000, 10000) for _ in range(10000)]

sorted_list, iterations, durations = bubble_sort(my_list.copy())
print("Пузырьковая сортировка:")
print("Количество итераций:", iterations)
print("Время выполнения:", durations)
print()

sorted_list, iterations, durations = counting_sort(my_list.copy())
print("Сортировка подсчетом (суммированием):")
print("Количество итераций:", iterations)
print("Время выполнения:", durations)
print()

sorted_list, iterations, durations = quick_sort(my_list.copy())
print("Рекурентная сортировка:")
print("Количество итераций:", iterations)
print("Время выполнения:", durations)
print()
