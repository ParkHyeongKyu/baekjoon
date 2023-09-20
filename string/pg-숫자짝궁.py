def solution(X, Y):
    answer = ''
    x_arr = [0] * 10
    y_arr = [0] * 10
    result_arr = [0] * 10

    for i in range(len(X)):
        x_arr[int(X[i])] += 1

    for i in range(len(Y)):
        y_arr[int(Y[i])] += 1

    for i in range(10):
        if x_arr[i] > 0 and y_arr[i] > 0:
            result_arr[i] = min(x_arr[i], y_arr[i])

    for i in range(9, -1, -1):
        cnt = result_arr[i]
        for j in range(cnt):
            answer += str(i)

    if answer == '':
        answer = "-1"
    if answer[0] == '0':
        answer = "0"
    return answer
