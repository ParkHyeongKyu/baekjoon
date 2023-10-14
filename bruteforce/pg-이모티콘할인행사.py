from itertools import product
from heapq import heappush, heappop


def solution(users, emoticons):
    sale = [10, 20, 30, 40]
    num_emo = len(emoticons)
    input_sales = [sale] * num_emo
    sale_list = list(product(*input_sales))

    heap = []

    for i in range(len(sale_list)):
        plus_user = 0
        money_all_sum = 0
        for j in range(len(users)):
            money_sum = 0
            for k in range(len(emoticons)):
                if sale_list[i][k] >= users[j][0]:
                    money_sum += emoticons[k] - (emoticons[k] * int(sale_list[i][k]) * 0.01)
            if money_sum >= users[j][1]:
                plus_user += 1
                money_sum = 0
            money_all_sum += money_sum
        heap.append((plus_user, money_all_sum))

    heap.sort(key=lambda x: (x[0], x[1]), reverse=True)

    return heap[0]