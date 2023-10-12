def solution(n, lost, reserve):
    answer = 0

    for i in range(1, n + 1):
        if i in lost and i in reserve:
            reserve.remove(i)
            lost.remove(i)

    for i in range(1, n + 1):
        if i not in lost:
            answer += 1
        elif i in lost and (i - 1 <= n and i - 1 in reserve):
            answer += 1
            reserve.remove(i - 1)
        elif i in lost and (i + 1 >= 1 and i + 1 in reserve):
            answer += 1
            reserve.remove(i + 1)
    return answer