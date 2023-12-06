"""
1. Прочитать в виде списков набор данных titanic.csv, взятый из открытых источников
2. Для прочитанного набора выполнить обработку в соответствии со своим вариантом.
Вариант № 9:
Определить количество пассажиров, севших в порту
Шербур, в возрастном интервале средний возраст  5 позиций и сколько из них выжило.
"""

import csv

f = open("tested.csv")

reader = list(csv.reader(f))
sherbur = []
sherbur_sred = []
sred_age = 0
cnt_live = 0

for i in reader:
    if i[11] == 'C':
        sherbur += [i]

for i in sherbur:
    if i[5] != '':
        sred_age += float(i[5])

sred_age = sred_age / len(sherbur)

for i in sherbur:
    if i[5] != '':
        if abs(float(i[5]) - sred_age) <= 5:
            if i[1] == '1':
                cnt_live += 1

print(cnt_live)
