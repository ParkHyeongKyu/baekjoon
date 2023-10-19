from collections import deque


def solution(order):
    answer = 0

    q = deque()
    stack = []
    pointer = 0

    for box in order:
        # print(stack, pointer)
        if stack and stack[-1] == box:
            stack.pop()
            answer += 1
            continue
        elif stack and box < pointer and stack[-1] != box:
            break

        for i in range(pointer + 1, len(order) + 1):
            pointer += 1
            if box != i:
                stack.append(i)
            else:
                answer += 1
                break
    return answer