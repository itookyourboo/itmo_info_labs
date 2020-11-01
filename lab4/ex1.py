# Задание на 70 баллов
# Вариант 28 % 5 = 3
# Требуется найти в тексте все фамилии, отсортировав их по алфавту

import re

REG_EXP = '\W([А-Я][а-я]*)\s+[А-Я]\.\s?[А-Я]'


def get_last_names_re(text):
    return sorted(re.findall(REG_EXP, text))


def get_last_names(text):
    symbols = '?!,:;()'
    for s in symbols:
        text = text.replace(s, ' ')
    text = text.replace('. .', '.').replace('  ', ' ')

    result = []
    words = text.split()
    for i, word in enumerate(words):
        if i != len(words) - 1:
            next = words[i + 1]
            if len(next) == 2 and next[0].isupper() and next[1] == '.':
                if i != len(words) - 2:
                    nextnext = words[i + 2]
                    if len(nextnext) == 2 and nextnext[0].isupper() and nextnext[1] == '.':
                        result.append(word)
            elif all(s == '' or s.isupper() for s in next.split('.')):
                result.append(word)
    result.sort()

    return result


tests = [
    'Студент Вася вспомнил, что на своей лекции Балакшин П.В. упоминал про старшекурсников, '
    'которые будут ему помогать: Анищенко А.А. и Машина Е.А.',

    'Лиза была удивлена тому, как ее новый преподаватель, Зотов А.Н., лояльно отнёсся к ней. '
    'Демидов   К.И. бы завалил её, а Шидловский М.И. даже не стал бы принимать работу.',

    'Вот их имена: Иванов И. И., старший лейтенант. Бутелин Л. Г., младший лейтенант. Рябцев П. С., лейтенант.',

    'Дискутируемая неизменность богослужений на церковнославянском имеет одно неоспоримое преимущество: '
    'точно такую же обедню выстаивал, скажем, Пушкин А. С. или Гоголь Н. В. '
    'Кого вы там любите в Золотом-Серебряном веке русской литературы?',

    'Съезд открывает Рыков А. И., ставший после смерти Ленина председателем Совнаркома. '
    'Разгром Сталиным «новой оппозиции» Зиновьева — Каменева (Зиновьев Г.Е., Каменев Л.Б., Сокольников Г.Я., '
    'впоследствии отошедшая от оппозиции Крупская Н.К.).'
]

for test in tests:
    res_re = get_last_names_re(test)
    res = get_last_names(test)
    print(f'TEST:\n{test}\nREGEXP ANSWER:\n{res_re}\nMY ANSWER:\n{res}\nEquals: {res_re == res}\n')
