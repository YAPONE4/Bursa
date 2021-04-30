from Person import Person
from Logg import logg

class Teacher(Person):
    def __init__(self, last_name, first_name, age, cabinet = ''):
        super().__init__(last_name, first_name, age)
        self.cabinet = cabinet
        self.subjects = {}
        logg('CRE', 'Created Teacher {} {}'.format(self.last_name, self.first_name))

    def change_cabinet(self, cabinet):
        self.cabinet = cabinet
        logg('INF', 'Changed cabinet of Teacher {} {}'.format(self.last_name, self.first_name))
    
    def add_subject(self, klas, subject):
        if klas not in self.subjects:
            newsubj = {klas : [subject]}
            self.subjects.update(newsubj)
        else:
            newsubj = {klas : subject}
            self.subjects[klas].append(newsubj[klas])
        logg('INF', 'Added subject to Teacher {} {}'.format(self.last_name, self.first_name))

    def del_subject(self, klas, subject):
        if subject not in self.subjects[klas]:
            print('Error, there is no such a subject')
            return 0
        if len(self.subjects[klas]) > 1:
            self.subjects[klas].remove(subject)
        else:
            del self.subjects[klas]
        logg('INF', 'Deleted subject of Teacher {} {}'.format(self.last_name, self.first_name))

    def __str__(self):
        info = ("Teacher info:\n{} {}, age: {}, cabinet number: {}\n".format(self.last_name, self.first_name, self.age, self.cabinet))
        info += ("Teachers' subjects:\n")
        c = 0
        for i in self.subjects:
            info += ("{} class: ".format(i))
            info += (', '.join(self.subjects[i]))
            c += 1
            info += '\n'
        logg('INF', 'Printed info about {} {}'.format(self.last_name, self.first_name))
        return info
            
if __name__ == '__main__':
    teach = Teacher("Ivanova", "Zinaida", 99, 12)
    teach.subjects = {10 : ["History", "Socionics"]}
    teach.add_subject(10, "Russian")
    teach.add_subject(11, "English")
    teach.del_subject(10, 'History')
    teach.change_cabinet(555)
    print(teach)