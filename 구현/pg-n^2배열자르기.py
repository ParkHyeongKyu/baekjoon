# 1 2 3 4 5 ..
# 2 2 3 4 5 ..
# 3 3 3 4 5 ..
# 4 4 4 4 5 ..
# 5 5 5 5 5 ..
# i번째 row는 i+1이 i+1개 있고 그 이후로는 다 1개씩 있음.


def solution(n, left, right):
    answer = []
    left_ans = left // n
    left_l = left % n
    right_ans = right // n
    right_l = right % n

    for i in range(left_ans, right_ans + 1):
        arr = [i + 1 for _ in range(i + 1)]
        for j in range(i + 1, n):
            arr.append(j + 1)

        if left_ans == right_ans:
            answer.extend(arr[left_l:right_l + 1])
            break

        if i == left_ans:
            answer.extend(arr[left_l:])
        elif i == right_ans:
            answer.extend(arr[:right_l + 1])
        else:
            answer.extend(arr)
    return answer