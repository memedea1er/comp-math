import math
import numpy as np
import matplotlib.pyplot as plt

def forward_diff(f, x, h):
    return (f(x + h) - f(x)) / h

def backward_diff(f, x, h):
    return (f(x) - f(x - h)) / h

def central_diff(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

# Пример функции для дифференцирования
def function(x):
    return np.sin(x)

# Задаем интервал и шаг для построения графика
x_values = np.linspace(0, 2*math.pi, 100)
h_value = 10**(-6)

# Вычисляем значения производных
forward_diff_values = [forward_diff(function, xi, h_value) for xi in x_values]
backward_diff_values = [backward_diff(function, xi, h_value) for xi in x_values]
central_diff_values = [central_diff(function, xi, h_value) for xi in x_values]

# Строим графики
plt.figure(figsize=(10, 6))
# plt.plot(x_values, function(x_values), label='f(x)')
plt.plot(x_values, forward_diff_values-np.cos(x_values), label='Forward Difference')
# plt.plot(x_values, backward_diff_values, label='Backward Difference')
# plt.plot(x_values, central_diff_values, label='Central Difference')
plt.legend()
plt.title('Numerical Differentiation')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
