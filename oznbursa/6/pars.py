import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import random
import re   
import urllib.request
import requests
from bs4 import BeautifulSoup
import xlrd
from datetime import*

def get_sch():
    page = requests.get('https://www.mirea.ru/schedule/')
    soup = BeautifulSoup(page.text, 'html.parser')
    result = soup.find('div', {'class' : 'rasspisanie'}).\
        find(string = 'Институт информационных технологий').\
        find_parent('div').\
        find_parent('div').\
        findAll(target = '_blank')
    ref_list = []
    for i in result:
        ref_list.append(i.attrs['href'])
    return ref_list

def download_link_save(group, list_links):
    group = group[8] + group[9]
    dl = -1
    if group == '20':
        dl = 0
    elif group == '19':
        dl = 1
    elif group == '18':
        dl = 2
    f = open('file.xlsx', 'wb')
    ulink = requests.get(list_links[dl])
    f.write(ulink.content)
    f.close()

def download_link_temp(group, list_links):
    group = group[8] + group[9]
    dl = -1
    if group == '20':
        dl = 0
    elif group == '19':
        dl = 1
    elif group == '18':
        dl = 2
    f = open('file2.xlsx', 'wb')
    ulink = requests.get(list_links[dl])
    f.write(ulink.content)
    f.close()

def xl_oneday(sheet, week, day, group, typeout):
    timenow = datetime.now()
    weekdays_dict = {
        1 : 'Понедельник',
        2 : 'Вторник',
        3 : 'Среда',
        4 : 'Четверг',
        5 : 'Пятница',
        6 : 'Суббота',
    }
    daysweek_dict = {
        'понедельник' : 0,
        'вторник' : 1,
        'среда' : 2,
        'четверг' : 3,
        'пятница' : 4,
        'суббота' : 5,
    }
    months_dict = {
        1 : 'января',
        2 : 'февраля',
        3 : 'марта',
        4 : 'апреля',
        5 : 'мая',
        6 : 'июня',
        7 : 'июля',
        8 : 'августа',
        9 : 'сентября',
        10 : 'октября',
        11 : 'ноября',
        12 : 'декабря'
    }
    column = None
    for i in range(sheet.ncols - 1):
        if sheet.cell_value(1, i) == group:
            column = i
            break
    if column == None:
        return 'Увы, вашей группы не существует'
    list_subj = []
    if typeout == 'dayweek':
        wd = 3 + 12 * daysweek_dict[week]
        list_subj.append('Нечётная неделя:')
        for i in range(1, 7):
            if sheet.cell_type(wd, column) == 0:
                list_subj.append('{}) —'.format(i))
            else:
                list_subj.append('{}) {}, {}, {}, {}'.format(i, sheet.cell_value(wd, column), sheet.cell_value(wd, column + 1), sheet.cell_value(wd, column + 2), sheet.cell_value(wd, column + 3)))
            wd += 2
        wd = 4 + 12 * daysweek_dict[week]
        list_subj.append('Чётная неделя:')
        for i in range(1, 7):
            if sheet.cell_type(wd, column) == 0:
                list_subj.append('{}) —'.format(i))
            else:
                list_subj.append('{}) {}, {}, {}, {}'.format(i, sheet.cell_value(wd, column), sheet.cell_value(wd, column + 1), sheet.cell_value(wd, column + 2), sheet.cell_value(wd, column + 3)))
            wd += 2
        outcome = '\n'.join(list_subj)
    elif typeout == 'day':
        timenow += timedelta(days = day)
        list_subj.append('Расписание на {} {}'.format(timenow.day, months_dict[timenow.month]))
        wd = (datetime.now()).weekday()
        wd = wd * 12 + 3 + 12 * day
        if week == 0:
            wd += 1
        for i in range(1, 7):
            if sheet.cell_type(wd, column) == 0:
                list_subj.append('{}) —'.format(i))
            else:
                list_subj.append('{}) {}, {}, {}, {}'.format(i, sheet.cell_value(wd, column), sheet.cell_value(wd, column + 1), sheet.cell_value(wd, column + 2), sheet.cell_value(wd, column + 3)))
            wd += 2
        outcome = '\n'.join(list_subj)
    if typeout == 'week':
        ots = 0
        if week == 0:
            ots += 1
        if day == 1:
            timenow += timedelta(days = 7)
        timenow -= timedelta(days = datetime.now().weekday())
        for i in range(1, 7):
            days = (i - 1) * 12 + 3 + ots
            list_subj.append('Расписание на {}, {} {}:'.format(weekdays_dict[i], timenow.day, months_dict[timenow.month]))
            for j in range(1, 7):
                if sheet.cell_type(days + (j - 1) * 2, column) == 0:
                    list_subj.append('{}) —'.format(j))
                else:
                    list_subj.append('{}) {}, {}, {}, {}'.format(j, sheet.cell_value(days + (j - 1) * 2, column), sheet.cell_value(days + (j - 1) * 2, column + 1), sheet.cell_value(days + (j - 1) * 2, column + 2), sheet.cell_value(days + (j - 1) * 2, column + 3)))
            list_subj.append('\n')
            timenow += timedelta(days = 1)
        outcome = '\n'.join(list_subj)
    return outcome

if __name__ == '__main__':
    print(get_sch())