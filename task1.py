# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

while True:
    number = int(input('Введите день недели  '))
    if number == 6 or number == 7:
        print('Выходной')
        break
    if number < 6:
        print('Рабочий день')
    else:
        print('Такого дня недели нет')