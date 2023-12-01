import re

inp = open("input.txt").read()

total = 0

for line in inp.splitlines():
    line = line.strip()

    tofind = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    all_ind = {}
    for i in tofind:
        indices = [m.start() for m in re.finditer(i, line)]
        for j in indices:
            all_ind[j] = i
    all_ind = dict(sorted(all_ind.items(), key=lambda item: item[0]))

    print(all_ind)
    word_to_int = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
   
    number = []
    for k, v in all_ind.items():
        if v in word_to_int.keys(): number.append(word_to_int[v])
        else: number.append(v)

    print(number, end=" ")
    number = int(number[0] + number[-1])
    print(number)
    total += int(number)

print(total)