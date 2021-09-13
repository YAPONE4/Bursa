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
import os

random.seed()

datenow = datetime.now()
datest = datetime(2021, 2, 8)
weeknow = ((datenow - datest).days) // 7
week =((((datenow - datest).days) // 7) % 2)

list_links = get_sch()

def main():
    
    vk_session = vk_api.VkApi(token = '')
    vk = vk_session.get_api()

    longpoll = VkLongPoll(vk_session)

    gr_to_use = {}

    usersdict = {}

    userprekol = {}

    filelist = os.listdir('картино4ки')
    for fichier in filelist:
        if (not(fichier.endswith(".png")) and not(fichier.endswith(".jpg")) and not(fichier.endswith(".gif"))):
            filelist.remove(fichier)

    keyboard_objective = VkKeyboard(one_time=True, inline=False)
    keyboard_objective.add_button('Я приколист', color=VkKeyboardColor.POSITIVE)
    keyboard_objective.add_button('Я практическая работа', color=VkKeyboardColor.NEGATIVE)
    keyboard_sch = VkKeyboard(one_time=True, inline=False)
    keyboard_sch.add_button('На сегодня', color=VkKeyboardColor.POSITIVE)
    keyboard_sch.add_button('На завтра', color=VkKeyboardColor.NEGATIVE)
    keyboard_sch.add_line()
    keyboard_sch.add_button('На эту неделю', color=VkKeyboardColor.PRIMARY)
    keyboard_sch.add_button('На следующую неделю', color=VkKeyboardColor.PRIMARY)
    keyboard_sch.add_line()
    keyboard_sch.add_button('Какая сейчас неделя?', color=VkKeyboardColor.SECONDARY)
    keyboard_sch.add_button('Расписание какой группы ты показываешь?', color=VkKeyboardColor.SECONDARY)
    keyboard_prek = VkKeyboard(one_time=True, inline=False)
    keyboard_prek.add_button('Хачу угадайку', color=VkKeyboardColor.POSITIVE)
    keyboard_ugad = VkKeyboard(one_time=True, inline=False)
    keyboard_ugad.add_button('Число 0', color=VkKeyboardColor.PRIMARY)
    keyboard_ugad.add_button('Число 1', color=VkKeyboardColor.PRIMARY)
    keyboard_ugad.add_button('Число 2', color=VkKeyboardColor.PRIMARY)
    keyboard_ugad.add_line()
    keyboard_ugad.add_button('Число 3', color=VkKeyboardColor.PRIMARY)
    keyboard_ugad.add_button('Число 4', color=VkKeyboardColor.PRIMARY)
    keyboard_ugad.add_button('Число 5', color=VkKeyboardColor.PRIMARY)
    keyboard_ugad.add_line()
    keyboard_ugad.add_button('Число 6', color=VkKeyboardColor.PRIMARY)
    keyboard_ugad.add_button('Число 7', color=VkKeyboardColor.PRIMARY)
    keyboard_ugad.add_button('Число 8', color=VkKeyboardColor.PRIMARY)
    keyboard_ugad.add_line()
    keyboard_ugad.add_button('Число 9', color=VkKeyboardColor.PRIMARY)

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
            elif event.text.lower().startswith('число'):
                if userprekol[event.user_id] == 0:
                    vk.messages.send(
                        user_id = event.user_id,
                        random_id = get_random_id(),
                        message = 'Ты даже не играешь в угадайку!'.format(event.text)
                    )
                else:
                    if userprekol[event.user_id][1] == event.text[6]:
                        pict = vk.photos.getMessagesUploadServer()
                        pictpost = requests.post(pict['upload_url'], files = {'photo': open('картино4ки/' + filelist[random.randint(0, len(filelist))], 'rb')}).json()
                        pictsave = vk.photos.saveMessagesPhoto(photo = pictpost['photo'], server = pictpost['server'], hash = pictpost['hash'])[0]
                        pictreveal = 'photo{}_{}'.format(pictsave['owner_id'], pictsave['id'])
                        vk.messages.send(
                            user_id = event.user_id,
                            random_id = get_random_id(),
                            keyboard = keyboard_prek.get_keyboard(),
                            attachment = pictreveal,
                            message = 'Молодец. С меня картиночка из моей мусорной коллекции.'.format(event.text)
                            )
                        userprekol[event.user_id] = 0
                    else:
                        if userprekol[event.user_id][0] == 2:
                            vk.messages.send(
                            user_id = event.user_id,
                            random_id = get_random_id(),
                            keyboard = keyboard_prek.get_keyboard(),
                            message = 'Ты проиграл.'.format(event.text)
                            )
                            userprekol[event.user_id] = 0
                        else:
                            vk.messages.send(
                                user_id = event.user_id,
                                random_id = get_random_id(),
                                keyboard = keyboard_ugad.get_keyboard(),
                                message = 'Неправильно, попытайся ещё раз.'.format(event.text)
                                )
                            userprekol[event.user_id][0] += 1
            elif event.text.lower() == 'я приколист':
                vk.messages.send(
                    user_id = event.user_id,
                    random_id = get_random_id(),
                    keyboard = keyboard_prek.get_keyboard(),
                    message = 'Хо-хо, ха-ха!'
                    )
            elif event.text.lower() == 'хачу угадайку':
                if event.user_id not in userprekol:
                    userprekol.update({event.user_id : 0})
                if userprekol[event.user_id] != 0:
                    vk.messages.send(
                    user_id = event.user_id,
                    random_id = get_random_id(),
                    message = 'Ты и так уже играешь.'
                    )
                else:
                    vk.messages.send(
                    user_id = event.user_id,
                    random_id = get_random_id(),
                    keyboard = keyboard_ugad.get_keyboard(),
                    message = 'Хорошо, я загадал цифру от 0 до 9. У тебя 3 попытки, чтобы его отгадать.'
                    )
                    userprekol[event.user_id] = [0, str(random.randint(0, 9))]

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
                    keyboard = keyboard_objective.get_keyboard(),
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
            elif event.text.lower() == 'я практическая работа':
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