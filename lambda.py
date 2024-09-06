add = lambda a,b: a + b
print(add(11,3))

multiply = lambda a,b: a * b
print(multiply(5,3))

#Cuadrados de cada numero
numers = range(1,11)
squared_numbers = list(map(lambda x:x**2, numers))
print('Cuadrados:', squared_numbers)

#Pares
even_numbers = list(filter(lambda x: x%2 ==0, numers))
print('Pares:', even_numbers)