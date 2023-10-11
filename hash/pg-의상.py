from collections import defaultdict


def solution(clothes):
    hashdict = defaultdict(list)

    for c in clothes:
        hashdict[c[1]].append(c[0])

    sum = 0
    x = 1
    for k, v in hashdict.items():
        x *= (len(v) + 1)

    return x - 1