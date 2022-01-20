import argparse

parser = argparse.ArgumentParser()

parser.add_argument("nums")

args = parser.parse_args()

with open(args.nums, 'r', encoding='utf8') as file:
    content = file.read()

content = content.split()
b = [int(x) for x in content]

middle = sorted(b)[len(b) // 2]
print(sum(abs(i - middle) for i in b))