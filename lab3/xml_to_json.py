from time import time


def parse_without_libs():
    schedule = {'Schedule': []}

    def get_value(line):
        return line[line.index('>') + 1:line.index('</')]

    with open('schedule.xml', 'r', encoding='utf8') as file:
        lines = file.readlines()

    lesson_tags = ['Time', 'Week', 'Room', 'Building', 'Subject', 'Teacher', 'Format']

    schedule1 = schedule['Schedule']
    for line in lines:
        if 'Schedule' in line:
            continue
        elif '<Day>' in line:
            schedule1.append({})
        elif '<DayName' in line:
            schedule1[-1]['DayName'] = get_value(line)
        elif '<Lesson' in line:
            if 'Lesson' not in schedule1[-1]:
                schedule1[-1]['Lesson'] = []
            schedule1[-1]['Lesson'].append({})
        for tag in lesson_tags:
            if f'<{tag}' in line:
                schedule1[-1]['Lesson'][-1][tag] = get_value(line)

    res = []

    def add(s, tabs=0):
        res.append('\t' * tabs + s.replace('\'', '\"'))

    tabs = 0
    add('{', tabs)
    tabs += 1
    add('"Schedule": [', tabs)
    for n, day in enumerate(schedule1):
        tabs += 1
        add('{', tabs)
        tabs += 1
        add(f'\"DayName\": \"{day["DayName"]}\",', tabs)
        add(f'\"Lesson\": [', tabs)
        tabs += 1
        for j, lesson in enumerate(day['Lesson']):
            add('{', tabs)
            tabs += 1
            for i, k in enumerate(lesson):
                add(f'\"{k}\": \"{lesson[k]}\"' + ('' if i == len(lesson) - 1 else ','), tabs)
            tabs -= 1
            add('}' + ('' if j == len(day['Lesson']) - 1 else ','), tabs)
        tabs -= 1
        add(']', tabs)
        tabs -= 1
        add('}' + ('' if n == len(schedule1) - 1 else ','), tabs)
        tabs -= 1
    add(']', tabs)
    tabs -= 1
    add('}', tabs)

    with open('schedule.json', 'w', encoding='utf8') as file:
        file.write('\n'.join(res))


def parse_with_libs():
    import xmltodict
    import json

    s = time()

    with open('schedule.xml', encoding='utf8') as file:
        data = xmltodict.parse(file.read())

    with open('schedule2.json', 'w', encoding='utf8') as file2:
        json.dump(data, file2, ensure_ascii=False, indent=4, separators=(', ', ': '))


print('\tWithout libs\t\t\t\tWith libs')
for i in range(10):
    start = time()
    parse_without_libs()
    total_without = time() - start
    start = time()
    parse_with_libs()
    total_with = time() - start
    print(f'{total_without}\t{("<", ">")[total_without > total_with]}\t{total_with}')
