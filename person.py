class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introducePerson(self):
        print('Seu nome é ' + self.name)
        print('Sua idade é ' + str(self.age))

Person(input('Seu nome: '), int(input('Sua idade: '))).introducePerson()
