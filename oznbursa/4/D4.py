import os
import subprocess
import sys
import shutil
import time

def folder_create():
    os.mkdir('Ознакомительная практика')
    os.mkdir('Ознакомительная практика/тема A')
    os.mkdir('Ознакомительная практика/тема B')

def copy_files():
    listfiles = os.listdir('ALL')
    for pyfile in listfiles:
        if pyfile.startswith('task_A'):
            pyfile = 'ALL/' + pyfile
            shutil.copy(pyfile, 'Ознакомительная практика/тема A', follow_symlinks = True)
        elif pyfile.startswith('task_B'):
            pyfile = 'ALL/' + pyfile
            shutil.copy(pyfile, 'Ознакомительная практика/тема B', follow_symlinks = True)

def all_file_func_read_and_exec():
    listfilesA = os.listdir('Ознакомительная практика/тема A/')
    listfilesB = os.listdir('Ознакомительная практика/тема B/')
    print('Функции темы А:\n')
    for pyfile in listfilesA:
        pyfile = 'Ознакомительная практика/тема A/' + pyfile
        with open(pyfile, 'r', encoding=' utf-8') as file:
            print('Function name: ')
            for line in file:
                if line.startswith('def'):
                    print(line)
                    break
            clockstart = time.time() 
            output = subprocess.run([sys.executable, pyfile])
            clockstop = time.time() 
            print("Elapsed time: ", clockstop - clockstart)
            print('\n\n')
    for pyfile in listfilesB:
        pyfile = 'Ознакомительная практика/тема B/' + pyfile
        with open(pyfile, 'r', encoding=' utf-8') as file:
            print('Function name: ')
            for line in file:
                if line.startswith('def'):
                    print(line)
                    break
            clockstart = time.time() 
            output = subprocess.run([sys.executable, pyfile])
            clockstop = time.time() 
            print("Elapsed time: ", clockstop - clockstart)
            print('\n\n')


def all_file_prog_exec():
    listfilesA = os.listdir('Ознакомительная практика/тема A/')
    listfilesB = os.listdir('Ознакомительная практика/тема B/')
    print('Запускаем программы темы A:\n')
    for pyfile in listfilesA:
        pyfile = 'Ознакомительная практика/тема A/' + pyfile
        output = subprocess.run([sys.executable, pyfile])
    print('Запускаем программы темы B:\n')
    for pyfile in listfilesA:
        pyfile = 'Ознакомительная практика/тема B/' + pyfile
        output = subprocess.run([sys.executable, pyfile])

folder_create()
copy_files()
all_file_func_read_and_exec()