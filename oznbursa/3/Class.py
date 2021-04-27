from Person import Person
from Student import Student
from Teacher import Teacher

class Klass:
    def __init__(self, number, class_journal = {}, class_teacher = ''):
        self.number = number
        self.class_journal = class_journal
        self.class_teacher = class_teacher

    def print_info(self):
        info = ('Class info:\n\n')
        info += self.class_teacher.print_info() + '\n'
        info += ('Students info:\n\n')
        for i in self.class_journal:
            info += self.class_journal[i].print_info() + '\n'
            info += self.class_journal[i].print_marks() + '\n'
        return info

    def students_number(self):
        return len(list(self.class_journal))
    
    def get_student(self, i):
        if i == 0:
            return(self.class_teacher.print_info())
        else:
            return(list(self.class_journal.values())[i].print_info())

    def add_student(self, nstudent):
        self.class_journal.update({"{} {}".format(nstudent.last_name, nstudent.first_name) : nstudent})

    def kill_student(self, i):
        for j in self.class_journal:
            if j[0] == str(i):
                del self.class_journal[j]
                break

    def export_all_info(self):
        export = open('class_info.txt', 'w')
        export.write(self.print_info())


if __name__ == '__main__':
    num = 12
    s1 = Student('Prin', 'Alex', 19, 11)
    s1.marks = {'Biology' : {'12/03' : '5', '13/03' : '4'}, 'Math' : {'12/03' : '5', '13/03' : '4'} }
    s2 = Student('Sas', 'Ayas', 19, 11)
    s2.marks = {'Biology' : {'12/03' : '5', '13/03' : '4'}, 'Math' : {'12/03' : '3', '13/03' : '4'} }
    s3 = Student('Vinokurov', 'Anton', 19, 11)
    s3.marks = {'Biology' : {'12/03' : '5', '13/03' : '1'}, 'Math' : {'12/03' : '5', '13/03' : '4'} }
    s4 = Student('Shishov', 'Ilya', 19, 11)
    s4.marks = {'Biology' : {'12/03' : '3', '13/03' : '4'}, 'Math' : {'12/03' : '3', '13/03' : '4'} }
    clj = {'Prin Alex' : s1, 'Sas Ayas' : s2, 'Vinokurov Anton' : s3}
    clt = Teacher('Ivanova', 'Zinaida', 55, 12)
    clt.subjects = {10 : ['English', 'Russian', 'Socionics'], 11 : ['History', 'Math']}
    myclass = Klass(num, clj, clt)
    myclass.add_student(s4)
    myclass.kill_student(2)
    print('Students number:')
    print('{}\n'.format(myclass.students_number()))
    print('Getting student/teacher:')
    print(myclass.get_student(0))
    print(myclass.get_student(2))
    print(myclass.print_info())
    myclass.export_all_info()