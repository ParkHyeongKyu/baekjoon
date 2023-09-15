# 문제
# 개똥벌레 한 마리가 장애물(석순과 종유석)로 가득찬 동굴에 들어갔다. 동굴의 길이는 N미터이고, 높이는 H미터이다. (N은 짝수) 첫 번째 장애물은 항상 석순이고,
# 그 다음에는 종유석과 석순이 번갈아가면서 등장한다.
# 아래 그림은 길이가 14미터이고 높이가 5미터인 동굴이다. (예제 그림)
# 이 개똥벌레는 장애물을 피하지 않는다. 자신이 지나갈 구간을 정한 다음 일직선으로 지나가면서 만나는 모든 장애물을 파괴한다.
# 위의 그림에서 4번째 구간으로 개똥벌레가 날아간다면 파괴해야하는 장애물의 수는 총 여덟개이다. (4번째 구간은 길이가 3인 석순과 길이가 4인 석순의 중간지점을 말한다)
# 하지만, 첫 번째 구간이나 다섯 번째 구간으로 날아간다면 개똥벌레는 장애물 일곱개만 파괴하면 된다.
# 동굴의 크기와 높이, 모든 장애물의 크기가 주어진다. 이때, 개똥벌레가 파괴해야하는 장애물의 최솟값과 그러한 구간이 총 몇 개 있는지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 H가 주어진다. N은 항상 짝수이다. (2 ≤ N ≤ 200,000, 2 ≤ H ≤ 500,000)
# 다음 N개 줄에는 장애물의 크기가 순서대로 주어진다. 장애물의 크기는 H보다 작은 양수이다.

# 출력
# 첫째 줄에 개똥벌레가 파괴해야 하는 장애물의 최솟값과 그러한 구간의 수를 공백으로 구분하여 출력한다.

# h를 이분 탐색 기준으로 삼으려고 했음 -> 이러면 만족하는 h의 개수를 찾을 수 없음
# N, H = map(int, input().split())
# rocks = []
#
# for i in range(N):
#     rocks.append(int(input()))
#
# start = 1
# end = H
# result = N + 1
# result_set = set()
#
# # while start <= end:
# for where in range(1, H+1):
#     low_bomb = 0
#     high_bomb = 0
#     # mid = (start + end) // 2
#     for i in range(0, N, 2):
#         if rocks[i] >= where:
#             low_bomb += 1
#     for i in range(1, N, 2):
#         if rocks[i] > H - where:
#             high_bomb += 1
#
#     if low_bomb + high_bomb < result:
#         result = low_bomb + high_bomb
#         result_set.clear()
#         result_set.add(where)
#     elif low_bomb + high_bomb == result:
#         result_set.add(where)
#
#     # if low_bomb > high_bomb:
#     #     start = where + 1
#     # else:
#     #     end = where - 1
#
# print(result, len(result_set))

# h에 대해서는 for loop을 통해 linear하게 탐색하고, 각 h에 대해 부딪히는 개수를 logN으로 찾자
# https://blog.naver.com/PostView.nhn?blogId=crm06217&logNo=222023706440&categoryNo=23&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView

import sys


def Binary_Search_Upper(data_list, x):                  #주어진 list에서 x보다 큰 데이터의 개수를 반환; log n 안에 찾음
    left = 0
    right = len(data_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if data_list[mid] <= x:
            left = mid + 1
        else:
            right = mid - 1
    return len(data_list) - (right + 1)                  #index, 개수 차이 때문에 1 더해줌

input_list = input().split()
N = int(input_list[0])
H = int(input_list[1])
data_down = []
data_up = []
for i in range(N):
    input_list_2 = sys.stdin.readline().split()
    input_num = int(input_list_2[0])
    if i % 2 == 0:              #아래부터 높이 재기
        data_down.append(input_num)
    else:                       #위부터 높이 재기
        data_up.append(input_num)
data_down.sort()
data_up.sort()
ans = N                         #장애물의 최솟값
cnt = 0                         #구간 몇 개 있는지
for h in range(1, H + 1):
    down_num = Binary_Search_Upper(data_down, h - 1)
    up_num = Binary_Search_Upper(data_up, H - h)
    cur_num = down_num + up_num     #현재 mid 값을 기준으로 잘랐을 때의 장애물의 수
    if cur_num < ans:               #새로운 최솟값이 나오면 정답 업데이트; 개수는 1부터 다시 셈
        ans = cur_num
        cnt = 1
    elif cur_num == ans:            #현재 최솟값과 같은 값이 한 번 더 나오면 개수 1 증가
        cnt += 1
print(ans, cnt)