# Решение Задания 1, пункты 1 - 9

print('--- 1-3 ---')

s = input('Enter string: \n')

# 1. Определите является ли строка записью числа. (Подсказка: ищите как это сделать с помощью методов строк)

if s.isnumeric():                           # Метод isnumeric(), в отличии от isdecimal() или isdigit(),
    print('Entered string is a number.')    # дает более полное покрытие условия "записью числа"
else:
    print('Entered string is NOT a number.')

# 2. Посчитайте сколько у вас пробелов в строке.

print('Entered string includes', s.count(' '), 'space(s).')

# 3. Посчитайте сколько у вас символов точки '.' в строке.

print('Entered string includes', s.count('.'), '"." symbol(s).')

# 4. Создайте строку "Homework". Преобразуйте её в строку длиной 100 символов, посередине которой исходное слово,
# а с обоих сторон строка заполнена пробелами. Выведите её на экран. Убедитесь, что у вас 100 символов (посчитайте
# длину).

print('--- 4 ---')

s = 'Homework'
s = s.center(100)  # Пробел - это символ заполнения по умолчанию
print('New centered string: \n', s, sep='')
print('The length of this string is', len(s), 'character(s)')

# 5. Сделайте первые буквы слов строки большими (upper case).

print('--- 5 ---')

s = input('Enter string (that includes non alphabetic symbols):\n')
s = s.title()  # Быстрое решение, которое работает только для строки, слова которой состоят исключительно из букв.
print('Result by title() method:\n', s, sep='')
print('This method is not working properly if string includes non alphabetic symbols.')

print('Let\'s use developed method.')

# Решение задачи для строки в словах которой есть дополнительные символы (',*,$, etc.),
# а не только "alphabetic" символы. Если без своих функций и других модулей, придумал решение
# только с использованием еще одной строки.

while 1:  # Метод title() умеет работать со строкой '', а мы просто добавим проверку после ввода строки пользователем.
    s1 = input('Enter string (that includes non alphabetic symbols):\n')
    if s1 != '':
        break
    else:
        print('Enter valid string, please!')

s2 = ''     # Строка, в которую будем сохранять результат.

for i in range(len(s1)):
    if i == 0:                          # Первый символ в строке всегда пробуем сделать uppercase.
        s2 += s1[0].upper()
    elif i >= 1 and s1[i - 1] == ' ':   # Если предыдущий символ был пробелом, то нашли начало слова.
        s2 += s1[i].upper()             # Сохраняем в результат uppercase символ.
    else:
        s2 += s1[i]                     # Сораняем в результат символ без изменений.
print('Result by developed method:\n', s2, sep='')

# 6. Определите заканчивается ли ваша строка подстрокой “ing”.

print('--- 6 ---')

s = input('Enter string:\n')

if s.endswith('ing'):
    print('Entered string ends with "ing".')
else:
    print('Entered string is NOT ends with "ing".')

# 7. Определите индекс первого вхождения символа “a” в вашей строке.

print('--- 7 ---')

s = input('Enter string:\n')
try:  # Выбран метод index() чтобы отследить исключение - в строке нет символа "а".
    print('First "a" symbol index:\n', s.index('a'), sep='')
except ValueError:
    print('There is no "a" symbol in the string.')

# 8. Разбейте строку на список подстрок по символу пробела.

print('--- 8 ---')

s = input('Enter string:\n')
print('Created list:\n', s.split(), sep='')

# 9. Пусть у вас строка имеет пробельные символы. Найдите метод,
# который удаляет пробельные символы вначале и в конце, но не посередине.

print('--- 9 ---')

s = input('Enter string:\n')
print('Modified string:\n', s.strip(), sep='')
