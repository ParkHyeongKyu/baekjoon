from collections import deque


def checkWordDiff(a, b):
    cnt = 0

    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1

    if cnt == 1:
        return True


def solution(begin, target, words):
    answer = 0

    visited = [False for _ in range(len(words))]
    q = deque()
    q.append((begin, 0))

    while q:
        now_word, cnt = q.popleft()

        if now_word == target:
            return cnt

        for idx, word in enumerate(words):
            if not visited[idx] and checkWordDiff(now_word, word):
                q.append((word, cnt + 1))
                visited[idx] = True

    return answer