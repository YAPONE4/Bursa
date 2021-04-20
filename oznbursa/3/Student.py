from Person import Person

class Student(Person):
    def __init__(self, last_name, first_name, age, klas = ''):
        super().__init__(last_name, first_name, age)
        self.klas = klas
        self.marks = {}

    def add_mark(self, subject, date, mark):
        newmark = {date, mark}
        if subject not in self.marks:
            self.marks.update({subject : newmark})
        else:
            self.marks[subject].update(newmark)

    def subj_marks(self, subject):
        print("Marks in the subject {}:".format(subject))
        list_marks = list(self.marks[subject].values())
        printlist = ' '.join(list_marks)
        print(printlist)

    def printmarks(self):
        list_marks = list(self.marks.items())
        print("School Journal of {} {}:\n".format(self.last_name, self.first_name))
        for i in range(0, len(list_marks)):
            print("{}:".format(list_marks[i][0]))
            for j in list(list_marks[i][1].items()):
                print("{} : {}".format(j[0], j[1]))

    def print_info(self):
        print("{} {}, age: {}, class: {}".format(self.last_name, self.first_name, self.age, self.klas))