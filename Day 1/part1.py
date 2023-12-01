inp = open("input.txt").read()

total = 0
for line in inp.splitlines():
    line = line.strip()
    number = []
    for char in line:
        try:
            char = int(char)
            number.append(char)
        except:
            continue
    numberstr = str(number[0])
    if len(number) > 1:
        numberstr += str(number[-1])
    else:
        numberstr += str(number[0])
    number = int(numberstr)
    total += int(number)

print(total)