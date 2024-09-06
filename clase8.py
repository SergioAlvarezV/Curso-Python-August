to_do = ['Dirigirnos al hotel',
        'ir al almorzar',
        'visitar un museo',
        'volver al hotel']
print(to_do)

numbers = [1, 2, 3, 4, 'cinco']
print(numbers)
print(type(numbers))

mix = ['uno', 2, 3.14, True, [1,2,3]]
print(mix)
print(len(mix))
print('Primera posicion',mix[0])
print('Ultima posicion',mix[-1])
print(len(mix[4]))

string = 'Hola mundo'
print('Primera posicion',string[0])
print('Segunda posicion',string[1])
print('Ultima posicion',string[-1])

print(mix[0:2])
print(mix)
mix.append(False)
print(mix)
mix.insert(0,['a','b','c'])
print(mix)
print(mix.index(['a','b','c']))
numbers = [10,2,3,-2,50]
print(numbers)
print('Mayor',max(numbers))
print('Menor',min(numbers))

del numbers[:2]
print(numbers)