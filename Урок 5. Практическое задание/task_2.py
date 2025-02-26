"""
Задание 2.

Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Попытайтесь решить это задание в двух вариантах.
1) через collections

defaultdict(list)
int(, 16)
reduce

2) через ООП

вспомните про перегрузку методов

__mul__
__add__
"""


from collections import defaultdict
from collections import deque


def my_func_1(string):
    func_1 = 0
    num = deque(string)
    num.reverse()
    for i in range(len(num)):
        func_1 += tab[num[i]] * 16 ** i
    return func_1


def my_func_2(numb):
    num = deque()
    while numb > 0:
        d = numb % 16
        for i in tab:
            if tab[i] == d:
                num.append(i)
        numb //= 16
    num.reverse()
    return list(num)


znak = '0123456789ABCDEF'
tab = defaultdict(int)
counter = 0
for key in znak:
    tab[key] += counter
    counter += 1

num_1 = my_func_1(input('Введите первое число в шестнадцатиричном формате:\n ').upper())
num_2 = my_func_1(input('Введите второе число в шестнадцатиричном формате:\n ').upper())

print(f'Сумма чисел: {my_func_2(num_1 + num_2)}')
print(f'Произведение чисел: {my_func_2(num_1 * num_2)}')
