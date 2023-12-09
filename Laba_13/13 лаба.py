"""
1. Прочитать в виде списков набор данных titanic.csv, взятый из открытых источников
2. Для прочитанного набора выполнить обработку в соответствии со своим вариантом.
Вариант № 9:
Определить количество пассажиров, севших в порту
Шербур, в возрастном интервале средний возраст +- 5 позиций и сколько из них выжило.
"""

import csv

f = open("tested.csv")
reader = list(csv.reader(f))

sherbur = []
sherbur_sred = []
sherbur_age_list = []
cnt_sherbur_sred_age = 0
cnt_sherbur_sred_age_alive = 0

for i in reader:
    if i[11] == 'C':
        sherbur += [i]
        if i[5] != '' and i[5] != ' ':
            sherbur_age_list.append(float(i[5]))

sred_age = float(str(sum(sherbur_age_list) / len(sherbur_age_list))[:4])

print(f'Средний возраст пассажиров севших в Шербуре: {sred_age}')

sorted_age_list = sorted(sherbur_age_list)

for i, n in enumerate(sorted_age_list):
    if n > sred_age:
        index_sred_age = i
        sorted_age_list.insert(index_sred_age, sred_age)
        break

position_age_list = sorted_age_list[index_sred_age - 5: index_sred_age + 6]

for i in sherbur:
    if i[5] != '' and i[5] != ' ' and (position_age_list[0] <= float(i[5]) <= position_age_list[-1]):
        cnt_sherbur_sred_age += 1
        if i[1] == '1':
            cnt_sherbur_sred_age_alive += 1

print(f'\nКоличество пассажиров, севших в порту Шербур в возрасте от {position_age_list[0]} до {position_age_list[-1]}: {cnt_sherbur_sred_age}')
print(f'\nКоличество выживших из них: {cnt_sherbur_sred_age_alive}')
