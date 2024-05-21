import math


# Определение функции, ее производной и эквивалентной функции
def f(x):
    return x ** 3 - x ** 2 + 2


def df(x):
    return 3 * x ** 2 - 2 * x


def g(x):
    return (x - 2) / (x ** 2 - x + 1)


# Метод дихотомии
def bisection(f, a, b, tol=1e-6):
    # f - функция
    # a - начало интервала
    # b - конец интервала
    # tol - погрешность
    if f(a) * f(b) > 0:
        print("Нет корня в данном интервале.")
        return
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:  # Если знаки на нижней границе и середине интервала разные
            b = c  # Изменение верхней границы интервала
        else:
            a = c  # Изменение нижней границы интервала
    return (a + b) / 2


# Метод простых итераций
def simple_iteration(g, x0, tol=1e-6):
    x1 = g(x0)
    while abs(x1 - x0) > tol:  # Вычисление приближения
        x0, x1 = x1, g(x1)
    return x1


# Метод Ньютона
def newton(f, df, x0, tol=1e-6):
    x1 = x0 - f(x0) / df(x0)
    while abs(x1 - x0) > tol:  # Вычисление приближения
        x0, x1 = x1, x1 - f(x1) / df(x1)
    return x1


# Использование методов
print("Метод дихотомии: ", bisection(f, -200, 200))
print("Метод простых итераций: ", simple_iteration(g, 5))
print("Метод Ньютона: ", newton(f, df, 5))
