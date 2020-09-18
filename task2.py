# Решение Задания 2, пункты 1 - 6
# Ошибки ввода пользователем негативных данных не отслеживаются.

# 1. Вычислите длину гипотенузы в прямоугольном треугольнике со сторонами 367 и 127.

print('--- 1 ---')

c = (367**2 + 127**2)**.5
print('Hypotenuse:\n', c, sep='')

# 2. Дано двузначное число. Найдите число десятков в нем.

print('--- 2 ---')

n = int(input('Enter two-digit number:\n'))
print(n // 10, 'tens in this number.')

# 3. Дано трёхзначное число. Найдите сумму его цифр.

print('--- 3 ---')

n = int(input('Enter three-digit number:\n'))     # Исходя из задания, начинаем работу с числа, а не строки.
n = str(n)
print(n[0], '+', n[1], '+', n[2], '=', int(n[0]) + int(n[1]) + int(n[2]))

# 4. Дано целое число n. Выведите следующее за ним чётное число.

print('--- 4 ---')

n = int(input('Enter integer:\n'))

if (n+1) % 2 == 0:
    print('Next even number:\n', n + 1, sep='')
else:
    print('Next even number:\n', n + 2, sep='')

# 5. Дано положительное действительное число X. Выведите его дробную часть.

print('--- 5 ---')

r = float(input('Enter positive real number:\n'))
print('Fractional part of this number:\n', r - int(r), sep='')

# 6. Дано положительное действительное число X. Выведите его первую цифру после десятичной точки.

print('--- 6 ---')

r = float(input('Enter positive real number:\n'))
print('First number after the "." symbol:\n', (int(r * 10) % 10), sep='')
