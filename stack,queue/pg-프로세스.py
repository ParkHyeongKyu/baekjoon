from collections import deque


def solution(priorities, location):
    answer = 0
    q = deque()

    for p in priorities:
        q.append(p)

    while q:
        m = max(q)
        left = q.popleft()
        if left != m:
            q.append(left)
        else:
            answer += 1
            if location == 0:
                return answer

        if location != 0:
            location -= 1
        else:
            location = len(q) - 1

    return answer