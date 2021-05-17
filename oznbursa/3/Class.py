from Person import Person
from Student import Student
from Teacher import Teacher
from Logg import logg
import pickle

class Klass:
    def __init__(self, number, class_journal = [], class_teacher = ''):
        self.number = number
        self.class_journal = class_journal
        self.class_teacher = class_teacher
        logg('CRE', 'Created Class {}'.format(number))

    def __str__(self):
        info = ('Class info:\n\n')
        info += str((self.class_teacher)) + '\n'
        info += ('Students info:\n\n')
        for i in self.class_journal:
            info += str(i) + '\n'
            info += i.print_marks() + '\n'
        return info

    def __len__(self):
        logg('INF', 'Getted info about class size')
        return len(self.class_journal)
    
    def get_student(self, i):
        if i > len(self):
            print('Error, cannot get the student')
            return 0
        logg('INF', 'Getted info about {} {}'.format(self.class_journal[i].last_name, self.class_journal[i].first_name))
        if i == 0:
            return str(self.class_teacher)
        else:
            return str(self.class_journal[i - 1])

    def __add__(self, nstudent):
        self.class_journal.append(nstudent)
        logg('INF', 'Added student to class {}'.format(self.number))

    def __sub__(self, nstudent):
        for j in range(0, len(self)):
            if self.class_journal[j] == nstudent:
                del self.class_journal[j]
                logg('INF', 'Killed student from class {}'.format(self.number))
                break

    def export_all_info(self):
        logg('INF', 'Exporting info about class {} started'.format(self.number))
        export = open('class_info.txt', 'w')
        export.write(str(self))

    def __getitem__(self, k):
        if k != 0:
            return self.class_journal[k]
        else:
            return self.class_teacher

    def __setitem__(self, obj, k):
        if k != 0:
            self.class_journal[k] = obj
        else:
             self.class_teacher = obj

    def __delitem__(self, k):
        if k != 0:
            del self.class_journal[k]
        else:
            del self.class_teacher

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
    clj = [s1, s2, s3]
    clt = Teacher('Ivanova', 'Zinaida', 55, 12)
    clt.subjects = {10 : ['English', 'Russian', 'Socionics'], 11 : ['History', 'Math']}
    myclass = Klass(num, clj, clt)
    myclass + s4
    myclass - s3
    print('Students number:')
    print(len(myclass))
    print('Getting student/teacher:')
    print(myclass.get_student(0))
    print(myclass.get_student(2))
    del myclass[1]
    print(myclass)
    print(myclass[0])
    print(myclass[1])
    myclass.export_all_info()
    pickle.dump(s1, open('s1.pkl', 'wb'))
    pickle.dump(s2, open('s2.pkl', 'wb'))
    pickle.dump(s3, open('s3.pkl', 'wb'))
    pickle.dump(s4, open('s4.pkl', 'wb'))
    pickle.dump(clt, open('clt.pkl', 'wb'))
    pickle.dump(myclass, open('myclass.pkl', 'wb'))