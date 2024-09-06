class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hola, mi nombre es {self.name} y tengo {self.age} Años")

person1 = Person("Juan", '22')
person2 = Person('Melisa', '26')

person1.greet()
person2.greet()