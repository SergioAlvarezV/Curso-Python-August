numbers = {1:'uno',2:'dos',3:'Tres'}
print(numbers[2])

name = input('cual es tu nombre => ')
last_name = input('Cual es tu apellido => ')
height = input('Cual es tu altura => ')
age = int(input('Cual es tu edad => '))


personal_information = {'Nombre':name,
                        'Apellido':last_name,
                        'Altura':height,
                        'Edad':age}
print(personal_information)
print(personal_information['Edad'] + 1)
keyss = personal_information.keys()
print(keyss)
values = personal_information.values()
print(values)
pairs = personal_information.items()
print(pairs)

contacts = {'Sergio':{'Nombre':name,'Apellido':last_name,'Altura':height,'Edad':age,
            }}