from heapq import heappush, heappop


def solution(scoville, K):
    answer = 0
    heap = []
    for i in range(len(scoville)):
        heappush(heap, scoville[i])

    while heap[0] < K:
        if len(heap) == 1:
            return -1
        a = heappop(heap)
        b = heappop(heap)
        new = a + (2 * b)
        heappush(heap, new)
        answer += 1
    return answer