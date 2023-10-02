from collections import deque
import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution(maps):
    answer = 0
    cnt_lever = [[sys.maxsize for _ in range(len(maps[0]))] for _ in range(len(maps))]
    visited_lever = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    start_x, start_y = 0, 0
    lever_x, lever_y = 0, 0
    end_x, end_y = 0, 0
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                start_x, start_y = i, j
            elif maps[i][j] == 'L':
                lever_x, lever_y = i, j
            elif maps[i][j] == 'E':
                end_x, end_y = i, j
            elif maps[i][j] == 'X':
                visited_lever[i][j] = True

    q = deque()
    q.append((start_x, start_y))
    visited_lever[start_x][start_y] = True
    cnt_lever[start_x][start_y] = 0
    while q:
        nx, ny = q.popleft()
        for i in range(4):
            kx = nx + dx[i]
            ky = ny + dy[i]

            if 0 <= kx < len(maps) and 0 <= ky < len(maps[0]) and not visited_lever[kx][ky]:
                visited_lever[kx][ky] = True
                q.append((kx, ky))
                if cnt_lever[kx][ky] > cnt_lever[nx][ny] + 1:
                    cnt_lever[kx][ky] = cnt_lever[nx][ny] + 1

    if cnt_lever[lever_x][lever_y] == sys.maxsize:
        return -1

    visited_end = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    cnt_end = [[sys.maxsize for _ in range(len(maps[0]))] for _ in range(len(maps))]

    eq = deque()
    eq.append((lever_x, lever_y))
    visited_end[lever_x][lever_y] = True
    cnt_end[lever_x][lever_y] = cnt_lever[lever_x][lever_y]

    while eq:
        nx, ny = eq.popleft()
        for i in range(4):
            kx = nx + dx[i]
            ky = ny + dy[i]

            if 0 <= kx < len(maps) and 0 <= ky < len(maps[0]) and not visited_end[kx][ky] and maps[kx][ky] != 'X':
                visited_end[kx][ky] = True
                eq.append((kx, ky))
                if cnt_end[kx][ky] > cnt_end[nx][ny] + 1:
                    cnt_end[kx][ky] = cnt_end[nx][ny] + 1

    if cnt_end[end_x][end_y] == sys.maxsize:
        return -1
    answer = cnt_end[end_x][end_y]
    return answer