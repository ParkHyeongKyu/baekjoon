# 문제
# 백준 사이트 참고

# 입력
# 첫째 줄에 집의 크기 N(3 ≤ N ≤ 16)이 주어진다. 둘째 줄부터 N개의 줄에는 집의 상태가 주어진다. 빈 칸은 0, 벽은 1로 주어진다. (1, 1)과 (1, 2)는 항상 빈 칸이다.

# 출력
# 첫째 줄에 파이프의 한쪽 끝을 (N, N)으로 이동시키는 방법의 수를 출력한다. 이동시킬 수 없는 경우에는 0을 출력한다. 방법의 수는 항상 1,000,000보다 작거나 같다.

# 맞았지만 bfs로 풀면 시간초과
# import sys
# from collections import deque
#
# n = int(sys.stdin.readline())
# graph = []
#
# for i in range(n):
#     graph.append(list(map(int, sys.stdin.readline().split())))
#     for j in range(n):
#         if graph[i][j] == 1:
#             graph[i][j] = -1
#
# if graph[n-1][n-1] == -1:
#     print(0)
#     exit(0)
#
# state = 1
# state_1_dx = [0, 1]
# state_1_dy = [1, 1]
# state_2_dx = [1, 1]
# state_2_dy = [0, 1]
# state_3_dx = [0, 1, 1]
# state_3_dy = [1, 0, 1]
#
# now = ((0, 1), 1)
# q = deque()
# q.append(now)
# graph[0][1] = 1
# while q:
#     loc, state = q.popleft()
#     if state == 1:
#         for i in range(2):
#             nx = loc[0] + state_1_dx[i]
#             ny = loc[1] + state_1_dy[i]
#
#             if i == 0:
#                 if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != -1:
#                     state = 1
#                     graph[nx][ny] += 1
#                     q.append(((nx, ny), state))
#             elif i == 1:
#                 if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != -1 and graph[nx-1][ny] != -1 and graph[nx][ny-1] != -1:
#                     state = 3
#                     graph[nx][ny] += 1
#                     q.append(((nx, ny), state))
#     elif state == 2:
#         for i in range(2):
#             nx = loc[0] + state_2_dx[i]
#             ny = loc[1] + state_2_dy[i]
#
#             if i == 0:
#                 if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != -1:
#                     state = 2
#                     graph[nx][ny] += 1
#                     q.append(((nx, ny), state))
#             elif i == 1:
#                 if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != -1 and graph[nx-1][ny] != -1 and graph[nx][ny-1] != -1:
#                     state = 3
#                     graph[nx][ny] += 1
#                     q.append(((nx, ny), state))
#     elif state == 3:
#         for i in range(3):
#             nx = loc[0] + state_3_dx[i]
#             ny = loc[1] + state_3_dy[i]
#
#             if i == 0:
#                 if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != -1:
#                     state = 1
#                     graph[nx][ny] += 1
#                     q.append(((nx, ny), state))
#             elif i == 1:
#                 if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != -1:
#                     state = 2
#                     graph[nx][ny] += 1
#                     q.append(((nx, ny), state))
#             elif i == 2:
#                 if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != -1 and graph[nx-1][ny] != -1 and graph[nx][ny-1] != -1:
#                     state = 3
#                     graph[nx][ny] += 1
#                     q.append(((nx, ny), state))
#
# print(graph[n-1][n-1])

# dp를 이용한 풀이
def solution():
    # 1행 미리 처리하기 → (3) 과정
    dp[0][0][1] = 1
    for i in range(2, N):
        if board[0][i] == 0:
            dp[0][0][i] = dp[0][0][i - 1]

    # 왜 1행과 1열을 제외하는지는 (3), (4) 과정에서 봤었죠?
    for r in range(1, N):
        for c in range(1, N):
            # (5) 과정
            # 대각선 파이프를 추가하는 과정
            if board[r][c] == 0 and board[r][c - 1] == 0 and board[r - 1][c] == 0:
                dp[1][r][c] = dp[0][r - 1][c - 1] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]

            # 가로, 세로 파이프를 추가하는 과정
            if board[r][c] == 0:
                dp[0][r][c] = dp[0][r][c - 1] + dp[1][r][c - 1]
                dp[2][r][c] = dp[2][r - 1][c] + dp[1][r - 1][c]

    # 최종 결과 출력
    print(sum(dp[i][N - 1][N - 1] for i in range(3)))


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]
solution()

