from heapq import heappush, heappop
from collections import defaultdict


def solution(k, tangerine):
    answer = 0

    heap = []
    dt = defaultdict(int)

    for i in range(len(tangerine)):
        dt[tangerine[i]] += 1

    for i in range(max(tangerine) + 1):
        heappush(heap, (-dt[i], i))

    for i in range(len(heap)):
        cnt = heappop(heap)
        if k > -cnt[0]:
            k -= -cnt[0]
            answer += 1
        else:
            k = 0
            answer += 1
            break
    return answer