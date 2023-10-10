from collections import deque


def solution(numbers, target):
    answer = 0

    q = deque()
    q.append((numbers[0], 0))
    q.append((-numbers[0], 0))

    while q:
        now_sum, idx = q.popleft()
        if idx == len(numbers) - 1 and now_sum == target:
            answer += 1

        if idx + 1 < len(numbers):
            idx = idx + 1
        else:
            continue

        q.append((now_sum + numbers[idx], idx))
        q.append((now_sum - numbers[idx], idx))

    return answer