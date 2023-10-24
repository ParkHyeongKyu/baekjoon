def solution(n):
    arr = [[] for _ in range(n)]
    for i in range(1, n + 1):
        for j in range(i):
            arr[i - 1].append(0)

    cnt = 1
    x, y = -1, 0
    for i in range(n):
        for j in range(n - i, 0, -1):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1
            arr[x][y] = cnt
            cnt += 1

    result = []
    for i in range(len(arr)):
        result.extend(arr[i])
    return result