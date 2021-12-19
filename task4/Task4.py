with open('task4.txt', 'r', encoding='utf8') as file:
    content = file.read()

content = content.split()
b = [int(x) for x in content]

middle = sorted(b)[len(b) // 2]
print(sum(abs(i - middle) for i in b))