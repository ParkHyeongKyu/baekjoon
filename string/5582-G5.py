# 문제
# 두 문자열이 주어졌을 때, 두 문자열에 모두 포함된 가장 긴 공통 부분 문자열을 찾는 프로그램을 작성하시오.
# 어떤 문자열 s의 부분 문자열 t란, s에 t가 연속으로 나타나는 것을 말한다.
# 예를 들어, 문자열 ABRACADABRA의 부분 문자열은 ABRA, RAC, D, ACADABRA, ABRACADABRA, 빈 문자열 등이다. 하지만, ABRC, RAA, BA, K는 부분 문자열이 아니다.
# 두 문자열 ABRACADABRA와 ECADADABRBCRDARA의 공통 부분 문자열은 CA, CADA, ADABR, 빈 문자열 등이 있다.
# 이 중에서 가장 긴 공통 부분 문자열은 ADABR이며, 길이는 5이다. 또, 두 문자열이 UPWJCIRUCAXIIRGL와 SBQNYBSBZDFNEV인 경우에는 가장 긴 공통 부분 문자열은 빈 문자열이다.

# 입력
# 첫째 줄과 둘째 줄에 문자열이 주어진다. 문자열은 대문자로 구성되어 있으며, 길이는 1 이상 4000 이하이다.

# 출력
# 첫째 줄에 두 문자열에 모두 포함 된 부분 문자열 중 가장 긴 것의 길이를 출력한다.

# 시간초과
# a = input()
# b = input()
#
# if len(a) > len(b):
#     temp = a
#     a = b
#     b = temp
#
# answer = 0
#
# for i in range(len(a)):
#     pivot = a[i:]
#     for j in range(len(b)):
#         cnt = 0
#         flag = True
#         for k in range(len(pivot)):
#             if j+k < len(b) and pivot[k] == b[j+k]:
#                 cnt += 1
#             else:
#                 break
#         if cnt > 0:
#             if cnt > answer:
#                 answer = cnt
#
# print(answer)

# 시간초과
# from collections import defaultdict
#
# a = input()
# b = input()
#
# if len(a) > len(b):
#     temp = a
#     a = b
#     b = temp
#
# answer = 0
#
# a_dict = defaultdict(list)
#
# for i in range(len(a)):
#     a_dict[a[i]].append(a[i:])
#
# for i in range(len(b)):
#     if not a_dict[b[i]]:
#         continue
#     else:
#         for j in range(len(a_dict[b[i]])):
#             cnt = 0
#             for k in range(len(a_dict[b[i]][j])):
#                 if i+k < len(b) and a_dict[b[i]][j][k] == b[i+k]:
#                     cnt += 1
#                 else:
#                     break
#             if cnt > answer:
#                 answer = cnt
#
# print(answer)

a = input()
b = input()

if len(a) > len(b):
    temp = a
    a = b
    b = temp

answer = 0

n = len(a)

dp = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]

for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            answer = max(dp[i][j], answer)


print(answer)
