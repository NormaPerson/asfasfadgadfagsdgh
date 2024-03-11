data = [[j.strip() for j in i.split(",")] for i in open('students.csv', encoding='UTF-8').readlines()][1:] # считываем данные из csv файла
WFdata = [i for i in data if i[4].isdigit()] # находим учеников у которых не пропали баллы
classMidScore = {} # создаём словарь списков для сохранения в нём среднего балла по классу (список: сумма всех баллов в классе, кол-во)
print(len(data), len(WFdata))
for el in WFdata: # заполняем словарь
    if not el[3] in classMidScore:
        classMidScore[el[3]] = [0, 0]
    q = classMidScore[el[3]]
    classMidScore[el[3]] = [q[0] + int(el[4]), q[1] + 1]
for i in range(len(data)): # находим детей с пропавшими оценками и заполняем их средней по классу
    if not data[i][4].isdigit():
        print(data[i][3])
        q = classMidScore[data[i][3]]
        data[i][4] = str(round(q[0] / q[1], 3))
t = '\n'.join([",".join(i) for i in data])
with open('students_new.csv', 'w', encoding="UTF-8") as f: # сохраняем в файл
    print(t, file=f)