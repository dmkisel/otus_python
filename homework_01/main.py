"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*number):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [num ** 2 for num in number]

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(num):
    """
       функция для проверки входящих чисел на простое число
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    else:
        return True

def filter_numbers(num_list, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    >>> filter_numbers([7629, 77, 7485, 2229, 7235, 5705, 7437, 3101, 3333, 3265, 6085, 7205, 789, 4323, 7935, 8749, 3565, 5525, 4867, 9639, 3269, 705, 2629, 3117, 8911, 6499, 5565, 6911, 5437, 4285, 2421, 795, 5955, 3927, 247, 8285, 8067, 5583, 1193, 3885, 3229, 7007, 1079, 2371, 7343, 6545, 4135], PRIME)
    <<< [6911, 5437, 1193, 3229, 2371]
    """
    if filter_type == ODD:
        return list(filter(lambda num: num % 2 != 0, num_list))
    elif filter_type == EVEN:
        return list(filter(lambda num: num % 2 == 0, num_list))
    elif filter_type == PRIME:
        return list(filter(is_prime, num_list))
    else:
        return
