# 문제
# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

# 입력
# 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.
# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

# 출력
# 첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

n = int(input())
arr = list(map(int, input().split()))
cnt_max = -1
cnt_max_idx = -1

dp = [(0, 0) for _ in range(n)]

dp[0] = (arr[0], 1)
for i in range(1, n):
    max_cnts = [1]
    for j in range(i):
        if arr[i] > dp[j][0]:
            max_cnts.append(dp[j][1] + 1)
    dp[i] = (arr[i], max(max_cnts))
    if dp[i][1] > cnt_max:
        cnt_max = dp[i][1]
        cnt_max_idx = i

print(dp[cnt_max_idx][1])

