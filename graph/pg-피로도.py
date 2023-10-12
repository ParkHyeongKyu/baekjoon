def solution(k, dungeons):
    answer = []

    visited = [False for _ in range(len(dungeons))]

    def checkAllVisit():
        nonlocal visited
        for i in visited:
            if not i:
                return False
        return True

    def notVisitOverK(k):
        nonlocal dungeons
        for i in range(len(dungeons)):
            if not visited[i] and k >= dungeons[i][0]:
                return False
        return True

    def dfs(k, cnt):
        nonlocal visited
        if notVisitOverK(k) or checkAllVisit():
            answer.append(cnt)
            return

        for i in range(len(dungeons)):
            if not visited[i] and k >= dungeons[i][0]:
                visited[i] = True
                dfs(k - dungeons[i][1], cnt + 1)
                visited[i] = False

    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True
            dfs(k - dungeons[i][1], 1)
            visited[i] = False

    return max(answer)