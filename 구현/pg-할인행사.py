from collections import defaultdict


def solution(want, number, discount):
    answer = 0
    product_cnt = sum(number)

    dt = defaultdict(int)

    # product_cnt만큼 초기화
    for i in range(product_cnt):
        dt[discount[i]] += 1

    for i in range(len(discount) - product_cnt + 1):
        flag = True
        if i > 0:
            dt[discount[i - 1]] -= 1
            if dt[discount[i - 1]] == 0:
                dt.pop(discount[i - 1])
            dt[discount[product_cnt + i - 1]] += 1

        # print(dt)
        for j in range(len(number)):
            if dt[want[j]] < number[j]:
                # print('go false', want[j])
                flag = False
                break
        if flag:
            answer += 1

    return answer