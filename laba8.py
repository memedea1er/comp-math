"""
Генерация псевдослучайных чисел, подсчет псевдопериода, расчет математического ожидания и дисперсии,
создание дискретной случайной величины.

Переменные:
- random_numbers: список, содержащий сгенерированные псевдослучайные числа
- pseudo_period_count: количество повторений первых пяти чисел в том же порядке (псевдопериод)
- mean: математическое ожидание псевдослучайных чисел
- variance: дисперсия псевдослучайных чисел
- values: значения дискретной случайной величины
- probabilities: вероятности соответствующих значений дискретной случайной величины
- random_value: случайное число от 0 до 1, используемое для создания дискретной случайной величины
- discrete_random_variable: значение дискретной случайной величины, сгенерированное на основе вероятностей
"""

import random
from collections import Counter

# Генерация большого массива псевдослучайных чисел
random_numbers = [random.randint(0, 10) for _ in range(100000)]

# Подсчет псевдопериода - сколько раз повторяются первые 2 числа в таком же порядке
pseudo_period_count = Counter(tuple(random_numbers[i:i + 2]) for i in range(len(random_numbers) - 2))
pseudo_period_count = pseudo_period_count[tuple(random_numbers[:2])]

# Расчет математического ожидания и дисперсии
mean = sum(random_numbers) / len(random_numbers)
variance = sum((x - mean) ** 2 for x in random_numbers) / len(random_numbers)

print("Псевдопериод:", pseudo_period_count)
print("Математическое ожидание:", mean)
print("Дисперсия:", variance)

# Создание дискретной случайной величины с заданными значениями и вероятностями
values = [1, 2, 3, 4, 5]
probabilities = [0.05, 0.2, 0.3, 0.4, 0.05]

cumulative_prob = 0
random_value = random.random()

# Выбор значения дискретной случайной величины на основе вероятностей
for i in range(len(values)):
    value = values[i]
    prob = probabilities[i]
    cumulative_prob += prob
    if cumulative_prob >= random_value:
        discrete_random_variable = value
        break


print("Дискретная случайная величина с заданными значениями и вероятностями:", discrete_random_variable)
