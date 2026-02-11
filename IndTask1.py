#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys 


def get_student():
    name = input("Фамилия и инициалы? ")
    group_number = input("Номер группы? ")
    marks = [int(mark) for mark in input("Успеваемость? (Список из 5 цифр, записывать через пробел)? ").split()]

    # Создать словарь
    return {
        'name': name,
        'group': group_number,
        'marks': marks,
    }

def display_students(staff):
    """
    Отобразить список работников.
    """
    # Проверить, что список работников не пуст.
    if staff:
        # Заголовок таблицы.
        line = '+{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 12
        )
        print(line)
        print(
            '| {:>4} | {:>30} | {:>20} | {:>8} |'.format(
                "№",
                "Ф.И.О.",
                "Номер группы",
                "Успеваемость"
            )
        )
        print(line)

        # Вывести данные о всех сотрудниках.
        for idx, student in enumerate(staff, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                    idx,
                    student.get('name', ''),
                    student.get('group', ''),
                    " ".join([str(mark) for mark in student.get('marks', '')])
                )
            )
        print(line)
    else:
        print("Список студентов пуст.")

def select_students(staff):
    result = []
    for student in staff:
        if (sum(student['marks']) / 5) > 4.0:
            result.append(student)

    # Возвратить список выбранных работников.
    return result

def main():
    """
    Главная функция программы.
    """
    # Список работников.
    students = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">> ").lower()

        # Выполнить действие в соответствии с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о работнике.
            student = get_student()
            # Добавить словарь в список.
            students.append(student)

            # Отсортировать список в случае необходимости.
            if len(students) > 1:
                students.sort(key=lambda item: item.get('group', ''))

        elif command == 'list':
            # Отобразить всех работников.
            display_students(students)

        elif command.startswith('select'):
            selected = select_students(students)
            # Отобразить выбранных студентов.
            display_students(selected)

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить студента;")
            print("list - вывести список студентов;")
            print("select <стаж> - запросить студентов со средним баллом больше 4.0;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
            return 1

    return 0

if __name__ == '__main__':
    sys.exit(main())