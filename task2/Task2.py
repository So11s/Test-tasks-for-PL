with open('C:/Users/lelik/Desktop/file1.txt','r',encoding='utf8') as file:
    content = file.read()

with open('C:/Users/lelik/Desktop/file2.txt', 'r', encoding='utf8') as file_2:
    content_2 = file_2.read()

import math

content = content.split()
okr = list(map(float, content))

content_2 = content_2.split()

for i, elem in enumerate(content_2):

    if ',' in elem:

        content_2[i] = elem.replace(',', '.')

points = list(map(float, content_2))

n = 0

while n < len(points):

    hypotenuse = math.sqrt((points[n] - okr[0])**2 + (points[n + 1] - okr[1])**2)

    if hypotenuse < okr[2]:
        print("1")
    elif hypotenuse == okr[2]:
        print("0")
    else:
        print("2")
    n+=2