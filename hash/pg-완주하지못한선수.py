def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()

    completion.append('hyeongkyu')

    for p, c in zip(participant, completion):
        if p != c:
            return p
    return answer