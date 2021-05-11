from tkinter import *
from tkinter.ttk import Combobox, Checkbutton, Radiobutton
from xmlwork import get_file
from xmlwork import get_file_2
from xmlwork import xml_fill_comboblox_names
import datetime
from tkinter import ttk
import xml.dom.minidom
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def dyn_button(state):
    if state == 4:
        date = yearcombo.get()
    if state == 3:
        date = quartcombo.get()
    if state == 2:
        date = monthcombo.get()
    if state == 1:
        date = weekcombo.get()        
    draw_plot(valute.get(), date)

def get_value(name, date):
    get_file_2(date)
    file2 = open('data2.xml', 'rb')
    dom = xml.dom.minidom.parse(file2)
    file2.close()
    dom.normalize()
    nodeArray = dom.getElementsByTagName('Valute')
    for node in nodeArray:
        childs = node.childNodes
        if childs[3].childNodes[0].nodeValue == name:
            value = childs[4].childNodes
            from_conv_res = float(value[0].nodeValue.replace(',', '.')) / float(childs[2].childNodes[0].nodeValue.replace(',', '.'))
            return from_conv_res

def draw_plot(name, period):
    if radio_state.get() == 4:
        date = ''
        for i in period:
            if i.isdigit():
                date += i
        date = int(date)
        date = datetime.date(date, 1, 1)
        names = [
            "Янв",
            '1/2',
            "Фев",
            '2/3',
            "Мар",
            '3/4',
            "Апр",
            '4/5',
            "Май",
            '5/6',
            "Июн",
            '6/7',
            "Июл",
            '7/8',
            "Авг",
            '8/9',
            "Сент",
            '9/10',
            "Окт",
            '10/11',
            "Ноя",
            '11/12',
            'Дек'
        ]
        values = []
        day = 16
        for i in range(2, 25):
            day += 15
            i = i // 2
            if i < 10:
                i = '0' + str(i)
            daystr = day % 30
            if daystr == 1:
                daystr = '0' + str(daystr)
            newdate = date.strftime('{}/{}/%Y'.format(daystr, i))
            values.append(get_value(name, newdate))
    elif radio_state.get() == 3:
        names = []
        values = []
        fdate = ''
        for i in period:
            if i.isdigit():
                fdate += i
        quart = int(fdate[0])
        fdate = fdate[1:]
        fdate = int(''.join(fdate))
        for i in range((quart - 1) * 3, quart * 3 + 1):
            days = -6
            if i < 10:
                i = '0' + str(i)
            for j in range(0, 4):
                days += 7
                newdays = days
                if newdays < 10:
                    newdays = '0' + str(newdays)
                newdate = '{}/{}/{}'.format(newdays, i, fdate)
                names.append('{}/{}/{}'.format(newdays, i, fdate % 1000))
                values.append(get_value(name, newdate))
    elif radio_state.get() == 2:
        ndict = {
            'Январь' : 1,
            'Февраль' : 2,
            'Март' : 3,
            'Апрель' : 4,
            'Май' : 5,
            'Июнь' : 6,
            'Июль' : 7,
            'Август' : 8,
            'Сентябрь' : 9,
            'Октрябрь' : 10,
            'Ноябрь' : 11,
            'Декабрь' : 12
        }
        month = ''
        year = ''
        names = []
        values = []
        for i in period:
            if i.isalpha():
                month += i
            elif i.isdigit():
                year += i
        month = ndict[month]
        if month < 10:
            month = '0' + str(month)
        for i in range(1, 32):
            if i < 10:
                i = '0' + str(i)
            newdate = '{}/{}/{}'.format(i, month, year)
            names.append(i)
            values.append(get_value(name, newdate))
    elif radio_state.get() == 1:
        names = []
        values = []
        days = period[0] + period[1]
        months = period[3] + period[4]
        years = period[6] + period[7] + period[8] + period[9]
        date = datetime.date(int(years), int(months), int(days))
        for i in range(0, 8):
            newdate = date.strftime('%d/%m/%Y')
            names.append(newdate)
            values.append(get_value(name, newdate))
            date += datetime.timedelta(days = 1)
    fig = plt.figure(figsize = (14, 5))
    fig.canvas.draw()
    window.geometry('1700x800')
    matplotlib.use('TkAgg')
    canvas = FigureCanvasTkAgg(fig, master = dynamics)
    fig.clear()
    plot_widget = canvas.get_tk_widget()
    plt.plot(names, values)
    plt.grid()
    plot_widget.grid(column = 0, row = 6, padx = 0, pady = 15)
        
def convert_button(from_conv, to_conv, count):
    if from_conv == 'Российский рубль':
        from_conv_res = 1.0
    if to_conv == 'Российский рубль':
        to_conv_res = 1.0
    file = open('data.xml', 'rb')
    dom = xml.dom.minidom.parse(file)
    file.close()
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
    result.config(text = str("%.4f" % (float(count) * (from_conv_res / to_conv_res))))

def show_period(per):
    weekcombo.grid_remove()
    monthcombo.grid_remove()
    quartcombo.grid_remove()
    yearcombo.grid_remove()
    todaytime = datetime.datetime.today()
    kostyl = datetime.datetime.today()
    info = []
    if per == 'W':
        for i in range(0, 4):
            prevtime = todaytime - datetime.timedelta(days = 6)
            info.append('{} - {}'.format(prevtime.strftime("%d.%m.%Y"), todaytime.strftime("%d.%m.%Y")))
            todaytime = prevtime - datetime.timedelta(days = 1)
        weekcombo['values'] = info
        weekcombo.grid(column = 2, row = 1, padx = 30, pady = 5)
    elif per == 'M':
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
        for i in range(0, 4):
            if int(todaytime.strftime("%m")) - i <= 0:
                kostyl -= datetime.timedelta(days = 366)
            info.append('{} {}'.format(mnths[(12 + (int(todaytime.strftime("%m"))) - i) % 12], int(kostyl.strftime("%Y"))))
        monthcombo['values'] = info
        monthcombo.grid(column = 2, row = 2, padx = 30, pady = 5)
    elif per == 'Q':
        for i in range(0, 4):
            info.append('{} квартал {} года'.format(int(todaytime.strftime('%m')) // 3 + 1, todaytime.strftime('%Y')))
            todaytime -= datetime.timedelta(days = 93)
        quartcombo['values'] = info
        quartcombo.grid(column = 2, row = 3, padx = 30, pady = 5)
    elif per == 'Y':
        for i in range(0, 4):
            info.append('{} год'.format(todaytime.strftime('%Y')))
            todaytime -= datetime.timedelta(days = 366)
        yearcombo['values'] = info
        yearcombo.grid(column = 2, row = 4, padx = 30, pady = 5)

#Взятие данных для калькулятора по сегодняшнему курсу
todaytime = datetime.datetime.today().strftime("%d/%m/%Y")
get_file(todaytime)
file = open('data.xml', 'rb')
names_list = xml_fill_comboblox_names(file)
file.close()

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
del names_list[0]
valute = Combobox(dynamics, values = names_list)
valute.grid(column = 0, row = 1, padx = 30, pady = 5)
graph_build = Button(dynamics, text = 'Построить график', command = lambda: dyn_button(radio_state.get()))
graph_build.grid(column = 0, row = 3, padx = 30, pady = 5)
radio_state = IntVar()
radio_state.set(None)
week = Radiobutton(dynamics, text = 'Неделя', value = 1, variable = radio_state, command = lambda: show_period('W'))
week.grid(column = 1, row = 1, padx = 30, pady = 5)
weekcombo = Combobox(dynamics, values = '')
month = Radiobutton(dynamics, text = 'Месяц', value = 2, variable = radio_state, command = lambda: show_period('M'))
month.grid(column = 1, row = 2, padx = 30, pady = 5)
monthcombo = Combobox(dynamics, values = '')
quart = Radiobutton(dynamics, text = 'Квартал', value = 3, variable = radio_state, command = lambda: show_period('Q'))
quart.grid(column = 1, row = 3, padx = 30, pady = 5)
quartcombo = Combobox(dynamics, values = '')
year = Radiobutton(dynamics, text = 'Год', value = 4, variable = radio_state, command = lambda: show_period('Y'))
year.grid(column = 1, row = 4, padx = 30, pady = 5)
yearcombo = Combobox(dynamics, text = '')

window.mainloop()