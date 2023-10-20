from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def solution(grid):
    answer = []

    check = [[[False for _ in range(4)] for _ in range(len(grid[0]))] for _ in range(len(grid))]

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for dir in range(4):
                if not check[x][y][dir]:
                    cnt = 0
                    q = deque()

                    q.append((x, y, dir))
                    check[x][y][dir] = True
                    while q:
                        nx, ny, ndir = q.popleft()

                        if nx == x and ny == y and ndir == dir and cnt != 0:
                            break
                        kx = (nx + dx[ndir]) % len(grid)
                        ky = (ny + dy[ndir]) % len(grid[0])

                        if grid[kx][ky] == 'S':
                            kdir = ndir
                        elif grid[kx][ky] == 'L':
                            kdir = (ndir + 1) % 4
                        elif grid[kx][ky] == 'R':
                            kdir = (ndir - 1) % 4

                        q.append((kx, ky, kdir))
                        check[kx][ky][kdir] = True
                        cnt += 1
                    answer.append(cnt)
    answer.sort()
    return answer