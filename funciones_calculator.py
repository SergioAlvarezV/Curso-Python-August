def add(a,b):
    return a + b
    
def substract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

def calculator():
    while True:
        print('Eliga una opcion')
        print('1. Suma')
        print('2. Resta')
        print('3. Multiplica')
        print('4. Divide')
        print('5. Salir')

        option = int(input('Ingrese su opcion (1,2,3,4,5): '))

        if option == 5:
            print('Saliendo de la Calculadora')
            break

        elif option in [1,2,3,4]:
            num1 = float(input('Ingrese el Primer Numero: '))
            num2 = float(input('Ingrese el Segundo Numero: '))

            if option == 1:
                print(f'La Suma de {num1} + {num2} es :', add(num1,num2))
            elif option == 2:
                print(f'La Resta de {num1} - {num2} es :', substract(num1,num2))
            elif option == 3:
                print(f'La Multiplicacion de {num1} X {num2} es :', multiply(num1,num2))
            elif option == 4:
                print(f'La Divicion de {num1} / {num2} es :', divide(num1,num2))

        else:
            print('Opcion no Valida Intente de nuevo')
                

calculator()
