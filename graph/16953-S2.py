# 문제
# 정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.
#
# 2를 곱한다.
# 1을 수의 가장 오른쪽에 추가한다.
# A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.

# 입력
# 첫째 줄에 A, B (1 ≤ A < B ≤ 10^9)가 주어진다.

# 출력
# A를 B로 바꾸는데 필요한 연산의 최솟값에 1을 더한 값을 출력한다. 만들 수 없는 경우에는 -1을 출력한다.

import sys
from collections import deque

a, b = map(int, sys.stdin.readline().split())

q = deque()
q.append((a, 0))

while q:
    now, cnt = q.popleft()

    if now == b:
        print(cnt + 1)
        exit(0)

    if now * 2 <= b:
        q.append((now*2, cnt+1))
    if int(str(now)+'1') <= b:
        q.append((int(str(now)+'1'), cnt+1))

print(-1)




