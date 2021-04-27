from Person import Person

class Student(Person):
    def __init__(self, last_name, first_name, age, klas = ''):
        super().__init__(last_name, first_name, age)
        self.klas = klas
        self.marks = {}

    def add_mark(self, subject, date, mark):
        newmark = {date : mark}
        if subject not in self.marks:
            self.marks.update({subject : newmark})
        else:
            self.marks[subject].update(newmark)

    def subj_marks(self, subject):
        info = ("Marks in the subject {}: ".format(subject))
        list_marks = list(self.marks[subject].values())
        info += (' '.join(list_marks))
        return info

    def print_marks(self):
        list_marks = list(self.marks.items())
        info = ''
        info += "School Journal of {} {}:\n".format(self.last_name, self.first_name)
        for i in range(0, len(list_marks)):
            info += ("{}: ".format(list_marks[i][0]))
            for j in list(list_marks[i][1].items()):
                info += ("{} - {}, ".format(j[0], j[1]))
            info += '\n'
        return info

    def print_info(self):
        return ("{} {}, age: {}, class: {}".format(self.last_name, self.first_name, self.age, self.klas))

if __name__ == '__main__':
    itsme = Student('Prin', 'Alexey', 18, 11)
    itsme.marks = {'History' : {'12/03' : '5'}, 'Biology' : {'12/03' : '5', '13/03' : '4'}, 'Math' : {'12/03' : '5', '13/03' : '4'}}
    itsme.add_mark('History', '13/03', '5')
    itsme.subj_marks('History')
    print(itsme.print_info())
    print(itsme.print_marks())