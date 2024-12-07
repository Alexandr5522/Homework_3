def apply_all_func(int_list, *functions):
    #  int_list - список из чисел (int, float)
    # *functions - неограниченное кол-во функций (которые применимы к спискам, состоящим из чисел)
    """Функция создает словарь из значений встроенных функций"""
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list)
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))