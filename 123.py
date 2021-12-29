import argparse

# def sloj(a,b):
#     return a+b

parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number", type=int)
args = parser.parse_args()
print(args.square**2)
# parser.add_argument("-a", dest="a", type=int)
# parser.add_argument("-b", dest="b", type=int)

# args = parser.parse_args()

# print(args)