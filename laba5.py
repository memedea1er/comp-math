"""
Численное решение дифференциальных уравнений
Решаются уравнения x''+x=0,t,sin(t)
Бояршинов, ч.4
"""

import numpy as np
import matplotlib.pyplot as plt


# Аналитические решения уравнений
def analytical_solution_1(t):
    return np.sin(t)


def analytical_solution_2(t):
    return t


def analytical_solution_3(t):
    return 3 * np.sin(t) / 2 - t * np.cos(t) / 2


"""
f - это функция, описывающая правую часть ОДУ.
Она должна принимать два аргумента: время t и текущее значение переменной x.
Возвращаемое значение должно быть производной x по времени в точке t.
x0 и v0 - начальные условия для переменных x и v соответственно.
t0 - начальное время.
tn - конечное время, до которого нужно проинтегрировать ОДУ.
h - шаг интегрирования.
"""


# Реализация метода Эйлера для дифференциального уравнения
def euler_method(f, x0, v0, t0, tn, h):
    t_values = [t0]
    x_values = [x0]
    v_values = [v0]

    while t_values[-1] < tn:
        # Получение текущих значений
        t = t_values[-1]
        x = x_values[-1]
        v = v_values[-1]

        # Вычисление производных
        dx_dt = v
        dv_dt = f(t, x)

        # Обновление значений
        x_new = x + h * dx_dt
        v_new = v + h * dv_dt
        t_new = t + h

        # Добавление новых значений в списки
        t_values.append(t_new)
        x_values.append(x_new)
        v_values.append(v_new)

    return t_values, x_values


# Функции правой части дифференциальных уравнений
def f1(t, x):
    return -x


def f2(t, x):
    return t - x


def f3(t, x):
    return np.sin(t) - x


# Начальные условия и параметры
x0, v0 = 0, 1
t0, tn = 0, 30
h = 0.001

# Вычисление значений методом Эйлера для каждого уравнения
t_values1, x_values1 = euler_method(f1, x0, v0, t0, tn, h)
t_values2, x_values2 = euler_method(f2, x0, v0, t0, tn, h)
t_values3, x_values3 = euler_method(f3, x0, v0, t0, tn, h)

# Вычисление аналитических решений
analytical_values1 = analytical_solution_1(np.array(t_values1))
analytical_values2 = analytical_solution_2(np.array(t_values2))
analytical_values3 = analytical_solution_3(np.array(t_values3))

# Построение графиков
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.plot(t_values1, x_values1 - analytical_values1, label="x''(t) + x(t) = 0")
plt.title("x''(t) + x(t) = 0")
plt.xlabel("t")
plt.ylabel("Разница с аналитическим значением")
plt.legend()

plt.subplot(1, 3, 2)
plt.plot(t_values2, x_values2 - analytical_values2, label="x''(t) + x(t) = t")
plt.title("x''(t) + x(t) = t")
plt.xlabel("t")
plt.ylabel("Разница с аналитическим значением")
plt.legend()

plt.subplot(1, 3, 3)
plt.plot(t_values3, x_values3 - analytical_values3, label="x''(t) + x(t) = sin(t)")
plt.title("x''(t) + x(t) = sin(t)")
plt.xlabel("t")
plt.ylabel("Разница с аналитическим значением")
plt.legend()

plt.tight_layout()
plt.show()
