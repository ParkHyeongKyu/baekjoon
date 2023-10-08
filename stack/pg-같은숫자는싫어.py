def solution(arr):
    answer = []
    stack = []
    stack.append(-1)
    for i in range(len(arr)):
        if stack.pop() != arr[i]:
            answer.append(arr[i])
        stack.append(arr[i])
    return answer