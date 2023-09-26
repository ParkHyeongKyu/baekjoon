# greedy algorithm

def solution(targets):
    answer = 0
    targets.sort(key=lambda x: x[1])
    misail = -1

    for target in targets:
        if target[0] >= misail:
            misail = target[1]
            answer += 1

    return answer