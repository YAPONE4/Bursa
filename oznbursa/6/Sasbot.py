import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import random
import re   
import urllib.request
import requests
from bs4 import BeautifulSoup
from pars import*
import xlrd
from datetime import*
from weather import*

random.seed()

datenow = datetime.now()
datest = datetime(2021, 2, 8)
weeknow = ((datenow - datest).days) // 7
week =((((datenow - datest).days) // 7) % 2)

list_links = get_sch()

def main():
    
    vk_session = vk_api.VkApi(token = 'f3f9fa0d9782c58d31c5bdcaac34aeed51e747d8ecec72ec6ee4fc899f547bff9e90a4332e85de73e02f7')
    vk = vk_session.get_api()

    longpoll = VkLongPoll(vk_session)

    gr_to_use = {}

    usersdict = {}

    keyboard_sch = VkKeyboard(one_time=True, inline=False)
    keyboard_sch.add_button('На сегодня', color=VkKeyboardColor.POSITIVE)
    keyboard_sch.add_button('На завтра', color=VkKeyboardColor.NEGATIVE)
    keyboard_sch.add_line()
    keyboard_sch.add_button('На эту неделю', color=VkKeyboardColor.PRIMARY)
    keyboard_sch.add_button('На следующую неделю', color=VkKeyboardColor.PRIMARY)
    keyboard_sch.add_line()
    keyboard_sch.add_button('Какая сейчас неделя?', color=VkKeyboardColor.SECONDARY)
    keyboard_sch.add_button('Расписание какой группы ты показываешь?', color=VkKeyboardColor.SECONDARY)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.text and event.to_me:
            if event.user_id not in usersdict:
                usersdict.update({event.user_id : 0})
            if event.user_id not in gr_to_use:
                gr_to_use.update({event.user_id : 0})
            print(event.text)
            if re.fullmatch(r'\w\w\w\w-\d\d-(1[8-9]|20)', event.text) != None:
                usersdict.update({event.user_id : event.text})
                vk.messages.send(
                        user_id = event.user_id,
                        random_id = get_random_id(),
                        message = 'Отлично! Я запомнил, что ты из группы {}!'.format(event.text)
                    )
                download_link_save(usersdict[event.user_id], list_links)
                book = xlrd.open_workbook("file.xlsx")
                sheet = book.sheet_by_index(0)
            elif event.text.lower() == 'расписание':
                gr_to_use.update({event.user_id : usersdict[event.user_id]})
                book = xlrd.open_workbook("file.xlsx")
                sheet = book.sheet_by_index(0)
                vk.messages.send(
                    user_id = event.user_id,
                    random_id = get_random_id(),
                    keyboard = keyboard_sch.get_keyboard(),
                    message = 'На какую дату?'
                    )
            elif event.text.lower() == 'привет':
                vk.messages.send(
                    user_id = event.user_id,
                    random_id = get_random_id(),
                    message = 'Привет, ' + vk.users.get(user_id = event.user_id)[0]['first_name']
                    )
            elif event.text.lower() == 'на сегодня':
                if gr_to_use[event.user_id] == 0:
                    vk.messages.send(
                        user_id = event.user_id,
                        random_id = get_random_id(),
                        message = 'Вы не записали группу!'
                        )
                else:
                    vk.messages.send(
                        user_id = event.user_id,
                        random_id = get_random_id(),
                        message = 'Ваше расписание на сегодня:\n' + xl_oneday(sheet, week, 0, gr_to_use[event.user_id], 'day')
                        )
            elif event.text.lower() == 'на завтра':
                if gr_to_use[event.user_id] == 0:
                    vk.messages.send(
                        user_id = event.user_id,
                        random_id = get_random_id(),
                        message = 'Вы не записали группу!'
                        )
                else:
                    vk.messages.send(
                        user_id = event.user_id,
                        random_id = get_random_id(),
                        message = 'Ваше расписание на завтра:\n' + xl_oneday(sheet, week, 1, gr_to_use[event.user_id], 'day')
                        )
            elif event.text.lower() == 'на эту неделю':
                if gr_to_use[event.user_id] == 0:
                    vk.messages.send(
                        user_id = event.user_id,
                        random_id = get_random_id(),
                        message = 'Вы не записали группу!'
                        )
                else:
                    vk.messages.send(
                        user_id = event.user_id,
                        random_id = get_random_id(),
                        message = 'Ваше расписание на эту неделю:\n' + xl_oneday(sheet, week , 0, gr_to_use[event.user_id], 'week')
                        )
            elif event.text.lower() == 'на следующую неделю':
                if gr_to_use[event.user_id] == 0:
                    vk.messages.send(
                        user_id = event.user_id,
                        random_id = get_random_id(),
                        message = 'Вы не записали группу!'
                        )
                else:
                    vk.messages.send(
                        user_id = event.user_id,
                        random_id = get_random_id(),
                        message = 'Ваше расписание на следующую неделю:\n' + xl_oneday(sheet, (week + 1) % 2, 1, gr_to_use[event.user_id], 'week')
                        )
            elif event.text.lower() == 'какая сейчас неделя?':
                vk.messages.send(
                        user_id = event.user_id,
                        random_id = get_random_id(),
                        message = 'Сейчас идёт {} неделя'.format(weeknow)
                        )
            elif event.text.lower() == 'расписание какой группы ты показываешь?':
                if gr_to_use[event.user_id] == 0:
                    vk.messages.send(
                        user_id = event.user_id,
                        random_id = get_random_id(),
                        message = 'Пока что никакой'
                        )
                else:
                    vk.messages.send(
                            user_id = event.user_id,
                            random_id = get_random_id(),
                            message = 'Группы {}'.format(gr_to_use[event.user_id])
                            )
            elif event.text.lower() == 'начать общение':
                comm = 'Привет! Сейчас я вкратце расскажу как мной пользоваться!\n\nДля того, чтобы записать свою группу, ты должен написать <(группа)>. Дальше, написав <Расписание>, в окошке будет выведены все возможные команды.\nЧтобы узнать погоду, напиши <Погода>.'
                comm += '\nТакже ты можешь посмотреть расписание чужих групп, не записывая их как свою! Для этого пишешь либо <Расписание (группа)>, либо <Расписание (день недели) (группа)>'
                vk.messages.send(
                        user_id = event.user_id,
                        random_id = get_random_id(),
                        message = comm
                    )
            elif re.fullmatch(r'расписание (понедельник|вторник|среда|четверг|пятница|суббота)', event.text.lower()) != None:
                gr_to_use.update({event.user_id : usersdict[event.user_id]})
                book = xlrd.open_workbook("file.xlsx")
                sheet = book.sheet_by_index(0)
                stri = event.text
                stri = stri.split(' ')
                vk.messages.send(
                        user_id = event.user_id,
                        random_id = get_random_id(),
                        message = xl_oneday(sheet, stri[len(stri) - 1], 1, gr_to_use[event.user_id], 'dayweek')
                    )
            elif event.text.lower() == 'погода':
                vk.messages.send(
                        user_id = event.user_id,
                        random_id = get_random_id(),
                        message = get_weather()
                    )
            elif re.fullmatch(r'расписание \w\w\w\w-\d\d-(1[8-9]|20)', event.text.lower()) != None:
                stri = event.text
                stri = stri.split(' ')
                gr_to_use.update({event.user_id : stri[len(stri) - 1]})
                download_link_temp(gr_to_use[event.user_id], list_links)
                book = xlrd.open_workbook("file2.xlsx")
                sheet = book.sheet_by_index(0)
                vk.messages.send(
                    user_id = event.user_id,
                    random_id = get_random_id(),
                    keyboard = keyboard_sch.get_keyboard(),
                    message = 'На какую дату?'
                    )
            elif re.fullmatch(r'расписание (понедельник|вторник|среда|четверг|пятница|суббота) \w\w\w\w-\d\d-(1[8-9]|20)', event.text.lower()) != None:
                stri = event.text
                stri = stri.split(' ')
                gr_to_use.update({event.user_id : stri[len(stri) - 1]})
                download_link_temp(gr_to_use[event.user_id], list_links)
                book = xlrd.open_workbook("file2.xlsx")
                sheet = book.sheet_by_index(0)
                vk.messages.send(
                        user_id = event.user_id,
                        random_id = get_random_id(),
                        message = xl_oneday(sheet, stri[len(stri) - 2], 1, gr_to_use[event.user_id], 'dayweek')
                    )
            else:
                vk.messages.send(
                        user_id = event.user_id,
                        random_id = get_random_id(),
                        message = 'Что ты сказал? Повтори, я не расслышал...'
                        )
            


if __name__ == '__main__':
    main()