import math


def square(side):
    return math.ceil(side) * math.ceil(side)


num_side = int(input('Введите сторону квадрата: '))
print(f'Площадь квадрата: {square(num_side)}')
