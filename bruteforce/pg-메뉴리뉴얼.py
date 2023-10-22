from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    counter = Counter()
    for c in course:
        for o in orders:
            res = list(combinations(o, c))
            for r in res:
                r = sorted(r)
                counter[''.join(r)] += 1

        max_value = 0
        max_ct = []
        for ct, v in counter.items():
            if len(ct) == c and v > max_value and v > 1:
                max_value = v
                max_ct.clear()
                max_ct.append(ct)
            elif len(ct) == c and v == max_value and v > 1:
                max_ct.append(ct)
        answer.extend(max_ct)
    answer.sort()
    return answer