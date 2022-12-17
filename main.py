import re

def get_prio(item):
    print(item)
    if item.isupper():
        return ord(item) - 64 + 26
    else:
        return ord(item) - 96

def find_repeated(str1, str2):
    for idx in range(0, len(str1)):
        if re.search(str1[idx], str2):
            return str1[idx]

    return None

def find_repeated2(str1, str2, str3):
    for idx in range(0, len(str1)):
        if re.search(str1[idx], str2):
            if re.search(str1[idx], str3):
                return str1[idx]

    return None


# with open('input.txt', 'r') as reader:
#     line = reader.readline()
#     prio = 0
#     while line != '':
#         res = re.split('\n', line)
#         part1 = line[0:int(len(line)/2)]
#         part2 = line[int(len(line)/2):int(len(line))]
#         prio += get_prio(find_repeated(part1, part2))
#         line = reader.readline()
with open('input.txt', 'r') as reader:
    line1 = reader.readline()
    line2 = reader.readline()
    line3 = reader.readline()
    prio = 0
    while line1 != '' and line2 != '' and line3 != '':
        prio += get_prio(find_repeated2(line1, line2, line3))
        line1 = reader.readline()
        line2 = reader.readline()
        line3 = reader.readline()

print(prio)