# Написать функцию biggest, на вход которой приходит список строк (числа). Необходимо объединить
# строки в одну таким образом, чтобы получаемое числовое значение было максимальным.
#
# Пример:
# biggest(['1', '2', '3']) ==> '321'
# biggest(['3', '30', '34', '5', '9']) ==> '9534330'


import traceback

from itertools import *

def biggest(s):
    k = 0
    n = len(s) - 1
    for i in permutations(s) :
        if int("".join(i)) > k :
            k = int("".join(i))
    return str(k)


# Тесты
try:
    assert biggest(['0', '0', '0']) == '0'
    assert biggest(['121', '12']) == '12121'
    assert biggest(['12', '128']) == '12812'
    assert biggest(['5051', '50']) == '505150'
    assert biggest(['3', '30', '34', '5', '9']) == '9534330'
    assert biggest(['824', '938', '1399', '5607', '6973', '5703', '9609', '4398', '8247']) \
           == '9609938824824769735703560743981399'
    assert biggest(['3803', '38', '380']) == '383803803'
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")