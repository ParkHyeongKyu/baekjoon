from collections import deque


def checkVisited(n, visited):
    for i in range(n):
        if not visited[i]:
            return i
    return -1


def solution(n, computers):
    answer = 0

    visited = [False for _ in range(n)]

    while True:
        first_node = checkVisited(n, visited)
        if first_node == -1:
            break
        stack = []
        stack.append(first_node)
        visited[first_node] = True
        while stack:
            now = stack.pop()
            for i in range(len(computers[now])):
                if computers[now][i] == 1 and now != i and not visited[i]:
                    stack.append(i)
                    visited[i] = True
        answer += 1

    return answer