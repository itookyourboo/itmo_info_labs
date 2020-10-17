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
    add('"Schedule": {', tabs)
    for n, day in enumerate(schedule1):
        tabs += 1
        add('"Day": [', tabs)
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
        add(']' + ('' if n == len(schedule1) - 1 else ','), tabs)
        tabs -= 1
    add('}', tabs)
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

# 	Without libs				With libs
# 0.0010001659393310547	<	0.2687656879425049
# 0.0020020008087158203	<	0.003989458084106445
# 0.002158641815185547	<	0.002980470657348633
# 0.0020339488983154297	<	0.002998828887939453
# 0.0023162364959716797	<	0.002683401107788086
# 0.0016820430755615234	<	0.003052949905395508
# 0.0018389225006103516	<	0.0029938220977783203
# 0.003914356231689453	<	0.003998517990112305
# 0.001951456069946289	<	0.0032165050506591797
# 0.0017516613006591797	<	0.003321409225463867
