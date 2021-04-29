# Задан список из четного количества целых положительных чисел.
# Написать функцию min_sum, которая возвращает минимальную сумму произведений по два числа.
#
# Пример:
# [5,4,2,3] => 22 -> 5 * 2 + 4 * 3 = 22


import traceback


def min_sum(arr):
    if len(arr) == 2 :
        return arr[0] * arr[1]
    num_sum = -1
    for i in range(1, len(arr)):
        arr_copy = arr.copy()
        multiply = arr_copy[0] * arr_copy[i]
        del arr_copy[i]
        del arr_copy[0]
        arr_sum = min_sum(arr_copy) + multiply
        if arr_sum < num_sum or num_sum == -1:
            num_sum = arr_sum
    return num_sum



# Тесты
try:
    assert min_sum([5,4,2,3]) == 22
    assert min_sum([12,6,10,26,3,24]) == 342
    assert min_sum([9,2,8,7,5,4,0,6]) == 74
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
