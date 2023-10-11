from collections import deque

visited = [[False for _ in range(102)] for _ in range(102)]
cnt = [[-1 for _ in range(102)] for _ in range(102)]


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    for i in range(len(rectangle)):
        rectangle[i][0] = 2 * rectangle[i][0]
        rectangle[i][1] = 2 * rectangle[i][1]
        rectangle[i][2] = 2 * rectangle[i][2]
        rectangle[i][3] = 2 * rectangle[i][3]

        for x in range(rectangle[i][0] + 1, rectangle[i][2]):
            for y in range(rectangle[i][1] + 1, rectangle[i][3]):
                visited[x][y] = True

    q = deque()
    q.append((characterX * 2, characterY * 2))
    visited[characterX * 2][characterY * 2] = True
    cnt[characterX * 2][characterY * 2] = 0

    while q:
        nx, ny = q.popleft()

        if nx == itemX * 2 and ny == itemY * 2:
            return cnt[nx][ny] // 2

        dx = []
        dy = []
        for i in range(len(rectangle)):
            # 왼쪽 변 중간 or 오른쪽 변 중간
            if (nx == rectangle[i][0] and rectangle[i][1] < ny < rectangle[i][3]) or (
                    nx == rectangle[i][2] and rectangle[i][1] < ny < rectangle[i][3]):
                dx.extend([0, 0])
                dy.extend([-1, 1])
            # 아래 변 중간 or 윗 변 중간
            if (ny == rectangle[i][1] and rectangle[i][0] < nx < rectangle[i][2]) or (
                    ny == rectangle[i][3] and rectangle[i][0] < nx < rectangle[i][2]):
                dx.extend([-1, 1])
                dy.extend([0, 0])
            # 왼쪽 아래 꼭짓점
            if nx == rectangle[i][0] and ny == rectangle[i][1]:
                dx.extend([1, 0])
                dy.extend([0, 1])
            # 왼쪽 위 꼭짓점
            if nx == rectangle[i][0] and ny == rectangle[i][3]:
                dx.extend([1, 0])
                dy.extend([0, -1])
            # 오른쪽 아래 꼭짓점
            if nx == rectangle[i][2] and ny == rectangle[i][1]:
                dx.extend([-1, 0])
                dy.extend([0, 1])
            # 오른쪽 위 꼭짓점
            if nx == rectangle[i][2] and ny == rectangle[i][3]:
                dx.extend([-1, 0])
                dy.extend([0, -1])
        for i in range(len(dx)):
            kx = nx + dx[i]
            ky = ny + dy[i]

            if 0 < kx <= 100 and 0 < ky <= 100 and not visited[kx][ky]:
                q.append((kx, ky))
                visited[kx][ky] = True
                cnt[kx][ky] = cnt[nx][ny] + 1

    return answer