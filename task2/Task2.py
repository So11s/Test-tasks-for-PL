with open('file1.txt','r',encoding='utf8') as file:
    content = file.read()

with open('file2.txt', 'r', encoding='utf8') as file_2:
    content_2 = file_2.read()

import math

content = content.split()
okr = list(map(float, content))

content_2 = content_2.split()
points = list(map(float, content_2))

n = 0

while n < len(points):
    x = points[n]
    y = points[n + 1]
    hypotenuse = math.sqrt((x - okr[0])**2 + (y - okr[1])**2)

    if hypotenuse < okr[2]:
        print("1")
    elif hypotenuse == okr[2]:
        print("0")
    else:
        print("2")
    n+=2