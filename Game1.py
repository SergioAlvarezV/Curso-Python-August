#Game de piedra papel o tijera version 0.0.0_beta
print('Bienvenido a el Game de Piedra Papel o Tijera')
option = ('Papel', 'Piedra', 'Tijera')
user_1 = input('Nombre primer jugador => ')
user_2 = input('Nombre Segundo jugador => ')
print(f'Bienvenidos {user_1} y {user_2} Eligan una opcion cada uno')
option_1 = input(f'{user_1} elige entre (Piedra Papel o Tijera) => ')
option_2 = input(f'{user_2} elige entre (Piedra Papel o Tijera) => ')
option_1 = option_1.capitalize()
option_2 = option_2.capitalize()
print(option_1)
print(option_2)
if option_1 not in option or option_2 not in option:
       print('Alguno de los dos no a elegido bien')
elif option_1 == 'Tijera' and option_2 == 'Piedra':
       print('Piedra Rompe Tijera')
       print(f'{user_2} es el Ganador')
elif option_1 == 'Papel' and option_2 == 'Piedra':
       print('Papel cubre a Piedra')
       print(f'{user_1} es el ganador')
elif option_1 == 'Tijera' and option_2 == 'Papel':
       print('Tijera rompe papel')
       print(f'{user_1} es el ganador')

elif option_1 == 'Piedra' and option_2 == 'Tijera':
       print('Piedra Rompe Tijera')
       print(f'{user_1} es el Ganador')
elif option_1 == 'Piedra' and option_2 == 'Papel':
       print('Papel cubre a Piedra')
       print(f'{user_2} es el ganador')
elif option_1 == 'Papel' and option_2 == 'Tijera':
       print('Tijera rompe papel')
       print(f'{user_2} es el ganador')
else:
    print('Ninguno a elegido bien')