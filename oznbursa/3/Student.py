from Person import Person

class Student(Person):
    def __init__(self, last_name, first_name, age, klas = ''):
        super().__init__(last_name, first_name, age)
        self.klas = klas
        self.marks = {}
    def add_mark(self, subject, date, mark):
        newmark = {date, mark}
        if subject not in self.marks:
            self.marks.update(subject)
        self.marks[subject].update(newmark)