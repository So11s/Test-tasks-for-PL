from itertools import cycle

with open('Task1_n.txt', 'r', encoding='utf8') as n:
    n0 = n.read()
    n0 = int(n0)

with open('Task1_m.txt', 'r', encoding='utf8') as m:
    m0 = m.read()
    m0 = int(m0)

way = []
i = 0
lst = cycle(list(range(1,n0+1)))
for item in lst:
    if i == 0:
        way.append(item)
    else:
        if i == m0 - 1:
            if item in way:
                break
            way.append(item)
            i = 0

    i += 1

print("".join(map(str,way)))