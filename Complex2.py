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

# Вводим и переводим сразу в список
message = list(input().lower())

# Очищаем список от не букв
onlyLettersMessage = []
for t in message:
    if t.isalpha():
        onlyLettersMessage.append(t)

# Очищаем список от повторяющихся подряд букв и составляем слово
word = onlyLettersMessage[0]
for i in range(len(onlyLettersMessage) - 1):
    if onlyLettersMessage[i + 1] != onlyLettersMessage[i]:
        word += onlyLettersMessage[i + 1]

# Ищем буквы по словарю и суммируем соответствующие буквам значения очков
totalPoints = 0
for letter in word:
    for key, value in points.items():
        if letter in value:
            totalPoints += key

# Выводим с правильным окончанием
if str(totalPoints).endswith(exception) or totalPoints % 10 in (0, 5, 6, 7, 8, 9):
    print(word, totalPoints, s[0])
elif totalPoints % 10 == 1:
    print(word, totalPoints, s[1])
else:
    print(word, totalPoints, s[2])
