# Решение Задания 3, пункты 1 - 7

lst = ['planet', 'continent', 'world', 'country', 'ocean', 'world', 'sea']

print('Initial list:\n', lst, sep='')

# 1. Выведите 3-е с конца слово из списка.

print('3rd element from the end of the list:\n', lst[-3], sep='')

# 2. Выведите 1-ю букву второго слова из списка.

print('1st symbol of the 2nd element from the list:\n', lst[1][0], sep='')

# 3. Выведите последнюю букву последнего слова из списка.

print('Last symbol of the last element from the list:\n', lst[-1][-1], sep='')

# 4. Добавьте в конец списка еще одно слово.

lst.append('river')
print('The string "river" is added to the end of the list:\n', lst, sep='')

# 5. Вставьте в середину списка еще одно слово.

lst.insert(len(lst) // 2, 'lake')
print('The string "lake" is added to the middle of the list:\n', lst, sep='')

# 6. Удалите первое слово из списка.

lst.pop(0)
print('1st element is removed from the list:\n', lst, sep='')

# 7. Удалите слово "world" из списка, если оно есть в списке.

while True:
    try:
        lst.remove('world')     # Вызываем метод remove() пока слово "world" есть в списке
    except ValueError:
        print('Now the string "world" is definitely not an element of the list.')
        break
print('Final list:\n', lst, sep='')
