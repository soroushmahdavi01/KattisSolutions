periods = int(input())
QALY = 0

for x in range (periods):
    comp = input()
    sect = comp.split(' ')
    value1 = float(sect[0])
    value2 = float(sect[1])
    value3 = value1 * value2
    QALY += value3
print(round(QALY, 3))


