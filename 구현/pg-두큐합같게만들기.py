from collections import deque


def solution(queue1, queue2):
    answer = 0

    q1 = deque(queue1)
    q2 = deque(queue2)

    now_sum1 = sum(q1)
    now_sum2 = sum(q2)
    all_sum = now_sum1 + now_sum2

    if all_sum % 2 != 0:
        return -1

    while now_sum1 != now_sum2:
        if now_sum1 > now_sum2:
            temp = q1.popleft()
            q2.append(temp)
            now_sum1 -= temp
            now_sum2 += temp
        else:
            temp = q2.popleft()
            q1.append(temp)
            now_sum1 += temp
            now_sum2 -= temp
        answer += 1
        if answer > len(queue1) * 4:
            return -1

    return answer