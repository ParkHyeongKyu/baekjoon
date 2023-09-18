# 문제
#         7
#       3   8
#     8   1   0
#   2   7   4   4
# 4   5   2   6   5
# 위 그림은 크기가 5인 정수 삼각형의 한 모습이다.
#
# 맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라.
# 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.
# 삼각형의 크기는 1 이상 500 이하이다. 삼각형을 이루고 있는 각 수는 모두 정수이며, 범위는 0 이상 9999 이하이다.

# 입력
# 첫째 줄에 삼각형의 크기 n(1 ≤ n ≤ 500)이 주어지고, 둘째 줄부터 n+1번째 줄까지 정수 삼각형이 주어진다.

# 출력
# 첫째 줄에 합이 최대가 되는 경로에 있는 수의 합을 출력한다.

# 점화식
# k == 0
# dp[i][0] = dp[i-1][0] + arr[i][0]
# k == i-1
# dp[i][i-1] = dp[i-1][i-2] + arr[i][i-1]
# else
# dp[i][k] = max(dp[i-1][k-1] + arr[i][k], dp[i-1][k] + arr[i][k])

n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = [[0 for _ in range(n)] for _ in range(n)]

dp[0][0] = arr[0][0]

for i in range(1, n):
    for k in range(i+1):
        if k == 0:
            dp[i][0] = dp[i-1][0] + arr[i][0]
        elif k == i:
            dp[i][i] = dp[i-1][i-1] + arr[i][i]
        else:
            dp[i][k] = max(dp[i-1][k-1] + arr[i][k], dp[i-1][k] + arr[i][k])

print(max(dp[n-1]))
