#Generador de impares
def impar_num(limit):
    x = 1
    while x<=limit:
        yield x
        x = x+2
for num in impar_num(11):
    print(num)


print('___________________________')

#Generador de pares
def par_num(limit):
    x = 0
    while x<=limit:
        yield x
        x = x+2
for num in par_num(11):
    print(num)

