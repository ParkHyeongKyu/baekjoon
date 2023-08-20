# 문제
# LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.
# 예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

# 입력
# 첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

# 출력
# 첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.

# 처음에 짠 코드 -> 재귀를 사용했는데, 입력이 큰 경우 파이썬의 최대 재귀 깊이를 초과하여 RuntimeError가 발생함.
# 또한, 이 알고리즘은 지수시간 복잡도를 가지기 때문에 큰 입력에 대해서는 매우 느 -> 동적 계획법(Dynammic Programming 사용)
# string1 = input()
# string2 = input()
#
#
# def lcs(str1, str2):
#     if len(str1) == 0 or len(str2) == 0:
#         return 0
#     if str1[0] == str2[0]:
#         return 1 + lcs(str1[1:], str2[1:])
#     else:
#         return max(lcs(str1, str2[1:]), lcs(str1[1:], str2))
#
#
# result = lcs(string1, string2)
# print(result)

# Dynammic Programming을 이용한 풀이
string1 = input()
string2 = input()

array = [[0] * (len(string2)+1) for _ in range(len(string1) + 1)]

for i in range(1, len(string1)+1):
    for j in range(1, len(string2)+1):
        if string1[i-1] == string2[j-1]:
            array[i][j] = array[i-1][j-1] + 1
        else:
            array[i][j] = max(array[i][j-1], array[i-1][j])

print(array[len(string1)][len(string2)])
