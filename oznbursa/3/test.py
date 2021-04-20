keks = {'12/03' : 5, '13/03' : 4}
marks = {'Sex' : keks}
subj = 'Sex'
newmark = {'14/03' : 5, '15/03' : 5}
marks[subj].update(newmark)
oof = list(marks[subj].items())
print(oof)


    #if __name__ == '__main__':
     #   keks = {'12/03' : 5, '13/03' : 4}
      #  marks = {'Math' : keks}
       # subj = 'Math'
        #newmark = {'14/03' : 5, '15/03' : 5}
        #marks[subj].update(newmark)
        #testst = Student('Prin', 'Alex', 19, 1)
        #testst.marks = marks
        #testst.subj_marks()"""