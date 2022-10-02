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

english = ['thunderstorm with light rain', 'thunderstorm with rain', 'thunderstorm with heavy rain', 'light thunderstorm', 'thunderstorm', 'heavy thunderstorm', 'ragged thunderstorm', 'thunderstorm with light drizzle', 'thunderstorm with drizzle', 'thunderstorm with heavy drizzle', 'light intensity drizzle', 'drizzle', 'heavy intensity drizzle', 'light intensity drizzle rain', 'drizzle rain', 'heavy intensity drizzle rain', 'shower rain and drizzle', 'heavy shower rain and drizzle', 'shower drizzle', 'light rain', 'moderate rain', 'heavy intensity rain', 'very heavy rain', 'extreme rain', 'freezing rain', 'light intensity shower rain', 'shower rain', 'heavy intensity shower rain', 'ragged shower rain', 'light snow', 'Snow', 'Heavy snow', 'Sleet', 'Light shower sleet', 'Shower sleet', 'Light rain and snow', 'Rain and snow', 'Light shower snow', 'Shower snow', 'Heavy showers snow', 'mist', 'Smoke', 'Haze', 'sand/ dust whirls', 'fog', 'sand', 'dust', 'volcanic ash', 'squalls', 'tornado', 'clear sky', 'few clouds', 'scattered clouds', 'broken clouds', 'overcast clouds']
russian = ['гроза с легким дождем', 'гроза с дождем', 'гроза с сильным дождем', 'легкая гроза', 'гроза', 'сильная гроза', 'рваная гроза', 'гроза с легкой моросью', 'гроза с моросью', 'гроза с сильной моросью', 'мелкая морось', 'морось', 'сильная морось', 'мелкий дождь с моросью', 'дождь с моросью', 'сильный дождь с моросью', 'ливень с моросью', 'сильный ливень с моросью', 'дождевая морось', 'небольшой дождь', 'умеренный дождь','сильный дождь', 'очень сильный дождь', 'экстремальный дождь', 'ледяной дождь', 'ливневый дождь с небольшой интенсивностью', 'ливневый дождь', 'сильный ливневый дождь', 'рваный ливневый дождь', 'легкий снег', 'Снег', 'Сильный снег', 'Мокрый снег', 'слякоть','Легкий дождь со снегом', 'Дождь со снегом', 'Легкий дождь со снегом', 'Дождь со снегом', 'Легкий снег со снегом', 'Сильный снег со снегом', 'туман', 'Дым', 'Дымка', 'вихри песка/ пыли', 'туман', 'песок', 'пыль', 'вулканический пепел', 'шквалы', 'торнадо', 'чистое небо', ' небольшое количество облаков', ' рассеянные облака', ' рассеянные облака', 'пасмурные облака']
dictionary = dict(zip(english,russian))
main_eng = ['Thunderstorm', 'Drizzle', 'Rain', 'Snow', 'Mist', 'Smoke', 'Haze', 'Dust', 'Fog', 'Sand', 'Dust', 'Ash', 'Squall', 'Tornado', 'Clear', 'Clouds']
main_rus = ['Гроза', 'Морось', 'Дождь', 'Снег', 'Туман', 'Смог', 'Легкий туман', 'Пыль', 'Туман', 'Песок', 'Пыль', 'Пепел', 'Шквал', 'Торнадо', 'Ясно', 'Облачность']
main_dict = dict(zip(main_eng, main_rus))
 
def speed(wind_speed):
    if wind_speed <= 0.2:
        return 'штиль'
    elif wind_speed <= 1.5:
        return 'тихий'
    elif wind_speed <= 3.3:
        return 'легкий'
    elif wind_speed <= 5.4:
        return 'слабый'
    elif wind_speed <= 10.7:
        return 'свежий'
    elif wind_speed <= 13.8:
        return 'сильный'
    elif wind_speed <= 17.1:
        return 'крепкий'
    elif wind_speed <= 20.7:
        return 'очень крепкий'
    elif wind_speed <= 24.4:
        return 'шторм'
    elif wind_speed <= 28.4:
        return 'сильный шторм'
    elif wind_speed < 33:
        return 'жестокий шторм'
    else:
        return 'ураган'

def direction(deg):
    if deg < 22.55:
        return 'северный'
    elif deg < 67.5:
            return 'северо-восточный'
    elif deg < 112.5:
            return 'восточный'
    elif deg < 157.5:
        return 'юго-восточный'
    elif deg < 202.5:
        return 'южный'
    elif deg < 247.5:
        return 'юго-западный'
    elif deg < 292.5:
        return 'западный'
    elif deg < 337.5:
        return 'северо-западный'
    else:
        return 'северный'

def get_weather():
    response = requests.get('')
    info = response.json()
    outcome = 'Погода в Москве: {}\n'.format(main_dict[info['weather'][0]['main']])
    outcome += '{}, температура: {} - {} °C\n'.format(dictionary[info['weather'][0]['description']], info['main']['temp_min'], info['main']['temp_max'])
    outcome += 'Давление: {} мм. рт. ст, влажность: {}%\n'.format(info['main']['pressure'], info['main']['humidity'])
    outcome += 'Ветер: {}, {} м/c, {}'.format(speed(info['wind']['speed']), info['wind']['speed'], direction(info['wind']['deg']))
    return outcome

if __name__ == '__main__':
    print(get_weather())
