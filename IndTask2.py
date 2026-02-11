#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def debug_call(*args, **kwargs):
    args_count = len(args)
    kwargs_count = len(kwargs)
    
    types_list = []
    
    # Добавляем типы позиционных аргументов
    for arg in args:
        types_list.append(type(arg).__name__)
    
    # Добавляем типы именованных аргументов
    for value in kwargs.values():
        types_list.append(type(value).__name__)
    
    types_str = ", ".join(types_list)
    
    return f"Args: {args_count}, Kwargs: {kwargs_count}, Types: {types_str}"


# Пример использования
if __name__ == "__main__":
    # Тестовые вызовы
    result1 = debug_call(1, "строка", 3.14, name="Иван", age=25)
    print(result1)
    
    result2 = debug_call(10, 20, 30, a=1, b=[2, 3], c={"x": 5})
    print(result2)