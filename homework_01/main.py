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
    if num > 1:
        for i in range(2,int(num/2+1)):
            if num % i == 0:
                return False
            else:
                return True
    else:
        return False

def filter_numbers(num_list, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter_type == ODD:
        return list(filter(lambda num: num % 2 != 0, num_list))
    elif filter_type == EVEN:
        return list(filter(lambda num: num % 2 == 0, num_list))
    elif filter_type == PRIME:
        return list(filter(is_prime, num_list))
    else:
        return
