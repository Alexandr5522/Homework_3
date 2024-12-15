import math


def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        k = 0
        for i in range(2, res // 2 + 1):
            if res % i == 0:
                k = k + 1
        if k <= 0:
            print(f'Число {res} является простым.')
        else:
            print(f'Число {res} составное.')
        return res

    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


@is_prime
def multiplication(*args):
    return math.prod(args)


@is_prime
def average_value(*args):
    return sum(args) // len(args)


@is_prime
def difference_max_min(*args):
    return max(args) - min(args)


result = sum_three(2, 3, 6)
print(f'Результат суммы чисел: {result}')

result2 = multiplication(2, 4, 5)
print(f'Результат произведения чисел: {result2}')

result3 = average_value(5, 5, 5, 5)
print(f'Среднее значение чисел: {result3}')

result4 = difference_max_min(33, 23, 45)
print(f'Результат вычитания: {result4}')
