# Решение Задания 6
# Ошибки ввода пользователем негативных данных не отслеживаются.

a = int(input('Enter value for the "a" side:\n'))
b = int(input('Enter value for the "b" side:\n'))
c = int(input('Enter value for the "c" side:\n'))

if (a + b) > c and (a + c) > b and (c + b) > a:     # Сумма значений любых двух сторон треугольника должна быть
    print('Result: YES')                            # больше значения третьей стороны.
else:
    print('Result: NO')
