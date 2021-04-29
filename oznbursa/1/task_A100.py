# Написать функцию very_even(number), которая определяет является ли число "очень четным".
# Однозначное число "очень четное", если оно четное. Числа >= 10 "очень четные",
# если сумма их цифр - "очень четное" число.
#
# Примеры:
# very_even(88) => False -> 8 + 8 = 16 -> 1 + 6 = 7 => 7 нечетное
# very_even(222) => True -> 2 + 2 + 2 = 8 => 8 четное

import traceback


def very_even(n):
    k = 0
    l = n
    while n >= 10 :
        while n > 0 :
            k += n % 10
            n //= 10
        n = k
        k = 0
    return n % 2 == 0


# Тесты
try:
    assert very_even(4) == True
    assert very_even(5) == False
    assert very_even(12) == False
    assert very_even(1234) == False
    assert very_even(7897) ==  True
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
