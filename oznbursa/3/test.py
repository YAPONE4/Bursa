keks = {'12/03' : 5, '13/03' : 4}
marks = {'Sex' : keks}
subj = 'Sex'
newmark = {'14/03' : 5, '15/03' : 5}
marks[subj].update(newmark)
print(marks)