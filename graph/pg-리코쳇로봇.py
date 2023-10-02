from collections import deque
import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution(board):
    answer = 0
    cnt = [[sys.maxsize for _ in range(len(board[0]))] for _ in range(len(board))]
    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

    start_x, start_y, end_x, end_y = 0, 0, 0, 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                start_x = i
                start_y = j
                cnt[i][j] = 0
            elif board[i][j] == 'G':
                end_x = i
                end_y = j
            elif board[i][j] == 'D':
                cnt[i][j] = -1
    q = deque()
    q.append([start_x, start_y])
    visited[start_x][start_y] = True
    while q:
        now_x, now_y = q.popleft()
        history_cnt = cnt[now_x][now_y]
        for i in range(4):
            nx = now_x
            ny = now_y
            while True:
                nx = nx + dx[i]
                ny = ny + dy[i]
                if nx < 0 or nx >= len(board) or ny < 0 or ny >= len(board[0]):
                    nx -= dx[i]
                    ny -= dy[i]
                    break
                elif 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == 'D':
                    nx -= dx[i]
                    ny -= dy[i]
                    break
            if not visited[nx][ny]:
                q.append([nx, ny])
                visited[nx][ny] = True
                cnt[nx][ny] = history_cnt + 1
    answer = cnt[end_x][end_y]
    if cnt[end_x][end_y] == sys.maxsize:
        answer = -1
    return answer