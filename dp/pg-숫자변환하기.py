def solution(x, y, n):
    answer = 0
    dp = [1000001 for _ in range(y + 1)]
    dp[x] = 0

    # 점화식
    # dp[i] = dp[i//3] + 1
    # dp[i] = dp[i//2] + 1
    # dp[i] = dp[i-30] + 1

    for i in range(x, y):
        if 2 * i <= y and dp[2 * i] > dp[i] + 1:
            dp[2 * i] = dp[i] + 1
        if 3 * i <= y and dp[3 * i] > dp[i] + 1:
            dp[3 * i] = dp[i] + 1
        if i + n <= y and dp[i + n] > dp[i] + 1:
            dp[i + n] = dp[i] + 1

    answer = dp[y]
    if answer == 1000001:
        return -1
    return answer