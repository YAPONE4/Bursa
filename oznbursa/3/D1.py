from Person import Person
from Student import Student
from Teacher import Teacher
from Logg import logg
from Class import Klass
import pickle

s1 = pickle.load(open('s1.pkl', 'rb'))
s2 = pickle.load(open('s2.pkl', 'rb'))
s3 = pickle.load(open('s3.pkl', 'rb'))
s4 = pickle.load(open('s4.pkl', 'rb'))
clt = pickle.load(open('clt.pkl', 'rb'))
myclass = pickle.load(open('myclass.pkl', 'rb'))
print(s1)
print(s2.print_marks())
s2.add_mark('Matan', '29/04', '3')
print(s2.print_marks())
print(s3.subj_marks('Biology'))
print(s4.print_marks())
print(clt)
clt.change_cabinet(777)
clt.add_subject(11, 'Matan')
clt.del_subject(10, 'Russian')
print(clt)