def solution(arr):
    answer = [0, 0]
    length = len(arr)

    def compression(x, y, l):
        nonlocal arr, answer
        init = arr[x][y]
        for i in range(x, x + l):
            for j in range(y, y + l):
                if arr[i][j] != init:
                    compression(x, y, l // 2)
                    compression(x, y + l // 2, l // 2)
                    compression(x + l // 2, y, l // 2)
                    compression(x + l // 2, y + l // 2, l // 2)
                    return
        answer[init] += 1

    compression(0, 0, length)
    return answer