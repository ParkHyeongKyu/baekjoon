# 한 정점에서 다른 모든 정점까지의 최단 거리를 구하는 다익스트라 알고리즘 구현

import sys
import heapq

n, m = map(int, sys.stdin.readline().split()) # node수, edge수
start = int(input()) # 시작하는 기준 node

INF = int(1e9)
distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 이제 node를 들렸다가 다른 곳으로 가는 경로들을 구할거임
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue

        for edge in graph[node]:
            cost = dist + edge[1]
            if cost < distance[edge[0]]:
                distance[edge[0]] = cost
                heapq.heappush(q, (cost, edge[0]))


dijkstra(start)

for i in range(1, len(distance)):
    if distance[i] == INF:
        print('도달할 수 없음')
    else:
        print(distance[i])
