# 문제
# 다음과 같은 flatten 함수를 구현하시오.
#
# input - output
#
# flatten([]) // []
# flatten([[[]]]) // []
# flatten([[0, 1], [2, 3], [4, 5]]) // [ 0, 1, 2, 3, 4, 5 ]
# flatten([[[0], [1]], [[2], [3]], [[4], [5]]]) // [ 0, 1, 2, 3, 4, 5 ]
# flatten([[0, [[[[1]]]]], [[2, 3]], 4, [5]]) // [ 0, 1, 2, 3, 4, 5 ]

# 야매풀이
# def flatten(input):
#     result = []
#     str_input = str(input)
#     for i in str_input:
#         if i == '[' or i == ']' or i == ',' or i == ' ':
#             pass
#         else:
#             result.append(i)
#
#     print(result)

# 정석

result = []


def flatten(input):
    if type(input) == int:
        result.append(input)
    else:
        for i in input:
            flatten(i)
    return result


flatten([[0, [[[[1]]]]], [[2, 3]], 4, [5]])
print(result)