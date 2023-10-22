def to2(a):
    result = ''

    while a != 1:
        result = str(a % 2) + result
        a = a // 2
    result = '1' + result
    return int(result)


def solution(s):
    answer = []
    zero_cnt = 0
    tx_cnt = 0

    while s != 1:
        s = str(s)
        for word in s:
            if word == "0":
                zero_cnt += 1
        s = s.replace('0', '')
        # print('replace 0', s)
        len_s = len(s)
        s = to2(len_s)
        # print('to2', s)
        tx_cnt += 1

    answer.append(tx_cnt)
    answer.append(zero_cnt)

    return answer