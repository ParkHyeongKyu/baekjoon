# 문제
# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다.
# 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다.
# 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다. 두 숫자 카드에 같은 수가 적혀있는 경우는 없다.
# 셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 넷째 줄에는 상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야 할 M개의 정수가 주어지며,
# 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다

# 출력
# 첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 가지고 있으면 1을, 아니면 0을 공백으로 구분해 출력한다.

n = input()
sanguen_cards = sorted(list(map(int, input().split())))
m = input()
questions = list(map(int, input().split()))

num_of_sanguen_cards = len(sanguen_cards)
result = []

for card in questions:
    start_idx = 0
    end_idx = num_of_sanguen_cards - 1
    mid_idx = num_of_sanguen_cards // 2
    mid = sanguen_cards[num_of_sanguen_cards // 2]

    while start_idx < end_idx:
        if card < mid:
            end_idx = mid_idx - 1
            if (start_idx + end_idx) / 2 > (start_idx + end_idx) // 2:
                mid_idx = (start_idx + end_idx) // 2 + 1
            else:
                mid_idx = (start_idx + end_idx) // 2
            mid = sanguen_cards[mid_idx]
        else:
            start_idx = mid_idx
            if (start_idx + end_idx) / 2 > (start_idx + end_idx) // 2:
                mid_idx = (start_idx + end_idx) // 2 + 1
            else:
                mid_idx = (start_idx + end_idx) // 2
            mid = sanguen_cards[mid_idx]

    if card == mid:
        result.append(1)
    else:
        result.append(0)

print(*result)

# 모범답안 -> binary search의 국룰 코드 이용
# def binary_search(target, left, right):
#     if left >= right and target != cards[left]:
#         return False
#     mid = (left + right) // 2
#     if target == cards[mid]:
#         return True
#     elif target > cards[mid]:
#         return binary_search(target, mid + 1, right)
#     else:
#         return binary_search(target, left, mid - 1)
#
# N = int(input())
# cards = sorted(list(map(int, input().split())))
# M = int(input())
# finds = list(map(int, input().split()))
# result = ''
# for i in finds:
#     if binary_search(i, 0, N - 1):
#         result += '1 '
#     else:
#         result += '0 '
# print(result[:-1])
