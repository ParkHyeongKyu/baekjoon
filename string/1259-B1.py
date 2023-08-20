# 문제
# 어떤 단어를 뒤에서부터 읽어도 똑같다면 그 단어를 팰린드롬이라고 한다. 'radar', 'sees'는 팰린드롬이다.
# 수도 팰린드롬으로 취급할 수 있다. 수의 숫자들을 뒤에서부터 읽어도 같다면 그 수는 팰린드롬수다.
# 121, 12421 등은 팰린드롬수다. 123, 1231은 뒤에서부터 읽으면 다르므로 팰린드롬수가 아니다.
# 또한 10도 팰린드롬수가 아닌데, 앞에 무의미한 0이 올 수 있다면 010이 되어 팰린드롬수로 취급할 수도 있지만, 특별히 이번 문제에서는 무의미한 0이 앞에 올 수 없다고 하자.

# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있으며, 각 줄마다 1 이상 99999 이하의 정수가 주어진다. 입력의 마지막 줄에는 0이 주어지며, 이 줄은 문제에 포함되지 않는다.

# 출력
# 각 줄마다 주어진 수가 팰린드롬수면 'yes', 아니면 'no'를 출력한다.

import sys
from collections import deque

while True:
    pelindrome = True
    input_case = input()
    # 여기서 sys.stdin.readline() 을 사용할 경우 마지막에 '\n'까지 포함하게 되므로 len가 생각했던 것보다 1이 높음.
    if input_case == '0':
        break

    stack = deque()
    if len(input_case) % 2 == 0:
        for i in range(int(len(input_case)//2)):
            stack.append(input_case[i])
        for i in range(int(len(input_case)//2), int(len(input_case))):
            if input_case[i] != stack.pop():
                pelindrome = False
                break
    else:
        for i in range(int(len(input_case)//2)):
            stack.append(input_case[i])
        for i in range(int(len(input_case)//2)+1, int(len(input_case))):
            if input_case[i] != stack.pop():
                pelindrome = False
                break
    if pelindrome:
        print('yes')
    else:
        print('no')

# 모범답안 -> string slicing을 사용하여 뒤집어서 검사하기

# while True:
#     n = input()
#
#     if n == '0':
#         break
#
#     if n == n[::-1]:
#         print('yes')
#     else:
#         print('no')
