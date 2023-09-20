from collections import deque


def checkVisited(n, m, visited):
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                return (i, j)
    return (-1, -1)


def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    answer = []
    n = len(maps)
    m = len(maps[0])

    visited = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'X':
                visited[i][j] = True

    q = deque()
    while True:
        start_x, start_y = checkVisited(n, m, visited)
        if start_x == -1:
            break
        q.append((start_x, start_y))
        visited[start_x][start_y] = True
        sum = int(maps[start_x][start_y])
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    visited[nx][ny] = True
                    sum += int(maps[nx][ny])
                    q.append((nx, ny))
        answer.append(sum)
    if len(answer) == 0:
        answer.append(-1)
    return sorted(answer)