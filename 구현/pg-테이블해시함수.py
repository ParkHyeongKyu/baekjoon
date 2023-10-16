def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x: x[0], reverse=True)
    data.sort(key=lambda x: x[col - 1])

    S_i = []
    for i in range(row_begin - 1, row_end):
        sum = 0
        for j in range(len(data[0])):
            sum += data[i][j] % (i + 1)
        S_i.append(sum)

    answer = S_i[0]
    for i in range(1, len(S_i)):
        answer = answer ^ S_i[i]

    return answer