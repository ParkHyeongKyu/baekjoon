from collections import deque

n, m, v = map(int, input().split())
adjacent_list = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for i in range(m):
    f, t = map(int, input().split())
    adjacent_list[f].append(t)
    adjacent_list[t].append(f)

for i in range(n+1):
    adjacent_list[i].sort()


def dfs(adjacent_list, v, visited):
    stack = [v]
    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            print(vertex, end=' ')
            visited[vertex] = True
            for i in range(len(adjacent_list[vertex]) - 1, -1, -1):
                stack.append(adjacent_list[vertex][i])


def bfs(adjacent_list, v, visited):
    queue = deque()
    queue.append(v)
    while queue:
        vertex = queue.popleft()
        if not visited[vertex]:
            print(vertex, end=' ')
            visited[vertex] = True
            for i in range(len(adjacent_list[vertex])):
                queue.append(adjacent_list[vertex][i])


dfs(adjacent_list, v, visited)
print('')
visited = [False] * (n+1)
bfs(adjacent_list, v, visited)
