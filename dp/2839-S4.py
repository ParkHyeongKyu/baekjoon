# 문제
# 상근이는 요즘 설탕공장에서 설탕을 배달하고 있다. 상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다.
# 설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.
# 상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다. 예를 들어, 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만,
# 5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.
# 상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다. (3 ≤ N ≤ 5000)

# 출력
# 상근이가 배달하는 봉지의 최소 개수를 출력한다. 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.

# 수학적 풀이 - 이것도 맞음
# n = int(input())
#
# init_5 = n // 5
#
# cnt_5 = init_5
# cnt_3 = 0
#
# while cnt_5 >= 0:
#     rest_kg = n - (cnt_5 * 5)
#     if rest_kg % 3 == 0:
#         cnt_3 = rest_kg // 3
#         break
#     else:
#         cnt_5 -= 1
#
# if cnt_5 == -1:
#     print(-1)
# else:
#     print(int(cnt_5) + int(cnt_3))

# dp풀이
# 점화식 dp[i] = min(dp[i-3]+1, dp[i-5]+1)

dp = [0 for _ in range(5001)]
# n >= 3이므로 3,4,5에 대해 index outof range가 나지 않도록 초기화해줌
dp[1] = -1
dp[2] = -1
dp[3] = 1
dp[4] = -1
dp[5] = 1

n = int(input())

if n <= 5:
    print(dp[n])
else:
    for i in range(6, n+1):
        if dp[i-5] != -1 and dp[i-3] != -1:
            dp[i] = min(dp[i-3]+1, dp[i-5]+1)
        elif dp[i-5] == -1 and dp[i-3] != -1:
            dp[i] = dp[i-3] + 1
        elif dp[i-5] != -1 and dp[i-3] == -1:
            dp[i] = dp[i-5] + 1
        elif dp[i-5] == -1 and dp[i-3] == -1:
            dp[i] = -1
    print(dp[n])



