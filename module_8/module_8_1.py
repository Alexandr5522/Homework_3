def add_everything_up(a, b):
    try:
        result = a + b
        print(round(result, 3))

    except TypeError as exc:
        print(f'{a},{b} - ', exc)


add_everything_up(123.456, 'строка')
add_everything_up('яблоко', 4215)
add_everything_up(123.456, 7)
