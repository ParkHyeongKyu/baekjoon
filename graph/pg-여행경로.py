def solution(tickets):
    answer = []
    # tickets.sort(key = lambda x: x[1])
    used_ticket = [False for _ in range(len(tickets))]

    def checkAllVisit(used_ticket):
        for t in used_ticket:
            if not t:
                return False
        return True

    def dfs(now, path):
        if checkAllVisit(used_ticket):
            answer.append(path)

        for idx, t in enumerate(tickets):
            if not used_ticket[idx] and now == t[0]:
                used_ticket[idx] = True
                dfs(t[1], path + [t[1]])
                used_ticket[idx] = False

    dfs("ICN", ["ICN"])

    return min(answer)