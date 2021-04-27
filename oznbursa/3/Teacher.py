from Person import Person

class Teacher(Person):
    def __init__(self, last_name, first_name, age, cabinet = ''):
        super().__init__(last_name, first_name, age)
        self.cabinet = cabinet
        self.subjects = {}

    def change_cabinet(self, cabinet):
        self.cabinet = cabinet
    
    def add_subject(self, klas, subject):
        if klas not in self.subjects:
            newsubj = {klas : [subject]}
            self.subjects.update(newsubj)
        else:
            newsubj = {klas : subject}
            self.subjects[klas].append(newsubj[klas])

    def del_subject(self, klas, subject):
        if len(self.subjects[klas]) > 1:
            self.subjects[klas].remove(subject)
        else:
            del self.subjects[klas]

    def print_info(self):
        info = ("Teacher info:\n{} {}, age: {}, cabinet number: {}\n".format(self.last_name, self.first_name, self.age, self.cabinet))
        info += ("Teachers' subjects:\n")
        c = 0
        for i in self.subjects:
            info += ("{} class: ".format(i))
            info += (', '.join(self.subjects[i]))
            c += 1
            info += '\n'
        return info
            
        

if __name__ == '__main__':
    teach = Teacher("Ivanova", "Zinaida", 99, 12)
    teach.subjects = {10 : ["History", "Socionics"]}
    teach.add_subject(10, "Russian")
    teach.add_subject(11, "English")
    teach.del_subject(10, 'History')
    teach.change_cabinet(555)
    print(teach.print_info())