from collections import defaultdict, deque


def solution(n, wires):
    answer = []

    for i in range(len(wires)):
        adjacent_dict = defaultdict(list)
        visited = [False for _ in range(len(wires) + 2)]
        for j in range(len(wires)):
            if i != j:
                adjacent_dict[wires[j][0]].append(wires[j][1])
                adjacent_dict[wires[j][1]].append(wires[j][0])

        q = deque()

        def findNotVisitedNode():
            nonlocal visited
            for i in range(1, len(visited)):
                if not visited[i]:
                    return i
            return -1

        chunk_count = []
        while True:
            node = findNotVisitedNode()
            if node == -1:
                break
            q.append(node)
            visited[node] = True
            cnt = 1
            while q:
                now = q.popleft()

                for i in range(len(adjacent_dict[now])):
                    if not visited[adjacent_dict[now][i]]:
                        visited[adjacent_dict[now][i]] = True
                        q.append(adjacent_dict[now][i])
                        cnt += 1
            chunk_count.append(cnt)
        answer.append(abs(chunk_count[0] - chunk_count[1]))
    return min(answer)