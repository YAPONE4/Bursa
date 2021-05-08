from tkinter import *
from tkinter.ttk import Combobox, Checkbutton, Radiobutton
from xmlwork import get_file
from xmlwork import xml_fill_comboblox_names
import datetime
from tkinter import ttk
import xml.dom.minidom

def convert_button(from_conv, to_conv, count):
    if from_conv == 'Российский рубль':
        from_conv_res = 1.0
    if to_conv == 'Российский рубль':
        to_conv_res = 1.0
    file = open('data.xml', 'rb')
    dom = xml.dom.minidom.parse(file)
    dom.normalize()
    nodeArray = dom.getElementsByTagName('Valute')
    for node in nodeArray:
        childs = node.childNodes
        if childs[3].childNodes[0].nodeValue == from_conv:
            value = childs[4].childNodes
            from_conv_res = float(value[0].nodeValue.replace(',', '.')) / float(childs[2].childNodes[0].nodeValue.replace(',', '.'))
        if childs[3].childNodes[0].nodeValue == to_conv:
            value = childs[4].childNodes
            to_conv_res = float(value[0].nodeValue.replace(',', '.')) / float(childs[2].childNodes[0].nodeValue.replace(',', '.'))
    result.config(text = str( (float(count) * (from_conv_res / to_conv_res))))

def show_period(per):
    todaytime = datetime.datetime.today()
    info = []
    if per == 'W':
        for i in range(0, 4):
            prevtime = todaytime - datetime.timedelta(days = 6)
            info.append('{} - {}'.format(prevtime.strftime("%d.%m.%Y"), todaytime.strftime("%d.%m.%Y")))
            todaytime = prevtime - datetime.timedelta(days = 1)
        period = Combobox(dynamics, values = info)
        period.grid(column = 2, row = 1, padx = 30, pady = 5)
    if per == 'M':
        mnths = [
            'Декабрь',
            "Январь",
            "Февраль",
            "Март",
            "Апрель",
            "Май",
            "Июнь",
            "Июль",
            "Август",
            "Сентябрь",
            "Октябрь",
            "Ноябрь",
        ]
        info = []
        for i in range(0, 4):
            info.append('{} {}'.format(mnths[(12 + (int(todaytime.strftime("%m"))) - i) % 12], int(todaytime.strftime("%Y"))))
        period = Combobox(dynamics, values = info)
        period.grid(column = 2, row = 2, padx = 30, pady = 5)

#Взятие данных для калькулятора по сегодняшнему курсу
todaytime = datetime.datetime.today().strftime("%d/%m/%Y")
get_file(todaytime)
file = open('data.xml', 'rb')
names_list = xml_fill_comboblox_names(file)

#Создание окна
window = Tk()
window.title('Конвертер валют')
window.geometry('600x200')
tab_control = ttk.Notebook(window)
calculate = ttk.Frame(tab_control)
dynamics = ttk.Frame(tab_control)
tab_control.add(calculate, text = 'Калькулятор валют')  
tab_control.add(dynamics, text = 'Динамика курса')
tab_control.pack(expand=1, fill='both')

#Калькулятор валют
convert = Button(calculate, text = 'Конвертировать', command = lambda: convert_button(str(input_value.get()), str(output_value.get()), count.get()))
convert.grid(column = 2, row = 0, padx = 10, pady = 30)
count = Entry(calculate)
count.focus()
count.grid(column = 1, row = 0, padx = 10, pady = 30)
input_value = Combobox(calculate, values = names_list)
input_value.grid(column = 0, row = 0, padx = 10, pady = 30)
output_value = Combobox(calculate, values = names_list)
output_value.grid(column = 0, row = 1, padx = 10, pady = 20)
result = Label(calculate, text = '0')
result.grid(column = 1, row = 1, padx = 10, pady = 20)

#Динамика курса
val = Label(dynamics, text = 'Валюта')
val.grid(column = 0, row = 0, padx = 30, pady = 5)
per = Label(dynamics, text = 'Период')
per.grid(column = 1, row = 0, padx = 30, pady = 5)
chp = Label(dynamics, text = 'Выбор периода')
chp.grid(column = 2, row = 0, padx = 30, pady = 5)
valute = Combobox(dynamics, values = names_list)
valute.grid(column = 0, row = 1, padx = 30, pady = 5)
graph_build = Button(dynamics, text = 'Построить график')
graph_build.grid(column = 0, row = 5, padx = 30, pady = 30)
radio_state = IntVar()
radio_state.set(None)
week = Radiobutton(dynamics, text = 'Неделя', value = 1, variable = radio_state, command = lambda: show_period('W'))
week.grid(column = 1, row = 1, padx = 30, pady = 5)
month = Radiobutton(dynamics, text = 'Месяц', value = 2, variable = radio_state, command = lambda: show_period('M'))
month.grid(column = 1, row = 2, padx = 30, pady = 5)
quart = Radiobutton(dynamics, text = 'Квартал', value = 3, variable = radio_state)
quart.grid(column = 1, row = 3, padx = 30, pady = 5)
year = Radiobutton(dynamics, text = 'Год', value = 4, variable = radio_state)
year.grid(column = 1, row = 4, padx = 30, pady = 5)

window.mainloop()