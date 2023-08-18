# 문제
# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
# N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

# 출력
# 첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

# sys.stdin.readline이 input() 보다 빠르다
import sys

n = int(sys.stdin.readline())
num_of_hansu = 0

for i in range(1, n+1):
    is_hansu = True
    before_digit = 10
    before_margin = 10
    margin = 0
    for digit in str(i):
        if i < 10 and before_digit == 10:
            pass
        elif i > 10 and before_digit == 10:
            before_digit = int(digit)
        elif i > 10 and before_digit != 10:
            margin = int(digit) - before_digit
            if before_margin == 10:
                before_margin = margin
            else:
                if before_margin != margin:
                    is_hansu = False
                    break
            before_digit = int(digit)
    if is_hansu:
        num_of_hansu += 1

print(num_of_hansu)