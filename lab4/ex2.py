# Задание на 12 баллов
# Вариант 28 % 4 = 0
# Найти все предложения, в которых ровно 6 слов, одно из которых двусложное

import re


REG_6_WORDS = '[\.\?\!]\s*((?:\w+\s*[,;:]?\s+){5}\w+[\.\?\!])'
VOWEL = '[aeiouyAEIOUY]'
REG_2_SYLLABLES = f'\\b(?:(?!{VOWEL})\w)*{VOWEL}+(?:(?!{VOWEL})\w)+{VOWEL}+(?:(?!{VOWEL})\w)*\\b'


with open('RomeoAndJuliet.txt') as file:
    text = file.read()

sentences = re.findall(REG_6_WORDS, text)
for sentence in sentences:
    words_with_2_syllables = re.findall(REG_2_SYLLABLES, sentence)
    # print(sentence, words_with_2_syllables)
    if len(words_with_2_syllables) == 1:
        print(sentence.replace(words_with_2_syllables[0], words_with_2_syllables[0].upper()))