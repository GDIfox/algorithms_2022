"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""



# O(N)
def poisk_1(company):
    in_max = {}
    list_q = dict(company)
    for i in range(3):
        maximum = max(list_q.items(), key=lambda spisok: spisok[1])
        del list_q[maximum[0]]
        in_max[maximum[0]] = maximum[1]
    print(in_max)

# O(N*logonN)
def poisk_2(company):
    list_dict = list(company.items())
    list_dict.sort(key=lambda i: i[1], reverse=True)
    for i in range(3):
        print(f"{list_dict[i][0]}: {list_dict[i][1]}")

poisk_1(company)
poisk_2(company)

# оптимальное решение будет в первом варианте, + в скорости
