import random


def gauss_elimination(matrix):
    n = len(matrix)  # Определение размера матрицы (количество уравнений)

    # Прямой ход
    for i in range(n):
        # Проверка на нулевой диагональный элемент
        if matrix[i][i] == 0:
            for k in range(i + 1, n):
                if matrix[k][i] != 0:  # Если нашли ненулевой элемент
                    # Меняем местами текущую строку и строку с ненулевым элементом
                    matrix[i], matrix[k] = matrix[k], matrix[i]
                    break
            else:
                # Если весь столбец нулевой, то система не имеет единственного решения
                raise ValueError("Система не имеет единственного решения")

        # Приведение к верхнетреугольному виду
        for j in range(i + 1, n):
            factor = matrix[j][i] / matrix[i][i]  # Вычисление коэффициента
            for k in range(i, n + 1):
                matrix[j][k] -= factor * matrix[i][k]  # Обнуление элементов
        for i in matrix:
            print(i)
        print()

    # Обратный ход
    x = [0] * n  # Инициализация списка для хранения решений
    for i in range(n - 1, -1, -1):
        x[i] = matrix[i][n] / matrix[i][i]  # Вычисление значения переменной
        for j in range(i - 1, -1, -1):  # Итерация в обратном порядке по строкам выше текущей
            matrix[j][n] -= matrix[j][i] * x[i]  # Обновление правой части

    return x


# Пример использования

matrix = [
    [0, -1, 2, 8],
    [0, 2, -2, -11],
    [9, 1, 2, 3]
]

# Рандомная матрица

# size = int(input("Введите размер: "))
# matrix = [[_ for _ in range(size + 1)] for i in range(size)]
#
# for i in range(size):
#     for j in range(len(matrix[size - 1])):
#         rand = random.randint(-10, 10)
#         matrix[i][j] = rand

for i in matrix:
    print(i)

solution = gauss_elimination(matrix)
print("Решение СЛАУ:", solution)
