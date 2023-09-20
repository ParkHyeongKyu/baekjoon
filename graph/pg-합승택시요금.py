import heapq
import sys


def dijkstra(start, adjacent_list, n):
    dist = [sys.maxsize for _ in range(n + 1)]
    q = []
    heapq.heappush(q, (start, 0))
    dist[start] = 0
    while q:
        node, weight = heapq.heappop(q)
        if dist[node] < weight:
            continue

        for edge in adjacent_list[node]:
            if edge[1] + weight < dist[edge[0]]:
                dist[edge[0]] = edge[1] + weight
                heapq.heappush(q, (edge[0], edge[1] + weight))

    return dist


def solution(n, s, a, b, fares):
    answer = 0
    min_dist = sys.maxsize

    adjacent_list = [[] for _ in range(n + 1)]
    for i in range(len(fares)):
        adjacent_list[fares[i][0]].append((fares[i][1], fares[i][2]))
        adjacent_list[fares[i][1]].append((fares[i][0], fares[i][2]))

    dist_from_s = dijkstra(s, adjacent_list, n)
    for i in range(1, n + 1):
        dist_i_to_node = dijkstra(i, adjacent_list, n)
        dist = dist_from_s[i] + dist_i_to_node[a] + dist_i_to_node[b]
        if dist < min_dist:
            min_dist = dist

    answer = min(min_dist, dist_from_s[a] + dist_from_s[b])
    # 1. 다익스트라를 통해 s에서 a까지의 최단거리 구하고 -> a에서 b까지의 최단거리 구하기
    # 2. 다익스트라를 통해 s에서 b까지의 최단거리 구하고 -> b에서 a까지의 최단거리 구하기
    # 아 근데 이걸로는 안되는게, 두명이 중간에 따로 타고 갈 수 있음.
    # => 다익스트라로 S에서 모든 노드까지의 최단거리 + 도착한 노드에서 각각 a,b까지 최단거리 이것의 최소 구하기
    # 3. S에서 a, b 각각의 최단거리 구하기
    # 위 두개 비교해서 최소가 answer
    return answer

