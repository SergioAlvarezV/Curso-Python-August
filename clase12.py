numbers = [1, 2, 3, 4, 5]
for x in numbers:
    print('Aqui x es igual a :',x+1)

for e in range(0,11):
    print(type(e))
    print(e)

fruits = ['Manzana', 'Pera', 'Uva', 'Naranja', 'Tomate']
for fruit in fruits:
    print(fruit)
    if fruit == 'Naranja':
        print('Naranja encontrada')

x = 0
while x<5:
    if x == 3:
        break
    print(x)
    x += 1

numbers = [1, 2, 3, 4, 5]
for x in numbers:
    if x ==3:
        continue
    print('Aqui x es igual a :',x+1)