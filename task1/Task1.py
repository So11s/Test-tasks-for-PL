from itertools import cycle
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("n", type=int, help="Argument n")
parser.add_argument("m", type=int, help="Argument m")

args = parser.parse_args()

def task1(n,m):

    way = []
    i = 0
    lst = cycle(list(range(1,n+1)))
    for item in lst:
        if i == 0:
            way.append(item)
        else:
            if i == m - 1:
                if item in way:
                    break
                way.append(item)
                i = 0

        i += 1

    print("".join(map(str,way)))

task1(args.n, args.m)