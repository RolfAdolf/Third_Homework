# Домашняя работа #3
к третьему спринту
##
##
### Задача №1
#### Условие
Реализовать перевод в двоичную систему без использования встроенных инструментов
#### Идея
Рекурсивно реализовать ручной перевод делением. Файл `first_task.py`.
##
##
### Задача №2
##### Условие
Определить, является ли строка палиндромом.
#### Первое решение (Python-однострчник)
##### Идея
Удалить все небуквенные (и нечисленные) символы, привести к одному регистру и перевернуть строку. Файл `second_task.py` с `pth = True`. Данное решение работает быстрее следующего метода.
#### Второе решение (Универсальное)
##### Идея
Использовать метод двух индексов и пройтись по строке попарно сравнивая крайний правый и крайний левый символы итерации, пропуская небуквенные (и нечисленные) символы. Файл `second_task.py` с `pth = False`. 
