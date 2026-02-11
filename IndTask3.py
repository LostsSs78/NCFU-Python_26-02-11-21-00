#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def remove_keys(data, condition):
    """
    Рекурсивно проходит по словарю и удаляет все ключи,
    для которых condition(key, value) возвращает True.
    """
    if not isinstance(data, dict):
        return data
    
    keys_to_delete = []
    for key, value in data.items():
        # Рекурсивно обрабатываем вложенные словари
        if isinstance(value, dict):
            data[key] = remove_keys(value, condition)
        
        # Проверяем условие для текущего ключа
        if condition(key, value):
            keys_to_delete.append(key)
    
    # Удаляем ключи, для которых условие истинно
    for key in keys_to_delete:
        del data[key]
    
    return data


# Пример использования
if __name__ == "__main__":
    data = {"a": 1, "b": {"c": 2, "d": 3}}
    print(f"Исходные данные: {data}")
    
    result = remove_keys(data.copy(), lambda k, v: isinstance(v, int) and v % 2 == 0)
    print(f"После удаления чётных значений: {result}")
    
    # Дополнительные примеры
    data2 = {
        "x": 10, 
        "y": 15, 
        "z": {"p": 20, "q": 25, "r": {"m": 30, "n": 35}}
    }
    print(f"\nДругой пример: {data2}")
    
    # Удаляем ключи с чётными значениями
    result2 = remove_keys(data2.copy(), lambda k, v: isinstance(v, int) and v % 2 == 0)
    print(f"После удаления чётных значений: {result2}")
    
    # Удаляем ключи, начинающиеся с определённой буквы
    data3 = {"apple": 5, "banana": 3, "cherry": {"apricot": 7, "blueberry": 2}}
    result3 = remove_keys(data3.copy(), lambda k, v: k.startswith('a'))
    print(f"\nУдаление ключей на 'a': {result3}")
