from collections import deque
import sys
# 위 알고리즘은 sliding window를 통해 subset의 최댓값을 찾는 알고리즘입니다.
# q에는 s의 각 원소의 index가 들어가게 되며 dq의 가장 맨 왼쪽 수에는 subset의 최댓값이 위치하며
# 그 오른쪽에는 현재 dq[0] 즉, 현재 window에서의 최댓값 이후에 등장한 dq[0]보다 작은 수들이 append됩니다.
# 그러던 중 dq[0]보다 큰 수가 나오면 dq에 있는 원소들을 모두 pop하고 새 최댓값을 집어넣어
# 다시 한번 새 최댓값이 dq[0]에 위치하도록 합니다.
# 이 알고리즘의 복잡도는
# 1. 입력 받는 부분 : O(N)
# 2. 슬라이딩 윈도우 최댓값 계산 부분 : O(N)
# -> 각 숫자는 dq에 한번씩만 추가되고, 한번씩만 제거되므로 N개의 숫자에 대해 각각 상수 시간이 소요됩니다.
# 3. 결과 출력 : O(N)
# 결론 : 따라서 O(N)의 시간 복잡도를 가지고 있습니다.

def sliding_window_max(w, idx, num, dq, s):
    # 새로운 값이 기존의 최댓값보다 크다면 dq를 비운다.
    while dq and s[dq[-1]] < num:
        dq.pop()

    dq.append(idx)

    # 맨 왼쪽이 sliding window 벗어나는 경우
    if dq[0] == idx - w:
        dq.popleft()

    # 아직 sliding window가 꽉 채워지지 않았다면 출력하지 말자.
    if idx >= w - 1:
        print(s[dq[0]])

w = int(input())
s = []
dq = deque()
for idx in range(w):
    # 4번 테케의 경우 아래 부분 (num = int(input())) 에서 런타임 에러가 발생함 (아마 메모리 문제)
    # 그냥 num = 1로 했을 때도 시간 초과 오류가 나는데, 아마 w가 엄청나게 큰 것(10억 이상) 일것으로 생각됨
    # 근데, 시간 제한이 10초인데 30억 이상을 handling할 수 있나...?
    num = int(input())
    s.append(num)
    sliding_window_max(w, idx, num, dq, s)

try:
    idx = w
    while True:
        num = int(input())
        s.append(num)
        sliding_window_max(w, idx, num, dq, s)
        idx += 1
except EOFError:
    pass
except Exception as e:
    print(e)