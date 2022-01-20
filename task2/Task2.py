import argparse

parser = argparse.ArgumentParser()

parser.add_argument("file1")
parser.add_argument("file2")

args = parser.parse_args()

with open(args.file1,'r',encoding='utf8') as file:
    content = file.read()

with open(args.file2, 'r', encoding='utf8') as file_2:
    content_2 = file_2.read()

import math

content = content.split()

for i0, elem0 in enumerate(content):

    if ',' in elem0:

        content[i0] = elem0.replace(',', '.')

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