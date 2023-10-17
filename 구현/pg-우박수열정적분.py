def solution(k, ranges):
    answer = []

    y = [k]
    result = k

    while result != 1:
        if result % 2 == 0:
            result /= 2
        else:
            result *= 3
            result += 1
        y.append(result)

    n = len(y) - 1

    for i in range(len(ranges)):
        if ranges[i][0] > n + ranges[i][1]:
            answer.append(-1)
            continue
        elif ranges[i][0] == n + ranges[i][1]:
            answer.append(0)
            continue
        sum = 0
        for j in range(ranges[i][0], n + ranges[i][1] + 1):
            if j == ranges[i][0] or j == n + ranges[i][1]:
                sum += y[j]
            else:
                sum += y[j] * 2
        answer.append(sum / 2)

    return answer