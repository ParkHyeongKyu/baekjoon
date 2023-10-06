from collections import defaultdict


def solution(weights):
    answer = 0

    weight_dict = defaultdict(int)

    for i in range(len(weights)):
        weight_dict[weights[i]] += 1

    for i in range(100, 1001):
        if weight_dict[i] > 1:
            answer += (weight_dict[i] * (weight_dict[i] - 1)) / 2
        for j in range(i + 1, 1001):
            if weight_dict[i] != 0 and weight_dict[j] != 0:
                if i * 2 == j or i * 3 == j * 2 or i * 4 == j * 3:
                    answer += weight_dict[i] * weight_dict[j]

    return answer