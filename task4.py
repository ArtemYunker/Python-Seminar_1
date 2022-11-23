# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

while True:
    number = int(input('Введите номер четверти:  '))
    if 1 <= number <= 4:
        if number == 1:
            print('x > 0 and y > 0')
        if number == 2:
            print('x < 0 and y > 0')
        if number == 3:
            print('x > 0 and y < 0')
        if number == 4:
            print('x > 0 and y < 0')
        break
    else:
        print('Вводимое чило жолжно быть от 1 до 4')