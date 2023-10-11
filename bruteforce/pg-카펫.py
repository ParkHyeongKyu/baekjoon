def solution(brown, yellow):
    answer = []
    # 가로 a, 세로 b

    # 1. a x b - yellow = brown
    # 2. m x n = yellow
    # a = m + 2, b = n + 2
    # 2m + 2n + 4 = brown
    # yellow + brown = a x b

    for m in range(1, yellow + 1):
        if yellow % m == 0:
            n = yellow // m
            if (2 * m) + (2 * n) + 4 == brown and m >= n:
                a = m + 2
                b = n + 2
                return [a, b]
    return answer