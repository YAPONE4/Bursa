import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
import random

random.seed()


def main():
    
    vk_session = vk_api.VkApi(token = 'a1acd3a38ed2e3cd673c14ca4a18bcf08c130af7da1953e00a95747c50e195aa7ce8daa79e60c3985251f')
    vk = vk_session.get_api()

    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.text.lower() == 'прив':
            vk.messages.send(
                user_id = event.user_id,
                random_id = get_random_id(),
                message = 'Привет, ' + vk.users.get(user_id = event.user_id)[0]['first_name']
                )
        elif event.type == VkEventType.MESSAGE_NEW and event.text.lower() == 'подбрось сасную монетку':
            coin = random.randint(0, 1)
            if coin == 0:
                coin = 'Аяс'
            else:
                coin = 'Сас'
            vk.messages.send(
            user_id = event.user_id,
            random_id = get_random_id(),
            message = 'У вас выпал ' + coin
            )
        elif event.type == VkEventType.MESSAGE_NEW and event.text.lower() == 'хачу угадайку':
            digit = str(random.randint(1, 10))
            vk.messages.send(
                user_id = event.user_id,
                random_id = get_random_id(),
                message = 'Я загадал число от 1 до 10. Не угадаешь -- гамасек'
                )
            if event.type == VkEventType.MESSAGE_NEW:
                if event.text == digit:
                    vk.messages.send(
                        user_id = event.user_id,
                        random_id = get_random_id(),
                        message = 'Ладно, ты угадал'
                    )
                    break
                else:
                    vk.messages.send(
                        user_id = event.user_id,
                        random_id = get_random_id(),
                        message = 'Хаха, гамасек'
                    )

if __name__ == '__main__':
    main()