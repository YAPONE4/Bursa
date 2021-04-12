class Person:
    def __init__(self, last_name, first_name, age):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age



if __name__ == '__main__':
    print('Тестирование модуля Person')

    last_name = input('Type last name: ')
    first_name = input('Type first name: ')
    age = int(input('Type age: '))

    person = Person(last_name, first_name, age)
    print('Info: {} {}, {}'.format(person.last_name, person.first_name, person.age))