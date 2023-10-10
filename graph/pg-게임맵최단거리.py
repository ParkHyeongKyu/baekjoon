from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution(maps):
    answer = 0

    n = len(maps)
    m = len(maps[0])

    visited = [[False for _ in range(m)] for _ in range(n)]
    cnt = [[-1 for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    cnt[0][0] = 1

    while q:
        nx, ny = q.popleft()

        for i in range(4):
            kx = nx + dx[i]
            ky = ny + dy[i]

            if 0 <= kx < n and 0 <= ky < m and not visited[kx][ky] and maps[kx][ky] != 0:
                q.append((kx, ky))
                visited[kx][ky] = True
                cnt[kx][ky] = cnt[nx][ny] + 1

    answer = cnt[n - 1][m - 1]

    return answer