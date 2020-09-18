# Решение Задания 7
# Ошибки ввода пользователем негативных данных не отслеживаются.

a = int(input('Enter value for the "a":\n'))
b = int(input('Enter value for the "b":\n'))
c = int(input('Enter value for the "c":\n'))

if a > b:           # Сортировка "бульбашкою" =) для 3-х чисел используя синтаксис Python.
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a

print('a=', a, 'b=', b, 'c=', c)
