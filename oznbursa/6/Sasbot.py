import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
import random
import re   

random.seed()


def main():
    
    vk_session = vk_api.VkApi(token = 'a1acd3a38ed2e3cd673c14ca4a18bcf08c130af7da1953e00a95747c50e195aa7ce8daa79e60c3985251f')
    vk = vk_session.get_api()

    longpoll = VkLongPoll(vk_session)

    usersdict = {}

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.text and event.to_me:
            print(event.text)
            group = re.sub('/w/w/w/w-/d/d-/d/d', 'KEY_EXECUTE_GROUP', event.text, count = 0, flags = 0)
            if event.text.lower() == 'прив':
                vk.messages.send(
                    user_id = event.user_id,
                    random_id = get_random_id(),
                    message = 'Привет, ' + vk.users.get(user_id = event.user_id)[0]['first_name']
                    )
            elif group == 'KEY_EXECUTE_GROUP':
                usersdict.update({event.user_id : event.text})
                vk.messages.send(
                    user_id = event.user_id,
                    random_id = get_random_id(),
                    message = 'Отлично! Я запомнил, что ты из группы {}!'.format(event.text)
                    )
            print(group)


if __name__ == '__main__':
    main()