# Задание на 18 баллов
# Вариант 28 % 6 = 4
# Найти в тексте все слова, в которых две гласные стоят подряд,
# а после этого слова идёт слово в котором не больше 3 согласных


import re

vowels = 'ёуеыаоэяию'
VOWEL = f'[{vowels}{vowels.upper()}]'
other = 'ъь'
NOT_CONSONANT = f'[{vowels + other}{(vowels + other).upper()}]'
consonants = 'бвгджзйклмнпрстфхцчшщ'
CONSONANT = f'[{consonants}{consonants.upper()}]'

REG_EXP = f'\\b(\w*{VOWEL}{{2}}\w*)\\b\W\\b(?:{VOWEL}|(?:{NOT_CONSONANT}*{CONSONANT}){{1,3}}{NOT_CONSONANT}*)\\b'

tests = [
    'Кривошеее существо гуляет по парку',

    'Реализуйте программный продукт на языке Python, '
    'используя регулярные выражения по варианту, представленному в таблице',

    'Для своей программы придумайте минимум пять тестов',

    'Я обожаю пить сок в окружении детей'
]

for test in tests:
    print(f'{test}\n{re.findall(REG_EXP, test)}')
