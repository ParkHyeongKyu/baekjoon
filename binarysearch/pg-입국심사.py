import math


def solution(n, times):
    answer = 0

    start = 0
    end = max(times) * math.ceil(n / len(times))

    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for i in range(len(times)):
            people = mid // times[i]
            cnt += people
        if cnt >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    return answer