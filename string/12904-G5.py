# 문제
# 수빈이는 A와 B로만 이루어진 영어 단어가 존재한다는 사실에 놀랐다. 대표적인 예로 AB (Abdominal의 약자), BAA (양의 울음 소리), AA (용암의 종류), ABBA (스웨덴 팝 그룹)이 있다.
# 이런 사실에 놀란 수빈이는 간단한 게임을 만들기로 했다. 두 문자열 S와 T가 주어졌을 때, S를 T로 바꾸는 게임이다. 문자열을 바꿀 때는 다음과 같은 두 가지 연산만 가능하다.
# 문자열의 뒤에 A를 추가한다.
# 문자열을 뒤집고 뒤에 B를 추가한다.
# 주어진 조건을 이용해서 S를 T로 만들 수 있는지 없는지 알아내는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 S가 둘째 줄에 T가 주어진다. (1 ≤ S의 길이 ≤ 999, 2 ≤ T의 길이 ≤ 1000, S의 길이 < T의 길이)

# 출력
# S를 T로 바꿀 수 있으면 1을 없으면 0을 출력한다.

# B
# ABBA

# 시간초과 풀이
# S = input()
# T = input()
#
# stack,queue = [S]
#
#
# def isSubstring(f, t) -> bool:
#     f_len = len(f)
#     t_len = len(t)
#     t_reverse = t[::-1]
#     for i in range(t_len):
#         if f == t[i:i+f_len] or f == t_reverse[i:i+f_len]:
#             return True
#     return False
#
#
# while stack,queue:
#     cand = stack,queue.pop()
#     cand_1 = cand + 'A'
#     cand_2 = cand[::-1] + 'B'
#     if cand_1 == T or cand_2 == T:
#         print('1')
#         exit(0)
#     if len(cand_1) <= len(T) and isSubstring(cand_1, T):
#         stack,queue.append(cand_1)
#     if len(cand_2) <= len(T) and isSubstring(cand_2, T):
#         stack,queue.append(cand_2)
#
# print('0')

S = input()
T = input()

while len(S) != len(T):
    if T[-1] == 'A':
        T = T[:-1]
    elif T[-1] == 'B':
        T = T[:-1]
        T = T[::-1]

if S == T:
    print(1)
else:
    print(0)
