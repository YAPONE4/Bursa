from Person import Person
from Student import Student
from Teacher import Teacher

class Klass:
    def __init__(self, number, class_journal = {}, class_teacher = ''):
        self.number = number
        self.class_journal = class_journal
        self.class_teacher = class_teacher

    def print_info(self):
        print('Class info:\n')
        self.class_teacher.print_info()
        print('Students info:')
        for i in self.class_journal:
            self.class_journal[i].print_info()

if __name__ == '__main__':
    num = 12
    s1 = Student('Prin', 'Alex', 19, 11)
    s2 = Student('Sas', 'Ayas', 19, 11)
    s3 = Student('Vinokurov', 'Anton', 19, 11)
    clj = {'Print Alex' : s1, 'Sas Ayas' : s2, 'Vinokurov Anton' : s3}
    clt = Teacher('Ivanova', 'Zinaida', 55, 12)
    clt.subjects = {10 : ['English', 'Russian', 'Socionics'], 11 : ['History', 'Math']}
    myclass = Klass(num, clj, clt)
    myclass.print_info()