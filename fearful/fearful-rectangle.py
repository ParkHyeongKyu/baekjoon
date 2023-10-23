# 문제
# 2xN 직사각형을 2×1, 1x2, 2×2 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
# N 의 범위는  1<= N <= 100 이며, input 으로 주어진다. 결과값이 정수 범위를 넘지 않는다고 가정해도 된다.

def rectangle(n):
    # dp[n] = dp[n-1] + 3 * dp[n-2]
    dp = [0 for _ in range(n+1)]

    dp[1] = 1
    dp[2] = 3
    for i in range(3, n+1):
        dp[i] = dp[i-1] + 2*dp[i-2]

    return dp[n]

print(rectangle(8))