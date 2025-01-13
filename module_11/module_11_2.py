from pprint import pprint


def introspection_info(obj):
    info = {} # пустой словарь
    info['type'] = type(obj) # Определение типа объекта

    info['id'] = id(obj) # определение id объекта

    # Получение атрибутов объекта
    info['attributes'] = [attr for attr in dir(obj) if not callable(attr) and not attr.startswith('__')]

    # Получение методов объекта
    info['methods'] = [method for method in dir(obj) if callable(getattr(obj, method))]

    info['module'] = obj.__class__.__module__ # Определение модуля, к которому объект принадлежит

    return info

# интроспекция для int
pprint(introspection_info(42))

# для list
pprint(introspection_info([2, 3, 'three']))
