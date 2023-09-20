def solution(cards):
    answer = 0
    n = len(cards)

    visited = [False] * n
    arr = []
    for i in range(n):
        sum = 0
        if visited[i]:
            continue
        now = i
        while not visited[now]:
            sum += 1
            visited[now] = True
            now = cards[now] - 1
        arr.append(sum)

    if len(arr) == 1:
        answer = 0
    else:
        max = -1
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] * arr[j] > max:
                    max = arr[i] * arr[j]
        answer = max

    return answer