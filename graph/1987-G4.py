# 문제
# 세로 R칸, 가로 C칸으로 된 표 모양의 보드가 있다. 보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (1행 1열) 에는 말이 놓여 있다.
# 말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다.
# 즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.
# 좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오. 말이 지나는 칸은 좌측 상단의 칸도 포함된다.

# 입력
# 첫째 줄에 R과 C가 빈칸을 사이에 두고 주어진다. (1 ≤ R,C ≤ 20) 둘째 줄부터 R개의 줄에 걸쳐서 보드에 적혀 있는 C개의 대문자 알파벳들이 빈칸 없이 주어진다.

# 출력
# 첫째 줄에 말이 지날 수 있는 최대의 칸 수를 출력한다.

# 틀렸는데 왜 틀렸지...
# r, c = map(int, input().split())
# graph = []
# visited = [[False for _ in range(c)] for _ in range(r)]
#
# for i in range(r):
#     graph.append(list(input()))
#
# history = set()
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# count = 1
#
# cnts = []
#
#
# def dfs(x, y):
#     global count
#     no_way = True
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#
#         if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] not in history and not visited[nx][ny]:
#             history.add(graph[nx][ny])
#             visited[nx][ny] = True
#             count += 1
#             dfs(nx, ny)
#             no_way = False
#
#     if no_way:
#         cnts.append(count)
#
#
# history.add(graph[0][0])
# visited[0][0] = True
# if graph[1][0] != graph[0][0]:
#     visited[1][0] = True
#     dfs(1, 0)
#
# count = 1
# history = set()
# visited = [[False for _ in range(c)] for _ in range(r)]
# history.add(graph[0][0])
# visited[0][0] = True
#
# if graph[0][1] != graph[0][0]:
#     visited[0][1] = True
#     dfs(0, 1)
#
# print(max(cnts))
import sys
sys.setrecursionlimit(10**9)

r, c = map(int, input().split())
graph = []

for i in range(r):
    graph.append(list(input()))

history = set()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0


def dfs(x, y, cnt):
    global result
    result = max(result, cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] not in history:
            history.add(graph[nx][ny])
            dfs(nx, ny, cnt+1)
            history.remove(graph[nx][ny])


history.add(graph[0][0])
dfs(0, 0, 1)
print(result)
