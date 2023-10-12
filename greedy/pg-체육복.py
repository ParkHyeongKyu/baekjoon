def solution(n, lost, reserve):
    answer = 0

    def existInLost(stu):
        nonlocal lost
        for i in range(len(lost)):
            if stu == lost[i]:
                return True
        return False

    def existInReserve(stu):
        nonlocal reserve
        for i in range(len(reserve)):
            if stu == reserve[i]:
                return True
        return False

    for i in range(1, n + 1):
        if existInLost(i) and existInReserve(i):
            reserve.remove(i)
            lost.remove(i)

    for i in range(1, n + 1):
        if not existInLost(i):
            answer += 1
        elif existInLost(i) and (i - 1 <= n and existInReserve(i - 1)):
            answer += 1
            reserve.remove(i - 1)
        elif existInLost(i) and (i + 1 >= 1 and existInReserve(i + 1)):
            answer += 1
            reserve.remove(i + 1)
    return answer