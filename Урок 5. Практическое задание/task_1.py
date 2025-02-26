"""
Задание 1.

Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените коллекцию из модуля collections
Для лучшего освоения материала можете сделать
несколько варианто решения этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога
Предприятия, с прибылью ниже среднего значения: Копыта
"""


from collections import namedtuple
from collections import defaultdict

Company = int(input('Введите количество предприятий для расчета прибыли: '))
CompanyData = namedtuple('OrganizationData', 'kvartal1 kvartal2 kvartal3 kvartal4 kvartal_sum')
Company_data = defaultdict(CompanyData)
Company_kvartal = 0
for i in range(Company):
    organization_name = input(f'Введите название предприятия ({i + 1}): ')
    while True:
        try:
            organization_kvartal = list(map(int, input('через пробел введите прибыль данного '
                                                 'предприятия за каждый квартал(Всего 4 квартала): ').split()))
            if len(organization_kvartal) != 4:
                print('4 значения через пробел')
                raise ValueError()
            break
        except ValueError:
            print('Вы ввели не корректное значение, попробуйте еще раз')

    Company_kvartal += sum(organization_kvartal)
    organization_kvartal.append(sum(organization_kvartal))
    Company_data[organization_name] = CompanyData(*organization_kvartal)

if Company <= 0:
    exit(0)

avg_Company_kvartal = Company_kvartal / Company
print(f'Средняя годовая прибыль всех предприятий: {avg_Company_kvartal}')

Company_good, Company_bad= [], []

for Company, data in Company_data.items():
    if data.kvartal_sum >= avg_Company_kvartal:
        Company_good.append(Company)
    else:
        Company_bad.append(Company)

print(f'Предприятия, с прибылью выше среднего значения: {",".join(Company_good)}')
print(f'Предприятия, с прибылью ниже среднего значения: {",".join(Company_bad)}')
