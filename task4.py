# Решение Задания 4, пункты 1 - 5

product = {'title': 'p1', 'price': 114, 'ingredients': ['i1.1', 'i1.2', 'i1.3']}
print('Specification of the product:\n', product, sep='')

# 1. Добавьте еще одну пару ключ-значение - "description" какой-то текст

product['description'] = 'd1'
print('Specification of the product:\n', product, sep='')

# 2. Увеличьте цену на 100.

product['price'] += 100
print('Specification of the product:\n', product, sep='')

# 3. Добавьте в список ингредиентов еще один ингредиент.

product['ingredients'].append('i1.4')
print('Specification of the product:\n', product, sep='')

# 4. Выделите на экран количество ингредиентов продукта.

print("Product consist of", len(product['ingredients']), "ingredients.")

# 5. Удалите из словаря значение с ключом "description"

product.pop('description')
print('Specification of the product:\n', product, sep='')
