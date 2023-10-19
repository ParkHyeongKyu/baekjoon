def solution(elements):
    answer = set()

    for i in range(len(elements)):
        sum = 0
        for j in range(len(elements)):
            sum += elements[(i + j) % len(elements)]
            answer.add(sum)
    return len(answer)