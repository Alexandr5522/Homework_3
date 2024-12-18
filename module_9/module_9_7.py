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
    a_value = sum(args) // len(args)
    if not isinstance(args, int):
        raise TypeError
    else:
        return a_value


@is_prime
def difference_max_min(*args):
    return max(args) - min(args)


@is_prime
def division(*args):
    # for i in args:                       # вариант проверки типа данных
    #     if not isinstance(i, int):
    #         lt = list(filter(lambda x: type(x) is int, args))
    #         return (max(lt) + sum(lt)) // min(lt)
    try:                                           # вариант проверки типа данных с исключением
        return (max(args) + sum(args)) // min(args)
    except TypeError as exc:
        print('Неверный тип данных:', exc)
    finally:
        lt = list(filter(lambda x: type(x) is int, args))
        return (max(lt) + sum(lt)) // min(lt)

@is_prime
def list_numbers(*args):
    return sum(args)




result = sum_three(2, 3, 6)
print(f'1. Результат суммы чисел: {result}')

result2 = multiplication(2, 4, 5)
print(f'2. Результат произведения чисел: {result2}')

try:
    result3 = average_value(5, 5, 5, 5, 'Green')
    print(f'3. Среднее значение чисел: {result3}')
except TypeError:
    print('3. Неверный тип данных ')


result4 = difference_max_min(33, 23, 45)
print(f'4. Результат вычитания: {result4}')

result5 = division(3, 5, 10, 'Apple', 6, 'Orange')
print(f'5. Результат функции: {result5}')

num1 = [5, 7, 5, 9, 2, 50]
num2 = [4, 3, 10, 8, 1]
result6 = list_numbers(*list(x for x in range(1, 11))) # с использованием сборки
print(f'6. Результат функции: {result6}')
result7 = list_numbers(*list(x for x in num1 + num2))
print(f'7. Результат функции: {result7}')
