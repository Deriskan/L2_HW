# Решение Задания 8
# Ошибки ввода пользователем негативных данных не отслеживаются.

a = int(input('Enter value for the "a":\n'))
b = int(input('Enter value for the "b":\n'))
c = int(input('Enter value for the "c":\n'))

if a == b == c:                     # Начинаем с однозначного условия.
    print('Result:', 3)
elif a == b or b == c or a == c:    # Сравниваем попарно.
    print('Result:', 2)
else:
    print('Result:', 0)
