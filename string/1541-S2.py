# 문제
# 세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.
# 그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.
# 괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다.
# 그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다. 수는 0으로 시작할 수 있다.
# 입력으로 주어지는 식의 길이는 50보다 작거나 같다.

# 출력
# 첫째 줄에 정답을 출력한다.

# idea -> '-'를 기준으로 식을 끊어서 괄호를 쳐준다.

all = input()
split_by_minus = all.split('-')
# 이렇게 하면 1+2-3+4+5-6 인 경우에 (1+2), (3+4+5), (6)으로 쳐짐
# 처음이 마이너스인 경우 -1+2-3+4 인 경우 (-1), (2), (3+4)로 끊어져야 함 -> 맨 처음이 -인 경우와 +인 경우로 분리하기
# -> 사실 문제에서 가장 처음 문자는 숫자라고 했으므로 처음이 마이너스인 경우를 분리할 필요가 없었음
result = 0
# -1-2-3+4
# -1+2-3
i = 0
for seperate_dump in split_by_minus:
    sum_of_dump = sum(map(int, seperate_dump.split('+')))
    if i == 0 and all[0] == '-':
        result = -sum_of_dump
        i += 1
    elif i == 0 and all[0] != '-':
        result = sum_of_dump
        i += 1
    else:
        result = result - sum_of_dump

print(result)