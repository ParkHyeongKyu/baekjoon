# 문제
# 루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

# 출력
# 첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.
from collections import deque

node_cnt = int(input())

adjacent_list = [[] for _ in range(node_cnt + 1)]
parent = [0 for _ in range(node_cnt + 1)]
visited = [False for _ in range(node_cnt + 1)]

for i in range(node_cnt - 1):
    f, t = map(int, input().split())
    adjacent_list[f].append(t)
    adjacent_list[t].append(f)


def bfs(node):
    q = deque()
    q.append(node)
    while q:
        n = q.popleft()
        for i in range(len(adjacent_list[n])):
            if not visited[adjacent_list[n][i]] and parent[adjacent_list[n][i]] == 0:
                visited[i] = True
                parent[adjacent_list[n][i]] = n
                q.append(adjacent_list[n][i])


bfs(1)
for i in range(2, node_cnt+1):
    print(parent[i])
