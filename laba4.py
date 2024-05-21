import numpy as np
import matplotlib.pyplot as plt

# Аналитическое решение интеграла
def analitic_integr(t):
    return 1 - np.cos(t)

# Метод прямоугольников для вычисления интеграла
def rectangle_rule_integration(t_values, num_points=1000):
    integrals = []
    for t in t_values:
        points = np.linspace(0, t, num_points)
        function_values = np.sin(points)
        step = t / num_points
        integral = np.sum(function_values) * step
        integrals.append(integral)
    return np.array(integrals)

# Метод трапеций для вычисления интеграла
def trapezoidal_rule_integration(t_values, num_points=1000):
    integrals = []
    for t in t_values:
        points = np.linspace(0, t, num_points)
        function_values = np.sin(points)
        step = t / num_points
        integral = 0
        for i in range(1, num_points):
            integral += step / 2 * (function_values[i-1] + function_values[i])
        integrals.append(integral)
    return np.array(integrals)

# Метод Симпсона для вычисления интеграла
def simpsons_rule_integration(t_values, num_points=1000):
    integrals = []
    for t in t_values:
        points = np.linspace(0, t, num_points)
        function_values = np.sin(points)
        step = t / num_points
        integral = 0
        for i in range(1, num_points - 1):
            integral += step / 6 * (function_values[i-1] + 4*function_values[i] + function_values[i+1])
        integrals.append(integral)
    return np.array(integrals)

# Значения t для интегрирования
t_values = np.linspace(0, np.pi, 1000)

# Вычисляем интегралы с помощью различных методов интегрирования
integrals_rectangle = rectangle_rule_integration(t_values)
integrals_trapezoidal = trapezoidal_rule_integration(t_values)
integrals_simpsons = simpsons_rule_integration(t_values)
integrals_analitic = analitic_integr(t_values)

# Графики для сравнения методов интегрирования
plt.figure(figsize=(10, 18))

# График разности между методом прямоугольников и аналитическим решением
plt.subplot(3, 1, 1)
plt.plot(t_values, integrals_rectangle - integrals_analitic, label='Метод прямоугольников')
plt.title('Сравнение методов интегрирования - Метод прямоугольников')
plt.xlabel('t')
plt.ylabel('Разница с аналитическим значением')
plt.grid(True)
plt.legend()

# График разности между методом трапеций и аналитическим решением
plt.subplot(3, 1, 2)
plt.plot(t_values, integrals_trapezoidal - integrals_analitic, label='Метод трапеций')
plt.title('Сравнение методов интегрирования - Метод трапеций')
plt.xlabel('t')
plt.ylabel('Разница с аналитическим значением')
plt.grid(True)
plt.legend()

# График разности между методом Симпсона и аналитическим решением
plt.subplot(3, 1, 3)
plt.plot(t_values, integrals_simpsons - integrals_analitic, label='Метод Симпсона')
plt.title('Сравнение методов интегрирования - Метод Симпсона')
plt.xlabel('t')
plt.ylabel('Разница с аналитическим значением')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
