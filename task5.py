# Решение Задания 5

while True:
    try:
        y = int(input('Enter a year:\n'))
        break
    except ValueError:
        print('NOT a year! Try again.')

if (not y % 4 and y % 100) or not y % 400:     # Если его номер кратен 4, но не кратен 100, а также если он кратен 400.
    print('YES')
else:
    print('NO')
