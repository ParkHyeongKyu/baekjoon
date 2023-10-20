from collections import deque
import sys


def solution(rows, columns, queries):
    answer = []
    map = [[0 for _ in range(columns)] for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            map[i][j] = i * columns + (j + 1)

    for query in queries:
        q = deque()
        q.append([query[0] - 1, query[1] - 1, map[query[0] - 1][query[1] - 1]])
        cnt = 0
        min = sys.maxsize

        while q:
            nx, ny, value = q.popleft()

            if nx == query[0] - 1 and ny == query[1] - 1 and cnt != 0:
                break
            if value < min:
                min = value

            if ny == query[1] - 1 and query[0] - 1 < nx <= query[2] - 1:
                q.append([nx - 1, ny, map[nx - 1][ny]])
                map[nx - 1][ny] = value
            elif nx == query[0] - 1 and query[1] - 1 <= ny < query[3] - 1:
                q.append([nx, ny + 1, map[nx][ny + 1]])
                map[nx][ny + 1] = value
            elif ny == query[3] - 1 and query[0] - 1 <= nx < query[2] - 1:
                q.append([nx + 1, ny, map[nx + 1][ny]])
                map[nx + 1][ny] = value
            elif nx == query[2] - 1 and query[1] - 1 < ny <= query[3] - 1:
                q.append([nx, ny - 1, map[nx][ny - 1]])
                map[nx][ny - 1] = value
            cnt += 1
        answer.append(min)

    return answer