# Делаем словарь с очками
points = {
    1: 'оеаинтс',
    2: 'рвлкм',
    3: 'дпуя',
    4: 'ыьгзбчй',
    5: 'хжшю',
    7: 'цщэ',
    10: 'фъё'
}

# Данные для окончаний
s = ('очков', 'очко', 'очка')
exception = ('11', '12', '13', '14', '15', '16', '17', '18', '19')

# Создаем пустой список
table = []
# Вписываем количество игроков
n = int(input())
# По количеству игроков заполняем список и вместе с этим считаем очки
for time in range(n):
    totalPoints = 0
    word, name, = input().split()
    # Копипаста из второй комлексной задачи
    for letter in word.lower():
        for key, value in points.items():
            if letter in value:
                totalPoints += key
    # Вписываем информацию об игроке в список в виде вложенного списка, totalPoints*1000-Time учитывает время
    table.append([totalPoints*1000-time, totalPoints, name])
# Сортируем список в формате невозрастания (сортировка происходит по первому элементу вложенного списка)
table.sort(reverse=True)

# К первым трём спискам прибавляем окончание
for m in range(3):
    if str(table[m][1]).endswith(exception) or table[m][1] % 10 in (0, 5, 6, 7, 8, 9):
        table[m].append(s[0])
    elif table[m][1] % 10 == 1:
        table[m].append(s[1])
    else:
        table[m].append(s[2])

# Выводим
for m in range(3):
    print(m + 1, 'место:', table[m][2], '-', table[m][1], table[m][3])
