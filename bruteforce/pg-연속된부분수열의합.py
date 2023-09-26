def solution(sequence, k):
    answer = []
    start = 0
    end = 0
    sum = sequence[0]
    while end < len(sequence) or start <= end:
        if sum < k:
            end += 1
            if end >= len(sequence):
                break
            sum += sequence[end]
        elif sum > k:
            sum -= sequence[start]
            start += 1
            if start >= len(sequence):
                break
        else:
            answer.append((start, end))
            sum -= sequence[start]
            start += 1
            if start >= len(sequence):
                break

    answer.sort(key=lambda x: (x[1] - x[0], x[0]))
    answer = answer[0]
    return answer